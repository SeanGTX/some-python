import vk_api.tools
import datetime
import os.path

vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()
vk = vk_session.get_api()

VkPublicName = str(input('Ссылка на паблик: '))
VkPublic = ''

try:
    VkPublic = vk.groups.getMembers(group_id=VkPublicName, count=1000)
except vk_api.exceptions.ApiError:
    print('Паблик не найден')
    exit(0)

VkPublicMembers = VkPublic['count']
VkPublicMembers_drop = VkPublic['count'] - VkPublicMembers * 1000

file = ''
file_read = 0  # 0 - запись с нуля, 1 - дозапись


def FindAndPrintWrite():
    global VkPublic
    global VkPublicMembers
    global file_read
    global file
    count = 1
    year = 0
    for x in range(1, (VkPublicMembers // 1000) + 2):
        print('новая тысча')
        for i in range(len(VkPublic['items'])):
            girl = \
                vk.users.get(user_id=VkPublic['items'][i], fields=['sex', 'bdate', 'screen_name', 'city', 'relation'])[
                    0]
            if 'bdate' in girl:
                if len(girl['bdate'].split('.')[-1]) == 4:
                    year = int(girl['bdate'].split('.')[-1])
                else:
                    year = 2001
            if ('deactivated' not in girl) and (girl['is_closed'] != True) and (
                    girl['sex'] == 1) and (year >= 2000) and (
                    (('relation' in girl) and (girl['relation'] in [0, 6, 1])) or ('relation' not in girl)):
                if (('city' in girl) and (girl['city']['id'] == 23)) or ('city' not in girl):
                    inf = str(count) + ' - ' + girl['first_name'] + ' ' + girl['last_name'] + ' https://vk.com/' + girl[
                        'screen_name']
                    # file_read = open(VkPublicName + '.txt', 'r')
                    # if inf not in file_read:
                    file.write(inf + '\n')
                    print(inf)
                    count += 1
                    #  file_read.close()
                    '''else:
                        print('Уже есть в файле: ' + girl['first_name'] + ' ' + girl['last_name'] + ' https://vk.com/' +
                              girl[
                                  'screen_name'])'''

        if VkPublicMembers - x * 1000 >= 1000:
            VkPublic = vk.groups.getMembers(group_id=VkPublicName, count=1000, offset=1000)
            print('смена тысчи')
        elif VkPublicMembers - x * 1000 > 0:
            VkPublic = vk.groups.getMembers(group_id=VkPublicName, count=1000, offset=VkPublicMembers_drop)
            print('остаток')


if not os.path.exists(VkPublicName + '.txt'):
    file = open(VkPublicName + '.txt', 'w', encoding='utf-8')
    today = datetime.datetime.today()
    file.write('Паблик: ' + 'https://vk.com/' + VkPublicName + ' - ' + today.strftime("%d.%m.%Y %H:%M:%S") + '\n')
    print('Поиск...')
    FindAndPrintWrite()
else:
    file = open(VkPublicName + '.txt', '')
    FindAndPrintWrite()
