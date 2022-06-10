import vk_api.tools

vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()
vk = vk_session.get_api()

print(vk.messages.send())