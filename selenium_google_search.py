# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_XPATH = '//*[@name="q"]'
WIKI_XPATH = '//h3//*[@href="https://en.wikipedia.org/wiki/Quality_assurance"]'
WIKI_LOGO_XPATH = '//*[@class="mw-wiki-logo"]'
LINK_XPATH = '//*[@href="https://en.wikipedia.org/wiki/Quality_assurance"]'

driver = webdriver.Chrome("C:\\Users\\Denis\\PycharmProjects\\untitled3\\chromedriver.exe")

# Go to www.google.com, search for the term “QA”
driver.get("https://www.google.com")
input_element = driver.find_element(By.XPATH, SEARCH_XPATH)
input_element.send_keys("QA")
input_element.submit()

# Click the 2nd link (https://en.wikipedia.org/wiki/Software_quality_assurance)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, WIKI_XPATH)))
result = driver.find_element(By.XPATH, WIKI_XPATH)
result.click()

# Wait for page to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, WIKI_LOGO_XPATH)))

# Verify that this page contains a link to “http://en.wikipedia.org/wiki/Quality_assurance”
wiki_link = driver.find_element(By.XPATH, LINK_XPATH)
assert 'https://en.wikipedia.org/wiki/Quality_assurance' in wiki_link.get_property(name='href')

# "http..." assertion would fail, it's "https..." time now :)
assert 'http://en.wikipedia.org/wiki/Quality_assurance' not in wiki_link.get_property(name='href')
