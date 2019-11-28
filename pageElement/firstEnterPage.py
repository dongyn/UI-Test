# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 17:07
#@Author: pengjuan
#@UITest: 用户首次安装进入app

import comm.common as common

# 允许手机电视访问权限
def click_permisson_allow(driver):
    common.find_id("com.android.packageinstaller:id/permission_allow_button").click()

# 跳过广告
def click_skip(driver):
    common.find_id("@+id/tv_skip").click()

# 引导页面
def swipe_guide(driver, n):
    common.find_id("dopool.player:id/splash_img_gugitide").swipeLeft()

# 立即体验
def click_experience(driver):
    common.find_id("dopool.player:id/btn_start_experience").click()

# 去勾选360.apk
def click_checkbox(self, driver):
    common.find_id("dopool.player:id/iv_checkbox").click()

# 不需要开启通知
def click_cancle(driver):
    common.find_id("dopool.player:id/tv_nf_cancle").click()

# 检测是否有升级
def is_update(driver):
    isExist = common.isElementExist(id, driver, "dopool.player:id/tv_update_cancle")
    return isExist
# 单击不升级
def click_update(driver):
    common.find_id("dopool.player:id/tv_update_cancle").click()

def check_icon(driver):
    common.find_name("android.widget.TextView").is_displayed()