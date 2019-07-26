import hashlib
from collections import OrderedDict
from typing import Dict, Any, Callable, Optional, ClassVar

import requests

try:
    from utils.ustring import to_bytes
    from utils.utime import timestamp
    from utils import udict
except (ImportError, ModuleNotFoundError) as e:
    from pysubway.utils.ustring import to_bytes
    from pysubway.utils.utime import timestamp
    from pysubway.utils import udict


class ShanghaishuheBase:
    url: ClassVar[str] = 'http://auth.shuhe360.cn:8801/auth/auth-core'
    auth_elements: ClassVar[Dict[str, str]] = {
        # 银行卡三要素
        'bankcard_triple_eles': "1101",
        # 银行卡四要素
        'bankcard_four_eles': "1111",
        # 运营商三要素
        'network_triple_eles': "1110",
        # 银行卡三要素详版
        'bankcard_triple_eles_detail': "1101#L",
        # 银行卡四要素详版
        'bankcard_four_eles_detail': "1111#L",
        # 身份二要素认证
        'idcard_two_eles': "1100",
    }
    unsigned_data_order = 'accountName|authElement|bankCardNo|idCardNo|idCardType|phoneNo|expired|cvn2|serialNo|userName|accountPassword'.split(
        '|')

    def __init__(self, account_name: str, account_pwd: str, version: str = '01'):
        self.account_name: str = account_name
        self.account_pwd: str = account_pwd
        self.version: str = version
        self.send_data: Dict = dict()

    @classmethod
    def fmt_func_bak(cls, data: Dict[str, Any]) -> str:
        result: OrderedDict = OrderedDict()
        for i in cls.unsigned_data_order:
            result[i] = str(data[i]) if i in data else ''
        return '|'.join(result.values())

    def generate_sign(self, data: Dict[str, str], fmt_func: Callable = None) -> str:
        """
        签名值为：
        SHA1(accountName|authElement|bankCardNo|idCardNo|idCardType|phoneNo|expired|cvn2|serialNo|userName|accountPassword)组合后的字符串通过SHA1摘要（大写），如无数据则
        采用||中间不留空。
        SHA1的计算小工具可参考：https://1024tools.com/hash
        :param data:
        :param fmt_func:
        :return:
        """
        data['accountPassword'] = self.account_pwd
        fmted = fmt_func(data) if fmt_func else self.fmt_func_bak(data)
        print(fmted)
        return hashlib.sha1(to_bytes(fmted)).hexdigest().upper()

    def request(self, send_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        send_data = send_data or self.send_data
        print('send_data', send_data)
        response = requests.post(self.url, json=send_data)
        if response.ok:
            return response.json()
        raise SystemError(f'response {response.text}')


class BankcardFourEles(ShanghaishuheBase):

    def generate_send_data(self, idCardNo: str = '', userName: str = '', bankCardNo: str = '', phoneNo: str = '',
                           idCardType: str = '01') -> Dict[str, str]:
        biz_data = udict.Dict.filter(locals())
        biz_data.update({
            'authElement': self.auth_elements['bankcard_four_eles'],
            'accountName': self.account_name,
            'serialNo': timestamp(precision='ms'),
            'version': self.version,
        })
        sign = self.generate_sign(biz_data)
        biz_data['sign'] = sign
        return biz_data

    def set_send_data(self, idCardNo: str = '', userName: str = '', bankCardNo: str = '', phoneNo: str = '',
                      idCardType: str = '01') -> 'BankcardFourEles':
        self.send_data = self.generate_send_data(idCardNo=idCardNo, userName=userName, bankCardNo=bankCardNo,
                                                 phoneNo=phoneNo,
                                                 idCardType=idCardType)
        return self


if __name__ == '__main__':
    from service.shanghaishuhe.gitignore import SHANGHAI_SHUHE_ACCOUNT_INFO

    s = BankcardFourEles(SHANGHAI_SHUHE_ACCOUNT_INFO['account_name'], SHANGHAI_SHUHE_ACCOUNT_INFO['account_pwd'],
                         BankcardFourEles.url).set_send_data(idCardNo='**', userName='**',
                                                             bankCardNo='**', phoneNo='**',
                                                             idCardType='**').request()
    print(s)
