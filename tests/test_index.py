"""
学生登出模块测试
"""
from unittest import result

import allure
import pytest
import logging

from attr.setters import validate

from config import log_config
from utils.assert_log_util import assert_log
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml

#初始化日志
logger = logging.getLogger("test_student_login")
@pytest.mark.usefixtures("index")
@allure.epic("学生考试系统首页测试")
class TestIndex:

    @pytest.mark.parametrize("caseinfo",read_yaml("./data/test_index.yaml"))
    def test_index(self, caseinfo):
        allure.dynamic.feature(caseinfo["feature"])
        allure.dynamic.story(caseinfo["story"])
        allure.dynamic.title(caseinfo["title"])


        #先进行登录,获取coookie
        login_url = "http://localhost:8000/api/user/login"
        login_data = {
            "userName": "student",
            "password": "123456",
            "remember": False
        }
        login_res = RequestUtil.send_all_request(method="POST", url=login_url, json=login_data)
        assert login_res.json().get("code") == 1, "登录前置条件失败，无法继续登出测试"
        logger.info("前置登录成功")
        #登出
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        res = RequestUtil.send_all_request(method=method, url=url)
        result = res.json()
        print(result)
        logger.info(f"响应结果{result}")
        #断言
        validate = caseinfo.get("validate", {})
        if validate:
            if "code" in validate:
                assert_log(result["code"] == validate["code"],
                           f"返回的code错误",
                           context={"实际code": result['code'], "期望code": validate["code"]})
            if "message" in validate:
                assert_log(result["message"] == validate["message"],
                           f"返回的message错误",
                           context={"实际message": result['message'], "期望message": validate["message"]})

            # 注意：fixedPaper 在 response 下，且是一个列表
            if "fixedPaper" in validate:
                # 取出实际的第一份试卷（如果列表为空，断言会失败）
                actual_fixed_papers = result["response"].get("fixedPaper", [])
                assert_log(len(actual_fixed_papers) > 0,
                           "fixedPaper 列表为空，无法校验第一份试卷",
                           context={"实际列表": actual_fixed_papers})

                actual_paper = actual_fixed_papers[0]
                expected_paper = validate["fixedPaper"]

                # 校验试卷 id
                assert_log(actual_paper["id"] == expected_paper["id"],
                           f"返回的fixedPaper中id错误",
                           context={"实际id": actual_paper["id"], "期望id": expected_paper["id"]})
                # 校验试卷 name
                assert_log(actual_paper["name"] == expected_paper["name"],
                           f"返回的fixedPaper中name错误",
                           context={"实际name": actual_paper["name"], "期望name": expected_paper["name"]})
                # 校验 limitStartTime
                assert_log(actual_paper["limitStartTime"] == expected_paper.get("limitStartTime"),
                           f"返回的fixedPaper中limitStartTime错误",
                           context={"实际limitStartTime": actual_paper["limitStartTime"],
                                    "期望limitStartTime": expected_paper.get("limitStartTime")})
                # 校验 limitEndTime
                assert_log(actual_paper["limitEndTime"] == expected_paper.get("limitEndTime"),
                           f"返回的fixedPaper中limitEndTime错误",
                           context={"实际limitEndTime": actual_paper["limitEndTime"],
                                    "期望limitEndTime": expected_paper.get("limitEndTime")})

            # timeLimitPaper 也在 response 下
            if "timeLimitPaper" in validate:
                assert_log(result["response"]["timeLimitPaper"] == validate["timeLimitPaper"],
                           f"返回的timeLimitPaper错误",
                           context={"实际timeLimitPaper": result["response"]["timeLimitPaper"],
                                    "期望timeLimitPaper": validate["timeLimitPaper"]})

            # pushPaper 也在 response 下
            if "pushPaper" in validate:
                assert_log(result["response"]["pushPaper"] == validate["pushPaper"],
                           f"返回的pushPaper错误",
                           context={"实际pushPaper": result["response"]["pushPaper"],
                                    "期望pushPaper": validate["pushPaper"]})
        logger.info(f"{caseinfo['title']}")