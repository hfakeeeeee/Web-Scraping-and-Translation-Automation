import argparse
import requests
import openai
import os
from bs4 import BeautifulSoup
from fpdf import FPDF

openai.api_key = ""

def remove_unwanted_parts(text):
    lines = text.splitlines()
    filtered_lines = []

    for line in lines:
        if not line.strip():
            continue
        if line.startswith("https://") or line.startswith("http://"):
            continue
        if len(line) > 10 and sum(1 for c in line if ord(c) < 128) / len(line) > 0.9:  
            if sum(1 for c in line if ord(c) > 128) / len(line) < 0.05:
                filtered_lines.append(line)

    return "\n".join(filtered_lines)

def crawl_and_clean(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for elem in soup(['script', 'style', 'aside', 'header', 'footer', 'nav']):
        elem.extract()

    content = soup.find('article')
    if content is None:
        content = soup.find('body')

    if content is None:
        return ""

    for a in content.find_all('a'):
        a.replace_with(a.get_text(strip=True))

    return content.get_text(strip=True)

def translate_text(text, target_language):
    max_chunk_size = 2000
    text_chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    translated_chunks = []

    for chunk in text_chunks:
        prompt = f"Translate the following text from Vietnamese to {target_language}: {chunk}"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
        translated_chunks.append(response.choices[0].text.strip())

    return " ".join(translated_chunks)


def export_to_pdf(translated_content, output_file):
    pdf = FPDF()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    pdf.add_page()
    pdf.set_font("Roboto", size=12)
    pdf.multi_cell(0, 10, translated_content)

    pdf.output(output_file)

parser = argparse.ArgumentParser(description="Translate vnexpress.net webpages")
parser.add_argument("N", type=int, help="Number of pages to crawl from homepage")
parser.add_argument("language", type=str, help="Target language for translation")
args = parser.parse_args()

def main(args):
    base_url = "https://vnexpress.net"
    homepage = requests.get(base_url)
    soup = BeautifulSoup(homepage.text, 'html.parser')

    article_links = [link['href'] for link in soup.find_all('a', href=True) if link['href'].startswith('https://vnexpress.net/') and 'title' in link.attrs][:args.N]

    print(f"Found {len(article_links)} article links:")
    print(article_links)

    for index, link in enumerate(article_links):
        print(f"Processing article {index + 1}: {link}") 
        content = crawl_and_clean(link)
        translated_content = translate_text(content, args.language)
        translated_content = remove_unwanted_parts(translated_content)

        output_file = f"output_{index + 1}.pdf"
        export_to_pdf(translated_content, output_file)
        print(f"Translated and saved {link} as {output_file}")

