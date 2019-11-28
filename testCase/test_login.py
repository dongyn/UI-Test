# -*- coding:utf-8 -*-
#@Time  : 2019/8/29 17:23
#@Author: pengjuan

import unittest
import comm.webDriver as driver
from pageElement.base_element_operate import base
from pageElement.loginPage import Login_Page

driver = driver().setUpClass()
base = base()
Login_Page = Login_Page

class Login(driver, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base.bottom_navigation_button("我的").click()


    @classmethod
    def tearDownClass(cls):
        pass

    def test_login(self):
        """输入正确的手机号和验证码，点击登录"""
        base.login("dopool.player:id/img_user_head")
        self.assertTrue(Login_Page().login_page_text(), "用户ID:7576640")













