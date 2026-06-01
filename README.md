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
- 🏷️ 标记管理：支持冒烟、普通、异常场景等测试标记

## 🛠️ 技术栈

| 技术 | 说明 | 版本 |
|------|------|------|
| Python | 编程语言 | 3.8+ |
| pytest | 测试框架 | 9.0+ |
| requests | HTTP客户端 | - |
| allure-pytest | Allure报告插件 | - |
| PyYAML | YAML解析 | - |

## 📁 项目结构

```
student_test/
├── .idea/                      # IDE配置文件
├── config/                     # 配置文件目录
│   └── log_config.py          # 日志配置
├── data/                       # 测试数据目录（YAML文件）
│   ├── test_answer_read.yaml      # 答卷查询测试数据
│   ├── test_index.yaml            # 首页接口测试数据
│   ├── test_paper_pageList.yaml   # 试卷分页测试数据
│   ├── test_paper_select.yaml     # 试卷查询测试数据
│   ├── test_paper_submit.yaml     # 试卷提交测试数据
│   ├── test_student_login.yaml    # 登录接口测试数据
│   ├── test_student_logout.yaml   # 登出接口测试数据
│   ├── test_student_register.yaml # 注册接口测试数据
│   ├── test_student_task.yaml     # 任务中心测试数据
│   └── test_subject_list.yaml     # 学科列表测试数据
├── logs/                       # 日志输出目录
│   └── student_test.log       # 测试执行日志
├── reports/                    # Allure原始数据目录
├── reports_html/               # Allure HTML报告目录
├── tests/                      # 测试用例目录
│   ├── test_answer_read.py       # 答卷查询测试
│   ├── test_index.py             # 首页接口测试
│   ├── test_paper_pageList.py    # 试卷分页测试
│   ├── test_paper_select.py      # 试卷查询测试
│   ├── test_paper_submit.py      # 试卷提交测试
│   ├── test_student_login.py     # 登录接口测试
│   ├── test_student_logout.py    # 登出接口测试
│   ├── test_student_register.py  # 注册接口测试
│   ├── test_student_task.py      # 任务中心测试
│   └── test_subject_list.py      # 学科列表测试
├── utils/                      # 工具类目录
│   ├── assert_log_util.py     # 断言日志工具
│   ├── request_util.py        # HTTP请求工具类
│   └── yaml_util.py           # YAML文件操作工具
├── conftest.py                 # pytest全局配置（fixture定义）
├── pytest.ini                  # pytest配置文件
├── run_test.py                 # 测试执行入口脚本
└── README.md                   # 项目说明文档
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- JDK 8+ (用于Allure报告生成)
- 学之思考试系统后端服务（默认：http://localhost:8000）

### 安装依赖

```bash
pip install pytest requests allure-pytest PyYAML
```

### 运行测试

```bash
# 方式1：使用pytest直接运行
pytest

# 方式2：运行指定测试文件
pytest tests/test_student_login.py

# 方式3：运行指定标记的测试
pytest -m smoke

# 方式4：使用运行脚本（自动生成Allure报告）
python run_test.py
```

### 查看测试报告

```bash
# 生成并查看Allure报告
allure generate ./reports -o ./reports_html --clean
allure open ./reports_html

# 或使用allure serve直接启动服务
allure serve ./reports
```

### Allure报告展示

<p align="center">
  <img width="80%" alt="Snipaste_2026-06-01_11-07-37" src="https://github.com/user-attachments/assets/8b54cedf-5ddd-4d55-a1ef-fd822ec0d2ed" />
</p>

<p align="center"><em>图1: Allure测试报告示例</em></p>

## 📋 测试标记说明

本项目使用pytest标记对测试用例进行分类：

| 标记 | 说明 | 使用场景 |
|------|------|----------|
| smoke | 冒烟用例 | 核心业务流程验证 |
| normal | 普通用例 | 常规功能验证 |
| exception | 异常场景用例 | 异常流程和边界条件验证 |

### 标记使用示例

```python
import pytest

@pytest.mark.smoke
def test_critical_login():
    """冒烟测试：核心登录功能"""
    pass

@pytest.mark.normal
def test_normal_feature():
    """普通测试：常规功能"""
    pass

@pytest.mark.exception
def test_invalid_input():
    """异常测试：无效输入处理"""
    pass
```

## 🔧 核心组件说明

### 1. 请求工具类（RequestUtil）

位于 `utils/request_util.py`，封装了HTTP请求功能：

- 使用 `requests.Session` 保持会话状态（Cookie自动管理）
- 支持Token自动注入到请求头
- 提供统一的请求发送接口

```python
from utils.request_util import RequestUtil

# 发送请求
res = RequestUtil.send_all_request(
    method="POST",
    url="http://localhost:8000/api/user/login",
    headers={"Content-Type": "application/json"},
    json={"userName": "student", "password": "123456"},
    token="Bearer xxx"  # 可选：自动注入Authorization头
)
```

### 2. YAML数据驱动

位于 `utils/yaml_util.py`，支持YAML文件的读写操作：

```python
from utils.yaml_util import read_yaml

# 读取测试数据
test_data = read_yaml("./data/test_student_login.yaml")
```

### 3. 断言工具（AssertLogUtil）

位于 `utils/assert_log_util.py`，提供带日志记录的断言功能：

```python
from utils.assert_log_util import assert_log

