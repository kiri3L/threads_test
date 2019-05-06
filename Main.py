import config
import pprint
import random
# import threading
import time
import requests
import re

# main_list = []
# tr = []


# def f(index: int) -> None:
#     print(main_list[index])
#     for j in range(len(main_list[index])):
#         main_list[index][j] += 10
#    # print(main_list[index])
#     return None
#
#
# for i in range(5):
#     main_list.append([i, i * 2, i * 3])
#     tr.append(Thread(target=f, args=[i], name='thread' + str(i)))
#     tr[i].start()
#
# print(main_list)

# def count(i: int):
#     for j in range(i, i + 5, 1):
#         print(j)
#         time.sleep(1)

# t1 = threading.Timer(0.0, count, args=[0])
# t2 = threading.Timer(5.0, count, args=[5])
# t3 = threading.Timer(10.0, count, args=[10])
# t4 = threading.Timer(15.0, count, args=[15])
# t5 = threading.Timer(20.0, count, args=[20])
# t6 = threading.Timer(25.0, count, args=[25])
# t7 = threading.Timer(30.0, count, args=[30])
# t8 = threading.Timer(35.0, count, args=[35])
# t9 = threading.Timer(40.0, count, args=[40])
# t10 = threading.Timer(45.0, count, args=[45])
# t11 = threading.Timer(50.0, count, args=[50])
# t12 = threading.Timer(55.0, count, args=[55])
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()
# t11.start()
# t12.start()
#
# def s():
#     for i in range(0, 60, 2):
#         print(i)
#         time.sleep(2)
#
#
# def s2():
#     for i in range(1, 60, 2):
#         print(i)
#         time.sleep(2)
#
#
# t1 = threading.Timer(0, s)
# t2 = threading.Timer(1, s2)
# t1.start()
# t2.start()

# 'https://api.vk.com/method/users.get?'
# 'https://api.vk.com/method/execute?'
# token_group = 'c77108dcb98bfcba34d6e1677a95f543b0f6f3de916b192392edaffda02653d57b28e464a0474a0b6f4b3'
# token = 'f11a124f2cb5599ba8b938393b643f3075501e645928f9a316ce4c8da8d080cb3acc7591f7de61bc49395'
# v = '5.95'
#
# r = requests.get('https://api.vk.com/method/friends.get?', params={
#                                                                    'access_token': token,
#                                                                    'v': v})
#
# print(r.json())
#
# users = set(r.json()['response']['items'])
# new_users = set()
#
# for i in users:
#     r = requests.get('https://api.vk.com/method/friends.get?', params={ 'user_id': i,
#                                                                         'access_token': token,
#                                                                         'v': v})
#
#     new_users.union(r.json()['response']['items'])
#     time.sleep(0.26)
#
# users.union(new_users)
#
# new_new_users = set()
#
# for i in new_users:
#     r = requests.get('https://api.vk.com/method/friends.get?', params={'user_id': i,
#                                                                        'access_token': token,
#                                                                        'v': v})
#
#     new_new_users.union(r.json()['response']['items'])
#     time.sleep(0.26)
#
# users.union(new_new_users)
#
#
#
# print(len(users))
#
# ss = []
#
# lusers = list(users)
#
# for i in range(len(lusers)):
#     if((i % 1000) == 0):
#         ss.append('"')
#     if(((i % 1000) == 999 ) | (i == len(lusers) - 1)):
#         ss[-1] += str(lusers[i]) + '"'
#     else:
#         ss[-1] += str(lusers[i]) + ','
#
# print(len(ss))
#
# code = """"""
#
# for i in range(min(len(ss),25)):
#     code += ' var a' + str(i) + ' = API.users.get({"user_ids": ' + ss[i] + ', "fields": "online,last_seen"});'
#     code += ' var b = [ a'
#
#
# code = """ var a = API.users.get({"user_ids": """ + s + """ "fields": "online,last_seen"});
#             return [ a@.id, a@.online, a@.last_seen ]; """
#
# r = requests.get('https://api.vk.com/method/execute?', params={'code': code,
#                                                                'access_token': token_group,
#                                                                'v': v})
# print(r.json())
#
# code = ' var %s = API.users.get({"user_ids": "%s", "fields": "online,last_seen"}); '
# print(code)
# code = code % ('a1', 'k3l')
# print(code)
# code = ' var a =  API.users.get( { "user_ids": "lol.poltora,cookiemonster0,zheem55", "fields": "online,last_seen" } );\n' \
#        ' var b =  API.users.get( { "user_ids": "shuuuurik", "fields": "online,last_seen" } );\n' \
#        ' return  [ [ a@.id, a@.online, a@.last_seen@.time ], [ b@.id, b@.online, b@.last_seen@.time ] ]; ' #,]];'
#
# print(code)
#
# r = requests.get('https://api.vk.com/method/execute?', params={'code': code,
#                                                                'access_token': token_group,
#                                                                'v': v})
# print(r.json())
# print()
#
# m = list(r.json()['response'])
#
# for i in m:
#     print(i)
# code = ' var %s = API.users.get({"user_ids": "%s", "fields": "online,last_seen"});\n'
# code *= 3
# print(code)
# code = code % ( 'a1', 'kirik', 'a2', 'k3l', 'a3', 'lol' )
# print(code)
#
# ret_code = ' return [ $s ];'
# r_code = '[ $s@.id, $s@.online, $s@.last_seen@.time ] '
#
# class A:
#
#     def __init__(self, val: int = 0, inc: int = 1) -> None:
#         self.val = val
#         self.inc = inc
#         print('Я родился ')
#
#     def __delete__(self, instance):
#         print('Я умир', instance)
#
#     def __del__(self):
#         print('я умир')
#
#     def increment(self):
#         self.val += self.inc
#
#
# def f():
#     a = A()
#     b = A(1)
#     c = A(inc=2)
#     d = A(-3, -1)
#     for i in range(10):
#         a.increment()
#         b.increment()
#         c.increment()
#         d.increment()
#         print(a.val, b.val, c.val, d.val)
#
#
# f()
# print('конец программы')

