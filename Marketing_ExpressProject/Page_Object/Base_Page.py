#coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
import time
from getExcel import GetExcel

class BasePage(object):
    #获取driver
    def __init__(self,driver):
        '''初始化'''
        self.driver = driver
        self.get_data = GetExcel()
    def find_element(self, *loc):
        '''重写元素定位的方法'''
        try:
            return self.driver.find_element(*loc)
        except:
            #print('没有查到元素！！！')
            return False

    def await_time(self, t):
        '''强制等待时间'''
        time.sleep(t)

    def implicit_for_wait(self, t):
        '''隐式等待'''
        self.driver.implicitly_wait(t)

    def show_wait(self, t, *loc):
        '''显示等待时间'''
        WebDriverWait(self.driver, t).until(lambda driver: driver.find_element(*loc))

    # 判断元素对象是否存在
    def is_element_exist(self, *loc):
        # if WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc)):
        #   return self.driver.find_element(*loc)
        # else:
        #   print("没找到元素！！！")
        flag = True
        try:
            self.await_time(10)
            self.driver.find_element(*loc)
            return flag
        except:
            flag = False
            return flag

    def redirect(self):
        '''重定向页面元素'''
        self.driver.switch_to_window(self.driver.current_window_handle)

    def getdata(self,rows):
        '''
        :param rows:输入行数
        :return: 获取用例data
        '''
        #创建一个GetExcel类
        return self.get_data.json_data(rows)

    def get_other(self,rows,headline):
        '''
        :param headline: 测试用例的每列的标题
        :return:
        '''
        return self.get_data.data_dict()[rows][headline]