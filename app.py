import streamlit as st
import requests
from bs4 import BeautifulSoup
import ollama
from urllib.parse import urljoin

st.set_page_config(page_title="Efficient Contact Retriever", layout="centered")
st.title("🔍 Efficient Contact Retrieval through Web Scraping and LLM")

st.markdown("Enter a website URL and your issue/problem. The app will extract contact-related information using web scraping and LLM.")

# Get user input
url = st.text_input("Website URL", "https://example.com")
problem = st.text_area("Briefly describe your issue", placeholder="e.g. I need technical support for my product...")

# Initialize web data container
web_data = []

def find_contact_pages(base_url):
    response = requests.get(base_url)
    if response.status_code != 200:
        st.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

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
        st.warning(f"Failed to retrieve contact page: {url}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    web_data.append(soup.get_text(separator='\n', strip=True))

if st.button("Extract Contact Info"):
    if url and problem:
        st.info("🔎 Searching for contact pages...")
        contact_urls = find_contact_pages(url)

        if contact_urls:
            for contact_url in contact_urls:
                st.write(f"Scraping: {contact_url}")
                scrape_contact_page(contact_url)

            # Send to LLM
            st.info("🤖 Generating contact info using LLM...")
            model_name = "llama3.2:latest"

            prompt = (
                f"From the provided data '{web_data}', find the most relevant contact details for the issue: '{problem}'. "
                "Only provide Name, Designation, Contact Number, Email, and Address (if available). Focus exclusively on contacts; "
                "do not include unrelated information or explanations."
            )

            try:
                response = ollama.generate(model=model_name, prompt=prompt)
                contact_details = response['response']
                st.success("✅ Contact Information Retrieved:")
                st.code(contact_details)
            except Exception as e:
                st.error(f"LLM Error: {str(e)}")

            web_data.clear()
        else:
            st.warning("No contact-related pages found.")
    else:
        st.warning("Please enter both URL and problem description.")
