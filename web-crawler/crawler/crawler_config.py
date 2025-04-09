from crawler import utils


class CrawlerConfig:
    def __init__(
        self,
        base_url: str,
        website_name: str,
        max_pages: int,
        max_products: int,
        exclude_patterns: list = None,
        match_patterns: list = None,
        crawler: str = "SoupCrawler",
        custom_headers: dict = {},
    ):
        self.base_url = base_url
        self.website_name = website_name
        self.max_pages = max_pages
        self.max_products = max_products
        self.exclude_patterns = exclude_patterns or []
        self.match_patterns = match_patterns or []
        self.domain = utils.domain(base_url)
        self.crawler = crawler
        self.custom_headers = custom_headers
