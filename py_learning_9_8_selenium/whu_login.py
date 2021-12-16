from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe")
    url = "https://cas.whu.edu.cn/authserver/login?service=https%3A%2F%2Fehall.whu.edu.cn%3A443%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.whu.edu.cn%2Fnew%2Findex.html"
    user_name = "2020302111298"
    password = "21341X"
    driver.get(url)
    user_name_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    login_button = driver.find_element_by_tag_name("button")
    user_name_input.send_keys(user_name)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    login_button.click()
