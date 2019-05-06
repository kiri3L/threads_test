
token_group = 'c77108dcb98bfcba34d6e1677a95f543b0f6f3de916b192392edaffda02653d57b28e464a0474a0b6f4b3'
token = '871c43f8871c43f8871c43f8e48775650d8871c871c43f8db9e1794b6a645f4b89b124b'
version_api = '5.95'
MAX_USERS_IN_EXECUTE = 5
MAX_USERS_IN_USERS_GET = 1_000
PERIOD_SEC = 20
CODE_TEMPLATE = ' var %s = API.users.get({ "user_ids": "%s", "fields": "online,last_seen"});\n'
RETURN_CODE_TEMPLATE = '[ %s@.id, %s@.online, %s@.last_seen@.time ]'
USER_GET_URL = ''
EXECUTE_URL = ''
FRIENDS_GET_URL = 'https://api.vk.com/method/friends.get'


# 165
# 1167
# 1284