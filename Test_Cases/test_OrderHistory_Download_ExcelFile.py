import pytest
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.bulkUpload import BulkUpload
from Page_Object_Model.orderHistory_Download_ExcelFile import DownloadExcelFile
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


# ************** Working code ************************

class Test_005_OrderHistoryDownloadExcel:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_OrderHistoryExcelDownload(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            
             # When we use otp method then use this code
            self.lp = LoginPage(self.driver)
            self.lp.clickloginIconButton()
            self.lp.clickEnterMobileNumber()
            self.lp.clickSignInButton()
            self.lp.clickNextButton()

            # When we use mobile no. with password filed then use this code
            '''self.lp.clickPasswordRadioButton()
            self.lp.setModileNumber(self.mobilenumber)
            self.lp.setPassword(self.password)
            self.lp.clickSignIn()''' 
        
            self.addcart = AddToCart(self.driver)
            self.addcart.clickWelcomeAccountPopup()
            
            self.bulkup = BulkUpload(self.driver)
            self.bulkup.clickMyDashboard()
            
            self.dwnexcel = DownloadExcelFile(self.driver)
            self.dwnexcel.click_Order()
            self.dwnexcel.click_History()
            self.dwnexcel.click_ExcelFile()
            
            print("Excel sheet Dowload successfully")
            time.sleep(20)
            self.driver.quit()
            
        finally:
            try:
                self.driver.save_screenshot(".\\Screenshots\\" + "Failed_OrderHistory_Download_Excelsheet.png")
            except Exception as e:
                print(f"failed to the screenshot: {e}")
        
        