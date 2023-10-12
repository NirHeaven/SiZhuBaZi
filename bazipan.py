
from utils import *

def baziAnalysis(year=None, month=None, day=None, hour=None, minute=None, gender=None, zone=None, bazi=None):
    if year is not None:
        qiYunNian, qiYunYue, qiYueRi, qiYunDiffNian, qiYunDiffYue, DaYunLiuNianInfo = getDaYun(year, month, day, gender)
        useDaYun = True
    else:
        useDaYun = False
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
            GanShen.append(['身主', '无'])
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
    GeJu, GeJuInfo, GeJuIndoubt = getGeJu(bazi)
    if GeJuIndoubt:
        GeJu = '(存疑)' + GeJu
    TianGanHe, TianGanChong = getTianGanHeChong(TianGan)
    # print(TianGanHe)
    # print(TianGanChong)

    DiZhiRelation = getDiZhiHeChongXingHai(DiZhi)
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
    # format_ganshen = list(map(lambda a:DotFormatWColor(a), GanShen))
    format_ganshen = list(map(lambda a:Format(a, sep='⋅', color_idx=1, align='^'), GanShen))
    format_tiangan = list(map(lambda a:Format(a, sep='⋅', color_idx=1, align='^'), TianGanWuXing))
    format_dizhi = list(map(lambda a:Format(a, sep='⋅', color_idx=1, align='^'), DiZhiWuXing))

    format_canggan = []
    format_zhishen = []
    format_geju = [GeJu if not GeJuIndoubt else Format(GeJu, align=None, color='火', sep='')]
    if GeJu != '':
        format_gejuinfo = GeJuInfo
    else:
        format_gejuinfo = ['']
    n_max = 0
    for cangan in CangGanWuXing:
        t = list(map(lambda a:Format(a, sep='⋅', color_idx=1), cangan))
        n_max = len(t) if len(t) > n_max else n_max
        format_canggan.append(t)
    for zhishen in ZhiShen:
        t = list(map(lambda a:Format(a, sep='⋅', color_idx=1), zhishen))
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
        format_tianganhechong.append(EmptyFormat(list(map(lambda a: EmptyFormat(a), t))))
    format_tianganhechong = [Format(format_tianganhechong, sep=',')]
    format_dizhihechongxinghai = []
    for t in [DiZhiHuiFang, DiZhiHuiJu, DiZhiBanHuiJu] + list(DiZhiRelation):
        if len(t) == 0:
            continue
        format_dizhihechongxinghai.append(Format(list(map(lambda a:EmptyFormat(a), t)), sep=',', color_idx=None, align=None))
    format_dizhihechongxinghai = [Format(format_dizhihechongxinghai, sep=',')]

    if DeLing:
        format_deling = [Format(LingInfo,  sep='⋅', color_idx=1)]
    else:
        format_deling = ['无']
    if DeDi:
        format_dedi = []
        for k in DiInfo:
            t = Format(list(map(lambda a:Format(a, sep='⋅', color_idx=1), DiInfo[k])), sep=',', color_idx=None)
            format_dedi.append(Format([k, t], sep=':', color_idx=None))

    else:
        format_dedi = ['无']
    if DeShi:
        format_deshi = [Format(list(map(lambda a: Format(a, sep='⋅', color_idx=1), ShiInfo)), sep=',', color_idx=None)]
    else:
        format_deshi = ['无']

    format_body = [body]
    format_yongshen = [Format(list(map(lambda a: Format(a, sep='⋅', color_idx=1), YongShenInfo)), sep=',', color_idx=None, align=None)]
    format_yongshenNeed =[EmptyFormat(list(map(lambda a: Format(a, sep='', color_idx=0, align=None), YongShenNeed)))]

    format_nayin = list(map(lambda a: Format(a, sep='', color_idx=2), NaYin))
    format_kongwang = KongWang
    format_bazikongwang = list(map(lambda a: Format(a, sep='⋅', color_idx=1) if a is not None else ' ' * 11, BaZiKongWang))

    format_sanqi = None
    if SanQi:
        format_sanqi = [Format(SanQiInfo, sep='⋅', color_idx=None, align=None)]
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
        # ['身'] + format_body,
        # ['用神'] + format_yongshen,
        # ['喜'] + format_yongshenNeed,
        ['------------------------------------------------------------------'],
        ['格局'] + format_geju,
        *format_gejuinfo,
        ['------------------------------------------------------------------'],
        (['三奇'] + format_sanqi) if format_sanqi is not None else '',
        (['魁罡'] + format_kuigang) if format_kuigang is not None else '',
    ]
    if useDaYun:
        print_str_yun = []
        # print_str_yun.append(['大运', ' ' * 20 + '{}年{}月{}日({}年{}个月) 起运'.format(qiYunNian, int(qiYunYue), qiYueRi, qiYunDiffNian, qiYunDiffYue)])
        print_str_yun.append(['大运', ' ' * 20 + '{}年{}月({}年{}个月) 起运'.format(qiYunNian, int(qiYunYue), qiYunDiffNian, qiYunDiffYue)])
        for k1 in DaYunLiuNianInfo:
            print_str_yun.append([k1[0] + '(' + k1[1] + ')'])
            v1 = DaYunLiuNianInfo[k1]
            for k2 in v1:
                v2 = v1[k2]
                for item in k2:
                    item = [item[0], '(' + item[1] + ')']
                    print_str_yun.append([Format(item, color_idx=0, sep='')])
                G_ls = []
                Z_ls = []
                sui_nian_ls = []
                for idx, k3 in enumerate(v2):
                    if idx < 4 or idx > 7:
                        n_space = 2
                    else:
                        n_space = 3
                    G, Z, sui, nian = k3
                    G = [' ' * n_space, G[0], '(' + G[1] + ')']
                    Z = [' ' * n_space, Z[0], '(' + Z[1] + ')']
                    sui_nian = [' ' * (3 - len(sui)),  sui,  '(' + nian + ')']
                    G_ls.append(Format(G, color_idx=1, sep=''))
                    Z_ls.append(Format(Z, color_idx=1, sep=''))
                    sui_nian_ls.append(sui_nian)
                print_str_yun.append(sui_nian_ls)
                print_str_yun.append(G_ls)
                print_str_yun.append(Z_ls)
            print_str_yun.append(['==============================================================='])

        print_str.extend(print_str_yun)
    for idx, s in enumerate(print_str):
        print(Format(list(map(lambda a:Format(a, sep='', align_w=8, color_idx=None), s)), sep=' ' * 4, color_idx=None))
        pass
