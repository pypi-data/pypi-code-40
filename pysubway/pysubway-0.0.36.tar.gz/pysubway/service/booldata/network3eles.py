from typing import Dict, Optional, Tuple, Any

import pandas as pd

try:
    from service.booldata.base import BoolDataBase
    from utils import udict
    from utils.file import File
    from utils.uexcel import Excel
    from errors import RequestFailed
except (ImportError, ModuleNotFoundError) as e:
    from pysubway.service.booldata.base import BoolDataBase
    from pysubway.utils import udict
    from pysubway.utils.uexcel import Excel
    from pysubway.utils.file import File
    from pysubway.errors import RequestFailed


class Network3Eles(BoolDataBase):
    service = 'network_operator_triple_elements'
    mode = 'mode_triple_elements'
    default_part = {
        'name': '',
        'phone': '',
        'idcard': ''
    }
    df_default_header = (
        "name",
        "phone",
        "ident_number",
        "result_code",
        "result_code_desc",
    )

    @classmethod
    def generate_biz_data(cls, name: str, phone: str, ident_number: str) -> Dict[str, Any]:
        biz_data = udict.Dict.filter(locals())
        biz_data.update({
            "service": cls.service,
            "mode": cls.mode
        })
        return biz_data

    def set_biz_data(self, name: str, phone: str, ident_number: str) -> 'Network3Eles':
        self.biz_data = self.generate_biz_data(name, phone, ident_number)
        return self

    def result_as_df_partial(self, append_biz_data: bool = True) -> pd.DataFrame:
        return self.result_as_df(self.response.get('resp_data', {}), self.default_part,
                                 append_biz_data=append_biz_data)


def batch_test(input: str,
               account: Dict[str, str],
               output_file: str,
               names: Optional[Tuple[str, ...]] = ('name', 'idcard', 'phone'),
               columns: Tuple[str, ...] = Network3Eles.df_default_header,
               raise_failed_exception: bool = False,
               error_log: Optional[str] = None,
               ) -> None:
    """
    batch test personal law, read from excel -> request personal law -> save result to excel

    :param input: excel file
    :param account: booldata account
    :param output_file: xlsx file that saving booldata personal law result
    :param names: input excel file header, you can adjust the sequence
    :param columns: output_file columns header
    :return: None
    """
    error_log = error_log or File.join_path(File(input).dirname, '.'.join((File(input).pure_name, 'error_log')))
    excel_ins = Excel(input).read(names=names)
    result_df = pd.DataFrame()
    guard_ins = Network3Eles(account['rsa_prv_key'], account['aes_key'], account['company_uuid'])
    for _, series in excel_ins.dataframe.iterrows():
        name = series['name']
        phone = series['phone']
        idcard = series['idcard']
        guard_result = guard_ins.set_biz_data(name, phone, idcard).request()
        if not guard_ins.is_succeed():
            if raise_failed_exception:
                raise RequestFailed(f'{guard_result}')
            print('error ins_result  ----> ', guard_result)
            with open(error_log, mode='a') as f:
                print(f"param is {series['idcard']} {series['name']} {series['phone']}")
                f.write(f"{series['idcard']},{series['name']},{series['phone']}\n")
        guard_result = guard_ins.result_as_df_partial()
        result_df = result_df.append(guard_result)
        print(f'{name} {phone} {idcard} result_df', result_df)
        # break
    result_df.to_excel(output_file, columns=columns, index=False)


if __name__ == '__main__':
    from gitignore import BOOLDATA_ACCOUNT

    # 姓名电话身份证银行卡
    file = '/Users/yutou/shouxin/sxProject/pysubway/pysubway/gitignore/chebei.xlsx'
    output = '/Users/yutou/shouxin/sxProject/pysubway/pysubway/gitignore/chebei_network3eles_result.xlsx'
    # with idcard
    batch_test(file, BOOLDATA_ACCOUNT, output, names=('name', 'phone', 'idcard', 'bankcard'))
