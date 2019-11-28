# -*- coding:utf-8 -*-
#@Time  : 2019/8/15 18:14
#@Author: pengjuan

import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base


driver = webDriver().get_driver()
base = base(driver)

class Login_Page():
    """
    1. 点击 [我的]
    2. 点击 [头像]
    3. 输入手机号+验证码
    4. 点击登录
    :return:
     """
    def __init__(self):
        self.driver = driver

    # 点击登录icon
    def login_page_text(self):
        return common.delayed_get_element(driver, 5, ("id", "dopool.player:id/userId")).text




