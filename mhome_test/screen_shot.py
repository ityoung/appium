from appium import webdriver
import time
import os
import sys
import logging

TIME_format = "%y%m%d%H%M%S"
img_path_base = 'F:/mhome/mhome_test/screeshot/'

def screenshot(driver):
    isExist = os.path.exists(img_path_base)
    if not isExist:
        os.makedirs(img_path_base)
    timestamp = time.strftime(TIME_format,time.localtime())
    screenshot = driver.get_screenshot_as_file(img_path_base+\
        sys._getframe().f_back.f_code.co_name+timestamp+'.png')
    logging.warning("screeshot: "+img_path_base+\
        sys._getframe().f_back.f_code.co_name+timestamp+'.png\n')

