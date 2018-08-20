#coding=utf-8
import os
import configparser
from getPath import directory

class ReadConfig(object):
    def __init__(self):
        #调用directory方法，得到文件目录路径
        dirpath = directory('Test_Config')
        #获取文件路径
        self.configPath = os.path.join(dirpath, "config.ini")
        #configparser初始化实例
        self.cf = configparser.ConfigParser()
        #读取配置文件
        self.cf.read(self.configPath)

    def get_config(self,filed,name):
        '''
        :param filed: 字段名
        :param name：key
        :return:返回键值
        '''
        result = self.cf.get(filed,name)
        return result

    def set_config(self,filed,key,value):
        '''
        :param filed: 字段名
        :param key: 字段键
        :param value: 字段值
        '''
        fd = open(self.configPath,'w',encoding='UTF-8')
        self.cf.set(filed,key,value)
        self.cf.write(fd)

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_config('EQUIPMENT', 'platformName'))