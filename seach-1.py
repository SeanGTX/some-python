import vk_api.tools
import sqlite3
import os
from tqdm import tqdm
import sys
import time
import urllib.request

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

conn = sqlite3.connect("PublicDB.sqlite3")
cursor = conn.cursor()

sqlite3_create = "CREATE TABLE " + VkPublicName + " (id integer primary key autoincrement not null ,name text not null, surname text not null, VKlink text not null)"

try:
    cursor.execute(sqlite3_create)
except sqlite3.OperationalError:
    pass


def recordExists(VKLink=str()):
    global VkPublicName
    VKLink = "'https://vk.com/" + VKLink + "'"
    SQLite_request = "SELECT * FROM " + VkPublicName + " WHERE VKLink=" + VKLink
    records = cursor.execute(SQLite_request)
    recordsValues = records.fetchall()
    if len(recordsValues) >= 1:
        return True
    else:
        return False


year = 0


def fitGirl(Girl=dict):
    global year
    if 'bdate' in Girl:
        if len(Girl['bdate'].split('.')[-1]) == 4:
            year = int(Girl['bdate'].split('.')[-1])
        else:
            year = 2001
    return ('deactivated' not in Girl) and (Girl['is_closed'] != True) and (
            Girl['sex'] == 1) and (year >= 2000) and (
                   (('relation' in Girl) and (Girl['relation'] in [0, 6, 1])) or ('relation' not in Girl)) and (
                   (('city' in Girl) and (Girl['city']['id'] == 23)) or ('city' not in Girl))


def downloadPhoto(url, name):
    img = urllib.request.urlopen(url).read()
    f = open("img/" + name + ".jpg", 'tw', encoding='utf-8')
    f.close()
    out = open("img/" + name + ".jpg", "wb")
    out.write(img)
    out.close()


init = tqdm(range(VkPublicMembers_Thousands), ncols=100, desc='Создание списка ползователей ' + VkPublicName)

x = 0
for i in init:
    VkPublic += VkPublic_temp['items']
    VkPublic_temp = vk.groups.getMembers(group_id=VkPublicName, count=1000, offset=(x + 1) * 1000)
    x += 1
init.close()

print('Готово!')

time.sleep(1)

init = tqdm(range(len(VkPublic)), ncols=100, desc='Поиск подходящих пользователей ' + VkPublicName)

for i in init:
    girl = \
        vk.users.get(user_id=VkPublic[i], fields=['sex', 'bdate', 'screen_name', 'city', 'relation', 'photo_400_orig'])[
            0]
    if fitGirl(girl) and not recordExists(girl['screen_name']):
        print(girl['screen_name'])
        downloadPhoto(girl['photo_400_orig'], girl['screen_name'])
        cursor.execute(
            "INSERT INTO " + VkPublicName + " (name, surname, VKlink) VALUES ('" + girl['first_name'] + "','" +
            girl['last_name'] + "', 'https://vk.com/" + girl['screen_name'] + "')")
        conn.commit()
