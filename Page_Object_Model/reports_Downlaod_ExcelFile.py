from selenium.webdriver.common.by import By

class ReportsDownloadExcelFile:
    headermenu_reports_xpath = "(//span[text() = ' REPORTS '])[1]"
    excelfile_icon_xapth = "(//span[@class='mat-button-wrapper'])[1]"


    def __init__(self, driver):
        self.driver = driver
        
    def click_Reports(self):
        self.driver.find_element(By.XPATH, self.headermenu_reports_xpath).click()

    def click_ExcelFile(self):
        self.driver.find_element(By.XPATH, self.excelfile_icon_xapth).click()
    
        