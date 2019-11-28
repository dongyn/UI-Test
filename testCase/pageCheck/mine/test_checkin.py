# -*- coding:utf-8 -*-
#@Time  : 2019/9/2 16:23
#@Author: dongyani
#@Function: checkin

import unittest, time
import comm.common as common
from comm.webDriver import webDriver
from pageElement.base_element_operate import base
from pageElement.checkInPage import checkin_page

driver = webDriver().get_driver()
base = base(driver)
checkin_page = checkin_page()

class CheckIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base.bottom_navigation_button("我的").click()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_checkin_notloggedin(self):
        """未登录时,签到页面下显示未登录"""
        checkin_down_text = checkin_page.checkin_down_text()
        self.assertEqual("未登录", checkin_down_text, "未登录时，签到按钮下方应显示未登录")


    def test_02_clickcheckin_loginpage(self):
        """未登录：点击登录跳转到登录页面"""
        driver.find_element_by_xpath("//*[@text='签到']").click()
        time.sleep(3)
        self.assertTrue(common.find_id("dopool.player:id/phoneEdit"), "点击签到应跳转到登录页面")

    def test_03_dailycheckin_before_checkin(self):
        """点击立即签到之前：本期已连续签到0天，第一天：可领取，立即签到按钮亮显"""
        base.login("//android.widget.ImageView[@resource-id='dopool.player:id/img_user_head']")
        driver.find_element_by_xpath("//*[@text='签到']").click()
        checkin_days = common.delayed_get_element(driver, 3, ("id", "dopool.player:id/tv_sign_days")).text
        self.assertEqual("本期已连续签到0天", checkin_days, "点击签到之前，每日签到页面应显示本期已连续签到0天")
        first_day_xpath = "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android." \
                "widget.LinearLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget." \
                "LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]"
        first_day = driver.find_element_by_xpath(first_day_xpath).text
        self.assertEqual("可领取", first_day, "点击签到之前，每日签到第一天应显示可领取")
        checkin_sign_xpath = "//android.widget.Button[@resource-id='dopool.player:id/btn_sign']"
        checkin_sign = driver.find_element_by_xpath(checkin_sign_xpath).text
        self.assertEqual("立即签到", checkin_sign, "点击签到之前，签到按钮应显示立即签到")
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='dopool.player:id/img_close']").click()


    def test_04_dailycheckin_after_checkin(self):
        """点击后：本期已连续签到1天，第一天：已领取，已签到按钮灰显;查看金币金额：累加5金币;签到显示已签到1天"""
        base.login("//android.widget.ImageView[@resource-id='dopool.player:id/img_user_head']")
        gold_coins_number = int(checkin_page.View_gold_coins_number())
        driver.find_element_by_xpath("//*[@text='签到']").click()
        common.delayed_get_element(driver, 3, ("id", "dopool.player:id/btn_sign")).click() #点击立即签到
        checkin_days = common.delayed_get_element(driver, 3, ("id", "dopool.player:id/tv_sign_days")).text
        self.assertEqual("本期已连续签到1天", checkin_days, "点击签到之后，每日签到页面应显示本期已连续签到1天")
        first_day_xpath = "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android." \
                          "widget.LinearLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget." \
                          "LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]"
        first_day = driver.find_element_by_xpath(first_day_xpath).text
        self.assertEqual("已领取", first_day, "点击签到之前，每日签到第一天应显示已领取")
        checkin_sign_xpath = "//android.widget.Button[@resource-id='dopool.player:id/btn_sign']"
        checkin_sign = driver.find_element_by_xpath(checkin_sign_xpath).text
        self.assertEqual("已签到", checkin_sign, "点击签到之前，签到按钮应显示立即签到")
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='dopool.player:id/img_close']").click()
        checkin_after_gold_coins_number = int(checkin_page.View_gold_coins_number())
        self.assertEqual(gold_coins_number + 5, checkin_after_gold_coins_number, "第一天签到之后，金币数量应累加5个")
        chenkin_sign = driver.find_element_by_xpath("//android.widget.TextView[@resource-id='dopool.player:id/signTv']").text
        self.assertEqual("已签到1天", chenkin_sign, "签到后签到按钮下应显示：已签到1天")








