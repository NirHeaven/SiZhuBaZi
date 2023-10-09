
from utils import *
from utils.constant import *

def baziAnalysis(year, month, day, hour, minute, bazi=None):
    if hour % 2 == 1 and minute < 10:
        hour -= 1
    if bazi is None:
        bazi, isInJi = getGanZhi(year, month, day, hour)
    else:
        isInJi = False
    TianGan = bazi[::2]
    DiZhi = bazi[1::2]
    RG = TianGan[-2]
    YZ = DiZhi[1]

    GanShen = []
    TianGanWuXing = []

    DiZhiWuXing = []
    CangGanWuXing = []
    ZhiShen = []
    for TG in TianGan:
        GanShen.append(getShiShen(RG, TG, True))
        TianGanWuXing.append([TG] + getTianGanWuXing(TG))
    for DZ in DiZhi:
        DiZhiWuXing.append([DZ] + getDiZhiWuXing(DZ))
        tCangGanWuXing = []
        tZhiShen = []
        for CG in getCangGan(DZ):
            tZhiShen.append(getShiShen(RG, CG))
            tCangGanWuXing.append([CG] + getTianGanWuXing(CG))
        CangGanWuXing.append(tCangGanWuXing)
        ZhiShen.append(tZhiShen)
    # print(GanShen)
    # print(TianGanWuXing)
    # print(DiZhiWuXing)
    # print(CangGanWuXing)
    # print(ZhiShen)
    TianGanHe, TianGanChong = getTianGanHeChong(TianGan)
    # print(TianGanHe)
    # print(TianGanChong)

    DiZhiHe, DiZhiChong, DiZhiHai ,DiZhiXing = getDiZhiHeChongXingHai(DiZhi)
    # print(DiZhiHe)
    # print(DiZhiChong)
    # print(DiZhiHai)
    # print(DiZhiXing)
    DiZhiHuiFang = getDiZhiHuiFang(DiZhi)
    DiZhiHuiJu, DiZhiBanHuiJu = getDiZhiHuiJu(DiZhi)
    # print(DiZhiHuiFang)
    # print(DiZhiHuiJu)
    # print(DiZhiBanHuiJu)
    DeLing, LingInfo = isDeLing(RG, YZ, isInJi)
    DeDi, DiInfo = isDeDi(RG, DiZhi)
    DeShi, ShiInfo = isDeShi(TianGan, DiZhi)
    body = isStrong(DeLing, DeDi, DeShi)

    # print(DeLing, LingInfo)
    # print(DeDi, DiInfo)
    # print(DeShi, ShiInfo)
    # print(body)
    exists, YongShenInfo = isYongShenExists(body, TianGan, DiZhi)
    # print(exists, YongShenInfo)
    format_ganshen = list(map(lambda a:DotFormatWColor(a), GanShen))
    format_tiangan = list(map(lambda a:DotFormatWColor(a), TianGanWuXing))
    format_dizhi = list(map(lambda a:DotFormatWColor(a), DiZhiWuXing))

    format_canggan = []
    format_zhishen = []
    n_max = 0
    for cangan in CangGanWuXing:
        t = list(map(lambda a:DotFormatWColor(a), cangan))
        n_max = len(t) if len(t) > n_max else n_max
        format_canggan.append(t)
    for zhishen in ZhiShen:
        t = list(map(lambda a:DotFormatWColor(a), zhishen))
        format_zhishen.append(t)
    for idx in range(len(format_canggan)):
        while len(format_canggan[idx]) < n_max:
            format_zhishen[idx].append(' '*11)
            format_canggan[idx].append(' '*11)
    format_canggan_r = []
    format_zhishen_r = []
    for item in zip(*format_canggan):
        format_canggan_r.append(list(item))

    for item in zip(*format_zhishen):
        format_zhishen_r.append(list(item))
    format_canggan = []
    for idx, item in enumerate(format_canggan_r):
        if idx == 0:
            format_canggan.append(['藏干'] + item)
        else:
            format_canggan.append([' '*6] + item)
    format_zhishen = []
    for idx, item in enumerate(format_zhishen_r):
        if idx == 0:
            format_zhishen.append(['支神'] + item)
        else:
            format_zhishen.append([' '*6] + item)

    format_tianganhechong = []
    for t in [TianGanHe, TianGanChong]:
        if len(t) == 0:
            continue
        format_tianganhechong.append(EmptyFormat(list(map(lambda a:EmptyFormat(a), t))))
    format_tianganhechong = [CommaFormat(format_tianganhechong)]
    format_dizhihechongxinghai = []
    for t in [DiZhiHuiFang, DiZhiHuiJu, DiZhiBanHuiJu, DiZhiHe, DiZhiChong, DiZhiHai, DiZhiXing]:
        if len(t) == 0:
            continue
        format_dizhihechongxinghai.append(EmptyFormat(list(map(lambda a:EmptyFormat(a), t))))
    format_dizhihechongxinghai = [CommaFormat(format_dizhihechongxinghai)]

    if DeLing:
        format_deling = [DotFormatWColor(LingInfo)]
    else:
        format_deling = ['无']
    if DeDi:
        format_dedi = []
        for k in DiInfo:
            t = CommaFormat(list(map(lambda a:DotFormatWColor(a), DiInfo[k])))
            format_dedi.append(ColonFormat([k, t]))

    else:
        format_dedi = ['无']
    if DeShi:
        format_deshi = [CommaFormat(list(map(lambda a: DotFormatWColor(a), ShiInfo)))]
    else:
        format_deshi = ['无']

    format_body = [body]
    format_yongshen = [CommaFormat(list(map(lambda a: DotFormatWColor(a), YongShenInfo)))]


    print_str = [
        ['  ', '年柱', '月柱', '日柱', '时柱'],
        ['=================================================================='],
        ['干神'] + format_ganshen,
        ['------------------------------------------------------------------'],
        ['天干'] + format_tiangan,
        ['地支'] + format_dizhi,
        ['------------------------------------------------------------------'],
        *format_canggan,
        ['------------------------------------------------------------------'],
        *format_zhishen,
        # ['藏干'] + format_canggan,
        # ['支神'] + format_zhishen,
        ['------------------------------------------------------------------'],
        ['天干合冲'] + format_tianganhechong,
        ['地支合冲'] + format_dizhihechongxinghai,
        ['------------------------------------------------------------------'],
        ['令'] + format_deling,
        ['地'] + format_dedi,
        ['势'] + format_deshi,
        ['身'] + format_body,
        ['用神'] + format_yongshen,
    ]
    for idx, s in enumerate(print_str):
        print(SpaceFormatWAlign(s))

if __name__ == '__main__':
    baziAnalysis(1993, 5, 13, 19, 5)
    # baziAnalysis('丙子辛丑癸亥乙卯')
    # print(getGanZhi(1993, 5, 13, 18))
    # import numpy as np
    # N = 31 + 28 + 31 + 30 + 13
    # year = 1993
    # N0 = 79.6764 + 0.2422*(year - 1985)-int(0.25*(year - 1985))
    # print(N0)
    # theta = 2*np.pi*(N - N0) / 365.2422 * 180
    # delta = 0.0028 - 1.9857 * np.sin(theta) + 9.9059 * np.sin(2*theta) - 7.0924 * np.cos(theta) - 0.6882 * np.cos(2*theta)
    # theta = 2*np.pi*(N - 81) / 364
    # delta = 9.87 * np.sin(2*theta) - 7.53 * np.cos(theta) - 1.5 *  np.sin(theta)
    # print(delta)