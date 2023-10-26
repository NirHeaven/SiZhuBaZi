import itertools as it

from .formater import *
from .constant import *
# from formater import *
# from constant import *
import sxtwl, json, math


def getTrueSolarTime(year, month, day, hour, minute, isLunarLeap, zone):
    SolarTimeDiff = json.load(open('utils/真太阳时.json'))
    diff = SolarTimeDiff[zone]['time']
    diff_minute = math.ceil(diff / 60)
    if diff_minute < 0:
        diff_minute *= -1
        while True:
            if minute > diff_minute:
                minute -= diff_minute
                return year, month, day, hour, minute
            minute += 60
            if hour > 0:
                hour -= 1
            else:
                hour = 23
                if day > 1:
                    day -= 1
                else:
                    if month > 1:
                        day = C_DayPerMonth[month - 1]
                        if month - 1 == 2 and isLunarLeap:
                            day += 1
                        month -= 1
                    else:
                        day = C_DayPerMonth[12]
                        month = 11
                        year -= 1
    else:
        while True:
            if minute + diff_minute < 60:
                minute += diff_minute
                return year, month, day, hour, minute
            diff_minute -= 60
            if hour < 23:
                hour += 1
            else:
                hour = 0
                c_day_num = C_DayPerMonth[month]
                if month == 2 and isLunarLeap:
                    c_day_num += 1
                if day < c_day_num:
                    day += 1
                else:
                    day = 1
                    if month < 11:
                        month += 1
                    else:
                        month = 1
                        year += 1


def getGanZhi(year, month, day, hour, minute, zone):

    info = sxtwl.fromSolar(year, month, day)
    print('北京时间:', year, month, day, hour, minute)
    year, month, day, hour, minute = getTrueSolarTime(year, month, day, hour, minute, info.isLunarLeap(), zone)
    print('真太阳时:', year, month, day, hour, minute)

    info = sxtwl.fromSolar(year, month, day)
    yGZ = info.getYearGZ(True)
    mGZ = info.getMonthGZ()
    dGZ = info.getDayGZ()
    hGZ = sxtwl.getShiGz(dGZ.tg, hour)
    isInJi = False
    for i in range(18):
        if info.hasJieQi():
            JQ = C_JQMC[info.getJieQi()]
            if JQ in ['立春', '立夏', '立秋', '立冬']:
                isInJi = True
                break
        info = info.after(1)
    return EmptyFormat([C_TianGan[yGZ.tg], C_DiZhi[yGZ.dz],
            C_TianGan[mGZ.tg], C_DiZhi[mGZ.dz],
            C_TianGan[dGZ.tg], C_DiZhi[dGZ.dz],
            C_TianGan[hGZ.tg], C_DiZhi[hGZ.dz]]), isInJi

def C_getShiShen(wuxingA, yinyangA, wuxingB, yinyangB):
    # 印
    ShiShenName, ShiShenAlias = '', ''
    if C_WuXingSheng[wuxingB] == wuxingA:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '正印', '印'
        else:
            ShiShenName, ShiShenAlias = '偏印', '枭'
    # 食伤
    elif C_WuXingSheng[wuxingA] ==  wuxingB:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '伤官', '伤'
        else:
            ShiShenName, ShiShenAlias = '食神', '食'
    # 财
    elif C_WuXingKe[wuxingA] == wuxingB:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '正财', '才'
        else:
            ShiShenName, ShiShenAlias = '偏财', '财'
    # 官杀
    elif C_WuXingKe[wuxingB] == wuxingA:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '正官', '官'
        else:
            ShiShenName, ShiShenAlias = '七杀', '杀'
    # 比劫
    else:
        assert wuxingA == wuxingB
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '劫财', '劫'
        else:
            ShiShenName, ShiShenAlias = '比肩', '比'
    return [ShiShenName, wuxingB, ShiShenAlias]

