# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 16:02
#@Author: dongyani
#@Function: 首页的icon组切换

import unittest
import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base
from comm.readConfig import ReadConfig


appPackage = ReadConfig().get_config("appPackage")
list_home_icon = ["CIBN", "央视", "卫视"]

class Home_icon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #打开应用，进入首页
        cls.driver = webDriver().get_driver()
        base(cls.driver).start_app()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.remove_app(appPackage)
        pass

    # 15-16
    def switch_home_icon(self, index, icon):
    # def test_switch_home_icon(self, icon = "CRI"):
        """在首页推荐页面，切换的icon图标组的按钮，等待页面刷新完成"""
        icon_xpath = f"//android.support.v7.widget.RecyclerView[@resource-id='dopool.player:id/common_rcy']/android." \
            f"widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[{index+1}]"
        # 等待推荐页面的icon按钮刷新出来
        common.delayed_get_element(self.driver, 60, ("xpath", icon_xpath)).click()
        common.delayed_get_element(self.driver, 60, ("id", "dopool.player:id/title_head"))
        # android.widget.FrameLayout：页面中模块的类名，页面一般会有多个这样的模块
        page_elements = self.driver.find_elements_by_class_name("android.widget.ImageView")
        self.driver.find_element_by_id("dopool.player:id/common_page_finish").click()
        self.assertTrue(len(page_elements) > 1, f"首页-推荐页面的icon组-{icon}页面未刷新出来")

    @staticmethod
    def getTestFunc(index, icon):
        def func(self):
            self.switch_home_icon(index, icon)
        return func

def __generateTestCases():
    for index, icon in enumerate(list_home_icon):
        setattr(Home_icon, 'test_switch_home_icon_%s' % (icon),
                Home_icon.getTestFunc(index, icon))

__generateTestCases()