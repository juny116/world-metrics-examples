"""Read numeric counters from a rendered Worldometer page."""
from bs4 import BeautifulSoup

def parse_counters(html):
    results = {}
    for counter in BeautifulSoup(html, "html.parser").select(".counter-group"):
        heading = counter.select_one("div.counter-heading")
        item = heading.select_one("span.counter-item") if heading else None
        if item is None:
            continue
        digits = "".join(s.get_text(strip=True) for s in heading.select("span.counter-number > span.rts-counter"))
        digits = digits.replace(",", "").replace(" ", "")
        if digits.isdigit():
            results[item.get_text(strip=True).replace(" ", "_").lower()] = int(digits)
    return results

def collect_counters(driver_factory=None):
    if driver_factory is None:
        from selenium import webdriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver_factory = lambda: webdriver.Chrome(options=options)
    driver = driver_factory()
    try:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        driver.get("https://www.worldometers.info")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#c1")))
        return parse_counters(driver.page_source)
    finally:
        driver.quit()
