import re
from typing import List, Dict
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.core.logging import logger
from app.services.mongo_client import get_policy_collection


class PolicyScraper:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.targets = [
            # Add government policy listing URLs here
        ]

    def parse_policy(self, html: str) -> Dict:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1")
        return {
            "title": title.get_text(strip=True) if title else "Untitled policy",
            "ministry": "Unknown",
            "category": "General",
            "eligibility": None,
            "benefits": None,
            "required_documents": None,
            "application_process": None,
            "deadline": None,
            "official_link": None,
            "target_audience": None,
            "summary": None,
            "source": None,
        }

    def fetch_page(self, url: str) -> str:
        logger.info("Scraping %s", url)
        self.driver.get(url)
        return self.driver.page_source

    def deduplicate(self, policies: List[Dict]) -> List[Dict]:
        seen = set()
        unique = []
        for policy in policies:
            key = policy.get("title", "").lower().strip()
            if key and key not in seen:
                seen.add(key)
                unique.append(policy)
        return unique

    def store_policies(self, policies: List[Dict]):
        collection = get_policy_collection()
        for policy in policies:
            query = {"title": policy["title"], "ministry": policy.get("ministry")}
            collection.update_one(query, {"$set": policy}, upsert=True)

    def run_scrape(self) -> Dict:
        results = []
        for url in self.targets:
            html = self.fetch_page(url)
            policy = self.parse_policy(html)
            policy["source"] = url
            results.append(policy)

        unique = self.deduplicate(results)
        self.store_policies(unique)
        return {"scraped": len(results), "stored": len(unique)}
