import logging

def assert_log(condition, message, context=None):
    logger = logging.getLogger("test_student_login")
    if not condition:
        if context:
            logger.error(f"断言失败: {message}，上下文: {context}")
        else:
            logger.error(f"断言失败: {message}")
    assert condition, message