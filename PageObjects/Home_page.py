from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginScreen:

    def __init__(self, driver):
        #Constructor for Login Screen
        self.driver=driver
        self.username=WebDriverWait(self.driver.instance,20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#username")))
        self.password=WebDriverWait(self.driver.instance,20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
        #self.SignIn = self.driver.find_element_by_css_selector("button[ng-bind*='SIGN IN']")
        #self.Warning = self.driver.find_element_by_css_selector("span[class='warning']")

    def assign_values(self,user_name,pass_word):
        #Assign Values for Username and Password
        self.username.clear()
        self.password.clear()
        self.username.send_keys(user_name)
        self.password.send_keys(pass_word)

    def login(self):
        #Clicking the enter button to login
        self.SignIn = WebDriverWait(self.driver.instance, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[ng-bind*='SIGN IN']")))
        self.SignIn.click()

    def warning_message(self):
        #Return warning text displayed on screen
        self.Warning = WebDriverWait(self.driver.instance, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "span[class='warning']")))
        #self.Checkfield=WebDriverWaitself.driver.instance, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "span[class='f-size-1-rem']").__getattribute__()))
        return self.Warning.text