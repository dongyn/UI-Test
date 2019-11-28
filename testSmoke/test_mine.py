# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 18:33
#@Author: pengjuan
#@Function: 我的页面

# import unittest, time
# import comm.common as common
# from comm.webDriver import webDriver
# from pageElement.homePage import homepage
# from comm.readConfig import ReadConfig
# from pageElement.base_element_operate import base
#
# telephone = ReadConfig().get_app("telephone")
#
# class Stream(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         #打开应用，进入首页
#         cls.driver = webDriver().get_driver()
#         base(cls.driver).start_login_app()
#         base(cls.driver).bottom_navigation("首页")
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close_app()
#         pass

import unittest
import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base
from comm.readConfig import ReadConfig

appPackage = ReadConfig().get_config("appPackage")

class Mine_tab(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webDriver().get_driver()
        base(cls.driver).start_login_app()
        base(cls.driver).play_collect_appoint_stream()
        base(cls.driver).bottom_navigation("我的")
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.remove_app(appPackage)
        pass

    # 37
    def test_01_mine_page(self):
        """在我的页面，查看页面显示正常"""
        mine_page_element = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/title_head")).text
        self.assertEquals(mine_page_element, "观看历史", "我的页面未刷新出来")

    # 38
    def test_02_switching_clarity(self):
         """
        在我的页面，查看观看历史
         """
         common.delayed_get_element(self.driver, 5, ("xpath", "//*[@text='查看更多']")).click()
         common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/imageView")).click()
         base(self.driver).click_play_float_button("backImage", [(53, 91)])
         self.assertTrue(common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/imageView")), "观看历史中无已播放过的视频")

    # 39
    def test_03_my_collection(self):
        """
         在我的页面，查看我的收藏
         """
        common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@resource-id='dopool.player:id/text'and@text='我的收藏']")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/imageView")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/backImage")).click()
        collection_element = common.delayed_get_element(self.driver, 10,("xpath", "//android.widget.TextView[@text='直播']")).text
        self.assertEqual(collection_element, "直播", "未正常返回我的收藏页面")

    # 39
    def test_04_my_appointment(self):
        """
        在我的页面，查看我的预约
        """
        common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='我的预约']")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/tv_epg_name")).click()
        base(self.driver).click_play_float_button("backImage", [(53, 91)])
        switch_stream_element = common.delayed_get_element(self.driver, 10,("id", "dopool.player:id/tv_switch_channel")).text
        self.assertEqual(switch_stream_element, "切换频道 >", "预约页面未刷新出来")

     #40
    def test_05_my_appointment(self):
        """
        在我的页面，意见反馈
        """
        common.swipeUp(self.driver)
        common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='意见反馈']")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/sug_edt_content")).send_keys("你好，还不错。")
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/sug_tv_send")).click()
        appointment_element = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/item_tv_user")).text
        self.assertEqual(appointment_element, "你好，还不错。", "意见反馈留言失败~")

    # 41
    def test_06_common_problem(self):
        """
       在我的页面，常见问题
       """
        common.swipeUp(self.driver)
        common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='意见反馈']")).click()
        common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='常见问题']")).click()
        normal_question_element = common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='我在使用手机电视软件，会收取其他费用吗？']")).text
        self.assertEqual(normal_question_element, "我在使用手机电视软件，会收取其他费用吗？", "常见问题页面未刷新出来")
    # 42
    def test_07_Setting(self):
        """
        在我的页面，设置
        """
        common.swipeUp(self.driver)
        common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='设置']")).click()
        setting_element = common.delayed_get_element(self.driver, 5, ("xpath", "//android.widget.TextView[@text='给手机电视加油']")).text
        self.assertEqual(setting_element, "给手机电视加油", "设置页面未刷新出来")

