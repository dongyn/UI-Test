# -*- coding:utf-8 -*-
#@Time  : 2019/8/28
#@Author: yanghuiyu
#@UITest：意见反馈页面

import comm.common as common
from comm.Log import Logger

logger = Logger().get_logger()

def mine(driver):
    # 点击底部“我的”
    xpath = "//android.widget.LinearLayout[@resource-id='dopool.player:id/bottomNavigationView']/android.widget." \
            "FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.ImageView[1]"
    driver.find_element_by_xpath(xpath).click()
def feedback(driver):
    # 点击意见反馈
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='dopool.player:id/rcy_other']/android.view.View[1]").click()


def opinion(driver):
    # 在意见反馈页面
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.TextView[2]").click()


def q_a(driver):
    # 在常见问题页面
    driver.find_element_by_xpath("//*[@text='常见问题']").click()


def set_message(driver, key):
    # 输入意见
    driver.find_element_by_id("dopool.player:id/sug_edt_content").send_key(key)


def set_set(driver):
    # 点击发送
    driver.find_element_by_id("dopool.player:id/sug_tv_send").click()


def unlogin_set(self,driver):
    # 未登录首次进入意见反馈页面
    unlogin_xpath = "//*[@text='填写意见反馈需要您先登录并且绑定手机号哦~'']"
    unlogin_toast_element = common.delayed_get_element(driver, 5, ("xpath", unlogin_xpath))
    self.assertEqual("填写意见反馈需要您先登录并且绑定手机号哦~",unlogin_toast_element.text,msg="未进入已经反馈页面")

def none_set(self,driver):
    # 发送的意见为空
    none_toast_element = common.delayed_get_element(driver, 5, ("xpath", "//*[@text='您反馈的内容不能为空哦~']"))
    self.assertEqual("您反馈的内容不能为空哦~",none_toast_element.text,msg="没有发送成功")


def list_message(self,driver,message):
    # 已经发送的消息
    try:
        common.delayed_get_element(driver, 5, ("xpath", f"//*[@text='{message}']"))
        return True
    except:
        logger.error('未定位到元素：' + '%s' % ())
        self.screenshot()
        return False
