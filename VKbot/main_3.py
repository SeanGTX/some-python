import vk_api.tools
import datetime

vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()
vk = vk_session.get_api()

VkPublicName = str(input('Ссылка на паблик: '))
VkPublic = ''


def FindAndPrintWrite(mode):
    if mode not in ['a', 'b']:
        print('Неизвестный код!')
        exit(0)
    count = 1
    year = 0
    inf = ''

    for i in range(len(VkPublic['items'])):
        girl = vk.users.get(user_id=VkPublic['items'][i], fields=['sex', 'bdate', 'screen_name', 'city', 'relation'])[0]
        if 'bdate' in girl:
            if len(girl['bdate'].split('.')[-1]) == 4:
                year = int(girl['bdate'].split('.')[-1])
            else:
                year = 2001
        if ('deactivated' not in girl) and ('is_closed' in girl) and (girl['is_closed'] != True) and (
                girl['sex'] == 1) and (year >= 2000) and (
                (('relation' in girl) and (girl['relation'] in [0, 6, 1])) or ('relation' not in girl)):
            if (('city' in girl) and (girl['city']['id'] == 23)) or ('city' not in girl):
                inf = str(count) + ' - ' + girl['first_name'] + ' ' + girl['last_name'] + ' https://vk.com/' + girl[
                    'screen_name']
                if mode == 'a' and inf not in file:
                    file.write(inf + '\n')
                elif mode == 'b':
                    file.write(inf + '\n')
                print(inf)
                count += 1


try:
    VkPublic = vk.groups.getMembers(group_id=VkPublicName)
except vk_api.exceptions.ApiError:
    print('Паблик не найден')
    exit(0)

file = ''

try:
    file = open(VkPublicName + '.txt')
except FileNotFoundError:
    file = open(VkPublicName + '.txt', 'r', encoding='utf-8')

if len(file.read()) > 0:
    choose = str(input('В файле уже хранятся данные. Варианты действий: a - дозапись, b - перезапись, e - выход '))
    if choose == 'a':
        file = open(VkPublicName + '.txt', 'a')
        FindAndPrintWrite('a')
    if choose == 'e':
        exit(0)
    if choose == 'b':
        file = open(VkPublicName + '.txt', 'w')
        today = datetime.datetime.today()
        file.write('Паблик: ' + VkPublicName + ' - ' + today.strftime("%d.%m.%Y %H:%M:%S") + '\n')
        FindAndPrintWrite('b')
else:
    print('Поиск...')
    FindAndPrintWrite('b')