# A为本身
def getShiShen(tianganA, tianganB):
    wuxingA, yinyangA = C_WuXingTianGan[tianganA]
    wuxingB, yinyangB = C_WuXingTianGan[tianganB]
    return C_getShiShen(wuxingA, yinyangA, wuxingB, yinyangB)[:2]


def C_getWuXing(D, K):
    wuxing, yiyang = D[K]
    yiyang = '阳' if yiyang else '阴'
    return [wuxing, yiyang]

def getTianGanWuXing(tiangan):
    return C_getWuXing(C_WuXingTianGan, tiangan)

def getDiZhiWuXing(dizhi):
    return C_getWuXing(C_WuXingDiZhi, dizhi)


def getCangGan(dizhi):
    return list(C_DiZhiCangGan[dizhi])


def isPairInDict(keys, D, permutate=True):
    results = set()
    n = len(keys)
    for i in range(n-1):
        k1 = keys[i]
        for j in range(i+1, n):
            k2 = keys[j]
            if permutate:
                seq = it.permutations([k1, k2])
            else:
                seq = [[k1, k2]]
            for item in seq:
                t_item = tuple(item)
                if t_item in D:
                    results.add(t_item + (D[t_item], ))
    return list(results)

def isAdjacentPairInDict(keys, D):
    results = set()
    n = len(keys)
    for i in range(n-1):
        k1 = keys[i]
        k2 = keys[i+1]
        t_item = tuple([k1, k2])
        if t_item in D:
            results.add(t_item + (D[t_item], ))
    return list(results)


def isTripletInDict(keys, D, permutate=True):
    results = set()
    n = len(keys)
    for i in range(n-2):
        k1 = keys[i]
        for j in range(i+1, n-1):
            k2 = keys[j]
            for k in range(j+1, n):
                k3 = keys[k]
                if permutate:
                    seq = it.permutations([k1, k2, k3])
                else:
                    seq = [[k1, k2, k3]]
                for item in seq:
                    t_item = tuple(item)
                    if t_item in D:
                        results.add(t_item + (D[t_item], ))
    return list(results)


def insertValueByIndex(datas, index, v):
    for idx in range(len(datas)):
        datas[idx] = list(datas[idx])
        datas[idx].insert(index, v)

def replaceNoneByKey(datas, key):
    rdata = []
    for item in datas:
        item = list(item)
        if item[-1] is None:
            item[-1] = key
        rdata.append(item)
    return rdata

def getNaYin(bazi):
    NY = []
    for idx in range(0, len(bazi), 2):
        NY.append(C_NaYin[bazi[idx:idx+2]])
    return NY

def getKongWang(bazi):
    KW = []
    for idx in range(0, len(bazi), 2):
        KW.append(C_KongWang[bazi[idx:idx+2]])
    return KW

def getBaZiKongWang(bazi):
    KW = getKongWang(bazi)
    RKW = KW[2]
    dizhis = bazi[1::2]
    isKW = []
    for dz in dizhis:
        if dz in RKW:
            wuxing, yiyang = getDiZhiWuXing(dz)
            isKW.append((dz, wuxing, yiyang))
        else:
            isKW.append(None)
    return KW, isKW

def getDiShi(bazi):
    DiShiInfo = []
    RG = bazi[4]
    for Z in bazi[1::2]:
        for k in C_ShiErChangSheng[RG]:
            if C_ShiErChangSheng[RG][k] == Z:
                DiShiInfo.append(k)
                break
    return DiShiInfo

def getTianGanHeChong(tiangans):
    He = isPairInDict(tiangans, C_TianGanWuHe)
    Chong = isPairInDict(tiangans, C_TianGanSiChong)
    He = replaceNoneByKey(He, '合')
    Chong = replaceNoneByKey(Chong, '冲')
    return He, Chong


