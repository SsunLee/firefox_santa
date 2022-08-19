
from selenium import webdriver

class mainClass():
    emailAddress = 'sunbae@yopmail.com'
    password = '1qaz2wsx'
    santa_url = 'https://ai.aitutorsanta.com/onboarding/intro?referrer='

    def __init__(self):
        try:
            self._option = webdriver.FirefoxOptions()
            self._option.add_argument("lang=ko_KR")
            #self.option.add_argument("__headless")
            self._driver = webdriver.Firefox(options=self._option)
            self._driver.get(self.santa_url)
            self._driver.implicitly_wait(30)
        except Exception as e:
            print(e)

    def get_driver(self):
        return self._driver