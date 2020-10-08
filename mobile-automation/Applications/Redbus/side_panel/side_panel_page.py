import os,time
from appium import webdriver

class  SidePanelPage:

    def __init__(self):
        self.driver_path = "G:\\BMS_POM\\Dependecies\\Drivers\\chromedriver.exe"
        if not os.path.exists(self.driver_path):
            print(f"Not able to find web driver. path {self.driver_path}")
        self.connect()
        self.launch_application()

    def connect(self):
        try:
            capabilities = {'browserName': 'Chrome', 'platformName': 'Android', 'platformVersion': '10',
                            'deviceName': 'chenna', 'deviceID': '8cc6f1da', 'noReset': 'true'}

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
            print("Android and Appium Connection successfully")
        except Exception as e:
            print("Error while connecting with appium {}".format(e))

    def launch_application(self):
        try:
            self.driver.get()
            print("Application launched successfully")

        except Exception as e:
            print("Error while launching Application{}".format(e))

    def click_side_menu(self):
        try:
            self.side = self.driver.find_element()
            self.side.click()
            print("side menu clicked successfully.......")
        except Exception as e:
            print("Error occured clicking the side-menu...")

    def naviage_login(self):
        try:
            self.signin = self.driver.find_element()
            self.signin.find_element()
            print("Sign-in or sign-up clicked successfully........")

        except Exception as e:
            print("Error occured clicking on the sign in/up....")

    def naviagte_search_buses(self):
        try:
            self.searchbuses = self.driver.find_element()
            self.searchbuses.click()
            print("search buses clicked successfully..........")
        except Exception as e:
            print("Error ocurred clicking on search buses.....")

    def naviagte_offers(self):
        try:
            self.offers = self.driver.find_element()
            self.offers.click()
            print("Offers clicked succesfully......")

        except Exception as e:
            print("Error occured clicking on offers.....")

    def navigate_refer_and_earn(self):
        try:
            self.refer = self.driver.find_element()
            self.refer.click()
            print("Refer and Earn clicked succesfully..........")
        except Exception as e:
            print("Error occured clicking on refer & earn .....")

    def navigate_help(self):
        try:
            self.Help = self.driver.find_element()
            self.Help.click()
            print("Help clicked succesfully..........")

        except Exception as e:
            print("Error occured clicking on help.....")

    def navigate_get_ticket_details(self):
        try:
            self.getticket = self.driver.find_element()
            self.getticket.click()
            print("Get ticket details clicked succesfully........")
        except Exception as e:
            print("Error occured clicking on get ticket deatils.....")

    def navigate_about_us(self):
        try:
            self.AboutUs = self.driver.find_element()
            self.AboutUs.click()
            print("About us clicked successfully.........")
        except Exception as e:
            print("Error occured clicking on about us.....")


    def navigate_cancel_ticket(self):
        try:
            self.Cancel = self.driver.find_element()
            self.Cancel.click()
            print("Cancel_Ticket clicked successfully......")
        except Exception as e:
            print("Error occured clicking on cancel ticket.....")

    def navigate_reschedule_ticket(self):
        try:
            self.reschedule = self.driver.find_element()
            self.reschedule.click()
            print("Reschedule_Ticket clicked successfully......")
        except Exception as e:
            print("Error occured clicking on reschedule ticket.....")

    def naviagte_settings(self):
        try:
            self.settings = self.driver.find_element()
            self.settings.click()
            print("Settings clicked successfully......")
        except Exception as e:
            print("Error occured clicking on settings.....")