def getDiZhiHeChongXingHai(dizhis):
    He = isPairInDict(dizhis, C_DiZhiLiuHe)
    AnHe = isPairInDict(dizhis, C_DiZhiSanAnHe)
    Chong = isPairInDict(dizhis, C_DiZhiLiuChong)
    Hai = isPairInDict(dizhis, C_DiZhiLiuHai)
    Xing = isPairInDict(dizhis, C_DiZhiSiXing)
    Po = isPairInDict(dizhis, C_DiZhiLiuPo)
    Gong = isAdjacentPairInDict(dizhis, C_DiZhiGong)
    He = replaceNoneByKey(He, '合')
    AnHe = replaceNoneByKey(AnHe, '暗合')
    Chong = replaceNoneByKey(Chong, '冲')
    Hai = replaceNoneByKey(Hai, '害')
    Xing = replaceNoneByKey(Xing, '刑')
    Po = replaceNoneByKey(Po, '破')
    Gong = replaceNoneByKey(Gong, '拱')

    return He, AnHe, Chong, Hai, Xing, Po, Gong


def getDiZhiSanHuiFang(dizhis):
    return isTripletInDict(dizhis, C_DiZhiSanHuiFang), isPairInDict(dizhis, C_DiZhiBanHuiFang)


def getDiZhiSanHeJu(dizhis):
    HeJu = isTripletInDict(dizhis, C_DiZhiSanHeJu)
    BanHeJu = isPairInDict(dizhis, C_DiZhiBanHeJu)
    GongHeJu = isPairInDict(dizhis, C_DiZhiGongHeJu)
    insertValueByIndex(HeJu, -1, '合')
    insertValueByIndex(BanHeJu, -1, '半合')
    insertValueByIndex(GongHeJu, -1, '拱')
    return HeJu, BanHeJu, GongHeJu

