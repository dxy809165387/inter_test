import os
import pytest

if __name__ == '__main__':
    pytest.main(['-sv', 'case', '--alluredir', 'report/xml/', "--clean-alluredir"])
    os.system('allure generate --clean ./report/xml/')
