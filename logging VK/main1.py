import vk_api
import sys

username = 'логин'

password = 'пороль'
#https://oauth.vk.com/blank.html#access_token=3f28ac46673546ab6889357e40888ebe94f9ad6a512aa6019427153b759d557ac8c03d8bf21f2f42a0a99&expires_in=86400&user_id=411198297
if __name__ == '__main__':

    vk_session = vk_api.VkApi(username, password)
    vk_session.auth()

    vk = vk_session.get_api()

    print(vk_session.token['access_token'])
    print(vk_session.token['user_id'])

