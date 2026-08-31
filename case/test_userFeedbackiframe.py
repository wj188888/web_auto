import pytest

from pages.users_feedbackiframe_page import UserFeedbackiframePage

class TestUserFeedbackiframe:

    @pytest.fixture(autouse=True)
    def open(self, userFeedbackiframePage:UserFeedbackiframePage):
        userFeedbackiframePage.open("/users/feedbackiframe/")
        userFeedbackiframePage.feedback_switch_iframe() # 切换到iframe上去


    def test_feedback_1(self, userFeedbackiframePage:UserFeedbackiframePage):
        '''反馈类型有三个，下拉检查是否是1.改进建议，页面布局、提BUG'''
        all_results = userFeedbackiframePage.select_all_object()
        actual_results = "".join(str(all_results).split())  # 去掉空格
        assert actual_results == "['改进建议','页面布局','提BUG']"



    # def test_feedback_2(self, userFeedbackiframePage:UserFeedbackiframePage):
    #     '''反馈的值是否被分别选中了'''
    #     userFeedbackiframePage.do_select_object(value="改进建议")
    #     # 断言
    #     assert userFeedbackiframePage.selected_value() == "改进建议"
    #
    #     userFeedbackiframePage.do_select_object(value="页面布局")
    #     assert userFeedbackiframePage.selected_value()== "页面布局"
    #
    #     userFeedbackiframePage.do_select_object(value="提BUG")
    #     assert userFeedbackiframePage.selected_value() == "提BUG"

    @pytest.mark.parametrize("test_input", ["改进建议", "页面布局", "提BUG"])
    def test_feedback_select(self, userFeedbackiframePage:UserFeedbackiframePage, test_input):
        '''参数化优化上述代码，减少重复'''
        userFeedbackiframePage.do_select_object(value=test_input)
        assert userFeedbackiframePage.selected_value() == test_input

    def test_feedback_send(self, userFeedbackiframePage:UserFeedbackiframePage):
        '''反馈类型：改进建议，反馈内容为空，联系邮箱为空，alert提示：提交成功！'''
        userFeedbackiframePage.do_select_object("改进建议")
        userFeedbackiframePage.input_textarea("")
        userFeedbackiframePage.input_email("")
        userFeedbackiframePage.click_send()

        text = userFeedbackiframePage.get_alert_text()
        # 断言
        assert text == "提交成功！"


    @pytest.mark.parametrize("test_input, expected", [
        [{"subject": "改进建议", "content": "", "email": ""},  "提交成功！"],
        [{"subject": "改进建议", "content": "测试反馈内容", "email": ""}, "提交成功！"],
        [{"subject": "改进建议", "content": "", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "改进建议", "content": "测试反馈内容22", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "页面布局", "content": "", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "提BUG", "content": "测试反馈内容333", "email": "1111@qq.com"}, "提交成功！"],

    ])
    def test_feedback_send_params(self, userFeedbackiframePage:UserFeedbackiframePage,test_input, expected):
        '''参数化上述操作，把其他用例补充进去'''
        userFeedbackiframePage.do_select_object(test_input["subject"])
        userFeedbackiframePage.input_textarea(test_input["content"])
        userFeedbackiframePage.input_email(test_input["email"])
        userFeedbackiframePage.click_send()

        text = userFeedbackiframePage.get_alert_text()
        # 断言
        assert text == expected