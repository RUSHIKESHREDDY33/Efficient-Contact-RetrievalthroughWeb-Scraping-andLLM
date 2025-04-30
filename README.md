
# Efficient Contact RetrievalthroughWeb Scraping andLLM

This project is a Flask web application that helps users extract relevant contact details from a given website and then processes the collected data using an LLM (LLaMA) to provide the most relevant contact information based on a user-defined problem.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Folder Structure](#folder-structure)

## Overview
The application performs two main tasks:
1. **Web Scraping**: Extracts potential contact page URLs from a given website and scrapes the contact details from those pages.
2. **LLM Processing**: Uses the `ollama` library and an LLM model (LLaMA) to process the scraped data and return contact information relevant to the user's problem.

## Features
- Web scraping using `requests` and `BeautifulSoup` to find and extract content from contact pages.
- Automatic identification of relevant contact pages on a website.
- Data processing with a pre-trained LLaMA model using the `ollama` library to filter and display important contact details.
- Simple and intuitive web interface for input and result display.

## Setup
Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.x
- Flask
- `requests` library
- `beautifulsoup4` library
- `ollama` library
- Any additional dependencies listed in the `requirements.txt` 

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yaswanthreddytadipatri/Automated-Contact-Search-Using-LLMs-and-Web-Scraping.git
   cd Automated-Contact-Search-Using-LLMs-and-Web-Scraping
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and run llama3 8B**:
   ```bash
   ollama pull llama3.2
   ```

4. **Run the Flask app**:
   ```bash
   python server.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage
1. **Enter the main URL**: On the home page (`front.html`), enter the base URL of the website you want to scrape.
2. **Describe the problem**: Provide a brief description of your problem or issue that will help the LLaMA model filter the contact details.
3. **Submit**: Click the submit button to start the scraping and LLM processing.
4. **View results**: The application will return the most relevant contact details, such as Name, Designation, Contact Number, Email, and Address.

## Dependencies
- **Flask**: Web framework for building the application.
- **requests**: Library for making HTTP requests.
- **BeautifulSoup (bs4)**: HTML parsing library for web scraping.
- **ollama**: Library for interacting with the LLaMA model.
- **urllib.parse**: For URL joining and manipulation.

Install dependencies using:
```bash
pip install Flask requests beautifulsoup4 ollama
```

## Folder Structure
```
/project-root
│
├── server.py               # Main Flask application code
├── templates
│   └── front.html          # HTML template for the user interface
├── requirements.txt        # List of project dependencies
└── README.md               # This README file
```
