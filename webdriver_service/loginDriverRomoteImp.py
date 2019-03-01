from logging_utils.log import mylog
from webdriver_service.driverBean import WebDriverImp
from webdriver_service.driverRemoteBean import WebDriverRemoteImp
from webdriver_service.loginDriverImp import LoginDriverImp


class LoginDriverRomoteImp(WebDriverRemoteImp):

    def __init__(self, MyPool, driver=None, headless=False, data=None):
        super().__init__(MyPool, driver, headless, data)
        self._login()  # 进行默认的登陆操作

    def _login(self):
        print("覆写该登陆方法,完成任务和操作")
        self.driver.get("http://www.163.com")
        pass
