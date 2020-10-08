import os,time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from Applications.Redbus.side_panel.locators import *

class SidePanelPage():

    def __init__(self):
        self.driver = webdriver
        self.connect()
        self.launch_application()
        self.click_side_menu()

    def connect(self):
        try:
            capabilities = {'browserName': 'Chrome', 'platformName': 'Android', 'platformVersion': '10',
                            'deviceName': 'chenna', 'deviceID': '8cc6f1da', 'noReset': 'true'}

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
            print("Android and Appium Connection successfully")
        except Exception as e:
            print("Error while connecting with appium {}".format(e))

    def launch_application(self):
        url = "https://www.redbus.in/"
        try:
            self.driver.get(url)
            print("Application launched successfully")

        except Exception as e:
            print("Error while launching Application{}".format(e))

    def click_side_menu(self, timeout=20):
        try:
            self.side = self.driver.find_element(MobileBy.XPATH, Locator.side_menu)
            self.side.click()
            print("side menu clicked successfully.......")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking the side-menu...")

    def naviage_login(self, timeout=10):
        try:
            self.signin = self.driver.find_element(MobileBy.XPATH, Locator.sign_in_up)
            self.signin.click()
            print("Sign-in or sign-up clicked successfully........")
            time.sleep(timeout)

        except Exception as e:
            print("Error occured clicking on the sign in/up....")

    def login_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.sign_page).text
            return expected_data
        except Exception as e:
            print("Error occured on sign in/up page....")

    def naviagte_search_buses(self, timeout=10):
        try:
            self.searchbuses = self.driver.find_element(MobileBy.XPATH, Locator.search_Buses)
            self.searchbuses.click()
            print("search buses clicked successfully..........")
            time.sleep(timeout)
        except Exception as e:
            print("Error ocurred clicking on search buses.....")
    def search_buses_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.Buses_page).text
            return expected_data
        except Exception as e:
            print("Error occured on search buses page....")

    def naviagte_offers(self, timeout=10):
        try:
            self.offers = self.driver.find_element(MobileBy.XPATH, Locator.Offers)
            self.offers.click()
            print("Offers clicked succesfully......")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on offers.....")
    def offers_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.offers_page).text
            return expected_data
        except Exception as e:
            print("Error occured on offers page....")

    def navigate_refer_and_earn(self, timeout=10):
        try:
            self.refer = self.driver.find_element(MobileBy.XPATH, Locator.Refer_and_Earn)
            self.refer.click()
            print("Refer and Earn clicked succesfully..........")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on refer & earn .....")
    def refer_and_earn_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.refer_page).text
            return expected_data
        except Exception as e:
            print("Error occured on refer and earn page....")

    def navigate_help(self, timeout=10):
        try:
            self.Help = self.driver.find_element(MobileBy.XPATH, Locator.Help)
            self.Help.click()
            print("Help clicked succesfully..........")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on help.....")
    def help_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.help_page).text
            return expected_data

        except Exception as e:
            print("Error occured on help page....")

    def navigate_get_ticket_details(self, timeout=10):
        try:
            self.getticket = self.driver.find_element(MobileBy.XPATH, Locator.Get_Ticket_Details)
            self.getticket.click()
            print("Get ticket details clicked succesfully........")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on get ticket deatils.....")
    def get_ticket_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.ticket_page).text
            return expected_data
        except Exception as e:
            print("Error occured on get ticket deatils page.....")

    def navigate_about_us(self, timeout=10):
        try:
            self.AboutUs = self.driver.find_element(MobileBy.XPATH, Locator.About_Us)
            self.AboutUs.click()
            print("About us clicked successfully.........")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on about us.....")
    def about_us_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.about_us_page).text
            return expected_data
        except Exception as e:
            print("Error occured on about us page.....")

    def navigate_cancel_ticket(self, timeout=10):
        try:
            self.Cancel = self.driver.find_element(MobileBy.XPATH, Locator.Cancel_Ticket)
            self.Cancel.click()
            print("Cancel_Ticket clicked successfully......")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on cancel ticket.....")
    def cancel_ticket_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.cancel_page).text
            return expected_data
        except Exception as e:
            print("Error occured on cancel ticket page.....")

    def navigate_reschedule_ticket(self, timeout=5):
        try:
            self.reschedule = self.driver.find_element(MobileBy.XPATH, Locator.Reschedule_Ticket)
            self.reschedule.click()
            print("Reschedule_Ticket clicked successfully......")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on reschedule ticket.....")
    def reschedule_ticket_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.reschedule_page).text
            return expected_data

        except Exception as e:
            print("Error occured on reschedule ticket page.....")

    def naviagte_settings(self, timeout=10):
        try:
            self.settings = self.driver.find_element(MobileBy.XPATH, Locator.Settings)
            self.settings.click()
            print("Settings clicked successfully......")
            time.sleep(timeout)
        except Exception as e:
            print("Error occured clicking on settings.....")
    def setting_page(self):
        try:
            expected_data = self.driver.find_element(MobileBy.XPATH, Locator.settings_page).text
            return expected_data

        except Exception as e:
            print("Error occured on settings page.....")


if __name__ == "__main__":
    Sidepage = SidePanelPage()
    # print(Sidepage.naviage_login())
    # print(Sidepage.naviagte_search_buses())
    # print(Sidepage.naviagte_offers())
    # print(Sidepage.navigate_refer_and_earn())
    # print(Sidepage.navigate_help())
    # print(Sidepage.navigate_get_ticket_details())
    # print(Sidepage.navigate_about_us())
    # print(Sidepage.navigate_cancel_ticket())
    #print(Sidepage.navigate_reschedule_ticket())
    # print(Sidepage.naviagte_settings())