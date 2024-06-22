import os
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin, urlparse

def create_directories(base_dir):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    js_dir = os.path.join(base_dir, 'javascript')
    php_dir = os.path.join(base_dir, 'php')
    other_dir = os.path.join(base_dir, 'others')

    for dir_path in [js_dir, php_dir, other_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
    return js_dir, php_dir, other_dir

def save_content(url, content, base_dir):
    parsed_url = urlparse(url)
    path = parsed_url.path.lstrip('/')
    if path.endswith('.js'):
        save_path = os.path.join(base_dir, 'javascript', path)
    elif path.endswith('.php'):
        save_path = os.path.join(base_dir, 'php', path)
    else:
        save_path = os.path.join(base_dir, 'others', path)

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with open(save_path, 'wb') as f:
        f.write(content)

def crawl(url, base_dir, visited):
    if url in visited:
        return
    visited.add(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return

    save_content(url, response.content, base_dir)

    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])
        if urlparse(next_url).netloc == urlparse(url).netloc:
            crawl(next_url, base_dir, visited)

def main():
    parser = argparse.ArgumentParser(description='Web crawler to recursively navigate web pages and store content.')
    parser.add_argument('start_url', help='The starting URL for the web crawler')
    parser.add_argument('output_dir', help='The directory where the retrieved content will be stored')
    
    args = parser.parse_args()
    
    js_dir, php_dir, other_dir = create_directories(args.output_dir)
    
    visited = set()
    crawl(args.start_url, args.output_dir, visited)

if __name__ == "__main__":
    main()
