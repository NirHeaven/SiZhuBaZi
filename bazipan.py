
from utils import *

def baziAnalysis(year, month, day, hour, minute, zone=None, bazi=None):
    if bazi is None:
        bazi, isInJi = getGanZhi(year, month, day, hour, minute, zone)
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
    for idx, TG in enumerate(TianGan):
        if idx == 2:
            GanShen.append(['身主'])
        else:
            GanShen.append(getShiShen(RG, TG))
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
    GeJu, GeJuInfo = getGeJu(bazi)
    TianGanHe, TianGanChong = getTianGanHeChong(TianGan)
    # print(TianGanHe)
    # print(TianGanChong)

    DiZhiHe, DiZhiChong, DiZhiHai ,DiZhiXing, DiZhiPo, DiZhiGong= getDiZhiHeChongXingHai(DiZhi)
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
    exists, YongShenInfo, YongShenNeed = isYongShenExists(body, TianGan, DiZhi)
    KongWang, BaZiKongWang = getBaZiKongWang(bazi)
    NaYin = getNaYin(bazi)
    # print(KongWang)
    # print(NaYin)
    SanQi, SanQiInfo = isSanQi(TianGan)
    KuiGang = isKuiGang(bazi)

    # print(exists, YongShenInfo)
    format_ganshen = list(map(lambda a:DotFormatWColor(a), GanShen))
    format_tiangan = list(map(lambda a:DotFormatWColor(a), TianGanWuXing))
    format_dizhi = list(map(lambda a:DotFormatWColor(a), DiZhiWuXing))

    format_canggan = []
    format_zhishen = []
    format_geju = [GeJu]
    if GeJu != '':
        format_gejuinfo = GeJuInfo
    else:
        format_gejuinfo = ['']
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
            format_zhishen[idx].append(' '*10)
            format_canggan[idx].append(' '*10)
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
    for t in [DiZhiHuiFang, DiZhiHuiJu, DiZhiBanHuiJu, DiZhiHe, DiZhiChong, DiZhiHai, DiZhiXing, DiZhiPo, DiZhiGong]:
        if len(t) == 0:
            continue
        format_dizhihechongxinghai.append(CommaFormat(list(map(lambda a:EmptyFormat(a), t))))
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
    format_yongshenNeed =[EmptyFormat(list(map(lambda a: EmptyFormatWColorNoAlign(a, 0), YongShenNeed)))]

    format_nayin = list(map(lambda a: EmptyFormatWColor(a, 2), NaYin))
    format_kongwang = KongWang
    format_bazikongwang = list(map(lambda a: DotFormatWColor(a) if a is not None else ' ' * 11, BaZiKongWang))

    format_sanqi = None
    if SanQi:
        format_sanqi = [DotFormat(SanQiInfo)]
    format_kuigang = None
    if KuiGang:
        format_kuigang = [EmptyFormat(bazi[4:6])]

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
        ['------------------------------------------------------------------'],
        ['纳音'] + format_nayin,
        ['------------------------------------------------------------------'],
        ['空亡'] + format_kongwang,
        ['     '] + format_bazikongwang,
        ['------------------------------------------------------------------'],
        ['天干合冲'] + format_tianganhechong,
        ['地支合冲'] + format_dizhihechongxinghai,
        ['------------------------------------------------------------------'],
        ['令'] + format_deling,
        ['地'] + format_dedi,
        ['势'] + format_deshi,
        ['身'] + format_body,
        # ['用神'] + format_yongshen,
        # ['喜'] + format_yongshenNeed,
        ['------------------------------------------------------------------'],
        ['格局'] + format_geju,
        *format_gejuinfo,
        ['------------------------------------------------------------------'],
        (['三奇'] + format_sanqi) if format_sanqi is not None else '',
        (['魁罡'] + format_kuigang) if format_kuigang is not None else '',
    ]
    for idx, s in enumerate(print_str):
        print(SpaceFormatWAlign(s))
        pass
if __name__ == '__main__':
    # XU
    # baziAnalysis(1993, 5, 13, 19, 5, bazi='甲戌丙子己丑丁卯')
    # harding
    # baziAnalysis(1993, 5, 13, 19, 5, bazi='丙子丙申乙酉戊寅')
    # harding对象
    # baziAnalysis(1993, 5, 13, 19, 5, bazi='乙亥丙戌丁酉丁未')
    # ZHOU
    # baziAnalysis(1993, 5, 13, 19, 5, bazi='癸酉乙卯丙申甲午')
    # ZHANG
    # baziAnalysis(1993, 5, 13, 19, 5, bazi='己卯乙亥丁亥甲辰')
    # yy
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='甲戌己巳癸巳丁巳')
    baziAnalysis(1993, 5, 13, 19, 5, '襄樊')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='丁亥丙午壬寅己酉')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='己巳乙亥壬子乙巳')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='癸巳丁巳丁卯丙午')
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
    # year = 1993
    # month = 12
    # day = 30
    # hour = 22
    # minute = 7
    # print(year, month, day, hour, minute)
    # diff_minute = 7300
    # print(diff_minute//60)
    # if diff_minute < 0:
    #     diff_minute *= -1
    #     while True:
    #         if minute > diff_minute:
    #             minute -= diff_minute
    #             break
    #         minute += 60
    #         if hour > 0:
    #             hour -= 1
    #         else:
    #             hour = 23
    #             if day > 1:
    #                 day -= 1
    #             else:
    #                 if month > 1:
    #                     day = C_DayPerMonth[month - 1]
    #                     if month - 1 == 2:
    #                         day += 1
    #                     month -= 1
    #                 else:
    #                     day = C_DayPerMonth[12]
    #                     month = 11
    #                     year -= 1
    # else:
    #     while True:
    #         if minute + diff_minute < 60:
    #             minute += diff_minute
    #             break
    #         diff_minute -= 60
    #         if hour < 23:
    #             hour += 1
    #         else:
    #             hour = 0
    #             c_day_num = C_DayPerMonth[month]
    #             if month == 2:
    #                 c_day_num += 1
    #             if day < c_day_num:
    #                 day += 1
    #             else:
    #                 day = 1
    #                 if month < 11:
    #                     month += 1
    #                 else:
    #                     month = 1
    #                     year += 1
    # print(year, month, day, hour, minute)