def getGeJu(baizi):

    _geju_map = {
        '比肩': '建禄',
        '劫财': '羊刃'
    }
    YZ = baizi[3]
    RG = baizi[4]
    YZCG = getCangGan(YZ)
    wuxingRG, yinyangRG = getTianGanWuXing(RG)
    wuxingYZBenQi, yinyangYZBenQi = getTianGanWuXing(YZCG[0])

    GeJuGanShen = None

    # 是否有合会局
    result, _ = getDiZhiSanHuiFang(baizi[1::2])
    if len(result) == 0:
        result, _, _ = getDiZhiSanHeJu(baizi[1::2])
    # 如果有，本格用和会后的五行
    if len(result) != 0:
        assert len(result) == 1
        info = result[0]
        Ju_Dizhi = info[0]
        HeHuaWuXing = info[1][-1]
        flag = False
        for Z in Ju_Dizhi:
            if YZ == Z:
                flag = True
                break
        if flag:
            GeJuGanShen = C_getShiShen(wuxingRG, yinyangRG, HeHuaWuXing, '阴' if yinyangRG == '阳' else '阳')[0]
    # 如果没有，以月令取
    if GeJuGanShen is None:
        GeJuGanShen = C_getShiShen(wuxingRG, yinyangRG, wuxingYZBenQi, yinyangYZBenQi)[0]
    tiangans = baizi[::2]
    reordered_tiangans = [tiangans[1], tiangans[0], tiangans[2], tiangans[3]]

    GeJuGanShen1 = None

    for CG in YZCG:
        find_flag = False
        for TG in reordered_tiangans:
            if CG == TG:
                wuxingCG, yinyangCG = getTianGanWuXing(CG)
                GeJuGanShen1 = C_getShiShen(wuxingRG, yinyangRG, wuxingCG, yinyangCG)[0]
                find_flag = True
                break
        if find_flag:
            break
    if GeJuGanShen in _geju_map:
        GeJuGanShen = _geju_map[GeJuGanShen]
    if GeJuGanShen1 in _geju_map:
        GeJuGanShen1 = _geju_map[GeJuGanShen1]
    if GeJuGanShen1 == GeJuGanShen:
        GeJuGanShen1 = None
    return GeJuGanShen, GeJuGanShen1


    # YZ = baizi[3]
    # RG = baizi[4]
    # GeJuGanShen = []
    # GeJuGanShenTianGan = []
    # YZCG = getCangGan(YZ)
    # wuxingRG, yinyangRG = getTianGanWuXing(RG)
    # inDoubtFlag = False
    # if C_ShiErChangSheng[RG]['帝旺'] == YZ and RG in C_YangTianGan:
    #     GeJuGanShen = '羊刃'
    # elif C_ShiErChangSheng[RG]['临官'] == YZ:
    #     GeJuGanShen = '建禄'
    # else:
    #     DiZhiCangGans = [YZCG]
    #     for i in [0, 1, 3]:
    #         DiZhiCangGans.append(getCangGan(baizi[i*2 + 1])[0:1])
    #     for DiZhiCangGan in DiZhiCangGans:
    #         for canggan in DiZhiCangGan:
    #             canggan_wuxing, canggang_yinyang = getTianGanWuXing(canggan)
    #             tiangan_wo_RG = baizi[::2]
    #             tiangan_wo_RG = tiangan_wo_RG[0] + tiangan_wo_RG[1] + tiangan_wo_RG[3]
    #             for tiangan in baizi[::2]:
    #                 wuxing, yiyang = getTianGanWuXing(tiangan)
    #                 if wuxing == canggan_wuxing:
    #                     GanShen = getShiShen(RG, tiangan)
    #                     if GanShen[0] in ['比肩', '劫财']:
    #                         continue
    #                     GeJuGanShen.append(getShiShen(RG, tiangan))
    #                     GeJuGanShenTianGan.append((tiangan, yiyang, yiyang==canggang_yinyang))
    #     if len(GeJuGanShen) == 0:
    #         GeJuGanShen = None
    #     elif len(GeJuGanShen) >= 1:
    #         GeJuGanShen = GeJuGanShen[0][0]
    #     else:
    #         t_idx = 0
    #         for idx in range(len(GeJuGanShenTianGan)):
    #             if GeJuGanShenTianGan[idx][-1]:
    #                 t_idx = idx
    #                 break
    #         GeJuGanShen = GeJuGanShen[t_idx][0]
    #     if GeJuGanShen is None:
    #         result = getDiZhiSanHuiFang(baizi[1::2])
    #         if len(result) == 0:
    #             result, _ = getDiZhiSanHeJu(baizi[1::2])
    #         if len(result) != 0:
    #             assert len(result) == 1
    #             for Z in result[0]:
    #                 if YZ == Z:
    #                     _, yinyang = getDiZhiWuXing(YZ)
    #                     wuxing = result[0][-1]
    #                     if len(wuxing) > 1:
    #                         wuxing = wuxing[-1]
    #                     GeJuGanShen = C_getShiShen(wuxingRG, yinyangRG, wuxing, yinyang)[0]
    #                     break
    #     if GeJuGanShen is None:
    #         benqi = YZCG[0]
    #         benqi_wuxing, benqi_yinyang = getTianGanWuXing(benqi)
    #         GeJuGanShen = C_getShiShen(wuxingRG, yinyangRG, benqi_wuxing, benqi_yinyang)[0]
    #         inDoubtFlag = True
    #
    # GeJu = GeJuGanShen + '格'
    # if GeJuGanShen in ['比肩', '劫财']:
    #     return GeJu, '', True
    # GeJuInfo = C_GeJu[GeJu]
    # GeJuInfoLs = []
    # for k, v in GeJuInfo.items():
    #     GeJuInfoLs.append([k, v])
    # return GeJu, GeJuInfoLs, inDoubtFlag


