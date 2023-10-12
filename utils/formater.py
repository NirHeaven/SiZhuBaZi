from utils.constant.tiangan import *
from utils.constant.dizhi import *

color_map = {
    '木': "\033[32m{}\033[0m",
    '火': "\033[31m{}\033[0m",
    '土': "\033[35m{}\033[0m",
    '金': "\033[33m{}\033[0m",
    '水': "\033[34m{}\033[0m",
}

def EmptyFormat(strs, n=1):
    return Format(strs, sep='', align=None, color_idx=None, n=n)

def Format(strs, sep='', align='^', align_w=7, space_pad_num=0, color_idx=0, color=None, n=1):
    if n != 1:
        new_strs = []
        for i in range(0, len(strs), n):
            new_strs.append(''.join(strs[i:i+n]))
        strs = new_strs
    if len(strs) == 0:
        return ''
    if align is None:
        f_align = '{}'
    else:
        assert align in ['<', '^', '>']
        f_align = '{:' + align + str(align_w) + 's}'
    f_space = ' ' * space_pad_num
    if color is not None:
        assert color in color_map
        f_color = color_map[color]
    elif color_idx is None or len(strs) < color_idx:
        f_color = '{}'
    else:
        if strs[color_idx] in color_map:
            f_color = color_map[strs[color_idx]]
        elif strs[color_idx] in C_TianGan:
            f_color = color_map[C_WuXingTianGan[strs[color_idx]][color_idx]]
        elif strs[color_idx] in C_DiZhi:
            f_color = color_map[C_WuXingDiZhi[strs[color_idx]][color_idx]]
        else:
            f_color = '{}'

    return f_space.join(f_color.format(f_align.format(sep.join(strs))))



