import datetime

import vk_api
import random
#from vk_api.longpoll import VkLongPoll, VkEventType

f = open('input.txt', 'r')

login = f.readline()
password = f.readline()

vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()
#longpoll = VkLongPoll(vk_session)


def isPerfect(name=str):
    return (False, True)[name.__contains__('МИРЭА')]


def messages_send(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +214783648)})


#print(vk.group.search(q='МИРЭА', count=10, offset=3))

messages_send(vk_session, 'user_id', 'id411198297', 'lol')

'''
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user:
                if response == "удачу":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'благословение удачи', 'random_id': 0})

            elif event.from_chat and not event.from_me:
                if response == "тест":
                    messages_send(vk_session, 'chat_id', event.chat_id, message='фываыф')'''