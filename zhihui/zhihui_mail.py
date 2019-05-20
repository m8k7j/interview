#!/usr/bin/env python
# coding=utf-8


import requests

response = requests.get("https://www.zhihuiya.com/", verify=False)
fp = open('result', 'w')
fp.write(response.content)
fp.close()
