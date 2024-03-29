# -*- coding: gbk -*-

import allure
import pytest
from util.request_com import RequestsCom
from util.yaml_com import *
from util.json_com import *

rootpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml_data = read_yaml(rootpath + '\\case_yaml\\System\\login.yaml')
request_data = datasort(yaml_data)


@allure.story('登录接口')
@pytest.mark.parametrize('data', request_data.get('/auth/oauth/token'))
def test_login(data):
    rsp, exp_rsp = RequestsCom().send_request(data)
    rsp = rsp.json()
    assert all([find(key, rsp) == find(key, exp_rsp) for key in exp_rsp.keys()])


@allure.story('工作台查询接口')
@pytest.mark.usefixtures('addtoken')
@pytest.mark.parametrize('data, role', addrole(request_data.get('/workflow/workflow/page_tasks'), 'AE'))
def test_workflow(data, role):
    rsp, exp_rsp = RequestsCom().send_request(data)
    rsp = rsp.json()
    assert all([find(key, rsp) == find(key, exp_rsp) for key in exp_rsp.keys()])


if __name__ == '__main__':
    pytest.main(['-sv'])
