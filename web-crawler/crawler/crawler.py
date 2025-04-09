from concurrent.futures import Future, ThreadPoolExecutor
import time
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urljoin
import re

import urllib
from crawler.crawler_config import CrawlerConfig
from crawler import utils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Crawler:
    def __init__(self, config: CrawlerConfig):
        self.config = config
        self.visited = set()
        self.product_urls = set()
        self.queue = [config.base_url]
        self.visited.add(config.base_url)
        self.lock = None
        self.pending_futures = []

    def should_exclude(self, url: str) -> bool:
        return any(re.search(pattern, url) for pattern in self.config.exclude_patterns)

    def is_product_url(self, url: str) -> bool:
        return any(re.search(pattern, url) for pattern in self.config.match_patterns)

    def is_outside_base_domain(self, url: str) -> bool:
        return utils.domain(url) != self.config.domain

    def has_required_products(self) -> bool:
        return len(self.product_urls) >= self.config.max_products
    
    def should_crawl(self) -> bool:
        self.cleanup_futures()
        return (
            len(self.product_urls) < self.config.max_products
            and len(self.visited) < self.config.max_pages
            and (len(self.queue) > 0 or len(self.pending_futures) > 0)
        )
    
    def cleanup_futures(self):
        self.pending_futures = [x for x in self.pending_futures if x.running()]

    def is_visited(self, url: str) -> bool:
        return url in self.visited

    def get_next_urls(self, current_url: str) -> List[str]:
        if(self.has_required_products()):
            return []
        urls = set()
        if self.config.crawler == "SeleniumCrawler":
            next_links = SeleniumCrawler().get_next_url(current_url)
        else:
            next_links = SoupCrawler().get_next_url(
                current_url, headers=self.config.custom_headers
            )
        
        if(self.has_required_products()):
            return []
        for link in next_links:
            full_url = urljoin(self.config.base_url, link)
            if (
                self.should_exclude(full_url)
                or self.is_outside_base_domain(full_url)
                or self.is_visited(full_url)
            ):
                continue
            urls.add(full_url)
        return list(urls)

    def fetch_product_urls(self) -> List[str]:

        def process(current_url):
            if(self.has_required_products()):
                return []
            try:
                for url in (self.get_next_urls(current_url)):
                    if self.is_product_url(url):
                        self.product_urls.add(url)
                    if not self.is_visited(url):
                        self.visited.add(url)
                        self.queue.append(url)
            except Exception as e:
                print(f"Error fetching {current_url}: {e}")

        with ThreadPoolExecutor(10) as executor:
            while self.should_crawl():
                if len(self.queue) == 0:
                    # if we're here, we have pending futures but empty queue. Just wait
                    time.sleep(0.1)
                    continue
                current_url = self.queue.pop(0)
                self.pending_futures.append(executor.submit(process, current_url))
        
        print(f'done crawling {self.config.website_name}: total products found: {len(self.product_urls)}')
        return list(self.product_urls)


class SoupCrawler:
    def __init__(self):
        pass

    def get_next_url(self, url: str, headers={}):
        req = urllib.request.Request(url)
        for key, value in headers.items():
            req.add_header(key, value)

        response = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(response, "html.parser")
        anchors = soup.find_all("a", href=True)
        return [anchor["href"] for anchor in anchors]


class SeleniumCrawler:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    def get_next_url(self, url: str):
        self.driver.get(url)
        anchors = self.driver.find_elements(By.TAG_NAME, "a")
        urls = [
            anchor.get_attribute("href")
            for anchor in anchors
            if anchor.get_attribute("href")
        ]
        return urls

    def close(self):
        self.driver.quit()
