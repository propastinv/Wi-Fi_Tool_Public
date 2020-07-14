import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from settings import *


class Selenium_chromedriver():
    """Class opening access point on webdriver"""

    def __init__(self, host, flashing_number = None, flashing_password = None, flashing_bs_sector = None, flashing_city = None, flashing_latit = None, flashing_longi = None):
        self.driver = webdriver.Chrome('src/chromedriver.exe')
        self.host = host
        self.flashing_number = flashing_number
        self.flashing_password = flashing_password
        self.flashing_bs_sector = flashing_bs_sector
        self.flashing_latit = flashing_latit
        self.flashing_longi = flashing_longi
        self.flashing_city = flashing_city
    def open(self):
        """Open page"""
        
        self.driver.get('http://' + str(self.host));
        time.sleep(4) 
    
    def authorize(self):
        """Authorize user"""

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        username.send_keys(UBNT_LOGIN)
        password.send_keys(UBNT_PASSWORD)
        username.send_keys(Keys.RETURN)
        time.sleep(3)

    def wireles(self):
        """Credential entry for tab Wireles"""

        self.driver.find_element_by_xpath('//a[@href="'+ 'link.cgi' +'"]').click()
        time.sleep(2)
        wpa_user = self.driver.find_element_by_name('wpa_ident').clear()
        wpa_pass = self.driver.find_element_by_name('wpa_passwd').clear()
        time.sleep(3)
        wpa_user = self.driver.find_element_by_name('wpa_ident')
        wpa_pass = self.driver.find_element_by_name('wpa_passwd')
        wpa_user.send_keys(self.flashing_number)
        wpa_pass.send_keys(self.flashing_password)
        time.sleep(2)
        wpa_pass.send_keys(Keys.RETURN)
        time.sleep(2)

    def network(self):
        """Credential entry for tab Wireles"""

        self.driver.find_element_by_xpath('//a[@href="'+ 'network.cgi' +'"]').click()
        time.sleep(2)
        wanPppoeUser = self.driver.find_element_by_name('wanPppoeUser').clear()
        wanPppoePassw = self.driver.find_element_by_name('wanPppoePassw').clear()
        time.sleep(1)
        wanPppoeUser = self.driver.find_element_by_name('wanPppoeUser')
        wanPppoePassw = self.driver.find_element_by_name('wanPppoePassw')
        wanPppoeUser.send_keys(self.flashing_number)
        wanPppoePassw.send_keys(self.flashing_password)
        time.sleep(2)
        wanPppoePassw.send_keys(Keys.RETURN)
        time.sleep(2)

    def system(self):
        """Filling data on a tab System"""

        self.driver.find_element_by_xpath('//a[@href="'+ 'system.cgi' +'"]').click()
        time.sleep(2)
        hostname = self.driver.find_element_by_name('hostname').clear()
        latitude = self.driver.find_element_by_name('latitude').clear()
        longitude = self.driver.find_element_by_name('longitude').clear()
        time.sleep(3)
        hostname = self.driver.find_element_by_name('hostname')
        latitude = self.driver.find_element_by_name('latitude')
        longitude = self.driver.find_element_by_name('longitude')

        hostname.send_keys(self.flashing_number + '_' + self.flashing_city + '_' + self.flashing_bs_sector)
        latitude.send_keys(self.flashing_latit)
        longitude.send_keys(self.flashing_longi)
        time.sleep(1)
        self.driver.find_element_by_name('change').click()



