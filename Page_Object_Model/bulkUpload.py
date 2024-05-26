from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from Utilities.readProperties import ReadConfig

import time

class BulkUpload:

    bulkuploadpath = ReadConfig.getBulkUploadFile()

    headermenu_mydashboard_xpath = "(//span[text() = ' MY DASHBOARD '])[1]"
    headermenu_bulkorderupload_xpath = "//a[text() = 'Bulk Order Upload ']"
    upload_button_xpath = "//mat-icon[text() = 'file_upload']"
    sumit_button_xpath = "//button[text() = 'Submit']"
    viewcart_button_xpath = "//button[text() = 'View all items']"

    
    def __init__(self, driver):
        self.driver = driver
        
    def clickMyDashboard(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.headermenu_mydashboard_xpath))).click()

    def clickBulkOrderUpload(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.headermenu_bulkorderupload_xpath))).click()
    
    def uploadBulkFile(self):
        self.driver.find_element(By.XPATH, self.upload_button_xpath).click()
        time.sleep(3)
        keyboard =  Controller()
        keyboard.type("C:\\All Project\\PV\\Customer_portal\\Bulk_Order_Upload.xlsx")

        # keyboard.type(self.bulkuploadpath)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    
    def clickSumbitButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sumit_button_xpath))).click()

    def clickViewCartButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.viewcart_button_xpath))).click()