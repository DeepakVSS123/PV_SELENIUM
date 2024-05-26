import pytest
from Page_Object_Model.login_page import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time


# ************** Working code ************************

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    mobilenumber = ReadConfig.getUserMobileNumber()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_HomePageTitle(self, setup):
        self.logger.info("****************** Test 001 Login ******************")
        self.logger.info("********* Started Home Page Title test *************")
        self.driver = setup
        
        self.logger.info("************ Open URL *************")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        if act_title == "E-Shoppe":
            self.logger.info("******** Home page title test passed *********")
            time.sleep(3)
            self.driver.close()
            assert True
            
        else:
            self.logger.error("********* Home page title Test case Fail ***********")
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\" + "failed_BeforeLogin_HomePageTitle.png")
            self.driver.close()
            assert False
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_Login(self, setup):
        self.logger.info("******* Started Home page ***********")
        self.logger.info("********* Started After Login Home Page Title test *************")
        self.driver = setup

        self.logger.info("************ Open URL *************")
        self.driver.get(self.baseURL)
        
        
        self.lp = LoginPage(self.driver)
        self.logger.info("******* Click login profil icon ************")
        self.lp.clickloginIconButton()
        
        self.logger.info("******* Click password radio button  **********")
        self.lp.clickPasswordRadioButton()
        
        self.logger.info("******* Enter Mobile Number **********")
        self.lp.setModileNumber(self.mobilenumber)
        
        self.logger.info("******* Enter Password **********")
        self.lp.setPassword(self.password)
        
        self.logger.info("******* click Sign In  **********")
        self.lp.clickSignIn()
        time.sleep(3)
        
        self.logger.info("******* check title **********")
        act_title = self.driver.title
        
        if act_title == "E-Shoppe":
            self.logger.info("******** Home page title test passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********* After Login Home page title Test case Fail ***********")
            self.driver.save_screenshot(".\\Screenshots\\" + "failed_AfterLogin_HomePageTitle.png")
            self.driver.close()
            assert False
            