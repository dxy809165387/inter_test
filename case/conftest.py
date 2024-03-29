# -*- coding: gbk -*-
import os

import pytest

from util.request_com import RequestsCom
from util.yaml_com import *


rootpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope='module', autouse=True)
def gettoken():
    datas = read_yaml(rootpath + '\\case_yaml\\logininfo.yaml')
    for data in datas:
        datatype = data["type"]
        del data["type"]
        rsp = RequestsCom().send_request(data)[0]
        datadump = {datatype: 'Bearer '+rsp.json()["content"]["access_token"]}
        write_yaml(rootpath + '\\case_yaml\\cach.yaml', datadump)
    yield
    clean_yaml(rootpath + '\\case_yaml\\cach.yaml')


@pytest.fixture()
def addtoken(data, role):
    token = read_yaml(rootpath + '\\case_yaml\\cach.yaml')
    data["headers"]["authorization"] = token[role]
