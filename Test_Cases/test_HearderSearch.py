import pytest
from Page_Object_Model.header_search import HeaderSearch
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
import time

# ************** Working code ************************

class Test_008_HeaderSearch:
    baseURL = ReadConfig.getApplicationURL()
    vehicleName = ReadConfig.getvehicleName()
    partName =  ReadConfig.getpartName()
    Logger = LogGen.loggen()
    
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_HeaderSearch(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            
            self.hdrsearch = HeaderSearch(self.driver)
            self.hdrsearch.clickHearchSearch(self.vehicleName)
            self.hdrsearch.clickSearchIcon()
            self.hdrsearch.clickViewAllParts()
            self.hdrsearch.clickSmartSearch(self.partName)
            self.hdrsearch.clickSmartSearchIcon()
            self.hdrsearch.clickPartCheckDescription()

            time.sleep(10)
            self.driver.quit()
            
        finally:
            try:
                self.driver.save_screenshot(".\\Screenshots\\" + "Falied_Header_Search_PartVehicle.png")
            except Exception as e:
                print(f"failed to the screenshot: {e}")