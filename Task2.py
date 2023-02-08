def unique_id():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    user1_set = set(ids['user1'])
    user2_set = set(ids['user2'])
    user3_set = set(ids['user3'])
    user = user1_set | user2_set | user3_set
    user = list(user)
    return user

