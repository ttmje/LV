import lxml
import markup as markup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
import pickle
import random
from faker import Faker
import string
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

#Генерим рандомную почту
def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

#Целевой URL
URL = 'https://pieraksts.mfa.gov.lv/ru/moskva'

#Прокси
proxy_username = "USERNAME"
proxy_password = "PASSWORD"

#Подключаем вебдрайвер
options = Options()
options = webdriver.ChromeOptions()

#Генерим рандомное имя
fake = Faker()
names = fake.name()

#список для прокси
proxys = []

mails = random_char(8) + "@gmail.com"
phone = '+79998887766'

#Генерируем фейковые юзерагенты
ua = UserAgent()
userAgent = ua.random

#Прокси и настройки хрома, открываем URL
#options.add_argument(f'--proxy-server=213.108.196.245:10053')
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.get(URL)

#Поиск элементов и заполенние формы

#STEP ONE
try:
    name = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div[1]/fieldset/div[1]/input')
    name.send_keys(names)
    time.sleep(0.1)

    surname = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div[1]/fieldset/div[2]/input')
    surname.send_keys(names)
    time.sleep(0.1)

    mail = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div[1]/fieldset/div[3]/input')
    mail.send_keys(mails)
    time.sleep(0.1)

    phone = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div[1]/fieldset/div[4]/input')
    phone.send_keys('+79998887766')
    time.sleep(0.1)

    button = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[3]/button')
    button.click()
    time.sleep(0.1)
except NoSuchElementException:
    pass
# STEP TWO
try:
    service = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div/section/div/div[1]')
    service.click()
    time.sleep(0.1)

    service_click = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div/section/div/div[2]/div[1]/label')
    service_click.click()
    time.sleep(0.1)

    checkbox = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div/section/div/div[2]/section[1]/div[2]/div[1]/label')
    checkbox.click()
    time.sleep(0.1)

    service_apply = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div/section/div/div[2]/section[1]/div[2]/div[2]/button')
    service_apply.click()
    time.sleep(0.1)

    apply = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[2]/button')
    apply.click()
    time.sleep(4)

    text = driver.find_element(By.XPATH, value='/html/body/main/section/form/div/div[1]/div/div').text
    if text == "Šobrīd visi pieejamie laiki ir aizņemti":
        print("Все доступные часы в настоящее время заняты")
    else:
        print('Беги скорее, места есть')


except NoSuchElementException:
    pass
