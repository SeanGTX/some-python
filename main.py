import vk_api.tools

vk_session = vk_api.VkApi('', '')
vk_session.auth()
vk = vk_session.get_api()

pva = vk.groups.getMembers(group_id='empire_pva', filter='friends')

sex = ''

for i in range(len(pva['items'])):
    guys_sex = vk.users.get(user_id = pva['items'][i], fields='sex')[0]['sex']
    if guys_sex == 0:
        sex = 'не указано'
    elif guys_sex == 1:
        sex = 'Девушка'
    elif guys_sex == 2:
        sex = 'Парень'
    if 'deactivated' not in vk.users.get(user_id = pva['items'][i])[0]:
        guys_screen_name = vk.users.get(user_id = pva['items'][i], fields='screen_name')[0]['screen_name']
        guys_name = vk.users.get(user_id = pva['items'][i])[0]['first_name']
        guys_lastName = vk.users.get(user_id = pva['items'][i])[0]['last_name']
        print(i,'- ',end='')
        print(guys_name, guys_lastName, sex, guys_screen_name)
    else:
        guys_name = vk.users.get(user_id=pva['items'][i])[0]['first_name']
        guys_lastName = vk.users.get(user_id=pva['items'][i])[0]['last_name']
        print(i, '- ', end='')
        print(guys_name, guys_lastName, sex, 'Заблокирован')

#print('deactivated' not in vk.users.get(user_id = pva['items'][9])[0])
