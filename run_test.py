import os
from time import time

import pytest

if __name__ == '__main__':
    pytest.main([])

    os.system("allure generate ./reports -o ./reports_html --clean")
    # os.system("allure open ./reports_html")