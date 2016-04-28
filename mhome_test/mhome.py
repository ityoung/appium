import unittest
import time
import os
import sys
import logging
from lib import HTMLTestRunner
from lib import mhome_element as me
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

phone_num = '18280336118'
new_phone_num = '12345611223'
password = 'lianai0217'
TIME_format = "%y%m%d%H%M%S"
img_path_base = 'F:/mhome/resource/'
    
def screenshot(driver):
    timestamp = time.strftime(TIME_format,time.localtime())
    screenshot = driver.get_screenshot_as_file(img_path_base+\
        sys._getframe().f_back.f_code.co_name+timestamp+'.png')
    logging.warning("screeshot: "+img_path_base+\
        sys._getframe().f_back.f_code.co_name+timestamp+'.png\n')

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
            screenshot(self.driver)
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
            screenshot(self.driver)
            raise nee
        self.test_Logout()

    def test_LoginByQQ(self):
        try:
            update = self.driver.find_element_by_id(me.cancel_btn_id)
            screenshot(self.driver)
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
            screenshot(self.driver)
            raise nee

    def test_Logout(self):
        try:
            self.driver.find_element_by_id(me.me_id).click()
            self.driver.swipe(540,1254,540,834,1000)
            self.driver.find_element_by_id(me.setting_id).click()
            self.driver.find_element_by_id(me.quit_btn).click()
            self.driver.find_element_by_id(me.confirm_btn_id).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class Test_Anniversary(unittest.TestCase):

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
        try:
            cls.driver.find_element_by_id(me.guide_img).click()
        except NoSuchElementException as nee:
            pass
        finally:
            try:
                cls.driver.find_element_by_id(me.ann_btn).click()
            except NoSuchElementException as nee:
                cls.screenshot()
                raise nee

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Date(self):
        try:
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_id(me.ann_date_btn).click()
            ### get location for swiping
            year_view = self.driver.find_element_by_id(me.date_year_view)
            month_view = self.driver.find_element_by_id(me.date_month_view)
            day_view = self.driver.find_element_by_id(me.date_day_view)
            yv_mid = int(year_view.location.get('x')+year_view.size['width']*0.5)
            yv_upy = year_view.location.get('y')+10
            yv_downy = year_view.location.get('y')+year_view.size['height'] - 10
            mv_mid = int(month_view.location.get('x')+month_view.size['width']*0.5)
            dv_mid = int(day_view.location.get('x')+day_view.size['width']*0.5)
            self.driver.swipe(yv_mid,yv_upy,yv_mid,yv_downy,1000)
            self.driver.swipe(mv_mid,yv_downy,mv_mid,yv_upy,1000)
            self.driver.swipe(dv_mid,yv_upy,dv_mid,yv_downy,1000)
            self.driver.find_element_by_id(me.lunnar_swap).click()
            time.sleep(0.5)
            self.driver.find_element_by_id(me.lunnar_swap).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            title = self.driver.find_element_by_id(me.ann_title_et)
            title.send_keys("测试时间")
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_name("测试时间").click()
            self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee

    def test_RemindDay_Single(self):
        try:
            for i in range(0,6):
                if i == 0:
                    self.driver.find_element_by_id(me.add_btn).click()
                    self.driver.find_element_by_id(me.ann_date_btn).click()
                    self.driver.find_element_by_id(me.date_confirm).click()
                else:
                    self.driver.find_element_by_name("测试提醒日"+str(i-1)).click()
                self.driver.find_element_by_id(me.ann_title_et).set_text("测试提醒日"+str(i))
                self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                remind = self.driver.find_elements_by_id(me.remind_day_id)
                remind[5].click()
                remind[i].click()
                self.driver.find_element_by_id(me.done_btn).click()
                self.driver.find_element_by_id(me.add_btn).click()
                self.driver.find_element_by_name("测试提醒日"+str(i)).click()
                self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee

    def test_RemindDay_Double(self):
        try:
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_id(me.ann_date_btn).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            title = self.driver.find_element_by_id(me.ann_title_et)
            self.driver.find_element_by_id(me.ann_remind_day_btn).click()
            remind = self.driver.find_elements_by_id(me.remind_day_id)
            for i in range(0,4):
                if i > 0:
                    self.driver.find_element_by_name("测试提醒日"+str(i-1)+"+"+str(j)).click()
                    self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                remind[5].click()
                for j in range(i+1, 5):
                    if j-i > 1:
                        self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j-1)).click()
                        self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                    remind[j-1].click()
                    remind[j].click()
                    self.driver.find_element_by_id(me.done_btn).click()
                    title.set_text("测试提醒日"+str(i)+"+"+str(j))
                    self.driver.find_element_by_id(me.add_btn).click()
                    self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j)).click()
                    self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee
        
    def test_RemindDay_Triple(self):
        try:
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_id(me.ann_date_btn).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            title = self.driver.find_element_by_id(me.ann_title_et)
            self.driver.find_element_by_id(me.ann_remind_day_btn).click()
            remind = self.driver.find_elements_by_id(me.remind_day_id)
            for i in range(0,3):
                if i > 0:
                    self.driver.find_element_by_name("测试提醒日"+str(i-1)+"+"+str(j)+"+"+str(k)).click()
                    self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                remind[5].click()
                for j in range(i+1, 4):
                    if j-i>1:
                        self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j-1)+"+"+str(k)).click()
                        self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                        remind[k].click()
                    remind[j-1].click()
                    for k in range(j+1, 5):
                        if k-j>1:
                            self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j)+"+"+str(k-1)).click()
                            self.driver.find_element_by_id(me.ann_remind_day_btn).click()
                        remind[k-1].click()
                        remind[k].click()
                        self.driver.find_element_by_id(me.done_btn).click()
                        title.set_text("测试提醒日"+str(i)+"+"+str(j)+"+"+str(k))
                        self.driver.find_element_by_id(me.add_btn).click()
                        self.driver.find_element_by_name("测试提醒日"+str(i)+"+"+str(j)+"+"+str(k)).click()
                        self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee

    def test_RemindTime(self):
        try:
            self.driver.find_element_by_id(me.add_btn).click()
            title = self.driver.find_element_by_id(me.ann_title_et)
            title.send_keys("测试提醒时间0")
            self.driver.find_element_by_id(me.ann_date_btn).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            self.driver.find_element_by_id(me.ann_remind_time_btn).click()
            self.driver.swipe(540, 1140, 540, 1740,500)
            time.sleep(0.3)
            self.driver.swipe(540, 1140, 540, 1740,500)
            self.driver.find_element_by_id(me.remind_time_confirm).click()
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_name("测试提醒时间0").click()
            self.driver.find_element_by_id(me.back_btn).click()
            for i in range(1,24):
                self.driver.find_element_by_name("测试提醒时间"+str(i-1)).click()
                title.set_text("测试提醒时间"+str(i))
                self.driver.find_element_by_id(me.ann_remind_time_btn).click()
                self.driver.swipe(540, 1440, 540, 1340,800)
                self.driver.find_element_by_id(me.remind_time_confirm).click()
                self.driver.find_element_by_id(me.add_btn).click()
                self.driver.find_element_by_name("测试提醒时间"+str(i)).click()
                self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee
        
    def test_Icon(self):
        try:
            for i in range(0,8):
                if i == 0:
                    self.driver.find_element_by_id(me.add_btn).click()
                    title = self.driver.find_element_by_id(me.ann_title_et)
                    self.driver.find_element_by_id(me.ann_date_btn).click()
                    self.driver.find_element_by_id(me.date_confirm).click()
                    self.driver.find_element_by_id(me.ann_icon_btn).click()
                    icon = self.driver.find_elements_by_id(me.icon_id)
                else:
                    self.driver.find_element_by_name("测试图标"+str(i-1)).click()
                    self.driver.find_element_by_id(me.ann_icon_btn).click()
                icon[i].click()
                title.set_text("测试图标"+str(i))
                self.driver.find_element_by_id(me.add_btn).click()
                self.driver.find_element_by_name("测试图标"+str(i)).click()
                self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee

    def test_FillUnset(self):
        try:
            self.driver.find_element_by_xpath(me.ann_item_xpath+"[1]").click()
            #title = self.driver.find_element_by_id(me.ann_title_et)
            #title.send_keys("测试未设定"+str(i))
            name = self.driver.find_element_by_id(me.ann_title_et).text
            self.driver.find_element_by_id(me.ann_date_btn).click()
            self.driver.find_element_by_id(me.date_confirm).click()
            self.driver.find_element_by_id(me.add_btn).click()
            self.driver.find_element_by_name(name).click()
            self.driver.find_element_by_id(me.back_btn).click()
        except NoSuchElementException as nee:
            screenshot(self.driver)
            raise nee
        
    def test_DelAnni_LongPress(self):
        try:
            anndateexist = self.driver.find_element_by_id(me.ann_date_exist)
        except NoSuchElementException as nee:
            print("No anniversary can delete!\n")
            screenshot(self.driver)
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
                    break
            else:
                continue
            
    def test_DelAnni_Swipe(self):
        try:
            anndateexist = self.driver.find_element_by_id(me.ann_date_exist)
            x = anndateexist.location.get('x')    #left x
            width = anndateexist.size['width']
            y = anndateexist.location.get('y')    #up y
        except NoSuchElementException as nee:
            print("No anniversary can delete!\n")
            screenshot(self.driver)
            raise nee
        while 1:
            self.driver.swipe(x+width,y,x,y,1000)
            self.driver.find_element_by_id(me.swipe_del).click()
            if self.driver.find_element_by_id(me.ann_del_title).text == '删除提示':
                self.driver.find_element_by_id(me.confirm_btn_id).click()
                try:
                    anndateexist = self.driver.find_element_by_id(me.ann_date_exist)
                except:
                    print("Anniversaries were all deleted!\n")
                    break
            else:
                continue
                            
            
if __name__ == '__main__':
    tests_login = ["test_LoginByTel","test_LoginByQQ"]
    tests_anniversary = ["test_DelAnni_Swipe"]#"test_FillUnset",'test_AddAnni',"test_RemindTime","test_RemindDay_Single",\
                        # "test_RemindDay_Double","test_DelAnni_Swipe","test_RemindDay_Triple","test_Icon","test_DelAnni_LongPress"
    #"test_FillUnset",'test_AddAnni',"test_RemindTime","test_RemindDay_Single","test_RemindDay_Double","test_RemindDay_Triple","test_Icon"
    #tests_anniversary.append()
    testlogin = unittest.TestSuite(map(Test_Login,tests_login))
    testanniversary = unittest.TestSuite(map(Test_Anniversary,tests_anniversary))
    #testsuite = unittest.TestSuite([testlogin, testanniversary])
    testsuite = unittest.TestSuite(testanniversary)
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

