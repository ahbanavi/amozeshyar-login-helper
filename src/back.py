from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle
from selenium.webdriver.common.keys import Keys
import time
import json

chrome_options = Options()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("headless")
chrome_options.add_argument("remote-debugging-port=9222")
chrome_options.add_argument("disable-gpu")

BASE_URL = "https://web.igap.net/"
CHAT_URL = BASE_URL + "app?q=@amoozeshbot"
LOGIN_URL = BASE_URL + "login"
PHONE = "9391234567"

d = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=chrome_options)


def login(phone=PHONE):
    d.find_element(By.NAME, "mobile").send_keys(phone)
    # sumbit
    d.find_element(By.ID, "submit").click()
    # click yes on xpath data-testid="confirm-mobile"
    d.find_element(By.XPATH, "//*[@data-testid='confirm-mobile']").click()
    code = input("Enter code: ")
    d.find_element(By.XPATH, "//*[@data-testid='otp-test-0']").send_keys(code)

    # sleep 5 sec
    time.sleep(5)

    d.get(CHAT_URL)

    # store cookies
    pickle.dump(d.get_cookies(), open("cookies.pkl", "wb"))


d.get(CHAT_URL)
time.sleep(1)

# login if not logged in
if d.current_url == LOGIN_URL:
    print("not logged in")
    login()

# get div that contains word
# div = d.find_element(By.XPATH, "//div[contains(text(), 'رمز ورود')]")


d.quit()
