from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    login_button_icon_xpath = "//img[@tabindex='0']"

    # if you use otp method then call this command 
    enter_mobilenumber_xpath = "//input[@data-placeholder='Enter mobile number']"
    signin_button_xpath = "//button[text() = 'Sign in']"
    next_button_xpath = "//button[text() = 'Next']"
    
    # if you use password radio button mobile or password field then call this command  
    radio_button_password_id= "Password"
    textbox_mobile_number_xpath = "//input[@placeholder='Enter mobile number']"
    texbox_password_xpath = "//input[@formcontrolname='password']"
    button_signin_xpath = "//button[text() = 'Sign in']"

    def __init__(self, driver):
        self.driver = driver
        
    def clickloginIconButton(self):
        self.driver.find_element(By.XPATH, self.login_button_icon_xpath).click()


    # if you use otp method then call this command
    def clickEnterMobileNumber(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.enter_mobilenumber_xpath))).send_keys("8109160706")

    def clickSignInButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.signin_button_xpath))).click()
        time.sleep(20)

    def clickNextButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.next_button_xpath))).click()


    # if you use password radio button mobile or password field then call this command  
    def clickPasswordRadioButton(self):
        self.driver.find_element(By.ID, self.radio_button_password_id).click()
        
    def setModileNumber(self, mobilenumber):
        self.driver.find_element(By.XPATH, self.textbox_mobile_number_xpath).send_keys(mobilenumber)
        
    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.texbox_password_xpath).send_keys(password)
        
    def clickSignIn(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()
        