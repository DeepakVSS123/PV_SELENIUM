from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SetPassword:
    header_menu_setpassword_xpath = "(//a[text() = 'Set Password'])[2]"
    button_request_otp_xpath = "//*[text() = 'Request OTP For Set Password']"
    textfield_password_xpath = "(//input[@type='password'])[1]"
    textfield_confirm_password_xpath = "(//input[@type='password'])[2]"
    button_save_xpath = "//button[text() = 'Save']"
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_HeaderMenu_SetPassword(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.header_menu_setpassword_xpath))).click()
          
    def click_Button_Request_OTP(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.button_request_otp_xpath))).click()
       
    def enter_Password(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.textfield_password_xpath)))
        element.send_keys("Tata9812@")
        
    def enter_Confirm_Password(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.textfield_confirm_password_xpath)))
        element.send_keys("Tata9812@")
        
    def click_Button_Save(self):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_save_xpath)))
        element.click()
