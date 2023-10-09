

color_map = {
    '木': "\033[32m{}\033[0m",
    '火': "\033[31m{}\033[0m",
    '土': "\033[35m{}\033[0m",
    '金': "\033[33m{}\033[0m",
    '水': "\033[34m{}\033[0m",
}

def mBracketFormatWDot(strs):
    return '【' + '⋅'.join(strs) + '】'

def DotFormat(strs):
    return '⋅'.join(strs)

def EmptyFormat(strs):
    return ''.join(strs)

def ColonFormat(strs):
    return ':'.join(strs)

def CommaFormat(strs):
    return ','.join(strs)

def SpaceFormat(strs, space_num=4):
    A = ' ' * space_num
    return A.join(strs)

def SpaceFormatWAlign(strs, space_num=4):
    A = ' ' * space_num
    return A.join(map(lambda a:"{:^8s}".format(a), strs))

def DotFormatWColor(strs):
    if len(strs) > 1:
        c = strs[1]
        return color_map[c].format("{:^7s}".format('⋅'.join(strs)))
    else:
        return"{:^7s}".format('⋅'.join(strs))