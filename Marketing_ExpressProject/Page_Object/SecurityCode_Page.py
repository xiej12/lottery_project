#coding:utf-8
from Base_Page import BasePage
from selenium.webdriver.common.by import By
from Common_Page import CommonPage

class SecurityCode(BasePage):
    #安全码输入框元素
    securitycode_loc = (By.ID, 'com.gzc.mylotterychat:id/et_code')
    #确认按钮元素
    comfirm_loc = (By.ID,'com.gzc.mylotterychat:id/bt_sure')
    #登录按钮元素
    denglu_loc = (By.ID,'com.gzc.mylotterychat:id/bt_login')

    def clear_securitycode_input_box(self,username,password):
        #清空输入框
        if self.find_element(*self.securitycode_loc) == False:
            self.com = CommonPage(self.driver)
            try:
                self.com.log_off_action(username,password)
                self.find_element(*self.securitycode_loc).clear()
            except:
                self.com.logout_action()
                self.find_element(*self.securitycode_loc).clear()


    def input_securitycode(self,securitycodetemp):
        #输入安全码
        self.find_element(*self.securitycode_loc).send_keys(securitycodetemp)

    def click_comfirm(self):
        #点击确认
        self.await_time(3)
        self.find_element(*self.comfirm_loc).click()

    def securitycode_action(self,username,password,securitycodetemp):
        self.clear_securitycode_input_box(username,password)
        self.input_securitycode(securitycodetemp)
        self.click_comfirm()

    #判断是否验证安全码失败
    def verify_securitycode_fail(self):
        '''
        :return:返回确认按钮文本
        '''
        self.await_time(3)
        return self.find_element(*self.comfirm_loc).text

    def verify_securitycode_pass(self):
        '''
        :return:返回登录按钮文本
        '''
        self.await_time(3)
        return self.find_element(*self.denglu_loc).text