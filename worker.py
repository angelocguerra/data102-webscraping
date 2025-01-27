# Selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service #microsft edge, change to webdriver.chrome.service for chrome

def scrape_more_info(url):
    data = []
    driver = webdriver.Chrome()
    driver.get(url)

    info_button = driver.find_element(By.XPATH, "//a[@class='toggle_info_btn']")
    
    # scroll and click 'more information' button 
    try:
        driver.execute_script("arguments[0].scrollIntoView();", info_button)
        info_button.click()
        time.sleep(2) # pause for it load a bit

    except NoSuchElementException:
        data.extend(["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"])
        driver.quit()
        return data
        
    status = driver.find_elements(By.XPATH, "//tr[td[text()='Status']]/td[2]")
    rating_row = driver.find_element(By.XPATH, "//tr[td[text()='Rating']]/td[2]")
    rating = rating_row.find_element(By.XPATH, "//div[@class='star_value']").get_attribute("content")
    rating_count = rating_row.find_element(By.XPATH, "//span[@class='rating_count']").get_attribute("content")
    tags = driver.find_elements(By.XPATH, "//tr[td[text()='Tags']]/td[2]")
    sesh_time = driver.find_elements(By.XPATH, "//tr[td[text()='Average session']]/td[2]")
    platforms = driver.find_elements(By.XPATH, "//tr[td[text()='Platforms']]/td[2]")

    # check if the element is empty
    data.append("N/A" if not status else status[0].text)
    data.append("N/A" if not rating else rating)
    data.append("N/A" if not rating_count else rating_count)
    data.append("N/A" if not tags else tags[0].text)
    data.append("N/A" if not sesh_time else sesh_time[0].text)
    data.append("N/A" if not platforms else platforms[0].text)
    driver.quit()

    return data