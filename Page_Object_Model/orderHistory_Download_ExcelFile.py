from selenium.webdriver.common.by import By

class DownloadExcelFile:
    headermenu_order_xpath = "(//span[text() = ' ORDER '])[1]"
    headermenu_orderhistory_xpath = "//a[text() = 'Order History ']"
    excelfile_icon_xapth = "(//span[@class='mat-button-wrapper'])[1]"


    def __init__(self, driver):
        self.driver = driver
        
    def click_Order(self):
        self.driver.find_element(By.XPATH, self.headermenu_order_xpath).click()
    
    def click_History(self):
        self.driver.find_element(By.XPATH, self.headermenu_orderhistory_xpath).click()
           
    def click_ExcelFile(self):
        self.driver.find_element(By.XPATH, self.excelfile_icon_xapth).click()
    
        