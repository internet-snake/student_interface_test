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
@pytest.mark.usefixtures("task")
@allure.epic("学生任务系统测试")
class TestIndex:

    @pytest.mark.parametrize("caseinfo",read_yaml("./data/test_student_task.yaml"))
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

            # 校验任务列表 tasks
            if "tasks" in validate:
                actual_tasks = result.get("response", [])
                expected_tasks = validate["tasks"]

                # 校验任务数量
                assert_log(len(actual_tasks) == len(expected_tasks),
                           f"任务数量不匹配",
                           context={"实际数量": len(actual_tasks), "期望数量": len(expected_tasks)})

                # 逐个任务校验
                for idx, (actual, expected) in enumerate(zip(actual_tasks, expected_tasks)):
                    # 校验任务 id
                    assert_log(actual.get("id") == expected.get("id"),
                               f"第{idx + 1}个任务 id 错误",
                               context={"实际id": actual.get("id"), "期望id": expected.get("id")})
                    # 校验任务 title
                    assert_log(actual.get("title") == expected.get("title"),
                               f"第{idx + 1}个任务 title 错误",
                               context={"实际title": actual.get("title"), "期望title": expected.get("title")})

                    # 校验 paperItems
                    actual_items = actual.get("paperItems", [])
                    expected_items = expected.get("paperItems", [])
                    assert_log(len(actual_items) == len(expected_items),
                               f"第{idx + 1}个任务的 paperItems 数量不匹配",
                               context={"实际数量": len(actual_items), "期望数量": len(expected_items)})

                    for j, (a_item, e_item) in enumerate(zip(actual_items, expected_items)):
                        # 校验 examPaperId
                        assert_log(a_item.get("examPaperId") == e_item.get("examPaperId"),
                                   f"第{idx + 1}个任务第{j + 1}个 paperItem 的 examPaperId 错误",
                                   context={"实际": a_item.get("examPaperId"), "期望": e_item.get("examPaperId")})
                        # 校验 examPaperName
                        assert_log(a_item.get("examPaperName") == e_item.get("examPaperName"),
                                   f"第{idx + 1}个任务第{j + 1}个 paperItem 的 examPaperName 错误",
                                   context={"实际": a_item.get("examPaperName"), "期望": e_item.get("examPaperName")})
                        # 如果期望值不为 None，则校验 examPaperAnswerId 和 status
                        if e_item.get("examPaperAnswerId") is not None:
                            assert_log(a_item.get("examPaperAnswerId") == e_item.get("examPaperAnswerId"),
                                       f"第{idx + 1}个任务第{j + 1}个 paperItem 的 examPaperAnswerId 错误",
                                       context={"实际": a_item.get("examPaperAnswerId"),
                                                "期望": e_item.get("examPaperAnswerId")})
                        if e_item.get("status") is not None:
                            assert_log(a_item.get("status") == e_item.get("status"),
                                       f"第{idx + 1}个任务第{j + 1}个 paperItem 的 status 错误",
                                       context={"实际": a_item.get("status"), "期望": e_item.get("status")})
        logger.info(f"{caseinfo['title']}")