from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AddToCart:
    welcome_popup_xpath = "//button[text() = 'OK']"
    button_proceedtopayment_xpath = "//button[text() = 'PROCEED TO PAYMENT']"
    checkbox_click_xpath = "//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"
    button_placeorder_xpath = "//button[text() = 'Place Order']"
    linktext_ordernotconfirmed_xpath ="//a[text() = 'Orders Not Confirmed']"
    module_orderhistory_xpath ="//a[text() = 'Order History ']"    
    
        
    def __init__(self, driver):
        self.driver = driver
        
    def scrollPage(self):
        scroll_pixels = 350  # Adjust this value according to your needs
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_pixels)
        
    def clickWelcomeAccountPopup(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.welcome_popup_xpath))).click()
    
    def clickProceedToPaymentButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.button_proceedtopayment_xpath))).click()
        time.sleep(2)


    def scrollPlaceOrderPage(self):
        scroll_pixels = 350  # Adjust this value according to your needs
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_pixels)
         
    def clickCheckBox(self):
        checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_click_xpath))).click()
        time.sleep(2)

    def clickPlaceOrderButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.button_placeorder_xpath))).click()

    def clickOrdersNotConfirmed(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.linktext_ordernotconfirmed_xpath))).click()
        time.sleep(5)

    def clickOrderHistory(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.module_orderhistory_xpath))).click()

        
    