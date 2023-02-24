import os
import math
import random
import requests

from datetime import date, datetime
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate

today = datetime.now()

# 微信公众测试号 ID 和 SECRET
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

# 可把 os.environ 结果替换成字符串在本地调试
user_ids = os.environ["USER_ID"].split(',')
template_id = os.environ["TEMPLATE_ID"]

# 字体随机颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)

for i in range(len(user_ids)):
    data = {
        "message": {"value": "删除 DevOps 计划", "color": get_random_color()},
    }
    res = wm.send_template(user_ids[i], template_id, data)
    print(res)
