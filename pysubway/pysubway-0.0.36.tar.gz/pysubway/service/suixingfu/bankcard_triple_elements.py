from typing import Dict

try:
    from service.suixingfu.base import SuixingfuBase
    from utils import udict
except Exception as e:
    from pysubway.service.suixingfu.base import SuixingfuBase
    from pysubway.utils import udict


class BankcardTripleElements(SuixingfuBase):
    verifyType = '03'

    def generate_biz_data(self, name: str, identNo: str, cardNo: str) -> Dict[str, str]:
        send_data = udict.Dict.filter(locals())
        send_data['verifyType'] = self.verifyType
        return send_data
