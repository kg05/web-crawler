import asyncio
import unittest
from crawler.crawler import Crawler, CrawlerConfig


class TestCrawler(unittest.TestCase):
    def test_crawl_virgio(self):
        async def async_test():
            config = CrawlerConfig(
                base_url="https://www.virgio.com/",
                website_name="Virgio",
                max_pages=200,
                max_products=10,
                exclude_patterns=[".*login.*", ".*cart.*"],
                match_patterns=["/products/"],
                custom_headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                },
                crawler="SoupCrawler",
            )
            crawler = Crawler(config)
            result =  crawler.fetch_product_urls()
            self.assertIsInstance(result, list)
            for url in result:
                self.assertIsInstance(url, str)
                self.assertTrue(url.startswith("http"))

        asyncio.run(async_test())

    def test_crawl_tatacliq(self):
        async def async_test():
            config = CrawlerConfig(
                base_url="https://www.tatacliq.com/",
                website_name="TataCliq",
                max_pages=150,
                max_products=20,
                exclude_patterns=[".*signin.*", ".*checkout.*"],
                match_patterns=["/p-mp"],
                custom_headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                },
                crawler="SeleniumCrawler",
            )
            crawler = Crawler(config)
            result = crawler.fetch_product_urls()
            self.assertIsInstance(result, list)
            for url in result:
                self.assertIsInstance(url, str)
                self.assertTrue(url.startswith("http"))

        asyncio.run(async_test())

    def test_crawl_nykaa(self):
        async def async_test():
            config = CrawlerConfig(
                base_url="https://nykaafashion.com/",
                website_name="Nykaa",
                max_pages=1500,
                max_products=20,
                exclude_patterns=[ ".*account.*",".*wishlist.*"],
                match_patterns=["/p/"],
                custom_headers={
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "no-cache",
                    "pragma": "no-cache",
                    "priority": "u=0, i",
                    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"macOS\"",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "none",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
                },
                crawler="SoupCrawler",
            )
            crawler = Crawler(config)
            result = crawler.fetch_product_urls()
            self.assertIsInstance(result, list)
            for url in result:
                self.assertIsInstance(url, str)
                self.assertTrue(url.startswith("http"))

        asyncio.run(async_test())

    def test_crawl_westside(self):
        async def async_test():
            config = CrawlerConfig(
                base_url="https://www.westside.com/",
                website_name="Westside",
                max_pages=1500,
                max_products=20,
                exclude_patterns=[".*account.*", ".*order.*"],
                match_patterns=["/shop/", "/products/"],
                custom_headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                },
                crawler="SeleniumCrawler",
            )
            crawler = Crawler(config)
            result =  crawler.fetch_product_urls()
            self.assertIsInstance(result, list)
            for url in result:
                self.assertIsInstance(url, str)
                self.assertTrue(url.startswith("http"))

        asyncio.run(async_test())


if __name__ == "__main__":
    unittest.main()
