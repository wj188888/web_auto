from common.base import Base

class RegisterPage(Base):

    email_loc = ("id", "id_email")
    # 定位父级元素/..
    email_div_loc = ("xpath", "//*[@id='id_email']/..")
    password_loc = ("id", "id_password")
    password_div_loc = ("xpath", "//*[@id='id_password']/..")
    btn_loc = ("id", "jsEmailRegBtn")

    go_login_loc = ("css selector", '.form-p>a') # 立即登录
    back_top_loc = ("class name", "index-font") # 回到首页

    register_success_loc = ("css selector", 'body>h1')

    def input_email(self, text):
        '''输入邮箱文本'''
        self.send(self.email_loc, text)

    def input_password(self, text):
        '''输入密码文本'''
        self.send(self.password_loc, text)

    def click_register_login(self):
        '''点击注册'''
        self.click(self.btn_loc)

    def click_back_top(self):
        '''点击返回首页'''
        self.click(self.back_top_loc)

    def register_success_text(self):
        '''获取注册成功提示文本'''
        return self.get_text(self.register_success_loc)

    def get_email_class(self):
        '''获取email  class属性'''
        return self.get_attribute(self.email_div_loc,"class")

    def get_password_class(self):
        '''获取password  class属性'''
        return self.get_attribute(self.password_div_loc,"class")

    def get_loc_href(self, a):
        '''对超链接进行定位，统一xpath方式
        1. 立即登录href属性检查'''
        loc = ("xpath", a)
        return self.get_attribute(loc, "href")

    # 清空函数不一定要统一写，非输入框等元素不能使用清空
    def clear_email(self):
        '''清空邮箱'''
        return self.clear(self.email_loc)

    def clear_pwd(self):
        '''清空密码款框'''
        return self.clear(self.password_loc)

    def get_email_attr(self, attr="value"):
        '''获取邮箱属性'''
        return self.get_attribute(self.email_loc, attr)

    # 使用get_pwd_attr(self, attr="type")这个方法更加好一些，可以复用几次
    def get_pwd_attr(self, attr="type"):
        '''获取密码属性'''
        return self.get_attribute(self.password_loc, attr)

    def get_to_current_url(self):
        '''获取目标url'''
        return self.driver.current_url



