import time

from pages.user_userinfo_page import UserinfoPage

import pytest


class TestUserInfoPage():

    @pytest.fixture(autouse=True)
    def open(self, userInfoPage:UserinfoPage):
        userInfoPage.open("/users/userinfo/")


    def test_nickname_1(self, userInfoPage:UserinfoPage):
        '''昵称为空，点击保存，提示：请输入昵称！'''
        userInfoPage.clear_nick_name_text()
        userInfoPage.input_nickname("")
        userInfoPage.click_save_btn()
        actual_result = userInfoPage.get_error_tips()
        # 断言
        assert actual_result == "请输入昵称！"

    @pytest.mark.parametrize("test_input", ["成都刀与菊", "juju"])
    def test_nickname_2(self, userInfoPage:UserinfoPage, test_input):
        '''昵称：成都juju，点击保存,保存成功提示'''
        userInfoPage.clear_nick_name_text()
        userInfoPage.input_nickname(test_input)
        userInfoPage.click_save_btn()
        actual_result = userInfoPage.get_with_save_dialog_text()
        # 断言
        assert actual_result == "个人信息修改成功！"

    def test_nickname_3(self, userInfoPage:UserinfoPage):
        '''昵称输入框输入超过10个字符，只显示10个字符'''
        userInfoPage.clear_nick_name_text()
        userInfoPage.input_nickname("yeuialoihdq") # 11个字符
        userInfoPage.click_save_btn()
        actual_result = userInfoPage.get_nickname_attr()
        # 断言
        assert actual_result == "yeuialoihd"