def isDeLing(RG, YZ, isInJi):
    wuxing, C_ = getTianGanWuXing(RG)
    wuxing_YZ, C_ = getDiZhiWuXing(YZ)
    for k in ['长生', '沐浴', '冠带', '临官', '帝旺'][::-1]:
    # for k in ['长生', '临官', '帝旺', '衰', '墓'][::-1]:
    # for k in ['长生', '临官', '帝旺'][::-1]:
        if C_ShiErChangSheng[RG][k] == YZ:
            return True, [YZ, wuxing_YZ, k]
    # wangshi = C_WuXingSiShi[wuxing]['旺']
    # if wangshi == '季':
    #     if isInJi:
    #         return True, [YZ, wuxing_YZ, '旺']
    #     else:
    #         return False, None
    # siji = C_DiZhiSiJi[wangshi]
    # if YZ in siji:
    #     return True, [YZ, wuxing_YZ, '旺']
    # xiangshi = C_WuXingSiShi[wuxing]['相']
    # if xiangshi == '季':
    #     if isInJi:
    #         return True, [YZ, wuxing_YZ, '相']
    #     else:
    #         return False, None
    # siji = C_DiZhiSiJi[xiangshi]
    # if YZ in siji:
    #     return True, [YZ, wuxing_YZ, '相']
    return False, None


def isDeDi(RG, dizhis):
    D = {}
    # if RG in ['戊', '己']:
    #     pass
    if True:
        if RG in C_YangTianGan:
            keys = ['帝旺', '临官', '长生', '墓', '衰']
        else:
            keys = ['临官', '帝旺', '死', '养', '冠带']
        for k in keys:
            D[C_ShiErChangSheng[RG][k]] = k
        # changsheng = C_ShiErChangSheng[RG]['长生']
        # lu = C_ShiErChangSheng[RG]['临官']
        #
        # D = {
        #     changsheng: '长生',
        #     lu: '禄'
        # }
        # if RG in C_YangTianGan:
        #     yangren = C_ShiErChangSheng[RG]['帝旺']
        #     D.update({yangren: '羊刃'})
        NZ, RZ, SZ = dizhis[0], dizhis[2], dizhis[3]
        DiInfo = {}
        for i in [NZ, RZ, SZ]:
            if i in D:
                wuxing, C_ = getDiZhiWuXing(i)
                k = D[i]
                if k not in DiInfo:
                    DiInfo[k] = [[i, wuxing]]
                else:
                    DiInfo[k].append([i, wuxing])
    return len(DiInfo) > 0, DiInfo


def isDeShi(tiangans, dizhis):
    wuxing_tiangan = []
    wuxing_dizhi = []
    for G in tiangans:
        GWX, C_ = C_getWuXing(C_WuXingTianGan, G)
        wuxing_tiangan.append(GWX)
    RGWX = wuxing_tiangan.pop(-2)
    wuxing_tiangan.insert(-1, '')
    for Z in dizhis:
        ZWX, C_ = C_getWuXing(C_WuXingDiZhi, Z)
        wuxing_dizhi.append(ZWX)

    for k in C_WuXingSheng:
        if C_WuXingSheng[k] == RGWX:
            SRGWX = k
            break
    valid_keys = [RGWX, SRGWX]
    ZhuInfo = []
    ShengInfo = []
    for idx, WX in enumerate(wuxing_tiangan):
        if WX == RGWX:
            G = tiangans[idx]
            ZhuInfo.append([G] + getTianGanWuXing(G))
        elif WX == SRGWX:
            G = tiangans[idx]
            ShengInfo.append([G] + getTianGanWuXing(G))
    for idx, WX in enumerate(wuxing_dizhi):
        if WX == RGWX:
            Z = dizhis[idx]
            ZhuInfo.append([Z] + getDiZhiWuXing(Z))
        elif WX == SRGWX:
            G = tiangans[idx]
            ShengInfo.append([G] + getTianGanWuXing(G))
    return len(ZhuInfo) > 1, ZhuInfo, len(ShengInfo) > 1, ShengInfo


