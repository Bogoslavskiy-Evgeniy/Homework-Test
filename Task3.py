def chanel_max_volume():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    chanel = max(stats, key = stats.get)
    return chanel
