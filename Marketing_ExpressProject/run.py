#coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


if __name__ == '__main__':

    report_dir='./Test_Report'
    test_dir='./Test_Case'

    print("start run test case")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="Test_*.py")

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + r'/result.html'

    print("start write report..")
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="测试用例执行情况")
        runner.run(discover)
        f.close()