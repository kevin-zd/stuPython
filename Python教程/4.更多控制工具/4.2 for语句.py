"""
    @project: stuPython
    @Author：Murk
    @file： 4.2 for语句.py
    @date：2024/2/21 16:13
    @Desc: 
"""
words = ['cat', 'windows', 'defenestrate']
for w in words:
    print(w, len(w))

print(' ---------- Strategy:  Iterate over a copy -----------')

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

print(' ---------- Strategy:  Create a new collection -----------')
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)