# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 16:02
#@Author: dongyani
#@Function: 首页的标签

import unittest
import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base
from comm.readConfig import ReadConfig

appPackage = ReadConfig().get_config("appPackage")
list_home_tabs = ["推荐(固定)", "70年", "电影", "热剧", "财经", "综艺", "动漫", "娱乐", "知宿", "体育", "纪录", "汽车",
  "文艺院线", "CRI", "真实影像", "青少", "生活", "音乐", "文化中国", "中国城市"]

class Home_tab(unittest.TestCase):

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

    # 7-14
    def switch_home_tabs(self, tab):
        """在首页推荐页面，点击顶部tabs列表按钮，在列表中点击要切换的tab，等待页面刷新完成后，点击顶部tabs列表按钮，循环以上操作"""
        base(self.driver).switch_home_tab(tab)
        common.delayed_get_element(self.driver, 60, ("id", "dopool.player:id/image"))
        page_elements = self.driver.find_elements_by_class_name("android.widget.ImageView")
        self.assertTrue(len(page_elements) > 1, f"首页-{tab}页面的元素未刷新出来")

    @staticmethod
    def getTestFunc(tab):
        def func(self):
            self.switch_home_tabs(tab)
        return func

def __generateTestCases():
    for tab in list_home_tabs:
        setattr(Home_tab, 'test_switch_home_%s' % (tab),
                Home_tab.getTestFunc(tab))

__generateTestCases()
