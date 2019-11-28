# -*- coding:utf-8 -*-
#@Time  : 2019/9/2 16:23
#@Author: dongyani
#@Function:startup & upgrade

import unittest
import comm.common as common
from comm.webDriver import webDriver
from comm.readConfig import ReadConfig
from pageElement.base_element_operate import base

global upgrade
upgrade = ReadConfig().get_test("upgrade")
appPackage = ReadConfig().get_config("appPackage")

class Startup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webDriver().get_driver()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.remove_app(appPackage)
        pass

    # 1,2
    def test_01_startapp(self):
        """验证三个引导页面，点击立即体验，进入首页"""
        base(self.driver).start_login_app()
        home_text = self.driver.find_element_by_id("dopool.player:id/tabText").text
        self.assertEqual("首页", home_text, "打开app后，默认定位在首页")


    # 3
    @unittest.skipIf(upgrade == "Ture", '弹出升级框才会验证升级')
    def test_02_upgrade(self):
        """点击立即升级，等待更新完毕，等待安装完毕，打开，进入首页"""
        base(self.driver).slide_guide_page()
        base(self.driver).enter_app()
        base(self.driver).close_privacy()
        common.delayed_get_element(self.driver, 6, ("id", "dopool.player:id/tv_update_now")).click()
        base(self.driver).permission_prompt()
        base(self.driver).enter_app()
        base(self.driver).close_privacy()
        base(self.driver).close_float()
        home_text = self.driver.find_element_by_id("dopool.player:id/tabText").text
        self.assertEqual("首页", home_text, "打开app后，默认定位在首页")










