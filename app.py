from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse
import together
import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer

app = Flask(__name__)
CORS(app)

with open("api_key.txt","r") as api_key_file:
   key = api_key_file.read()

if key == '':
    print("No API key found in api_key.txt")
else:
    client = together.Together(api_key=key)

# Load BART model and tokenizer for webpage content summarization
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def extract_text_from_webpage(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3'])
    text_content = ' '.join([para.get_text() for para in paragraphs])
    return text_content

@app.route("/website_info", methods=["POST"])
def website_info():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({'error': 'URL not provided'}), 400

    try:
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split('.')

        if 'www' in domain_parts:
            domain_parts.remove('www')

        if len(domain_parts) >= 2:
            website_name = domain_parts[-2].title()
            formatted_website_name = website_name.replace('-', ' ').title()
            prompt = f"Provide a 2-line summary of the website {formatted_website_name}."
            completion = client.chat.completions.create(model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", messages=[{"role": "user", "content": prompt}])
            summary_text = completion.choices[0].message.content.replace('\n', '').strip()
            return jsonify({'summary': summary_text})  # Return as JSON
        else:
            return jsonify({"error": "Invalid domain"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/summarize_webpage", methods=["POST"])
def summarize_webpage():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({'error': 'URL not provided'}), 400

    try:
        webpage_text = extract_text_from_webpage(url)
        if not webpage_text.strip():
            return jsonify({'error': 'No content found on the webpage.'}), 400

        summary = summarize_text(webpage_text)
        return jsonify({'summary': summary})  # Return as JSON

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
