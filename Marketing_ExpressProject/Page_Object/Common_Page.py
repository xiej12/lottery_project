#coding:utf-8
from Base_Page import BasePage
from selenium.webdriver.common.by import By

class CommonPage(BasePage):
    #账户输入框元素对象
    account_loc = (By.ID,'com.gzc.mylotterychat:id/et_username')
    #密码输入框元素对象
    password_loc = (By.ID,'com.gzc.mylotterychat:id/et_password')
    #登录按钮元素对象
    login_loc = (By.ID,'com.gzc.mylotterychat:id/bt_login')
    #首页个人中心按钮元素对象
    personal_center_loc = (By.ID,'com.gzc.mylotterychat:id/btn_personal_center')
    #退出登录按钮元素对象
    logout_loc = (By.XPATH,"//android.widget.TextView[@text='退出登录']")

    def input_account(self,username):
        # 清空账户输入框
        self.find_element(*self.account_loc).clear()
        #输入账户名
        self.find_element(*self.account_loc).send_keys(username)

    def input_password(self,pwd):
        # 清空密码输入框
        self.find_element(*self.password_loc).clear()
        #输入密码
        self.find_element(*self.password_loc).send_keys(pwd)

    def click_login(self):
        #点击登录
        self.find_element(*self.login_loc).click()

    def login_action(self,username,pwd):
        #用户登录
        self.input_account(username)
        self.input_password(pwd)
        self.click_login()

    def click_personal_center(self):
        #点击个人中心按钮
        self.await_time(3)
        self.find_element(*self.personal_center_loc).click()

    def click_logout(self):
        #点击退出登录
        self.find_element(*self.logout_loc).click()

    def logout_action(self):
        #退出登录状态
        self.click_personal_center()
        self.click_logout()

    def log_off_action(self,username,pwd):
        #登录并退出
        self.login_action(username,pwd)
        self.logout_action()