## Web Scraping and Translation Automation

This Python project automates the process of crawling news articles from [vnexpress.net](https://vnexpress.net), translating them into multiple languages through OpenAI's API, and exporting the translated content as PDF files. It is designed to minimize manual effort for content translation and localization.

## Features

- **Automated Web Scraping**: Fetches articles from the homepage of `vnexpress.net`.
- **Content Cleaning**: Removes unnecessary HTML elements (e.g., scripts, styles, footers) to extract clean text.
- **AI Translation**: Translates the extracted Vietnamese text into any specified target language.
- **PDF Export**: Saves translated articles as PDF files.
- **Command-Line Interface**: Allows customization of the number of articles and target translation language.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hfakeeeeee/Web-Scraping-and-Translation-Automation.git
    ```

2. Navigate to the project directory:
    ```bash 
    cd /Web-Scraping-and-Translation-Automation
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the project, use the following command:

```bash
python main.py <number_of_articles> <target_language>
```
For example, to scrape and translate 3 articles into English:

```bash
python main.py 3 English
```

This will save the translated articles as PDF files in the project directory.

## Dependencies
Python 3.x
requests
beautifulsoup4
openai
FPDF
argparse

# API Key Setup
Make sure to replace the openai.api_key in the main.py file with your own OpenAI API key.