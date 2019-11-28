# -*- coding:utf-8 -*-
#@Time  : 2019/11/26 10:30
#@Author: dongyani
#@Function: 这个文件与caseList.txt一同使用，是用来单跑跑错的测试用例的。

import os, unittest

path = os.path.split(os.path.dirname(__file__))[0]
'''
read case name from 'caseList.txt'
:return:caseList
'''
def set_case_list():

    caseList = []
    caseListPath = os.path.join(os.path.split(os.path.dirname(__file__))[0], "caseList.txt")
    fb = open(caseListPath,encoding='UTF-8')
    for case in fb.readlines():
        caseName = str(case)
        if caseName != "" and not caseName.startswith("#"):
            caseList.append(caseName.replace("\n", ""))
    fb.close()
    return caseList

"""
set test suite
return:suite_list
"""
def set_suite():
    global filePath
    suite_list = unittest.TestSuite()
    suite_module = []

    case_list = set_case_list()
    for case in case_list:
        case_Name = str(case)
        filePath = os.path.join(path, 'testCase'+'/')
        discover = unittest.defaultTestLoader.discover(filePath, pattern=case_Name+'.py', top_level_dir=None)
        suite_module.append(discover)

    if len(suite_module) > 0:
        for case in suite_module:
            suite_list.addTest(case)
    else:
        return None
    return suite_list


