from common.base import Base

class UserLoginPage(Base):

    login_username_loc = ("id", "username")
    login_password_loc = ("id", "password_l")
    login_btn_loc = ("id", "jsLoginBtn")

    login_tips_loc = ("class name", "errorlist")

    def input_login_email(self, text):
        '''输入登录邮箱'''
        return self.send(self.login_username_loc, text)

    def input_login_pwd(self, text):
        '''登录密码'''
        return self.send(self.login_password_loc, text)

    def click_login_btn(self):
        '''点击立即登录'''
        return self.click(self.login_btn_loc)


    def get_tips_text(self):
        '''获取提示文本'''
        return self.get_text(self.login_tips_loc)