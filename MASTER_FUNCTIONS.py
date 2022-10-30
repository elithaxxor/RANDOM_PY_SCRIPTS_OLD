def min_pattern(self):
    time_pattern = re.compile(r"[:\d:]")
    time_list = time_pattern.findall(str(now))
    min_str = ''
    min_list = time_list[11:13]
    min_list = min_list[0:2]
    min_str = min_str.join(min_list[0:2])
    return min_str


def hour_pattern(self):
    hour_pattern = re.compile(r"[:\d:]")
    time_hour_list = hour_pattern.findall(str(now))
    print(time_hour_list)
    hour_str = ''
    hour_list = time_hour_list[8:11]
    hour_list = hour_list[0:2]
    print(hour_list)
    print(), print('X' * 25)
    hour_str = hour_str.join(hour_list[0:2])
    return hour_str


