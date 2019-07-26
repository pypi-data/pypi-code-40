from collections.abc import Iterable
from typing import Tuple, Union, Dict

import requests


class Robot:

    def __init__(self, url: Union[str, Tuple[str, ...]]):
        self.url: Tuple[str, ...] = tuple(list(url, )) if isinstance(url, str) else url

    def _send(self, data: Dict) -> None:
        if isinstance(self.url, str):
            raise TypeError(f'data {data} must be iterable and not str')
        if not isinstance(self.url, Iterable):
            raise TypeError(f'data {data} must be iterable and not str')
        for url in self.url:
            requests.post(url, json=data)

    def send_text(self, text: str) -> None:
        data = {"msgtype": "text",
                "text": {
                    "content": f"{text}"
                }
                }
        self._send(data)

    def send_markdown(self, title: str, text: str) -> None:
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"{title}",
                "text": f"{text}"
            }
        }
        self._send(data)


class LogRot(Robot):

    def info(self, text: str) -> None:
        self.send_text(text)

    def error(self, text: str) -> None:
        self.send_text(text)


if __name__ == '__main__':
    from gitignore import ROBOT_TIMOR

    Robot(ROBOT_TIMOR).send_markdown('客户留言', '# 我是客户')
