# import yaml
import yaml
with open('config.yml', 'r') as yml:
    config = yaml.safe_load(yml)

# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
memo_url = config['memo_url']

# html_text = requests.get(login_url).text
# soup = BeautifulSoup(html_text, 'html.parser')

# メモ起動処理
memo_url = config['memo_url']
browser.get(memo_url)

text_area = browser.find_element(By.XPATH, '//*[@id="main"]')

text_area.send_keys(config['memo_temp'])
browser.execute_script("window.open('https://www.linkedin.com/search/results/all/?keywords=%E6%AD%A6%E7%94%B0&sid=_9K');")
