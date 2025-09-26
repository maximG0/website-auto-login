from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import json

def load_credentials(file_path='credentials.json'):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Credentials file {file_path} not found.")
    
    with open(file_path, 'r') as file:
        return json.load(file)

def login():
    driver = webdriver.Chrome()
    driver.get(creds.get('url'))
    driver.maximize_window()
    button = driver.find_element(By.LINK_TEXT, "Account")
    button.click()
    account_field = driver.find_element(By.ID, "txtUserName")
    password_field = driver.find_element(By.ID, "txtAccountPassword")
    account_field.send_keys(creds.get('username'))
    password_field.send_keys(creds.get('password'))
    password_field.send_keys(Keys.RETURN)
    time.sleep(int(creds.get('interval')))
    driver.quit()

if __name__ == "__main__":
    creds = load_credentials()
    while True:
        login()