import vk_api.tools
import sqlite3
import os
from tqdm import tqdm
import sys
import time

vk_session = vk_api.VkApi('', '')
vk_session.auth()
vk = vk_session.get_api()

VkPublicName = str(input('Ссылка на паблик: '))
VkPublic_temp = []
VkPublic = []

try:
    VkPublic_temp = vk.groups.getMembers(group_id=VkPublicName, count=1000)
except vk_api.exceptions.ApiError:
    print('Паблик не найден')
    exit(0)

VkPublicMembers = VkPublic_temp['count']
VkPublicMembers_Thousands = VkPublicMembers // 1000 + 1

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
