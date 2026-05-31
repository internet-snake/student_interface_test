import logging

import pytest

@pytest.fixture(scope="module",autouse=False,name="log")
def login_module_stu():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行学生登录测试================================================")
    yield
    logger.info("==================================学生登录测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="register")
def register_module_stu():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行学生注册测试================================================")
    yield
    logger.info("================================学生注册测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="logout")
def logiut_module_stu():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行学生登出测试================================================")
    yield
    logger.info("================================学生登出测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="index")
def index_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行考试首页测试================================================")
    yield
    logger.info("================================考试首页测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="task")
def task_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行学生任务测试================================================")
    yield
    logger.info("================================学生任务测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="subject")
def subject_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行学科列表测试================================================")
    yield
    logger.info("================================学科列表测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="paperpage")
def paperpage_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行试卷分页测试================================================")
    yield
    logger.info("================================试卷分页测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="paperselect")
def paperselect_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行试卷查询测试================================================")
    yield
    logger.info("================================试卷查询测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="papersubmit")
def papersubmit_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行试卷提交测试================================================")
    yield
    logger.info("================================试卷提交测试完成================================================")

@pytest.fixture(scope="module",autouse=False,name="answerread")
def answerread_module():
    logger = logging.getLogger("test_student_login")
    logger.info("===============================开始执行答卷查询测试================================================")
    yield
    logger.info("================================答卷查询测试完成================================================")