# def f1():
#     print(' f1 пишет привет')
#
#
# def f2():
#     print(' f2 пишет 1, 2, 3')
#
#
# ff = [f1, f2]
#
# for i in ff:
#     i()
#
# print('bI')


# class User:
#
#     def __init__(self, id:int):
#         self.id = id
#         self.online = 0
#         self.session_time = 0
#         self.start_time = int(time.time())
#
#     def get_online_status(self) -> int:
#         return self.online
#
#     def set_new_data(self, online, time):
#         if self.online > online:
#         #    if self.start_time == time:
#         #        self.session_time = int(time.time()) -  !!!!
#             self.session_time = time - self.start_time
#             self.update_database()
#             self.online = 0
#         if self.online < online:
#             self.online = 1
#             self.start_time = time
#
#     def update(self) -> None:
#         print('id = ' + str(self.id),
#               'online = ' + str(self.online),
#               'start_time = ' + str(self.start_time),
#               'session_time = ' + str(self.session_time), sep='\n')
#         print('\n')
#
#     def update_database(self) -> None:
#         print('INSERT')
#         print('id = ' + str(self.id),
#               'start_time = ' + str(self.start_time),
#               'session_time = ' + str(self.session_time), sep='\n')
#         print('\n')
#
#
# def code_creator(ids:list)->str:
#     template = ' var %s = API.users.get({ "user_ids": "%s", "fields": "online,last_seen"});\n'  # вынести в отдельный файл
#     template2 = '[ %s@.id, %s@.online, %s@.last_seen@.time ]'                                   # вынести в отдельный файл
#     r_code = template2
#     r_code = r_code % ('a0', 'a0', 'a0')
#     code = template
#     code = code % ('a0', ids[0])
#     for i in range(len(ids) - 1):
#         code += template
#         code = code % ('a' + str(i+1), ids[i+1])
#         r_code += ', ' + template2
#         r_code = r_code % ('a' + str(i+1), 'a' + str(i+1), 'a' + str(i+1))
#
#     return code + ' return [%s];' % r_code
#
#
# def f(r: list)->list:
#     id = []
#     online = []
#     t = []
#     for i in r:
#         id.extend(i[0])
#         online.extend(i[1])
#         t.extend(i[2])
#     return [id, online, t]
#
#
# def get_vk_response(code:str) -> list:
#     r = requests.get('https://api.vk.com/method/execute?', params={'code': code,
#                                                                    'access_token': token_group,
#                                                                    'v': v})
#     resp = r.json()['response']
#     return f(resp)
#
#
# users = [User(134585618), User(246798438), User(384723145), User(390066347),
#          User(148387956), User(444077788), User(83773338), User(145461362)]
# users_ids = ['134585618,246798438,384723145', '390066347,148387956,444077788', '83773338,145461362']
#
# code = code_creator(users_ids)
# print(code)
#
#
# while True:
#     a = get_vk_response(code)
#     for i in range(len(users)):
#         users[i].set_new_data(a[1][i], a[2][i])
#     for u in users:
#          u.update()
#     time.sleep(10)

