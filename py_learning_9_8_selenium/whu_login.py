from selenium import webdriver
import time
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver_version_96/chromedriver.exe")
    url = "https://cas.whu.edu.cn/authserver/login?service=https%3A%2F%2Fehall.whu.edu.cn%3A443%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.whu.edu.cn%2Fnew%2Findex.html"
    user_name = input("user")
    password = input("password")
    driver.get(url)
    user_name_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")
    user_name_input.send_keys(user_name)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    login_button.click()
