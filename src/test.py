'''
Author: wz-fu
Date: 2023-03-27 16:00:00
LastEditors: wz-fu
LastEditTime: 2023-03-27 16:17:35
Description: 临时测试py文件
email:wz-fu@qq.com
QQ:1498598369
'''
import requests
import sys
import time
import json


def test():
    key = sys.argv[1]
    content = str(time.time())
    # get方式
    requests.get(
        f'http://www.pushplus.plus/send?token={key}&content={content}')
    time.sleep(2)
    # post方式
    data = {"token": key, "title": "post", "content": content}
    body = json.dumps(data).encode(encoding='utf-8')
    header = {'Content-Type': 'application/json'}
    requests.post('http://www.pushplus.plus/send', data=body, headers=header)


if __name__ == '__main__':
    test()