def isStrong(DeLing, DeDi, DeZhu, DeSheng):
    if DeLing:
        if DeDi and DeZhu and DeSheng:
            return '过旺'
        if DeDi + DeZhu + DeSheng == 2:
            return '偏旺'
        if DeDi + DeZhu + DeSheng == 1:
            return '身旺'
        if DeDi + DeZhu + DeSheng == 0:
            return '平衡'
    else:
        if DeDi and DeZhu and DeSheng:
            return '身旺'
        if DeDi + DeZhu + DeSheng == 2:
            return '平衡'
        if DeDi + DeZhu + DeSheng == 1:
            return '身弱'
        if DeDi + DeZhu + DeSheng == 0:
            return '过弱'
    # if DeLing and DeDi and DeShi:
    #     return '最强'
    # elif DeLing and DeShi:
    #     return '极强'
    # elif DeLing and DeDi:
    #     return '极强'
    # elif DeShi:
    #     return '中强'
    # elif DeDi:
    #     return '次强'
    # elif DeLing and not DeDi:
    #     return '次弱'
    # elif DeLing and not DeShi:
    #     return '中弱'
    # else:
    #     return '最弱'


def isYongShenExists(body, tiangans, dizhis):
    wuxing_tiangan = []
    wuxing_dizhi = []
    for G in tiangans:
        GWX, C_ = C_getWuXing(C_WuXingTianGan, G)
        wuxing_tiangan.append(GWX)
    RGWX = wuxing_tiangan.pop(-2)
    wuxing_tiangan.insert(-1, '')
    for Z in dizhis:
        ZWX, C_ = C_getWuXing(C_WuXingDiZhi, Z)
        wuxing_dizhi.append(ZWX)
    if '弱' in body:
        for k in C_WuXingSheng:
            if C_WuXingSheng[k] == RGWX:
                SRGWX = k
                break
        valid_keys = [RGWX, SRGWX]
    else:

        for k in C_WuXingKe:
            if C_WuXingKe[k] == RGWX:
                KRGWX = k
                break
        valid_keys = [KRGWX, C_WuXingSheng[RGWX], C_WuXingKe[RGWX]]

    YongShen = []
    for idx, WX in enumerate(wuxing_tiangan):
        if WX in valid_keys:
            G = tiangans[idx]
            YongShen.append([G] + getTianGanWuXing(G))
    for idx, WX in enumerate(wuxing_dizhi):
        if WX in valid_keys:
            Z = dizhis[idx]
            YongShen.append([Z] + getDiZhiWuXing(Z))
    return len(YongShen) > 0, YongShen, valid_keys


def isSanQi(tiangans):
    SanQi = isTripletInDict(tiangans[:-1][::-1], C_SanQi, False)
    t = None
    if len(SanQi) == 0:
        SanQi = isTripletInDict(tiangans[:-1], C_SanQi, False)
        if len(SanQi) > 0:
            t = '富'
    else:
        t = '贵'
    if t is None:
        return False, None
    else:
        sanqi = list(SanQi[0])
        return True, [Format(sanqi[:-1], sep='⋅', color_idx=None, align=None), sanqi[-1], t]

def isKuiGang(bazi):
    RGZ = bazi[4:6]
    for item in C_KuiGang:
        if RGZ == item:
            return True
    return False


# 合盘
def getTianGanRelation(M, F):
    if (M, F) in C_TianGanWuHe or (F, M) in C_TianGanWuHe:
        return '合'
    if M == F:
        return '比合'
    if (M, F) in C_TianGanSiChong or (F, M) in C_TianGanSiChong:
        return '冲'
    return '无'