assert_log(
    condition=result["code"] == 1,
    message="返回的code错误",
    context={"实际code": result["code"], "期望code": 1}
)
```

### 4. 日志配置

位于 `config/log_config.py`，配置测试执行日志：

- 日志文件位置：`logs/student_test.log`
- 同时输出到控制台和文件
- 日志格式：`时间 - 名称 - 级别 - 消息`

## 📡 接口文档

### 基础信息

- **Base URL**: `http://localhost:8000`
- **认证方式**: Session + Cookie

### 接口列表

| 编号 | 接口名称 | 请求方法 | 接口地址 | 测试文件 |
|------|----------|----------|----------|----------|
| 1 | 登录 | POST | /api/user/login | test_student_login.py |
| 2 | 注册 | POST | /api/student/user/register | test_student_register.py |
| 3 | 登出 | POST | /api/user/logout | test_student_logout.py |
| 4 | 首页 | POST | /api/student/dashboard/index | test_index.py |
| 5 | 任务中心 | POST | /api/student/dashboard/task | test_student_task.py |
| 6 | 学科列表 | POST | /api/student/education/subject/list | test_subject_list.py |
| 7 | 试卷分页 | POST | /api/student/exam/paper/pageList | test_paper_pageList.py |
| 8 | 试卷查询 | GET | /api/student/exam/paper/select/{id} | test_paper_select.py |
| 9 | 试卷提交 | POST | /api/student/exampaper/answer/answerSubmit | test_paper_submit.py |
| 10 | 答卷查询 | GET | /api/student/exampaper/answer/read/{id} | test_answer_read.py |

### 接口详情

#### 1. 登录接口

**接口地址**: `POST /api/user/login`

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

#### 2. 注册接口

**接口地址**: `POST /api/student/user/register`

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

#### 3. 首页接口

**接口地址**: `POST /api/student/dashboard/index`

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

##  测试用例编写指南

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
import logging
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml
from utils.assert_log_util import assert_log

logger = logging.getLogger("test_student_login")

@pytest.mark.usefixtures("log")
@allure.epic("学生考试系统")
class TestStudentLogin:

    @pytest.mark.parametrize("caseinfo", read_yaml("./data/test_student_login.yaml"))
    def test_student_login(self, caseinfo):
        # 动态设置Allure报告信息
        allure.dynamic.feature(caseinfo["feature"])
        allure.dynamic.story(caseinfo["story"])
        allure.dynamic.title(caseinfo["title"])

        # 发送请求
        res = RequestUtil.send_all_request(
            method=caseinfo["request"]["method"],
            url=caseinfo["request"]["url"],
            headers=caseinfo["request"].get("headers", {}),
            json=caseinfo["request"].get("json", {})
        )
        result = res.json()
        logger.info(f"响应结果: {result}")

        # 断言验证
        validate = caseinfo.get("validate", {})
        if "code" in validate:
            assert_log(
                result["code"] == validate["code"],
                "返回的code错误",
                context={"实际code": result["code"], "期望code": validate["code"]}
            )
```

## 🔧 配置说明

### pytest.ini 配置

```ini
[pytest]
;全局默认参数
addopts = -vs --alluredir=./reports --clean-alluredir
;测试脚本存放目录
testpaths = ./tests
;测试文件命名规则
python_files = test_*.py
;测试类命名规则
python_classes = Test*
;测试函数命名规则
python_functions = test_*
;注册自定义标记
markers =
    smoke: 冒烟用例（核心流程）
    normal: 普通用例
    exception: 异常场景用例
```

## 🐛 常见问题

### Q1: 测试运行失败怎么办？

1. 检查后端服务是否启动：`http://localhost:8000`
2. 检查数据库连接是否正常
3. 查看 `logs/student_test.log` 详细日志
4. 确认测试数据YAML格式是否正确

### Q2: 如何添加新的测试用例？

1. 在 `data/` 目录创建或编辑YAML文件
2. 按照现有格式添加测试数据
3. 在 `tests/` 目录创建或编辑Python测试文件
4. 在 `conftest.py` 添加对应的fixture（可选）
5. 运行 `pytest` 执行测试

### Q3: Allure报告无法生成？

1. 确认已安装JDK 8+
2. 确认已安装Allure命令行工具
3. 检查 `reports` 目录是否有原始数据文件
4. 使用命令 `allure --version` 验证安装

### Q4: 如何修改测试环境地址？

编辑对应YAML文件中的 `url` 字段，或修改测试代码中的Base URL配置。

## 🔄 Jenkins持续集成

本项目支持通过Jenkins实现持续集成。

### 配置步骤

1. **创建Jenkins任务**
   - 新建Pipeline项目
   - 配置源码管理（Git）

2. **配置构建环境**
   - 确保Jenkins服务器已安装Python 3.8+
   - 安装Allure Jenkins插件

3. **配置构建步骤**
   ```bash
   pip install -r requirements.txt
   python run_test.py
   ```

4. **配置Allure报告**
   - 构建后操作：Allure Report
   - 指定报告路径：`reports_html`

### Jenkins构建视图

<p align="center">
  <img width="80%" alt="Snipaste_2026-06-01_11-35-57" src="https://github.com/user-attachments/assets/d15d1548-8bd0-4346-917e-7a7787dc86e1" />
</p>

<p align="center"><em>图2: Jenkins构建视图示例</em></p>

## 📄 许可证

本项目基于 MIT 许可证开源。

## 🙏 致谢

- [学之思开源考试系统](https://gitee.com/mindskip/xzs)
- [pytest](https://docs.pytest.org/)
- [Allure](https://docs.qameta.io/allure/)
