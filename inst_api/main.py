from instabot import Bot
import os
import glob
''''
cookie_del = glob.glob("config/*cookie.json")
try:
    os.remove(cookie_del[0])
except IndexError:
    pass
'''
INST_USERNAME = 'логины'
INST_PASSWORD = 'пароле'

bot = Bot()

bot.login(username=INST_USERNAME,  password=INST_PASSWORD, use_cookie=True)
print('Пащель пащель')

user = input()

user_following = bot.get_user_following(user)


user_info = [bot.get_user_info(x) for x in user_following]

for x in user_info:
    if ('biography' in x) and ('vk.com' in x['biography']):
        print('_________________________________________')
        print(x['username'] + " " + x['biography'])