def getDiZhiRelation(M, F):
    if (M, F) in C_DiZhiLiuHe or (F, M) in C_DiZhiLiuHe:
        return '合'
    if (M, F) in C_DiZhiSanAnHe or (F, M) in C_DiZhiSanAnHe:
        return '暗合'
    if (M, F) in C_DiZhiBanHuiFang or (F, M) in C_DiZhiBanHuiFang:
        return '半合'
    if M == F:
        return '比合'
    if (M, F) in C_DiZhiLiuChong or (F, M) in C_DiZhiLiuChong:
        return '冲'
    if (M, F) in C_DiZhiSiXing or (F, M) in C_DiZhiLiuChong:
        return '刑'
    if (M, F) in C_DiZhiLiuHai or (F, M) in C_DiZhiLiuHai:
        return '害'
    if (M, F) in C_DiZhiLiuPo or (F, M) in C_DiZhiLiuPo:
        return '破'
    return '无'



def getNaYinRelation(mZhu, fZhu):
    mNaYin = C_NaYin[mZhu]
    fNaYin = C_NaYin[fZhu]
    mNaYinWuXing = mNaYin[-1]
    fNaYinWuXing = fNaYin[-1]
    return mNaYin, fNaYin, C_NNayinHeHui[mNaYinWuXing][fNaYinWuXing]


def isShun(year, month, day, gender):
    info = sxtwl.fromSolar(year, month, day)
    yGZ = info.getYearGZ(True)
    yZ = C_DiZhi[yGZ.dz]

    return not ((gender == '男') ^ C_WuXingDiZhi[yZ][1])

def getQiYunNianYue(year, month, day, isShunFlag):
    info = sxtwl.fromSolar(year, month, day)
    mGZ = info.getMonthGZ()
    mZ = C_DiZhi[mGZ.dz]
    diff = -1
    while True:
        if C_DiZhi[info.getMonthGZ().dz] != mZ:
            break
        diff += 1
        if isShunFlag:
            info = info.after(1)
        else:
            info = info.before(1)
    qiYunDiffNian = diff // 3
    qiYunDiffYue = (diff % 3) * 4
    month += qiYunDiffYue
    year += qiYunDiffNian
    return qiYunDiffNian, qiYunDiffYue, year, month, day

def getNextTianGan(tiangan):
    return C_TianGan[(C_TianGan.index(tiangan) + 1) % len(C_TianGan)]

def getNextDizhi(dizhi):
    return C_DiZhi[(C_DiZhi.index(dizhi) + 1) % len(C_DiZhi)]

def getPreTianGan(tiangan):
    return C_TianGan[(C_TianGan.index(tiangan) + 9) % len(C_TianGan)]

def getPreDizhi(dizhi):
    return C_DiZhi[(C_DiZhi.index(dizhi) + 11) % len(C_DiZhi)]

def getLiChunYueGZ(year):
    info = sxtwl.fromSolar(year, 12, 31)
    while True:
        if info.hasJieQi():
            JQ = C_JQMC[info.getJieQi()]
            if JQ == '立春':
                mGZ = info.getMonthGZ()
                LiuYueG = C_TianGan[mGZ.tg]
                LiuYueZ = C_DiZhi[mGZ.dz]
                break
        info = info.before(1)
    return LiuYueG, LiuYueZ

def isInShengZhengKu(dizhis, dayuanZ, liunianZ):
    for i in range(len(dizhis)):
        for j in range(i+1, len(dizhis)):
            dizhi1 = dizhis[i]
            dizhi2 = dizhis[j]
            k = tuple(sorted([dizhi1, dizhi2, dayuanZ, liunianZ]))
            if len(set(k)) != 4:
                continue
            if k in C_ShengZhengKu:
                return (k, C_ShengZhengKu[k])
    for i in range(len(dizhis)):
        for j in range(i+1, len(dizhis)):
            for k in range(j+1, len(dizhis)):
                dizhi1 = dizhis[i]
                dizhi2 = dizhis[j]
                dizhi3 = dizhis[k]
                k1 = tuple(sorted([dizhi1, dizhi2, dizhi3, liunianZ]))
                k2 = tuple(sorted([dizhi1, dizhi2, dizhi3, dayuanZ]))
                if len(set(k1)) == 4 and k1 in C_ShengZhengKu:
                    return (k1, C_ShengZhengKu[k1])
                if len(set(k2)) == 4 and k2 in C_ShengZhengKu:
                    return (k2, C_ShengZhengKu[k2])

    return None

