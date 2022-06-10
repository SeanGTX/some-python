import vk_api.tools
import sqlite3

vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()
vk = vk_session.get_api()

obj_friends = vk.friends.get(user_id=561278993)

friends_list = obj_friends['items']

# print(vk.friends.search(user_id=412320464, q='Мария'))

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS mariam ( id integer primary key autoincrement, name text not null, surname text not null, link text not null )")

a = []
d = []

for i in range(len(friends_list)):
    obj = vk.users.get(user_ids=friends_list[i])
    print(obj)
    if ('deactivated' not in obj[0]) and (not obj[0]['is_closed']):
        s = vk.friends.search(user_id=friends_list[i], q='Мария', fields=['screen_name'])['items']
        if len(s) > 0:
            for j in range(len(s)):
                if 'deactivated' not in s[j]:
                    link = 'https://vk.com/' + s[j]['screen_name']
                    d.append([s[j]['first_name'], s[j]['last_name'], link])
                    a.append(d)
                    cursor.execute("INSERT INTO mariam (name, surname, link) VALUES('" + s[j]['first_name'] + "', '" + s[j]['last_name'] + "', '" + link + "')")
                    conn.commit()

print(a)
print(len(a))

