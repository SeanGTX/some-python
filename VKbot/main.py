import vk_api.tools

vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()
vk = vk_session.get_api()

pva = vk.groups.getMembers(group_id='empire_pva')

sex = ''

for i in range(len(pva['items'])):
    people = vk.users.get(user_id=pva['items'][i], fields=['sex', 'bdate', 'screen_name', 'city', 'relation'])[0]
    if 'deactivated' not in people:
        print(people)

#print('deactivated' not in vk.users.get(user_id = pva['items'][9])[0])

print(vk.users.get(user_ids='litaokda',  fields='country'))
