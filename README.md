# 学之思开源考试系统 - 学生端接口自动化测试

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/pytest-9.0+-green.svg" alt="Pytest">
  <img src="https://img.shields.io/badge/Allure-Reports-orange.svg" alt="Allure">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

> 基于pytest的学之思开源考试系统学生端接口自动化测试项目

## 📖 项目简介

本项目是学之思开源考试系统的学生端接口自动化测试套件，采用pytest框架结合数据驱动模式，实现了对学生端核心接口的自动化测试。

**特性：**
- 🎯 数据驱动：使用YAML文件管理测试数据，实现测试用例与代码分离
- 📊 测试报告：集成Allure报告，生成可视化的测试结果
- 🔄 会话管理：使用Session保持Cookie，实现登录状态自动管理
- 📝 日志记录：详细的测试执行日志，便于问题排查
- ✅ 断言验证：自定义断言工具，提供详细的错误上下文信息

## 🛠️ 技术栈

| 技术 | 说明 | 版本 |
|------|------|------|
| Python | 编程语言 | 3.8+ |
| pytest | 测试框架 | 9.0+ |
| requests | HTTP客户端 | - |
| Allure | 测试报告 | - |
| PyYAML | YAML解析 | - |

## 📁 项目结构

```
student_test1/
├── conftest.py                 # pytest配置文件（fixture定义）
├── data/                       # 测试数据目录
│   ├── test_index.yaml        # 首页接口测试数据
│   ├── test_student_login.yaml # 登录接口测试数据
│   ├── test_student_logout.yaml# 登出接口测试数据
│   ├── test_student_register.yaml # 注册接口测试数据
│   ├── test_student_task.yaml  # 任务中心测试数据
│   ├── test_subject_list.yaml  # 学科列表测试数据
│   ├── test_paper_pageList.yaml# 试卷分页测试数据
│   ├── test_paper_select.yaml  # 试卷查询测试数据
│   ├── test_paper_submit.yaml  # 试卷提交测试数据
│   └── test_answer_read.yaml   # 答卷查询测试数据
├── tests/                      # 测试用例目录
│   ├── test_index.py          # 首页接口测试
│   ├── test_student_login.py   # 登录接口测试
│   ├── test_student_logout.py  # 登出接口测试
│   ├── test_student_register.py # 注册接口测试
│   ├── test_student_task.py    # 任务中心测试
│   ├── test_subject_list.py    # 学科列表测试
│   ├── test_paper_pageList.py  # 试卷分页测试
│   ├── test_paper_select.py    # 试卷查询测试
│   ├── test_paper_submit.py    # 试卷提交测试
│   └── test_answer_read.py     # 答卷查询测试
├── utils/                      # 工具类目录
│   ├── assert_log_util.py     # 断言日志工具
│   ├── request_util.py        # 请求工具类
│   └── yaml_util.py           # YAML读取工具
├── reports_html/              # Allure报告目录
└── README.md                 # 项目说明文档

## 🚀 快速开始

### 环境要求

- Python 3.8+
- JDK (用于Allure报告)
- MySQL 5.7+
- 学之思考试系统后端服务

### 安装依赖

```bash
pip install pytest requests allure-pytest PyYAML
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest tests/test_student_login.py

# 生成Allure报告
pytest --alluredir=./reports_html
allure serve reports_html
```

## 📚 学生端接口文档

### 基础信息

- **Base URL**: `http://localhost:8000`
- **认证方式**: Session + Cookie

### 接口列表

| 编号 | 接口名称 | 请求方法 | 接口地址 |
|------|----------|----------|----------|
| 1 | 登录 | POST | /api/user/login |
| 2 | 注册 | POST | /api/student/user/register |
| 3 | 登出 | POST | /api/user/logout |
| 4 | 首页 | POST | /api/student/dashboard/index |
| 5 | 任务中心 | POST | /api/student/dashboard/task |
| 6 | 学科列表 | POST | /api/student/education/subject/list |
| 7 | 试卷分页 | POST | /api/student/exam/paper/pageList |
| 8 | 试卷查询 | GET | /api/student/exam/paper/select/{id} |
| 9 | 试卷提交 | POST | /api/student/exampaper/answer/answerSubmit |
| 10 | 答卷查询 | GET | /api/student/exampaper/answer/read/{id} |

### 1. 登录接口

**接口地址**: `/api/user/login`

**请求参数**:
```json
{
    "userName": "student",
    "password": "123456",
    "remember": false
}
```

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": {
        "userName": "student",
        "imagePath": ""
    }
}
```

### 2. 注册接口

**接口地址**: `/api/student/user/register`

**请求参数**:
```json
{
    "userName": "student5",
    "password": "123456",
    "userLevel": 1
}
```

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": null
}
```

### 3. 登出接口

**接口地址**: `/api/user/logout`

**请求参数**: 无

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": null
}
```

### 4. 首页接口

**接口地址**: `/api/student/dashboard/index`

**请求参数**: 无

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": {
        "fixedPaper": [
            {
                "id": 2399,
                "name": "test33333",
                "limitStartTime": null,
                "limitEndTime": null
            }
        ],
        "timeLimitPaper": []
    }
}
```

### 5. 任务中心

**接口地址**: `/api/student/dashboard/task`

**请求参数**: 无

**响应示例**:
```json
[
    {
        "id": 14,
        "title": "2021-04-25作业",
        "paperItems": [
            {
                "examPaperId": 181,
                "examPaperName": "第一次出卷",
                "examPaperAnswerId": 579,
                "status": 2
            }
        ]
    }
]
```

