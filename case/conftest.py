import pytest
from selenium import webdriver

from pages.register_page import RegisterPage
from pages.users_login_page import UserLoginPage
from pages.users_feedbackiframe_page import UserFeedbackiframePage
from pages.user_userinfo_page import UserinfoPage
from common.connect_mysql import DBConnect, db_conf


@pytest.fixture(scope="session", name="driver")
def bowser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit() # 退出浏览器

@pytest.fixture(scope="session")
def base_url():
    url = r"http://47.116.12.183:8200"
    return url

@pytest.fixture(scope="session")
def registerPage(driver, base_url):
    register = RegisterPage(driver, base_url)
    return register

@pytest.fixture(scope="session")
def userLoginPage(driver, base_url):
    userLogin = UserLoginPage(driver, base_url)
    return userLogin

@pytest.fixture(scope="session")
def userFeedbackiframePage(driver, base_url):
    userFeedbackiframe = UserFeedbackiframePage(driver, base_url)
    return userFeedbackiframe

@pytest.fixture(scope="session")
def db():
    '''db实例化，一次session对话，实例化一次'''
    _db = DBConnect(db_conf=db_conf, database="online") # 可以修改连接的数据库
    yield _db
    _db.close()

@pytest.fixture(scope="session")
def login_dirver(driver, base_url):
    userLoginPage = UserLoginPage(driver, base_url)
    userLoginPage.open("/users/login/")
    userLoginPage.input_login_email("1112345678@qq.com")
    userLoginPage.input_login_pwd("31234567")
    userLoginPage.click_login_btn()
    return driver



@pytest.fixture(scope="session")
def userInfoPage(login_dirver, base_url):
    userInfoPage= UserinfoPage(login_dirver, base_url)
    return userInfoPage





# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------

# 关于用例执行失败截图
# conftest.py (简洁版)
# 待补充