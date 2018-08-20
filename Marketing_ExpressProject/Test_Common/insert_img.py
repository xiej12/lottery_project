#coding:utf-8
import os
from selenium import webdriver

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    #print(func_path)
    base_dir=os.path.dirname(func_path)
    #print(base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    #print(base_dir)

    base=base_dir.split('/Marketing_ExpressProject')[0]

    #print(base)
    filepath=base+'/Marketing_ExpressProject/Test_Report/screenshot/'+filename
    #print(filepath)
    driver.get_screenshot_as_file(filepath)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver, 'sougou.png')
