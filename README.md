<div align="center">
  <img src="https://i.ibb.co/gDjsWyg/Logo-Image.png"><br>
</div>

-----------------

# Surfer: AI-Powered Website & Webpage Summarizer

![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![License](https://img.shields.io/badge/license-MIT-red)
![Together-AI](https://img.shields.io/badge/Together%20AI-0f6fff
)
![BART](https://img.shields.io/badge/BART-8A2BE2)

## What is it?

Surfer is an AI-powered Chrome extension designed to make web browsing faster and smarter by summarizing both website overviews and webpage content. 
Whether you're doing in-depth research or just exploring a new site, 
Surfer delivers concise summaries tailored to your needs.
With Surfer, you can :
 - Get brief website summaries with just two lines of information.
 - Generate detailed webpage content summaries from articles, blogs, and more.
 - Choose between paragraph summaries or bullet points for a customized reading experience.

## Main Features

Here’s what makes **Surfer** essential :

 - **Website Information Summarization** : Receive a 2-line overview of any website for a quick glance at its purpose and content.
 - **Webpage Content Summarization** : Get comprehensive summaries of webpage content in a concise format. 
 - **Real-time API Integration** : Surfer uses Together API and state-of-the-art models like BART for real-time summarization. 

## Where to get it?

The extension is hosted on GitHub at : https://github.com/your-repo-link/surfer

## Installation and Setup

#### 1. Clone the repository :
``` 
git clone https://github.com/your-repo-link/surfer.git 
```

#### 2. Backend setup (Make sure the ```app.py``` server is running) :
 - Navigate to the project directory.
 - Install the required Python dependencies :
    ```
    pip install -r requirements.txt
    ```
 - Make sure to enter your [Together AI]("https://www.together.ai/") API key in ```api_key.txt```.

 - Start the Flask server :
    ```
    python app.py
    ```
#### 2. Load the extension in Chrome :
 - Go to **chrome://extensions/** in your browser.
 - Enable **Developer Mode** in the top-right corner.
 - Click **Load unpacked** and select the ```surfer``` directory.

## Usage
Once installed, Surfer can summarize websites and webpage content directly from your Chrome browser :
#### 1. Open the Surfer Extension :
 - Click on the Surfer icon in your Chrome toolbar.
#### 2. Select a Radio Button :
 - **Website Information** : Summarizes the website's core details.
- **Webpage Content Summary** : Summarizes the visible content of the webpage you're currently on.
#### 3. Submit Button :
 - Click **Submit** to get the summary of the webpage or website information directly in the extension's popup.

## Requirements
 - **Flask** : Backend server for handling summarization requests.
 - **Together API** : Real-time AI API for generating summaries.
 - **BART Model** : Summarization model for content extraction.

## Contact

- `Email` - ggambhir1919@gmail.com
- `Instagram` - https://www.instagram.com/gautamxgambhir/
- `Twitter` - https://www.twitter.com/gautamxgambhir/