def getDaYun(year, month, day, gender, dizhis):
    # 正排逆排
    isShunFlag = isShun(year, month, day, gender)
    # 起运时间
    qiYunDiffNian, qiYunDiffYue, qiYunNian, qiYunYue, qiYueRi = getQiYunNianYue(year, month, day, isShunFlag)
    QiYunNian = qiYunDiffNian + int(qiYunDiffYue > 6)
    # 大运开始的干支
    info = sxtwl.fromSolar(year, month, day)

    mGZ = info.getMonthGZ()
    DaYunG = C_TianGan[mGZ.tg]
    DaYunZ = C_DiZhi[mGZ.dz]

    yGZ = info.getYearGZ(True)
    LiuNianG = C_TianGan[yGZ.tg]
    LiuNianZ = C_DiZhi[yGZ.dz]

    dGZ = info.getDayGZ()
    RG = C_TianGan[dGZ.tg]

    DaYunLiuNianInfo = {}
    SiZhengShengKuInfo = []
    s = 1
    ckey_reg = '{}~{}岁'
    info_dayun_years = [(s, max(s, QiYunNian))] + [(s, s + 9) for s in range(QiYunNian + 1, QiYunNian + 1 + 90, 10)]
    for idx, (s, e) in enumerate(info_dayun_years):
        ckey = (ckey_reg.format(s, e), str(year + s - 1))
        if idx == 0:
            ganshen = '小'
            zhishen = '运'
        else:
            canggan = getCangGan(DaYunZ)[0]
            ganshen = getShiShen(RG, DaYunG)[0]
            zhishen = getShiShen(RG, canggan)[0]
        k1 = ((DaYunG, ganshen), (DaYunZ, zhishen))
        DaYunLiuNianInfo[ckey] = {k1: {}}
        for i in range(s, e + 1):
            canggan = getCangGan(LiuNianZ)[0]
            ganshen = getShiShen(RG, LiuNianG)[0]
            zhishen = getShiShen(RG, canggan)[0]
            k2 = ((LiuNianG, ganshen), (LiuNianZ, zhishen), str(i)+'岁', str(year + i - 1))
            DaYunLiuNianInfo[ckey][k1][k2] = []
            LiuYueG, LiuYueZ = getLiChunYueGZ(year + i - 1)
            isInInfo = isInShengZhengKu(dizhis, DaYunZ, LiuNianZ)
            if isInInfo is not None:
                SiZhengShengKuInfo.append([isInInfo, str(i)+'岁',  str(year + i - 1)])
            for j in range(12):
                canggan = getCangGan(LiuYueZ)[0]
                ganshen = getShiShen(RG, LiuYueG)[0]
                zhishen = getShiShen(RG, canggan)[0]
                DaYunLiuNianInfo[ckey][k1][k2].append(((LiuYueG, ganshen), (LiuYueZ, zhishen)))
                LiuYueG = getNextTianGan(LiuYueG)
                LiuYueZ = getNextDizhi(LiuYueZ)
            if QiYunNian == 0 and idx == 0:
                continue
            LiuNianG = getNextTianGan(LiuNianG)
            LiuNianZ = getNextDizhi(LiuNianZ)
        if isShunFlag:
            DaYunG = getNextTianGan(DaYunG)
            DaYunZ = getNextDizhi(DaYunZ)
        else:
            DaYunG = getPreTianGan(DaYunG)
            DaYunZ = getPreDizhi(DaYunZ)
    return qiYunNian, qiYunYue, qiYueRi, qiYunDiffNian, qiYunDiffYue, DaYunLiuNianInfo, SiZhengShengKuInfo








