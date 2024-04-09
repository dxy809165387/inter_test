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

    pass


