"""
Scenario:

Launch the red- bus application via Chrome browser
Select from and to
Select the date
And book a ticket
"""
import time
from appium import webdriver

class App:

    def __init__(self):
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
            self.driver.get("https://www.redbus.in/")
            print("Application launched successfully")

        except Exception as e:
            print("Error while launching Application{}".format(e))


    def Enter_source(self):
        try:
            self.source = self.driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[1]/div[1]/div[2]')
            self.source.click()
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="suggestInput"]').send_keys('ongole')
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="sourceCity"]/div/div[3]/ul/li').click()
            time.sleep(5)
            print("source selected successfully")

        except Exception as e:
            print("Error while Entering a source {}".format(e))

    def Enter_destination(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[1]/div[3]/div[2]/div').click()
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="suggestInput"]').send_keys('proddutur')
            time.sleep(10)
            self.driver.find_element_by_xpath('//*[@id="destinationCity"]/div/div[3]/ul/li[1]').click()
            time.sleep(5)
            print("Destination selected successfully")

        except Exception as e:
            print("Error while entering a destination {}".format(e))

    def select_date(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/div[2]/div/button[2]').click()
            time.sleep(5)
            print("Date selected successfully")

        except Exception as e:
            print("Error occurred while selecting date {}".format(e))

    def pop_up(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[7]/div/div/div[3]').click()
            time.sleep(3)
            print("Pop-up clicked successfully ")

        except Exception as e:
            print("pop-up not displayed ")

    def Search_bus(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="15261785"]').click()
            time.sleep(2)
            print("Bus selected successfully")

        except Exception as e:
            print("Error occured while searching for buses {}".format(e))


if __name__ == "__main__":
    s = App()
    s.Enter_source()
    s.Enter_destination()
    s.select_date()
    s.pop_up()
    s.Search_bus()
