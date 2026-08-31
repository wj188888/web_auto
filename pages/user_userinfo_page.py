import time

from common.base import Base

class UserinfoPage(Base):

    nickname_loc = ("id", "nick_name") # 昵称
    error_tips_loc = ("xpath", "//*[@class='errorput']/i") # 请输入昵称
    date_day_loc = ("id", 'date_day') # 日期
    birth_day_loc = ("id", "birth_day") # 生日
    radio_female_loc = ("xpath", "//*[@value='female']") # radio ： 女
    radio_male_loc = ("xpath", "//*[@value='male']")  # radio ： 男
    checkbox_selenium_loc = ("xpath", "//*[@value='selenium']")
    checkbox_appium_loc = ("xpath", "//*[@value='appium']")
    checkbox_cypress_loc = ("xpath", "//*[@value='cypress']") # 复选框
    address_loc = ("id", "address") # 地址
    mobile_loc = ("id", "mobile") # 手机号
    save_btn = ("id", "jsEditUserBtn") # 表单保存按钮
    dialog_tips_loc = ("xpath", "//*[@id='jsSuccessTips']/div[@class='cont']/h2") # 保存后的dialog提示，个人信息修改成功

    edit_email_loc = ("class name", "green changeemai_btn") # 邮箱修改按钮
    new_email_loc = ("id", "jsChangeEmail") # 新邮箱
    email_code_loc= ("id", "jsChangeEmailCode") # 验证码
    email_code_btn_loc = ("id", "jsChangeEmailCodeBtn") # 获取验证码按钮
    email_finish_btn_loc = ("id", "jsChangeEmailBtn") # 修改完成按钮

    def clear_nick_name_text(self):
        '''清空昵称文本内容'''
        return self.clear(self.nickname_loc)

    def input_nickname(self, text=""):
        '''输入昵称'''
        return self.send(self.nickname_loc, text)

    def get_nickname_attr(self, attr="value"):
        '''获取nickname属性'''
        time.sleep(0.1)
        return self.get_attribute(self.nickname_loc, attr)

    def input_date_day(self, text=""):
        '''输入日期'''
        return self.send(self.date_day_loc, text)

    def input_birth_day(self, text=""):
        '''输入生日'''
        return self.send(self.birth_day_loc, text)

    def select_gender_male(self):
        '''单选：选中男'''
        if not self.is_selected(self.radio_male_loc):
            self.click(self.radio_male_loc)

    def select_gender_female(self):
        '''单选：选中女'''
        if not self.is_selected(self.radio_female_loc):
            self.click(self.radio_female_loc)

    def checkbox_good(self, value="all"):
        '''兴趣多选'''
        if not "all":
            if value == "selenium":
                self.click(self.checkbox_selenium_loc)
            elif value == "appium":
                self.click(self.checkbox_appium_loc)
            elif value == "cypress":
                self.click(self.checkbox_cypress_loc)
        else:
            self.click(self.checkbox_selenium_loc)
            self.click(self.checkbox_appium_loc)
            self.click(self.checkbox_cypress_loc)

    def input_address(self, text=""):
        '''输入地址'''
        return self.send(self.address_loc, text)

    def input_mobile(self, text=""):
        '''输入手机号'''
        return self.send(self.mobile_loc, text)

    def click_email_btn(self):
        '''点击邮箱修改'''
        return self.click(self.edit_email_loc)

    def click_save_btn(self):
        '''点击保存按钮'''
        return self.click(self.save_btn)

    def get_error_tips(self):
        '''获取文本'''
        time.sleep(0.3)
        return self.get_text(self.error_tips_loc)

    def get_with_save_dialog_text(self):
        '''获取保存成功提示信息'''
        time.sleep(0.3)
        return self.get_text(self.dialog_tips_loc)