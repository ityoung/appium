import unittest
import time
import os
import sys
from Lib import HTMLTestRunner
from Lib import mhome_element as me
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

phone_num = '18280336118'
new_phone_num = '12345611223'
password = 'lianai0217'
TIME_format = "%y%m%d%H%M%S"
img_path_base = 'F:/mhome/resource/'

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
            self.screenshot()
            update.click()
        except NoSuchElementException:
            self.test_Logout()
        try:
            tel = self.driver.find_element_by_xpath(me.tel_xpath)
            if tel.text =='请输入手机号':
                tel.send_keys(phone_num)
                psw = self.driver.find_element_by_xpath(me.pwd_xpath)
                psw.send_keys(password)
            self.driver.find_element_by_id(me.login_btn).click()
            time.sleep(5)
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee
        self.test_Logout()

    def test_LoginByQQ(self):
        try:
            update = self.driver.find_element_by_id(me.cancel_btn_id)
            self.screenshot()
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
            self.screenshot()
            raise nee

    def test_Logout(self):
        try:
            self.driver.find_element_by_id(me.me_id).click()
            self.driver.swipe(540,1254,540,834,1000)
            self.driver.find_element_by_id(me.setting_id).click()
            self.driver.find_element_by_id(me.quit_btn).click()
            self.driver.find_element_by_id(me.confirm_btn_id).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee
    def screenshot(self):
        timestamp = time.strftime(TIME_format,time.localtime())
        screenshot = self.driver.get_screenshot_as_file(img_path_base+\
                sys._getframe().f_back.f_code.co_name+timestamp+'.png')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class Test_Anniversary(unittest.TestCase):
    
    def screenshot(self):
        timestamp = time.strftime(TIME_format,time.localtime())
        screenshot = self.driver.get_screenshot_as_file(img_path_base+\
                sys._getframe().f_back.f_code.co_name+timestamp+'.png')

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'appPackage': 'com.changhong.mhome',
            'appActivity': 'com.changhong.activity.login.LoginActivity',
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': 'Nexus 5',
            'newCommandTimeout': 30,
            'unicodeKeyboard': 'True',
            "resetKeyboard": "True"
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_AddAnni(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee
        try:
            self.driver.find_element_by_id(me.add_btn).click()
            title = self.driver.find_element_by_id(me.ann_title_et)
            title.send_keys("测试添加")
            self.driver.find_element_by_id(me.ann_date_btn).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_name("测试添加").click()
            self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee

    def test_RemindDay_Single(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
        try:
            for i in range(1,7):
                self.driver.find_element_by_id(me.add_btn).click()
                title = self.driver.find_element_by_id(me.ann_title_et)
                title.send_keys("测试提醒日"+str(i))
                self.driver.find_element_by_id(me.ann_date_btn).click()
                self.driver.find_element_by_id(me.date_confirm).click()
                self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                if 1<i:
                    self.driver.find_element_by_xpath(me.remind_day_xpath+'['+str(i)+']').click()
                if i<6:
                    self.driver.find_element_by_id(me.remind_day_id).click()
                self.driver.find_element_by_id(me.done_btn).click()
                self.driver.find_element_by_id(me.add_btn).click()
                self.driver.find_element_by_name("测试提醒日"+str(i)).click()
                self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee

    def test_RemindDay_Double(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
        try:
            for i in range(1,5):
                for j in range(i+1, 6):
                    self.driver.find_element_by_id(me.add_btn).click()
                    title = self.driver.find_element_by_id(me.ann_title_et)
                    title.send_keys("测试提醒日"+str(i)+"+"+str(j))
                    self.driver.find_element_by_id(me.ann_date_btn).click()
                    self.driver.find_element_by_id(me.date_confirm).click()
                    self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                    self.driver.find_element_by_xpath(me.remind_day_xpath+'['+str(j)+']').click()
                    if i>1:
                        self.driver.find_element_by_xpath(me.remind_day_xpath+'['+str(i)+']').click()
                        self.driver.find_element_by_id(me.remind_day_id).click()
                    self.driver.find_element_by_id(me.done_btn).click()
                    self.driver.find_element_by_id(me.add_btn).click()
                    self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j)).click()
                    self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee
        
    def test_RemindDay_Triple(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
        try:
            for i in range(1,4):
                for j in range(i+1, 5):
                    for k in range(j+1, 6):
                        self.driver.find_element_by_id(me.add_btn).click()
                        title = self.driver.find_element_by_id(me.ann_title_et)
                        title.send_keys("测试提醒日"+str(i)+"+"+str(j)+"+"+str(k))
                        self.driver.find_element_by_id(me.ann_date_btn).click()
                        self.driver.find_element_by_id(me.date_confirm).click()
                        self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                        self.driver.find_element_by_xpath(me.remind_day_xpath+'['+str(j)+']').click()
                        self.driver.find_element_by_xpath(me.remind_day_xpath+'['+str(k)+']').click()
                        if i>1:
                            self.driver.find_element_by_id(me.remind_day_id).click()
                            self.driver.find_element_by_xpath(me.remind_day_xpath+'['+str(i)+']').click()
                        self.driver.find_element_by_id(me.done_btn).click()
                        self.driver.find_element_by_id(me.add_btn).click()
                        self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j)+"+"+str(k)).click()
                        self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee

    def test_RemindTime(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
        try:
            self.driver.find_element_by_id(me.add_btn).click()
            title = self.driver.find_element_by_id(me.ann_title_et)
            title.send_keys("测试提醒时间")
            self.driver.find_element_by_id(me.ann_date_btn).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            self.driver.find_element_by_id(me.ann_remind_time_btn).click()
            self.driver.swipe(540, 1350, 540, 1700,1000)
            self.driver.find_element_by_id(me.done_btn).click()
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_name("测试添加").click()
            self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee
        
    def test_Icon(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
        try:
            for i in range(1,9):
                self.driver.find_element_by_id(me.add_btn).click()
                title = self.driver.find_element_by_id(me.ann_title_et)
                title.send_keys("测试图标"+str(i))
                self.driver.find_element_by_id(me.ann_date_btn).click()
                self.driver.find_element_by_id(me.date_confirm).click()
                self.driver.find_element_by_id(me.ann_icon_btn).click()
                if i == 1:
                    self.driver.find_element_by_id(me.icon_id).click()
                else:
                    self.driver.find_element_by_xpath(me.icon_xpath+"["+str(i)+"]").click()
                self.driver.find_element_by_id(me.add_btn).click()
                self.driver.find_element_by_name("测试图标"+str(i)).click()
                self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
            raise nee
        
    def test_DelAnni_LongPress(self):
        try:
            self.driver.find_element_by_id(me.ann_btn).click()
        except NoSuchElementException as nee:
            self.screenshot()
        try:
            anndateexist = self.driver.find_element_by_id(me.ann_date_exist)
        except NoSuchElementException as nee:
            print("No anniversary can delete!\n")
            self.screenshot()
            raise nee
        while 1:
            action1 = TouchAction(self.driver)
            action1.long_press(anndateexist).perform()
            if self.driver.find_element_by_id(me.ann_del_title).text == '删除提示':
                self.driver.find_element_by_id(me.confirm_btn_id).click()
                try:
                    anndateexist = self.driver.find_element_by_id(me.ann_date_exist)
                except:
                    print("Anniversaries were all deleted!\n")
                    self.screenshot()
                    break
            else:
                continue
                            
            
if __name__ == '__main__':
    tests_login = ["test_LoginByTel","test_LoginByQQ"]
    tests_anniversary = ["test_RemindTime","test_DelAnni_LongPress"]
    #'test_AddAnni',"test_RemindDay_Single","test_RemindDay_Double",,"test_RemindDay_Triple","test_Icon"
    #tests_anniversary.append()
    testlogin = unittest.TestSuite(map(Test_Login,tests_login))
    testanniversary = unittest.TestSuite(map(Test_Anniversary,tests_anniversary))
    testsuite = unittest.TestSuite([testlogin, testanniversary])
    #testsuite = unittest.TestSuite(testanniversary)
    #testsuite.addTest(TestMhome("test_screenshot"))
    file_name = 'F:\\mhome\\test_result.html'
    fp = open(file_name,'wb')
    renner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title= 'test result',
            description='test result report')
    renner.run(testsuite)
    fp.close()
#    unittest.main()

