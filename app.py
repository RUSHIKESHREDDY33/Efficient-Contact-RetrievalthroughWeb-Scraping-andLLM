import streamlit as st
from your_scraping_function import scrape_contact_info  # Your function to scrape contacts

st.title("Efficient Contact Retrieval App")
st.write("Enter a website URL below to extract contact-related information.")

url = st.text_input("Website URL", "https://example.com")

if st.button("Extract Contact Info"):
    if url:
        try:
            result = scrape_contact_info(url)  # Call your scraping function
            st.success("Contact Info Retrieved!")
            st.write(result)  # Display the result
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a valid URL.")
