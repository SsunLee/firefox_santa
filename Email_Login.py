from curses.ascii import EM
import email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from mainControl import mainClass
from SlackClient import Logger

class LoginClass(mainClass):

    def __init__(self):
        super().__init__()
        self._driver = super().get_driver()
        self._emailAddress = super().emailAddress
        self._password = super().password

    def email_function(self):
        try:
            # aleady have a account 
            sleep(0.5)
            alreadyBtn = self._driver.find_element(By.XPATH, '//div[2]/button[2]')
            alreadyBtn.click()
            Logger("이미 계정이 있어요")

            # other way
            sleep(0.5) 
            OtherWaybtn = self._driver.find_element(By.XPATH, '//div[2]/button[4]')
            OtherWaybtn.click()
            Logger("다른 방법으로 할래요")

            # email login 
            sleep(0.5)
            EmailLoginBtn = self._driver.find_element(By.XPATH, '//div[2]/button[5]')
            EmailLoginBtn.click() 
            Logger("Email로 로그인")
            # enter email id and password to each fields
            sleep(0.5)

            emailField = self._driver.find_element(By.XPATH, '//form/div[1]/div[1]/div[2]/input')
            for c in self._emailAddress:
                sleep(0.1)
                emailField.send_keys(c)

            passField = self._driver.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]/input')
            for p in self._password:
                sleep(0.1)
                passField.send_keys(p)

            passField.send_keys(Keys.ENTER)
            sleep(1)

            self._driver.implicitly_wait(30)
            sleep(10)
        except Exception:
            pass
            self._driver.close()