def req(fr:set)->set:
    fff = set()
    for f in fr:
        r = requests.get('https://api.vk.com/method/friends.get', params={'access_token': config.token,
                                                                          'user_id': f,
                                                                          'v': config.version_api})
        r = r.json()
        if 'response' in r:
            fff = fff.union(r['response']['items'])

    return fff


def get_data()->list:
    t = time.time()
    friends = set()
    friends.add(134585618)
    friends = friends.union(req(friends))
    print(len(friends), '\n', friends)
    print(time.time() - t)
    friends = friends.union(req(friends))
    print(len(friends), '\n', friends)
    print(time.time() - t)
   # friends = friends.union(req(friends))
   # print(len(friends), '\n', friends)
   # print(time.time() - t)
    return list(friends)


# my_file = open('users.txt','w')
# print(get_data(), file=my_file)
# my_file.close()

my_file = open('users.txt', 'r')
#print(my_file.readline())
l = my_file.read()
users = re.findall('\d+', l)
# print(ls)
# print(type(ls))
my_file.close()

# users = get_data()


def get_new_users():
    global users
    t = random.randint(0, 3)
    l = []
    if get_new_users.count > 0:
        for i in range(get_new_users.count, get_new_users.count + t):
            l.append(users[i])
    get_new_users.count += t
    return l


def delete_users(m):
    if m < 2:
        return []
    global users
    t = random.randint(0, 50)
    if t % 2 == 0:
        return users[random.randint(0, m)]
    return []


get_new_users.count = -4


users_ids = []
users_ids_in_string = []
raund = 0


class User:
    def __init__(self, id: str):
        self.id = id
        self.online = 0
        self.last_seen = 0
        self.session_time = 0

    def update(self, id, online, last_seen):
        if self.id != id:
            print(' FATAL ERROR ')
            exit(-1)
        if self.online > online:
            pass
        elif self.online < online:
            self.online = 1
            self.last_seen = last_seen

    def get_id(self):
        return self.id


class Pool:

    def __init__(self):
        self.size = 0
        self.users_str = ''
        self.users = []

    def is_full(self) -> bool:
        if self.size < config.MAX_USERS_IN_EXECUTE:
            return False
        return True

    def free_spase(self):
        return config.MAX_USERS_IN_EXECUTE - self.size

    def add(self, ids:list):
        if self.free_spase() >= len(ids):
            users.extend(ids)
            if self.size != 0:
                self.users_str += ',' + ','.join(ids)
            else:
                self.users_str += ','.join(ids)
            self.size += len(ids)
            print(self.users_str)

    def remove(self, id):
        if self.users_str.find(id) != '':
            self.users.remove(id)
            self.users_str = ','.join(self.users)
            print(self.users_str)


while True:
    raund += 1
    u = get_new_users()
    if len(u) > 0:
        if len(users_ids) == 0:
            users_ids.append([])
            users_ids_in_string.append('')
        ptr = 0
        for i in range(len(users_ids)):
            a = config.MAX_USERS_IN_EXECUTE - len(users_ids)
            b = len(u) - ptr
            for j in range(min(a, b)):
                users_ids[i].append(u[j])
                users_ids_in_string[i] += u[j]
                if ptr < len(u) - 1:
                    users_ids_in_string[i] += ','
                ptr += 1
            if ptr == len(u):
                break
        while ptr < len(u):
            users_ids.append([])
            a = config.MAX_USERS_IN_EXECUTE
            b = len(u) - ptr
            for j in range(min(a, b)):
                users_ids[-1].append(u[j])
                users_ids_in_string[-1] += u[j]
                if ptr < len(u) - 1:
                    users_ids_in_string[-1] += ','
                ptr += 1

    if len(users_ids) == 0:
        print('empty')
    else:
        print('raund = ', raund)
        print('u size = ', len(u))
        print('count of lists =', len(users_ids))
        for i in range(len(users_ids)):
            print('\t', i)
            print(users_ids_in_string[i])
        print()

    u = delete_users(get_new_users.count)
    if len(u) != 0:
        for i in range(len(users_ids)):
            if u[0] in users_ids:
                print(users_ids_in_string[i])
                print('u[0] = ', u[0])
                users_ids[i].remove(u[0])
                users_ids_in_string[i].replace(u[0], '')
                users_ids_in_string[i].replace(',,', ',')

    # print(len(users_ids_in_string))
    # for s in users_ids_in_string:
    #     print('\t', s)
    time.sleep(3)









