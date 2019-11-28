# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 16:02
#@Author: dongyani
#@Function: 直播页面的标签切换

import unittest, time
import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base
from comm.readConfig import ReadConfig

appPackage = ReadConfig().get_config("appPackage")
list_stream_tabs = ["推荐", "CIBN", "央视", "卫视", "特色", "地方台", "国际"]

class Stream_tab(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webDriver().get_driver()
        base(cls.driver).start_app()
        base(cls.driver).bottom_navigation("直播")

    @classmethod
    def tearDownClass(cls):
        cls.driver.remove_app(appPackage)
        pass

    # 19-31
    def switch_stream_tabs(self, tab):
        """在直播页面，点击顶部tabs列表按钮，在列表中点击要切换的tab，等待页面刷新完成后，点击顶部tabs列表按钮，循环以上操作"""
        if tab == "CIBN": time.sleep(2) #CIBN页签不加延时过不去
        if tab == "国际": common.swipeLeft(self.driver)
        common.delayed_get_element(self.driver, 3, ("xpath", f"//*[@text='{tab}']")).click()
        common.delayed_get_element(self.driver, 60, ("id", "dopool.player:id/image"))
        page_elements = self.driver.find_elements_by_class_name("android.widget.ImageView")
        self.assertTrue(len(page_elements) > 1, f"直播-{tab}页面的元素未刷新出来")


    @staticmethod
    def getTestFunc(tab):
        def func(self):
            self.switch_stream_tabs(tab)
        return func

def __generateTestCases():
    for tab in list_stream_tabs:
        setattr(Stream_tab, 'test_switch_stream_%s' % (tab),
                Stream_tab.getTestFunc(tab))

__generateTestCases()
