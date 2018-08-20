#coding:utf-8
import unittest
from Test_Common import readConfig
from appium import webdriver

class Lottery_Start(unittest.TestCase):
    def setUp(self):
        '''
        :return: 启动设备，返回driver

        # 创建一个readConfig类
        '''

        read = readConfig.ReadConfig()
        # 获取设备配置
        equipment_dict = {
            'platformName': read.get_config('EQUIPMENT', 'platformName'),
            'deviceName': read.get_config('EQUIPMENT', 'deviceName'),
            'platformVersion': read.get_config('EQUIPMENT', 'platformVersion'),
            'appPackage': read.get_config('EQUIPMENT', 'apppackage'),
            'appActivity': read.get_config('EQUIPMENT', 'appActivity'),
            'automationName': read.get_config('EQUIPMENT', 'automationName')
        }
        # 启动app,返回driver
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', equipment_dict)

    def tearDown(self):
        #退出设备
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()