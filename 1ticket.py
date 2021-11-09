def get_nearest_lucky_ticket (number:int)->int:
    if re.match('[^0-9]',int):
        raise Exception('error input')
    if len(int) % 2 == 1:
        raise Exception('error input')
    else:
        if len(string) % 2 == 0:
            p = sum([int(i) for i in numberlist[::2]])
            q = sum([int(i) for i in numberlist[1::2]])
            if p == q:
                return True
    else return False