### 6. 学科列表

**接口地址**: `/api/student/education/subject/list`

**请求参数**: 无

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": [
        {
            "id": "18",
            "name": "英语"
        }
    ]
}
```

### 7. 试卷分页

**接口地址**: `/api/student/exam/paper/pageList`

**请求参数**:
```json
{
    "paperType": 1,
    "subjectId": 158,
    "pageIndex": 1,
    "pageSize": 10
}
```

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": {
        "total": 1,
        "list": [
            {
                "id": 2520,
                "name": "生理卫生",
                "questionCount": 1,
                "score": 20,
                "createTime": "2021-05-31 13:34:49",
                "createUser": 2,
                "subjectId": 158,
                "subjectName": "英语",
                "paperType": 1,
                "frameTextContentId": 9016
            }
        ]
    }
}
```

### 8. 试卷查询

**接口地址**: `/api/student/exam/paper/select/{id}`

**请求参数**: 无

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": {
        "id": 14,
        "level": 1,
        "subjectId": 1,
        "paperType": 1,
        "name": "测试一",
        "suggestTime": 22,
        "limitDateTime": null,
        "titleItems": [
            {
                "name": "一、选择题",
                "questionItems": [
                    {
                        "id": 14,
                        "questionType": 5,
                        "subjectId": 1,
                        "title": "默写咏鹅",
                        "items": [],
                        "analyze": "咏鹅可以带拼音",
                        "correctArray": null,
                        "correct": "鹅鹅鹅，曲项向天歌。白毛浮绿水，红掌拨清波。",
                        "score": "10",
                        "difficult": 3,
                        "itemOrder": 1
                    }
                ]
            }
        ],
        "score": "10"
    }
}
```

### 9. 试卷提交

**接口地址**: `/api/student/exampaper/answer/answerSubmit`

**请求参数**:
```json
{
    "questionId": null,
    "doTime": 14,
    "answerItems": [
        {
            "questionId": 4,
            "content": null,
            "contentArray": ["测试", "1"],
            "completed": true,
            "itemOrder": 1
        }
    ],
    "id": 4
}
```

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": "2"
}
```

### 10. 答卷查询

**接口地址**: `/api/student/exampaper/answer/read/{id}`

**请求参数**: 无

**响应示例**:
```json
{
    "code": 1,
    "message": "成功",
    "response": {
        "paper": {
            "id": 14,
            "level": 1,
            "subjectId": 1,
            "paperType": 4,
            "name": "限时考试二",
            "suggestTime": 20,
            "limitDateTime": [
                "2021-06-22 00:00:00",
                "2021-08-06 00:00:00"
            ]
        }
    }
}
```

## 💾 数据库设计

### 主要数据表

| 表名 | 说明 |
|------|------|
| t_user | 用户表 |
| t_subject | 学科表 |
| t_exam_paper | 试卷表 |
| t_exam_paper_answer | 试卷答案表 |
| t_question | 题目表 |
| t_task_exam | 任务表 |
| t_message | 消息表 |
| t_user_token | 用户Token表 |

### 试卷类型说明

| 类型值 | 说明 |
|--------|------|
| 1 | 固定试卷 |
| 4 | 时段试卷 |
| 6 | 任务试卷 |

### 题目类型说明

| 类型值 | 说明 |
|--------|------|
| 1 | 单选题 |
| 2 | 多选题 |
| 3 | 判断题 |
| 4 | 填空题 |
| 5 | 简答题 |

## 📝 测试用例示例

### YAML测试数据格式

```yaml
- feature: 用户模块
  story: 登录接口
  title: 成功登录
  request:
    method: POST
    url: http://localhost:8000/api/user/login
    headers:
      Content-Type: application/json
    json:
      userName: "student"
      password: "123456"
      remember: false
  validate:
    code: 1
    message: 成功
```

### Python测试用例格式

```python
import pytest
import allure
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml

@allure.epic("学生考试系统")
class TestStudentLogin:

    @pytest.mark.parametrize("caseinfo", read_yaml("./data/test_student_login.yaml"))
    def test_student_login(self, caseinfo):
        allure.dynamic.feature(caseinfo["feature"])
        allure.dynamic.story(caseinfo["story"])
        allure.dynamic.title(caseinfo["title"])

        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        headers = caseinfo["request"].get("headers", {})
        data = caseinfo["request"].get("json", {})

        res = RequestUtil.send_all_request(
            method=method,
            url=url,
            headers=headers,
            json=data
        )
        result = res.json()

        validate = caseinfo.get("validate", {})
        if validate:
            if "code" in validate:
                assert result["code"] == validate["code"]
            if "message" in validate:
                assert result["message"] == validate["message"]
```

## 🔧 常见问题

### Q1: 测试运行失败怎么办？

1. 检查后端服务是否启动：`http://localhost:8000`
2. 检查数据库连接是否正常
3. 查看详细日志输出
4. 确认测试数据是否正确

### Q2: 如何添加新的测试用例？

1. 在 `data/` 目录创建或编辑YAML文件
2. 按照现有格式添加测试数据
3. 在 `tests/` 目录创建或编辑Python测试文件
4. 运行 `pytest` 执行测试

### Q3: 如何生成测试报告？

```bash
# 生成报告
pytest --alluredir=./reports_html

# 查看报告
allure serve reports_html
```

## 📄 许可证

本项目基于 MIT 许可证开源。

## 🙏 致谢

- [学之思开源考试系统](https://gitee.com/mindskip/xzs)
- [pytest](https://docs.pytest.org/)
- [Allure](https://docs.qameta.io/allure/)
