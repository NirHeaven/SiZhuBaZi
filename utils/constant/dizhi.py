from .wuxing import *
C_DiZhi =          ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
C_ShengXiao =      ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
C_ShengXiaoEmoji = ['🐭', '🐮', '🐯', '🐰', '🐲', '🐍', '🐎', '🐑', '🐒', '🐔', '🐶', '🐷']

C_WuXingDiZhi = {
    '寅': ['木', 1],
    '卯': ['木', 0],
    '辰': ['土', 1],
    '巳': ['火', 0],
    '午': ['火', 1],
    '未': ['土', 0],
    '申': ['金', 1],
    '酉': ['金', 0],
    '戌': ['土', 1],
    '亥': ['水', 0],
    '子': ['水', 1],
    '丑': ['土', 0],
}

C_DiZhiLiuHe = {
    ('子', '丑'): '合⋅化土',
    ('寅', '亥'): '合⋅化木',
    ('卯', '戌'): '合⋅化火',
    ('辰', '酉'): '合⋅化金',
    ('巳', '申'): '合⋅化水',
    ('午', '未'): '合⋅化土', #？？？
}

C_DiZhiSanAnHe = {
    ('卯', '申'): None,
    ('寅', '丑'): None,
    ('午', '亥'): None,
}
C_DiZhiLiuChong = {
    ('子', '午'): None,
    ('丑', '未'): None,
    ('寅', '申'): None,
    ('卯', '酉'): None,
    ('辰', '戌'): None,
    ('巳', '亥'): None,
}
C_DiZhiLiuHai = {
    ('戌', '酉'): None,
    ('亥', '申'): None,
    ('子', '未'): None,
    ('丑', '午'): None,
    ('寅', '巳'): None,
    ('卯', '辰'): None,
}
C_DiZhiLiuPo = {
    ('子', '酉'): None,
    ('午', '卯'): None,
    ('申', '巳'): None,
    ('寅', '亥'): None,
    ('辰', '丑'): None,
    ('戌', '未'): None,
}
C_DiZhiSiXing = {
    #  无礼
    ('子', '卯'): None,
    ('卯', '子'): None,
    # 恃势
    ('寅', '巳'): None,
    ('巳', '申'): None,
    ('申', '寅'): None,
    # 无恩
    ('戌', '丑'): None,
    ('丑', '未'): None,
    ('未', '戌'): None,
    # 自刑
    ('辰', '辰'): None,
    ('午', '午'): None,
    ('酉', '酉'): None,
    ('亥', '亥'): None,
}

C_DiZhiSanHuiFang = {
    ('寅', '卯', '辰'): '会⋅东方一气⋅木',
    ('巳', '午', '未'): '会⋅南方一气⋅火',
    ('申', '酉', '戌'): '会⋅西方一气⋅金',
    ('亥', '子', '丑'): '会⋅北方一气⋅水',
}
C_DiZhiBanHuiFang= {
    ('寅', '卯'): '半会⋅东方一气⋅木',
    ('卯', '辰'): '半会⋅东方一气⋅木',
    ('巳', '午'): '半会⋅南方一气⋅火',
    ('午', '未'): '半会⋅南方一气⋅火',
    ('申', '酉'): '半会⋅西方一气⋅金',
    ('酉', '戌'): '半会⋅西方一气⋅金',
    ('亥', '子'): '半会⋅北方一气⋅水',
    ('子', '丑'): '半会⋅北方一气⋅水',
}
C_DiZhiSanHeJu = {
    ('亥', '卯', '未'): '木',
    ('寅', '午', '戌'): '火',
    ('巳', '酉', '丑'): '金',
    ('申', '子', '辰'): '水',
    ('辰', '戌', '丑', '未'): '土',
}

C_DiZhiBanHeJu = {
    ('亥', '卯'): '木',
    ('卯', '未'): '木',
    ('寅', '午'): '火',
    ('午', '戌'): '火',
    ('巳', '酉'): '金',
    ('酉', '丑'): '金',
    ('申', '子'): '水',
    ('子', '辰'): '水',
}
C_DiZhiGongHeJu = {
    ('亥', '未'): '木',
    ('寅', '戌'): '火',
    ('巳', '丑'): '金',
    ('申', '辰'): '水',
}


C_DiZhiGong = {
    ('亥', '卯'): None,
    ('卯', '未'): None,
    ('亥', '未'): None,
    ('寅', '午'): None,
    ('午', '戌'): None,
    ('寅', '戌'): None,
    ('巳', '酉'): None,
    ('酉', '丑'): None,
    ('巳', '丑'): None,
    ('申', '子'): None,
    ('子', '辰'): None,
    ('申', '辰'): None,
}
C_DiZhiSiJi = {
    '春': ('寅', '卯', '辰'),
    '夏': ('巳', '午', '未'),
    '秋': ('申', '酉', '戌'),
    '冬': ('亥', '子', '丑'),
}

C_DiZhiCangGan = {
    #
    '寅': ('甲', '丙', '戊'),
    '巳': ('丙', '庚', '戊'),
    '申': ('庚', '壬', '戊'),
    '亥': ('壬', '甲'),
    #
    '辰': ('戊', '乙', '癸'),
    '未': ('己', '丁', '乙'),
    '戌': ('戊', '辛', '丁'),
    '丑': ('己', '癸', '辛'),
    #
    '卯': ('乙',),
    '午': ('丁', '己'),
    '酉': ('辛',),
    '子': ('癸',),
}