from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Email_Login import LoginClass
from slack_client import Logger




class CourseLearningClass(LoginClass):
    def __init__(self):
        super().__init__()
        self._driver = super().get_driver()


    def EnterCourseLearning(self):
        recommanded_cell = self._driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]')
        recommanded_cell.click()
        Logger("추천학습 클릭!")
        sleep(3)

        while(True):





