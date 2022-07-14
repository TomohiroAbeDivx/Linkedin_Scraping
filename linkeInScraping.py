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

# html_text = requests.get(login_url).text
# soup = BeautifulSoup(html_text, 'html.parser')

# login処理
browser.get(login_url)
elem_username = browser.find_element(By.XPATH, '//*[@id="username"]')
elem_password = browser.find_element(By.XPATH, '//*[@id="password"]')
elem_username.send_keys(config['login_email'])
elem_password.send_keys(config['login_password'])
sleep(1)
elem_login_btn = browser.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
elem_login_btn.click()
