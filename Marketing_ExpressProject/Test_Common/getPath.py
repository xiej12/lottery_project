#coding:utf-8
import os

def directory(dirname):
    '''
    :param dirname: 目录名
    :return:
    '''
    # 获取当前目录
    prodir = os.path.dirname(os.path.realpath(__file__))
    #print(prodir)
    # 获取上一级目录
    parentdir = os.path.dirname(prodir)
    #print(parentdir)
    #拼接log存放路径
    logdir = os.path.join(parentdir, dirname)
    #print(logdir)
    # 如果目录不存在，则创建该目录
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    return logdir

if __name__ == '__main__':
    directory('Test_Case')