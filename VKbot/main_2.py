import vk_api.tools

vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()
vk = vk_session.get_api()

pva = vk.groups.getMembers(group_id='empire_pva')

count = 1
year = 0

# print(vk.users.get(user_ids='id176708780',fields=['has_mobile', 'relation', 'schools']))

for i in range(len(pva['items'])):
    girl = vk.users.get(user_id=pva['items'][i], fields=['sex', 'bdate', 'screen_name', 'city', 'relation'])[0]
    if 'bdate' in girl:
        if len(girl['bdate'].split('.')[-1]) == 4:
            year = int(girl['bdate'].split('.')[-1])
    else:
        year = 2001
    if ('deactivated' not in girl) and ('is_closed' in girl) and (girl['is_closed'] != True) and (girl['sex'] == 1) and (year >= 2000) and (girl['relation'] in [0, 6, 1]):
        if (('city' in girl) and (girl['city']['id'] == 23)) or ('city' not in girl):
            print(count, '-', girl['first_name'], girl['last_name'], 'https://vk.com/' + girl['screen_name'])
            count += 1


vk.messages.send(user_id='iloveowsla', message='Привет!')

'''date = '6.10.1988'

a = []

a = date.split('.')

print(a)'''
