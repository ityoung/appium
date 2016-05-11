import unittest
import os
from lib import HTMLTestRunner
from test_login import Test_Login
from test_anniversary import Test_Anniversary

new_phone_num = '12345611223'
    
if __name__ == '__main__':
    tests_login = ["test_LoginByTel","test_LoginByQQ"]
    tests_anniversary = ["test_RemindDay_Triple","test_Icon","test_DelAnni_LongPress"]
    #"test_FillUnset",'test_Date',"test_RemindTime","test_RemindDay_Single","test_DelAnni_Swipe",\
    #                     "test_RemindDay_Double",
    testlogin = unittest.TestSuite(map(Test_Login,tests_login))
    testanniversary = unittest.TestSuite(map(Test_Anniversary,tests_anniversary))
    testsuite = unittest.TestSuite([testlogin, testanniversary])
    #testsuite = unittest.TestSuite(testanniversary)
    file_name = 'F:\\mhome\\test_result.html'
    fp = open(file_name,'wb')
    renner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title= 'test result',
            description='test result report')
    renner.run(testsuite)
    fp.close()
#    unittest.main()

