from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def send_image(driver, recipient, image_path):
    driver.get(f'https://www.instagram.com/direct/t/{recipient}/')
    time.sleep(2)
    driver.find_element_by_xpath('//input[@accept="image/*"]').send_keys(image_path)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
