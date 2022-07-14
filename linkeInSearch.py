# import yaml
import yaml
with open('config.yml', 'r') as yml:
    config = yaml.safe_load(yml)

# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()

login_url = config['login_url']
browser.get(login_url)
elem_username = browser.find_element(By.XPATH, '//*[@id="username"]')
elem_password = browser.find_element(By.XPATH, '//*[@id="password"]')
elem_username.send_keys(config['login_email'])
elem_password.send_keys(config['login_password'])
sleep(1)
elem_login_btn = browser.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
if elem_login_btn:
    elem_login_btn.click()


# メモ起動処理
print('検索する担当者名、会社名(スペースを空けてください。)')

customer_name, company_name= input('>> ').split()
memo_url = config['memo_url']
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[-1])
browser.get(memo_url)
text_area = browser.find_element(By.XPATH, '//*[@id="main"]')

message = config['memo_temp'].replace('CUSTOMER_NAME',customer_name)
message = message.replace('COMPANY_NAME', company_name)
text_area.send_keys(message)

# 検索処理
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[-1])
search_url = config['search_url']
browser.get(search_url + customer_name)

sleep(30)

browser.close()
