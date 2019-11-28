# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 18:30
#@Author: pengjuan
#@Function: vip

import unittest
import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base
from comm.readConfig import ReadConfig

appPackage = ReadConfig().get_config("appPackage")

class Vip(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #打开应用，进入
        cls.driver = webDriver().get_driver()
        base(cls.driver).start_app()
        base(cls.driver).bottom_navigation("会员").click()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.remove_app(appPackage)
        pass

    # 34
    def test_01_vip_page(self):
        """在vip页面，查看显示正常"""
        buy_vip_element =  common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/tv_buy_vip")).text()
        self.assertEqual(buy_vip_element, "开通会员", "vip页面未能正常刷新显示")

    # 35
    def test_02_try_watch(self):
        """
        点击会员视频，试看
        """
        base(self.driver).watch_vip_video()
        video_element = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/tv_hd_buy_memberships")).text
        self.assertEqual(video_element, "购买VIP会员", "购买VIP会员按钮未出现，VIP视频试看异常。")

    # 36
    def test_03_buy_pay_vip(self):
        """
        购买VIP会员 - 支付
        """
        base(self.driver).watch_vip_video()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/tv_hd_buy_memberships")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/btn_pay")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/backImage")).click()
        open_vip_element = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/tv_vip_protocal")).text
        self.assertEqual(open_vip_element, "《会员服务协议》", "未正常返回到开通VIP页面")






