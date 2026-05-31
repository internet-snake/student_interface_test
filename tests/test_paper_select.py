"""
试卷查询模块测试
"""
import allure
import pytest
import logging

from utils.assert_log_util import assert_log
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml

logger = logging.getLogger("test_student_login")

@pytest.mark.usefixtures("paperselect")
@allure.epic("学生考试系统试卷查询测试")
class TestPaperSelect:

    @pytest.mark.parametrize("caseinfo", read_yaml("./data/test_paper_select.yaml"))
    def test_paper_select(self, caseinfo):
        allure.dynamic.feature(caseinfo["feature"])
        allure.dynamic.story(caseinfo["story"])
        allure.dynamic.title(caseinfo["title"])

        login_url = "http://localhost:8000/api/user/login"
        login_data = {
            "userName": "student",
            "password": "123456",
            "remember": False
        }
        login_res = RequestUtil.send_all_request(method="POST", url=login_url, json=login_data)
        assert login_res.json().get("code") == 1, "登录前置条件失败，无法继续试卷查询测试"
        logger.info("前置登录成功")

        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]

        if method == "GET":
            res = RequestUtil.send_all_request(method=method, url=url)
        else:
            headers = caseinfo["request"].get("headers", {})
            data = caseinfo["request"].get("json", {})
            res = RequestUtil.send_all_request(method=method, url=url, headers=headers, json=data)

        result = res.json()
        print(result)
        logger.info(f"响应结果{result}")

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

        logger.info(f"{caseinfo['title']}")
