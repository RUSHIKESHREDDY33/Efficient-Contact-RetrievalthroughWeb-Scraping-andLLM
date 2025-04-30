from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import ollama
from urllib.parse import urljoin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/submit', methods=['POST'])
def submit():

    web_data = []
    print("\n\n************** Web Scraper Started **************\n\n")

    def find_contact_pages(base_url):
        response = requests.get(base_url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return []

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        contact_keywords = [
            'contact', 'get in touch', 'support', 'help', 'customer service', 'reach us',
            'contact us', 'support us', 'connect', 'talk to us', 'inquire', 'service',
            'customer care', 'contact center', 'customer support', 'feedback', 'contact form',
            'get support', 'contact information', 'contact page', 'service center'
        ]

        contact_page_urls = []
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            
            if any(keyword in full_url.lower() for keyword in contact_keywords) and base_url in full_url:
                contact_page_urls.append(full_url)

        return contact_page_urls

    def scrape_contact_page(url):
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve the contact page. Status code: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        web_data.append(soup.get_text(separator='\n', strip=True))

    main_url = request.form['url']
    contact_urls = find_contact_pages(main_url)
    if contact_urls:
        for contact_url in contact_urls:
            print(f"Scraping Contact Page: {contact_url}")
            scrape_contact_page(contact_url)
    else:
        print("No contact pages found.")

    print("\n\n************** Data sending to llama3 model **************\n\n")
    # LLM processing
    model_name = "llama3.2:latest"
    # model_name = "llama3:8b"
    problem = request.form['problem']
    
    prompt = (
        f"From the provided data '{web_data}', find the most relevant contact details for the issue: '{problem}'. "
        "Only provide Name, Designation, Contact Number, Email, and Address (if available). Focus exclusively on contacts; "
        "do not include unrelated information or explanations."
    )

    response = ollama.generate(model=model_name, prompt=prompt)
    contact_details = response['response']

    print("\n\n************** Response from the Model **************\n\n")
    print(contact_details)
    print("*****************************************************\n\n")

    # Clear `web_data` after generating the response to avoid stale data
    web_data.clear()
    return contact_details

if __name__ == '__main__':
    app.run(debug=True)