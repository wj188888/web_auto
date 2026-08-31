import pytest
from pages.users_login_page import UserLoginPage


class TestUserLoginPage():
    @pytest.fixture(autouse=True)
    def open(self, userLoginPage:UserLoginPage):
        userLoginPage.open("/users/login/")

    def test_login_email_null(self, userLoginPage:UserLoginPage):
        '''邮箱为空，登录失败，提示文字检查'''
        userLoginPage.input_login_email("")
        userLoginPage.input_login_pwd("123242")
        userLoginPage.click_login_btn()

        # 实际结果
        actual_results = userLoginPage.get_tips_text()
        # 断言
        assert "这个字段是必须的" in actual_results