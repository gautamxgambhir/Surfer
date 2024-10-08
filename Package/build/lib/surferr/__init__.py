import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer
import warnings
from urllib.parse import urlparse
import together
import socket

__version__ = '0.6'

def version():
    return __version__

warnings.filterwarnings("ignore", message=r"`clean_up_tokenization_spaces` was not set", category=FutureWarning)

class Surfer: 
    def __init__(self, api_key):
        self.client = together.Together(api_key=api_key)
        self.model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)

    def summarize_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        return summary

    def extract_text_from_webpage(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3'])
            text_content = ' '.join([para.get_text() for para in paragraphs])
            return text_content
        except requests.exceptions.RequestException as e:
            return f"Error fetching webpage: {str(e)}"

    def summarize_webpage(self, url):
        webpage_text = self.extract_text_from_webpage(url)
        if not webpage_text.strip():
            return "No content found on the webpage."

        try:
            inputs = self.tokenizer(webpage_text, return_tensors="pt", max_length=1024, truncation=True)
            summary_ids = self.model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
            return summary
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
    def website_info_summary(self, url):
        if not url:
            return "Error: URL not provided"
        try:
            socket.create_connection(("www.google.com", 80))
            parsed_url = urlparse(url)
            domain_parts = parsed_url.netloc.split('.')
            if 'www' in domain_parts:
                domain_parts.remove('www')

            if len(domain_parts) >= 2:
                website_name = domain_parts[-2].title()
                formatted_website_name = website_name.replace('-', ' ').title()
                prompt = f"Provide a 2-line summary of the website {formatted_website_name}."
                completion = self.client.chat.completions.create(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", messages=[{"role": "user", "content": prompt}])
                summary_text = completion.choices[0].message.content.replace('\n', '').strip()
                return summary_text
            else:
                return "Error: Invalid Domain"
        except OSError:
            return "Network error. Please check your internet connection and try again."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

__all__ = ['website_info_summary','summarize_webpage','extract_from_webpage','summarize_text','version']