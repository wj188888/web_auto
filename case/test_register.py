import time

from pages.register_page import RegisterPage
import pytest

@pytest.fixture(scope="session")
def delete_testdata(db):
    '''删除已使用的测试数据'''
    sql = 'delete from users where id=100'
    db.execute(sql)


class TestRegister:

    @pytest.fixture(autouse=True)
    def open(self, registerPage:RegisterPage):
        registerPage.open("/users/register/")

    @pytest.mark.skip()
    def test_success_register(self, registerPage:RegisterPage):
        '''
        邮箱和密码正常，注册成功
        :param registerPage:
        :return:
        '''
        # 操作步骤
        registerPage.input_email("1112345678@qq.com")
        registerPage.input_password("31234567")

        registerPage.click_register_login()

        # 实际结果
        actual_result = registerPage.register_success_text()
        # 断言
        assert actual_result == "尊敬的用户，您好，账户已激活成功！"

    def test_fail_register(self, registerPage:RegisterPage):
        '''
        注册已有的账号注册失败
        :param registerPage:
        :return:
        '''

        # 操作步骤
        registerPage.input_email("41234567@qq.com")
        registerPage.input_password("31234567")

        registerPage.click_register_login()

        # 实际结果
        actual_result = registerPage.register_success_text()
        # 断言
        assert actual_result != "尊敬的用户，您好，账户已激活成功！"


    def test_emailAndpwd_null(self, registerPage:RegisterPage):
        '''邮箱和密码为空，有红色框提示,class属性包含errorput'''
        registerPage.input_email("")
        registerPage.input_password("")
        registerPage.click_register_login()
        time.sleep(0.1)

        # 实际结果
        actual_result1 = registerPage.get_email_class()
        actual_result2 = registerPage.get_password_class()
        # 断言
        assert "errorput" in actual_result1
        assert "errorput" in actual_result2

    def test_pwd_2(self, registerPage:RegisterPage):
        '''邮箱正确，密码为空，注册失败，红狂提示，class属性为errorput'''
        registerPage.input_email("726661@126.com")
        registerPage.input_password("")
        registerPage.click_register_login()
        time.sleep(0.1)
        # 实际结果
        actual_result = registerPage.get_password_class()
        # 断言
        assert "errorput" in actual_result

    def test_email_3(self, registerPage:RegisterPage):
        '''邮箱格式不正确，密码不为空，注册失败，有红框提示，class属性包含errorput'''
        registerPage.input_email("19293892933")
        registerPage.input_password("1293821")
        registerPage.click_register_login()
        time.sleep(0.1)
        # 实际结果
        actual_result = registerPage.get_email_class()
        # 断言
        assert "errorput" in actual_result

    def test_pwd_04(self, registerPage:RegisterPage):
        '''密码超过20位的，注册失败'''
        registerPage.input_email("82726181@qq.com")
        registerPage.input_password("012345678901234567890") # 21位数字
        registerPage.click_register_login()
        time.sleep(0.1)
        # 实际结果
        actual_result = registerPage.get_password_class()
        # 断言
        assert "errorput" in actual_result

    def test_email_pwd_05(self,registerPage:RegisterPage):
        '''输入框可以清空'''
        registerPage.input_email("82726181@qq.com")
        registerPage.input_password("012345678901234567890")  # 21位数字
        registerPage.clear_pwd() # 清空密码框
        time.sleep(0.1)
        # 实际结果
        actual_result = registerPage.get_pwd_attr("value")
        assert actual_result == ""

    def test_pwd_06(self,registerPage:RegisterPage):
        '''密码输入后显示为*号，加密显示的'''
        registerPage.input_email("82726181@qq.com")
        registerPage.input_password("012345678901234567890")  # 21位数字
        # 实际结果
        actual_result = registerPage.get_pwd_attr("type")
        assert actual_result == "password"

    def test_07(self,registerPage:RegisterPage, base_url):
        '''回到首页跳转'''
        registerPage.click_back_top()
        # 实际结果
        actual_result = registerPage.get_to_current_url()
        # 断言
        assert actual_result == base_url + "/" # 当前当前url是否跳转回首页了

    def test_08(self,registerPage:RegisterPage, base_url):
        '''点击登录跳转检查'''
        # 实际结果
        actual_result = registerPage.get_loc_href("//*/div/p/a") # 立即登录也可以用 xpath:   '//*[text()="[立即登录]"'
        # 断言
        assert actual_result == base_url + "/users/login/"  # 当前当前url是否跳转回首页了
