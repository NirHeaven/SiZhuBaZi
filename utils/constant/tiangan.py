from .wuxing import *

C_TianGan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

C_YangTianGan = ['甲', '丙', '戊', '庚', '壬']
C_YinTianGan = ['乙', '丁', '己', '辛', '癸']

C_WuXingTianGan = {}
for i in range(len(C_TianGan)):
    C_WuXingTianGan[C_TianGan[i]] = [C_WuXingShengL[i//2], 1 - i % 2]

C_TianGanWuHe = {
    ('甲', '己'): '合⋅化土',
    ('乙', '庚'): '合⋅化金',
    ('丙', '辛'): '合⋅化水',
    ('丁', '壬'): '合⋅化木',
    ('戊', '癸'): '合⋅化火',
}

C_TianGanSiChong = {
    ('甲', '庚'): None,
    ('乙', '辛'): None,
    ('丙', '壬'): None,
    ('丁', '癸'): None,
}

