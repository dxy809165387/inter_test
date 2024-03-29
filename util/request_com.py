import requests


class RequestsCom(object):
    def __init__(self):
        self.session = requests.session()
        self.host = 'http://test-oaapi.rsth.plus'

    def send_request(self, data):
        key_value = ['url', 'method']
        if all([True if key in data.keys() else False for key in key_value]):
            data['url'] = self.host + data['url']
            if 'rsp' in data.keys():
                exp_rsp = data.pop('rsp')
            else:
                exp_rsp = None
            rsp = self.session.request(**data)
            return rsp, exp_rsp
        else:
            raise ValueError('传入参数缺失url或method')


if __name__ == '__main__':

    data_dict = {'method': 'POST', 'url': '/auth/oauth/token', 'headers': {'api-version': '1.0', 'path': '/login', 'authorization': 'Basic d2ViLWNsaWVudDpUVFNTT0RtQUJwRVNCTUZSYXpPb0ZwdEhFa2FsV3loVw=='}, 'data': {'username': 'Test_OVH_AE', 'password': 'afdd0b4ad2ec172c586e2150770fbf9e', 'grant_type': 'password', 'remember': True, 'scope': 'all'}, 'rsp': {'user_id': '309'}}

    req_t = RequestsCom()
    rsp_t, exp_rsp_t = req_t.send_request(data_dict)
    print(req_t, exp_rsp_t)


