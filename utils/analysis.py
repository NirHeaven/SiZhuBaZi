import itertools as it
from .formater import *
from .constant import *
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
    yTG = info.getYearGZ(True)
    mTG = info.getMonthGZ()
    dTG = info.getDayGZ()
    hTG = sxtwl.getShiGz(dTG.tg, hour)
    isInJi = False
    for i in range(18):
        if info.hasJieQi():
            JQ = C_JQMC[info.getJieQi()]
            if JQ in ['立春', '立夏', '立秋', '立冬']:
                isInJi = True
                break
        info = info.after(1)
    return EmptyFormat([C_TianGan[yTG.tg], C_DiZhi[yTG.dz],
            C_TianGan[mTG.tg], C_DiZhi[mTG.dz],
            C_TianGan[dTG.tg], C_DiZhi[dTG.dz],
            C_TianGan[hTG.tg], C_DiZhi[hTG.dz]]), isInJi

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


def getDiZhiHuiFang(dizhis):
    return isTripletInDict(dizhis, C_DiZhiSiHuiFang)


def getDiZhiHuiJu(dizhis):
    HuiJu = isTripletInDict(dizhis, C_DiZhiWuHuiJu)
    BanHuiJu = isPairInDict(dizhis, C_DiZhiBanHuiJu)
    insertValueByIndex(HuiJu, -1, '合')
    insertValueByIndex(BanHuiJu, -1, '半合')
    return HuiJu, BanHuiJu

def getGeJu(baizi):
    YZ = baizi[3]
    RG = baizi[4]
    GeJuGanShen = []
    GeJuGanShenTianGan = []
    YZCG = getCangGan(YZ)
    wuxingRG, yinyangRG = getTianGanWuXing(RG)
    inDoubtFlag = False
    if C_ShiErChangSheng[RG]['帝旺'] == YZ and RG in C_YangTianGan:
        GeJuGanShen = '羊刃'
    elif C_ShiErChangSheng[RG]['临官'] == YZ:
        GeJuGanShen = '建禄'
    else:
        for canggan in YZCG:
            canggan_wuxing, canggang_yinyang = getTianGanWuXing(canggan)
            tiangan_wo_RG = baizi[::2]
            tiangan_wo_RG = tiangan_wo_RG[0] + tiangan_wo_RG[1] + tiangan_wo_RG[3]
            for tiangan in tiangan_wo_RG:
                wuxing, yiyang = getTianGanWuXing(tiangan)
                if wuxing == canggan_wuxing:
                    GanShen = getShiShen(RG, tiangan)
                    if GanShen[0] in ['比肩', '劫财']:
                        continue
                    GeJuGanShen.append(getShiShen(RG, tiangan))
                    GeJuGanShenTianGan.append((tiangan, yiyang, yiyang==canggang_yinyang))
        if len(GeJuGanShen) == 0:
            GeJuGanShen = None
        elif len(GeJuGanShen) == 1:
            GeJuGanShen = GeJuGanShen[0][0]
        else:
            t_idx = 0
            for idx in range(len(GeJuGanShenTianGan)):
                if GeJuGanShenTianGan[idx][-1]:
                    t_idx = idx
                    break
            GeJuGanShen = GeJuGanShen[t_idx][0]
        if GeJuGanShen is None:
            result = getDiZhiHuiFang(baizi[1::2])
            if len(result) == 0:
                result, _ = getDiZhiHuiJu(baizi[1::2])
            if len(result) != 0:
                assert len(result) == 1
                for Z in result[0]:
                    if YZ == Z:
                        _, yinyang = getDiZhiWuXing(YZ)
                        wuxing = result[0][-1]
                        GeJuGanShen = C_getShiShen(wuxingRG, yinyangRG, wuxing, yinyang)[0]
                        break
        if GeJuGanShen is None:
            benqi = YZCG[0]
            benqi_wuxing, benqi_yinyang = getTianGanWuXing(benqi)
            GeJuGanShen = C_getShiShen(wuxingRG, yinyangRG, benqi_wuxing, benqi_yinyang)[0]
            inDoubtFlag = True

    GeJu = GeJuGanShen + '格'
    GeJuInfo = C_GeJu[GeJu]
    GeJuInfoLs = []
    for k, v in GeJuInfo.items():
        GeJuInfoLs.append([k, v])
    return GeJu, GeJuInfoLs, inDoubtFlag


def isDeLing(RG, YZ, isInJi):
    wuxing, C_ = getTianGanWuXing(RG)
    wuxing_YZ, C_ = getDiZhiWuXing(YZ)
    wangshi = C_WuXingSiShi[wuxing]['旺']
    if wangshi == '季':
        if isInJi:
            return True, [YZ, wuxing_YZ, '旺']
        else:
            return False, None
    siji = C_DiZhiSiJi[wangshi]
    if YZ in siji:
        return True, [YZ, wuxing_YZ, '旺']
    xiangshi = C_WuXingSiShi[wuxing]['相']
    if xiangshi == '季':
        if isInJi:
            return True, [YZ, wuxing_YZ, '相']
        else:
            return False, None
    siji = C_DiZhiSiJi[xiangshi]
    if YZ in siji:
        return True, [YZ, wuxing_YZ, '相']
    return False, None


def isDeDi(RG, dizhis):
    changsheng = C_ShiErChangSheng[RG]['长生']
    lu = C_ShiErChangSheng[RG]['临官']

    D = {
        changsheng: '长生',
        lu: '禄'
    }
    if RG in C_YangTianGan:
        yangren = C_ShiErChangSheng[RG]['帝旺']
        D.update({yangren: '羊刃'})
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
    ShiInfo = []
    for idx, WX in enumerate(wuxing_tiangan):
        if WX in valid_keys:
            G = tiangans[idx]
            ShiInfo.append([G] + getTianGanWuXing(G))
    for idx, WX in enumerate(wuxing_dizhi):
        if WX in valid_keys:
            Z = dizhis[idx]
            ShiInfo.append([Z] + getDiZhiWuXing(Z))
    return len(ShiInfo) > 1, ShiInfo


def isStrong(DeLing, DeDi, DeShi):
    if DeLing and DeDi and DeShi:
        return '最强'
    elif DeLing and DeShi:
        return '极强'
    elif DeLing and DeDi:
        return '极强'
    elif DeShi:
        return '中强'
    elif DeDi:
        return '次强'
    elif DeLing and not DeDi:
        return '次弱'
    elif DeLing and not DeShi:
        return '中弱'
    else:
        return '最弱'


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
    if (M, F) in C_DiZhiBanHuiJu or (F, M) in C_DiZhiBanHuiJu:
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









