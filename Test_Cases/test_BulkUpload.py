import pytest
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.bulkUpload import BulkUpload
from Page_Object_Model.addToCartWithoutLogin import AddToCartWithoutLogin
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


class Test_004_BulkUplaod:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    # bulkuploadpath = ReadConfig.getBulkUploadFile()
    logger = LogGen.loggen()

    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_BulkUpload(self, setup):
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
            self.bulkup.clickBulkOrderUpload()
            self.bulkup.uploadBulkFile()
            self.bulkup.clickSumbitButton()

            self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
            self.addcartwithoutogin.clickIconCart()

            self.bulkup.clickViewCartButton()

            self.addcartwithoutogin.clickNextButton()

            self.addcart = AddToCart(self.driver)
            self.addcart.scrollPage()
            self.addcart.clickProceedToPaymentButton()
            self.addcart.scrollPlaceOrderPage()
            self.addcart.clickCheckBox()
            self.addcart.clickPlaceOrderButton()
            self.addcart.clickOrdersNotConfirmed()
            self.addcart.clickOrderHistory()
                
            self.driver.quit()
        finally:
            try:
                self.driver.save_screenshot(".\\Screenshots\\" + "Failed_BulkUpload.png")
            except Exception as e:
                print(f"failed to the screenshot: {e}")