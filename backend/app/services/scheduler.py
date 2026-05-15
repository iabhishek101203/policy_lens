from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.scraper import PolicyScraper
from app.core.logging import logger


class SchedulerService:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="UTC")
        self.scraper = PolicyScraper()

    def start(self):
        self.scheduler.add_job(self.scraper.run_scrape, "interval", hours=24, id="daily_policy_scrape")
        self.scheduler.start()
        logger.info("Policy scraping scheduler started")
