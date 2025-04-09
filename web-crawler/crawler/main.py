from concurrent.futures import ThreadPoolExecutor
import json
from crawler.crawler import Crawler
from crawler.crawler_config import CrawlerConfig
from typing import List
import os


def load_configs(config_file: str) -> List[CrawlerConfig]:
    return [CrawlerConfig(**config) for config in json.load(open(config_file))]


def save_urls_to_file(output_dir: str, website_name: str, urls: List[str]):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{website_name}_urls.txt")
    with open(file_path, "w") as file:
        for url in urls:
            file.write(url + "\n")


def process_crawl():
    config_path = os.path.join(os.path.dirname(__file__), "configs.json")
    output_dir = os.path.join(os.path.dirname(__file__), "output")

    for config in load_configs(config_path):
        print(f"Crawling {config.website_name}...")
        crawler = Crawler(config)
        product_urls = crawler.fetch_product_urls()
        save_urls_to_file(output_dir, config.website_name, product_urls)


def main():
    process_crawl()


if __name__ == "__main__":
    main()
