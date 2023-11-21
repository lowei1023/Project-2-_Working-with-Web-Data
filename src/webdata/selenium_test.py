from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def get_article_count(self):
        try:
            self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
            
            # Apply an implicit wait
            self.driver.implicitly_wait(10)  # Waits for 10 seconds
            
            # Explicit wait for the element to be clickable
            article_count = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#articlecount a")))
            
            return article_count.text
        except NoSuchElementException as e:
            print("Element not found:", e)
        finally:
            self.driver.quit()

# Usage
scraper = WikipediaScraper()
count = scraper.get_article_count()
print(count)
