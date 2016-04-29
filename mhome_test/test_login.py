import screen_shot as ss
from lib import mhome_element as me
import unittest
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'appPackage': 'com.changhong.mhome',
            'appActivity': 'com.changhong.activity.login.LoginActivity',
            'appwaitActivity': 'com.tencent.open.agent.AuthorityActivity',      #qq login
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': 'Nexus 5',
            'newCommandTimeout': 30,
            'unicodeKeyboard': 'True',
            "resetKeyboard": "True"
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        cls.driver.implicitly_wait(5)
    def test_LoginByTel(self):
        try:
            update = self.driver.find_element_by_id(me.cancel_btn_id)
            ss.screenshot(self.driver)
            update.click()
        except NoSuchElementException:
            self.test_Logout()
        try:
            tel = self.driver.find_element_by_xpath(me.tel_xpath)
            if tel.text =='请输入手机号':
                phone_num = input('请输入手机号:')
                tel.send_keys(phone_num)
                psw = self.driver.find_element_by_xpath(me.pwd_xpath)
                password = input('请输入密码:')
                psw.send_keys(password)
            self.driver.find_element_by_id(me.login_btn).click()
            time.sleep(5)
        except NoSuchElementException as nee:
            ss.screenshot(self.driver)
            raise nee
        self.test_Logout()

    def test_LoginByQQ(self):
        try:
            update = self.driver.find_element_by_id(me.cancel_btn_id)
            ss.screenshot(self.driver)
            update.click()
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element_by_id(me.qqlogin_btn).click()
            #time.sleep(10)
            #self.driver.start_activity('com.tencent.mobileqq','com.tencent.open.agent.AuthorityActivity')
            self.driver.find_element_by_class_name(me.qq_confirm_btn).click()
            #self.driver.start_activity('com.changhong.mhome','com.changhong.activity.login.LoginActivity')
            time.sleep(5)
        except NoSuchElementException as nee:
            ss.screenshot(self.driver)
            raise nee

    def test_Logout(self):
        try:
            self.driver.find_element_by_id(me.guide_img).click()
        except NoSuchElementException as nee:
            pass
        try:
            self.driver.find_element_by_id(me.me_id).click()
            self.driver.swipe(540,1254,540,834,1000)
            self.driver.find_element_by_id(me.setting_id).click()
            self.driver.find_element_by_id(me.quit_btn).click()
            self.driver.find_element_by_id(me.confirm_btn_id).click()
        except NoSuchElementException as nee:
            ss.screenshot(self.driver)
            raise nee

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

