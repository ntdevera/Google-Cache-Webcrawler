import random
import time
import os
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json
import codecs
import pdfkit


c = webdriver.ChromeOptions()
#prefs = {'download.default_directory' : edited_folder}
#c.add_experimental_option('prefs', prefs)

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
           'savefile.default_directory': 'Downloads'}
c.add_experimental_option('prefs', profile)
c.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

#c.add_argument("--incognito")
c.add_argument("--no sandbox")
#c.add_argument("--start maximized")
#c.add_argument("--start-fullscreen")
c.add_argument("--single-process")
c.add_argument("--disable-dev-shm-usage")
c.add_argument("--disable-blink-features=AutomationControlled")
c.add_argument("--disable-infobars")
#remove automation flags
c.add_experimental_option('useAutomationExtension', False)
c.add_experimental_option("excludeSwitches", ["enable-automation"])
#modify user agent parameters
c.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5563.64 Safari/537.36")
driver = webdriver.Chrome(options=c)
delay = random.uniform(0.01, 0.05)  # Random delay between 100ms and 500ms
wait_time=300

def search_google(base_url,page):
    driver.get("https://www.google.com/")
    ## enter login info
    search_field = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#APjFqb')))
    for char in base_url:
        search_field.send_keys(char)
        time.sleep(delay)
    search_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                        'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b'))
    )
    search_button.click()
    time.sleep(1)
    if page==1:
        threedots_button = WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > div > div.csDOgf.BCF2pd.L48a4c > div > div > span > span > svg'))
        )
    else:
        threedots_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#rso > div > div > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > div > div.csDOgf.BCF2pd.L48a4c > div > div > span > span > svg > path'))
         )
    threedots_button.click()
    time.sleep(1)
    cached_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#gsr > div.h2Nkyc > div > div > div.OAssce > div > span > span > div > a > span'))
    )
    cached_button.click()
    time.sleep(1)
def go_through_page(question):
    button_1 = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div:nth-child(2) > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(1) > div.card-body.question-body > a.btn.btn-secondary.question-discussion-button.d-print-none'))
    )
    button_1.click()
    time.sleep(1)
    answer_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div.sec-spacer.pt-50 > div > div:nth-child(3) > div > div.discussion-header-container > div.question-body.mt-3.pt-3.border-top > a.btn.btn-primary.reveal-solution'))
    )
    answer_button.click()
    time.sleep(1)
    question=question+1
    current_url=driver.current_url
    download_page(current_url,question)
    driver.back()


    button_2 = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div:nth-child(2) > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(2) > div.card-body.question-body > a.btn.btn-secondary.question-discussion-button.d-print-none'))
    )
    button_2.click()
    time.sleep(1)
    answer_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div.sec-spacer.pt-50 > div > div:nth-child(3) > div > div.discussion-header-container > div.question-body.mt-3.pt-3.border-top > a.btn.btn-primary.reveal-solution'))
    )
    answer_button.click()
    time.sleep(1)
    question=question+1
    current_url = driver.current_url
    download_page(current_url, question)
    driver.back()

    button_3 = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div:nth-child(2) > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(3) > div.card-body.question-body > a.btn.btn-secondary.question-discussion-button.d-print-none'))
    )
    button_3.click()
    time.sleep(1)
    answer_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div.sec-spacer.pt-50 > div > div:nth-child(3) > div > div.discussion-header-container > div.question-body.mt-3.pt-3.border-top > a.btn.btn-primary.reveal-solution'))
    )
    answer_button.click()
    time.sleep(1)
    question=question+1
    current_url = driver.current_url
    download_page(current_url, question)
    driver.back()

    button_4 = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div:nth-child(2) > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(4) > div.card-body.question-body > a.btn.btn-secondary.question-discussion-button.d-print-none'))
    )
    button_4.click()
    time.sleep(1)
    answer_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          'body > div.sec-spacer.pt-50 > div > div:nth-child(3) > div > div.discussion-header-container > div.question-body.mt-3.pt-3.border-top > a.btn.btn-primary.reveal-solution'))
    )
    answer_button.click()
    time.sleep(1)
    question=question+1
    current_url = driver.current_url
    download_page(current_url, question)

    return question

# Press the green button in the gutter to run the script.

def download_page(url,page):
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # Point pdfkit configuration to wkhtmltopdf.exe
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    # Convert HTML file to PDF
    path = str(page)+".pdf"
    pdfkit.from_url(url, output_path=path, configuration=config)

if __name__ == '__main__':
    base_url = '"INPUT BASEURL'
    page = 10
    page_limit=44
    question = 4
    while page!=page_limit:
        if page== 1:
            base_url = '"INPUT BASEURL"'
        else:
            base_url = base_url + str(page) + '"'
        search_google(base_url,page)
        download_page(driver.current_url,page)
        time.sleep(60)
        #question=go_through_page(question)
        base_url = '"INPUT BASEURL'
        page=page+1


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
