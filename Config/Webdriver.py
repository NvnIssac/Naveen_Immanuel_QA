from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Driver:
    def __init__(self,url):
        #Constructor- Default Browser to be tested Chrome
        self.instance = webdriver.Chrome()
        self.instance.maximize_window()
        self.instance.get(url)
        timeout = 20  # seconds
        try:
            myElem = WebDriverWait(self.instance, timeout).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
            print("Page has been launched succesfully")
        except TimeoutException:
            print("Loading took too much time!")

    def browser_select(self,browser,url):
        #Selction of Browser to be tested for the Portal
        if browser=="Chrome":
            self.instance = webdriver.Chrome()
            self.instance.maximize_window()
        elif browser=="Firefox":
            self.instance = webdriver.Firefox()
            self.instance.maximize_window()
        elif browser=="Ie":
            self.instance = webdriver.Ie()
            self.instance.maximize_window()
        else:
            raise ValueError("Enter a browser option from Chrome or Firefox or Ie")
        self.instance.get(url)

    def open_web(self, url):
        #Open Web page
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("Enter Valid URL")

    def screenshot_page(self,Screen_path):
        #Take screenshot of page post validation
        self.instance.save_screenshot(Screen_path)

    def close_web(self):
        #Close web page post execution
        self.instance.quit()
