from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddToCartWithoutLogin:
    oil_def_coolant_button_xpath = "(//span[text() = ' OIL, DEF & COOLANT '])[1]"
    select_parts_xpath = "(//div[@class='prod-img mx-auto text-center position-relative'])[1]"
    addtocart_button_xpath = "//a[text() = ' Add To Cart']"
    icon_cart_id = "cart-details"
    button_viewcart_xpath = "//button[text() = 'View Cart']"
    button_next_xpath = "//button[text() = ' Next ']"
    button_proceedtopayment_xpath = "//button[text() = 'PROCEED TO PAYMENT']"  
    
        
    def __init__(self, driver):
        self.driver = driver
    
    def clickOilDefCoolant(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.oil_def_coolant_button_xpath))).click()
        time.sleep(5)

    def clickselectpart(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.select_parts_xpath))).click()
       
    def clickAddToCartButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.addtocart_button_xpath))).click()

    def clickIconCart(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.icon_cart_id))).click()
        
    def clickViewCartButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.button_viewcart_xpath))).click()
    
    def clickNextButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.button_next_xpath))).click()
        time.sleep(5)