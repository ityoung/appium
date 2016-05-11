import screen_shot as ss
import devices_description as dd
from lib import mhome_element as me
import unittest
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class Test_Anniversary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'appPackage': 'com.changhong.mhome',
            'appActivity': 'com.changhong.activity.login.LoginActivity',
            'platformName': 'Android',
            'newCommandTimeout': 30,
            'unicodeKeyboard': 'True',
            "resetKeyboard": "True"
        }
        desired_caps.update(dd.dd)
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
                ss.screenshot(cls.driver)
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
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
            raise nee
        
    def test_DelAnni_LongPress(self):
        try:
            anndateexist = self.driver.find_element_by_id(me.ann_date_exist)
        except NoSuchElementException as nee:
            print("No anniversary can delete!\n")
            ss.screenshot(self.driver)
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
            ss.screenshot(self.driver)
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
                            
            
