from common.base import Base

class UserFeedbackiframePage(Base):

    iframe_loc = ("id", "feedback_iframe")
    select_feedbackTpye_loc = ("class name", "select1")
    textarea_loc = ("id", "mesaage")
    email_loc = ("xpath", "//label/input[@type='text']")
    click_send_loc =  ("class name", "button")


    def feedback_switch_iframe(self):
        '''切换iframe'''
        return self.switch_iframe(self.iframe_loc)

    def select_feedbackType(self, value=""):
        '''选择反馈类型'''
        return self.select_by_value(self.iframe_loc, value)

    def input_textarea(self, text):
        '''反馈内容'''
        return self.send(self.textarea_loc, text)

    def input_email(self, text):
        '''联系方式邮箱'''
        return self.send(self.email_loc, text)

    def click_send(self):
        '''点击send'''
        return self.click(self.click_send_loc)

    def do_select_object(self, value=""):
        '''选择下拉列表的元素对象'''
        self.select_by_value(self.select_feedbackTpye_loc, value)

    def select_all_object(self):
        '''选中所有的元素对象'''
        all_objects = self.select_object(self.select_feedbackTpye_loc).options
        all_texts = [i.text for i in all_objects]
        print(f'获取的下拉列表： {all_texts}')
        return all_texts

    def selected_value(self):
        '''返回已被选中的'''
        option = self.select_object(self.select_feedbackTpye_loc).first_selected_option
        print(f"option= {option.text}")
        return option.text