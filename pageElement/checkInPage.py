# -*- coding:utf-8 -*-
#@Time  : 2019/8/15 18:35
#@Author: pengjuan
import comm.common as common

class checkin_page():
    def __init__(self, driver):
        self.driver=driver

    #查看金币数量
    def View_gold_coins_number(self):
        # 点击下我的按钮，等出现我的页面的时候获取gold_coins_number
        return common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/goldTv")).text


    # 签到按钮下方的内容
    def checkin_down_text(self):
        return common.delayed_get_element(self.driver, 50, ("id", "dopool.player:id/signTv")).text

    #点击签到，弹出每日签到页面
    # def dailycheckin_sign(self):
    #     self.driver.find_element_by_xpath("//*[@text='签到']").click()
    #     checkin_sing_xpath_list = ["//android.widget.TextView[@resource-id='dopool.player:id/tv_sign_has_get1']",
    #                                "//android.widget.Button[@resource-id='dopool.player:id/btn_sign']"]
    #     checkin_sing_list = []
    #     for sign_xpath in checkin_sing_xpath_list:
    #         checkin_sing_list.append(self.driver.find_element_by_xpath(sign_xpath).text)
    #     return checkin_sing_list








