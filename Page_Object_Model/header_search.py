from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.readProperties import ReadConfig


class HeaderSearch:
    firstpartsearch = ReadConfig.getFirstPartSearch()
    secondpartsearch = ReadConfig.getSecondPartSearch()

    headersearch_searchtext_id = "header-paste-search"
    heardersearch_searchicon_xpath = "//button[@class='btn-search']"
    viewallpartsforthemodel_xpath = "//a[text() = 'View all parts for this Model ']"
    smartsearch__searchfield_id = "text-focus"
    smartsearch_searchicon_xpath = "(//button[@class='btn-search'])[2]"
    part_description_xpath = "//h4[@class='prod-name mb-2']"
    
    
    def __init__(self, driver):
        self.driver = driver
    
    def clickHearchSearch(self, vehicleName):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.headersearch_searchtext_id)))
        element.send_keys(vehicleName)                                  
    
    def clickSearchIcon(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.heardersearch_searchicon_xpath))).click()
     
    def clickViewAllParts(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.viewallpartsforthemodel_xpath))).click()
    
    def clickSmartSearch(self, partName):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.smartsearch__searchfield_id))).send_keys(partName)
        
    def clickSmartSearchIcon(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.smartsearch_searchicon_xpath))).click()

    def clickPartCheckDescription(self):
        elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, self.part_description_xpath)))
        
        # if you want to see all parts description in print statement then use this code
        '''print("Total parts find :- " , len(elements))
        for ele in elements:
            print(ele.text)'''
            
        # Loop through each string in the list , Check if "head" or "lamp" is a substring
        for string in elements:
            string = string.text
            if self.firstpartsearch in string.lower() or self.secondpartsearch in string.lower():
                pass
            else:
                print(string)
                


            
