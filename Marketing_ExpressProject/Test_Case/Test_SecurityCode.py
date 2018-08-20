#coding:utf-8
from Test_Common import myUnit,insert_img
from SecurityCode_Page import SecurityCode
import unittest

class SecurityCodeTest(myUnit.Lottery_Start):
    # @unittest.skip('skip this case')
    def test_securitycode1(self):
        '''输入正确的安全码！'''
        print("securitycode1 开始测试！")
        securitycode = SecurityCode(self.driver)
        username = securitycode.getdata(0)['username']
        password = securitycode.getdata(0)['password']
        security_code = securitycode.getdata(0)['securityCode']
        verify = securitycode.get_other(0,'verify')
        securitycode.securitycode_action(username,password,security_code)
        securitycode.await_time(2)
        self.assertEqual(securitycode.verify_securitycode_pass(),verify)
        insert_img.insert_img(self.driver, "verify_securitycode_succeed.jpg")
        print("securitycode1 测试结束")

    # @unittest.skip('skip this case')
    def test_securitycode2(self):
        '''输入错误的安全码！'''
        print("securitycode2 开始测试！")
        securitycode = SecurityCode(self.driver)
        username = securitycode.getdata(1)['username']
        password = securitycode.getdata(1)['password']
        security_code = securitycode.getdata(1)['securityCode']
        verify = securitycode.get_other(1, 'verify')
        securitycode.securitycode_action(username,password,security_code)
        securitycode.await_time(2)
        self.assertEqual(securitycode.verify_securitycode_fail(), verify)
        insert_img.insert_img(self.driver, "verify_securitycode_fail.jpg")
        print("securitycode2 测试结束")

        # @unittest.skip('skip this case')

    def test_securitycode3(self):
        '''输入错误的安全码！'''
        print("securitycode3 开始测试！")
        securitycode = SecurityCode(self.driver)
        username = securitycode.getdata(2)['username']
        password = securitycode.getdata(2)['password']
        security_code = securitycode.getdata(2)['securityCode']
        verify = securitycode.get_other(2, 'verify')
        securitycode.securitycode_action(username, password, security_code)
        securitycode.await_time(2)
        self.assertEqual(securitycode.verify_securitycode_fail(), verify)
        insert_img.insert_img(self.driver, "verify_securitycode_fail.jpg")
        print("securitycode3 测试结束")

    def test_securitycode4(self):
        '''输入错误的安全码！'''
        print("securitycode4 开始测试！")
        securitycode = SecurityCode(self.driver)
        username = securitycode.getdata(3)['username']
        password = securitycode.getdata(3)['password']
        security_code = securitycode.getdata(3)['securityCode']
        verify = securitycode.get_other(3, 'verify')
        securitycode.securitycode_action(username, password, security_code)
        securitycode.await_time(2)
        self.assertEqual(securitycode.verify_securitycode_fail(), verify)
        insert_img.insert_img(self.driver, "verify_securitycode_fail.jpg")
        print("securitycode4 测试结束")

if __name__ == "__main__":
    unittest.main()
