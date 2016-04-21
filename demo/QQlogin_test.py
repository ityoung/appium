import unittest
import HTMLTestRunner
from appium import webdriver
class TestQQLogin(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            'appPackage': 'com.tencent.mobileqq',
            'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
            'appWaitActivity': '.activity.LoginActivity',       #change Activity after start
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': 'Nexus 5',
            'unicodeKeyboard': 'True',
            "resetKeyboard": "True"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)

    def test_loginQQ(self):
        self.login_btn = 'com.tencent.mobileqq:id/login'
        self.search_edit = 'com.tencent.mobileqq:id/et_search_keyword'
        self.search_result_name = 'com.tencent.mobileqq:id/name'
        self.input_edit = 'com.tencent.mobileqq:id/input'
        self.send_btn = 'com.tencent.mobileqq:id/fun_btn'
        self.driver.find_element_by_id(self.login_btn).click()

    def tearDown(self):
        self.driver.quit()
        print("end")

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestQQLogin("test_loginQQ"))
    file_name = 'F:\\test_result.html'
    fp = open(file_name,'wb')
    renner = HTMLTestRunner.HTMLTestRunner(stream=fp, title= 'test result', description='test result report')
    renner.run(testsuite)
    fp.close()
#    unittest.main()
