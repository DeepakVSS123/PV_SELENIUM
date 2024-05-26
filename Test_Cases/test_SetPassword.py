import pytest
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.setPassword import SetPassword
from Page_Object_Model.bulkUpload import BulkUpload
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


class Test_007_SetPassword:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_SetPassword(self, setup):
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
            
            self.setpwd = SetPassword(self.driver)
            self.setpwd.click_HeaderMenu_SetPassword()
            self.setpwd.click_Button_Request_OTP()
            # self.setpwd.enter_OTP()
            # time.sleep(15)
            self.setpwd.enter_Password()
            self.setpwd.enter_Confirm_Password()
            self.addcart = AddToCart(self.driver)
            self.addcart.scrollPage()
            
            self.setpwd.click_Button_Save()
        
            time.sleep(10)
            self.driver.quit()
        
        finally:
            try:
                self.driver.save_screenshot(".\\Screenshots\\" + "Failed_SetPassword.png")
            except Exception as e:
                print(f"failed to the screenshot: {e}")