if __name__ == '__main__':
    # XU
    # baziAnalysis(1993, 5, 13, 19, 5, bazi='甲戌丙子己丑丁卯')
    # baziAnalysis(1994, 12, 29, 7, 5, '女', '咸阳')
    # 柯
    # baziAnalysis(1994, 3, 5, 13, 45, '男', '十堰')
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
    baziAnalysis(1994, 5, 7, 10, 25, '女', '咸阳')
    # baziAnalysis(1993, 5, 13, 19, 5, '男', '襄樊')
    # 官印相生--身弱，官强，印为相，见印化官生身
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='戊戌辛酉癸巳癸亥')

    # 杀印相生--印格，身弱，七杀为相，用杀生印，不得已而为之，低于官印相生
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='癸巳甲子丁酉甲辰')
    # 财滋弱杀格--身强，月令为财；日坐禄刃；七杀透干一位，最好有弱根，不可官杀混杂；比、劫透干
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='己酉丙寅庚申庚辰')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='己未癸酉丁巳丁未')

    # 食神制杀格--身弱，食神为格神；偏官旺而为杀，高透；杀需强，食神临杀且有根且透；不能见财；不喜印不喜官；越纯越好
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='壬子壬子丙戌戊戌')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='壬申丙午庚午丙戌')
    # 食神生财格--身强
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='丁巳己酉丁酉甲辰')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='癸巳丙辰辛亥甲午')
    # 反面例子:无财
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='庚申壬午庚戌壬午')

    # 伤官佩印格--身弱，伤官在月令且藏干透出天干，身弱不从，日主有根，印透且强， 日主和印不被刑冲合化
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='丁亥庚戌己巳庚午')
    # 伤官生财格--身强
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='甲辰丁卯癸未甲寅')
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='甲午丁卯甲子壬申')
    # 康熙
    # baziAnalysis(1993, 5, 13, 19, 5, '襄樊', bazi='甲午戊辰戊申丁巳')
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