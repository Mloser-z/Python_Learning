from selenium import webdriver

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe", options=chrome_options)
    url = "https://www.bilibili.com/v/popular/all?spm_id_from=333.851.b_7072696d61727950616765546162.3"
    browser.get(url)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    print(browser.page_source)
