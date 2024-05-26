import pytest
from Page_Object_Model.addToCartWithoutLogin import AddToCartWithoutLogin
from Page_Object_Model.login_page import LoginPage
from Page_Object_Model.addToCartWithLogin import AddToCart
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time

# ************** Working code ************************

class Test_003_AddToCartWithLogin:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    Logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_addToCartWithLogin(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            
            # using WithoutLogin addtocart test data
            self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
            self.addcartwithoutogin.clickOilDefCoolant()   
            self.addcartwithoutogin.clickselectpart()
            self.addcartwithoutogin.clickAddToCartButton()
            self.addcartwithoutogin.clickIconCart()
            self.addcartwithoutogin.clickViewCartButton()
            self.addcartwithoutogin.clickNextButton()

            # When we use otp method then use this code
            self.lp = LoginPage(self.driver)
            self.lp.clickEnterMobileNumber()
            self.lp.clickSignInButton()
            self.lp.clickNextButton()

            # When we use mobile no. with password filed then use this code
            '''self.lp.clickPasswordRadioButton()
            self.lp.setModileNumber(self.mobilenumber)
            self.lp.setPassword(self.password)
            self.lp.clickSignIn()'''

            # using login Addtocart data
            self.addcart = AddToCart(self.driver)
            self.addcart.clickWelcomeAccountPopup()

            # using WithoutLogin addtocart test data
            self.addcartwithoutogin = AddToCartWithoutLogin(self.driver)
            self.addcartwithoutogin.clickIconCart()
            self.addcartwithoutogin.clickViewCartButton()
            self.addcartwithoutogin.clickNextButton()
            
            # using login Addtocart data
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
                self.driver.save_screenshot(".\\Screenshots\\" + "Failed_AddToCart_with_Login.png")
            except Exception as e:
                print(f"failed to the screenshot: {e}")
        