"""
学生注册模块测试
"""
from unittest import result

import allure
import pytest
import logging
from utils.assert_log_util import assert_log
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml

#初始化日志
logger = logging.getLogger("test_student_login")
@pytest.mark.usefixtures("register")
@allure.epic("学生考试系统注册测试")
class TestStudentRegister:
    @pytest.mark.skip(reason="已经注册过了")
    @pytest.mark.parametrize("caseinfo",read_yaml("./data/test_student_register.yaml"))
    def test_student_Register(self, caseinfo):
        allure.dynamic.feature(caseinfo["feature"])
        allure.dynamic.story(caseinfo["story"])
        allure.dynamic.title(caseinfo["title"])

        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        data = caseinfo["request"].get("json", {})



        logger.info(f"数据为:{data}")

        res = RequestUtil.send_all_request(method=method, url=url, headers=headers, json=data)
        result = res.json()
        print(result)
        logger.info(f"响应结果{result}")
        #断言
        validate = caseinfo.get("validate", {})
        if validate:
            if "code" in validate:
                assert_log(result["code"] == validate["code"],
                           f"返回的code错误",
                           context={"实际code": result['code'],"期望code": validate["code"]}
                           )
            if "message" in validate:
                assert_log(result["message"] == validate["message"],
                           f"返回的message错误",
                           context={"实际message": result['message'], "期望message": validate["message"]}
                           )


        logger.info(f" {caseinfo['title']}")

