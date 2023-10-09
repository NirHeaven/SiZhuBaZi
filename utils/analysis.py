from .constant import *
import itertools as it

import sxtwl

def getGanZhi(year, month, day, hour):

    day = sxtwl.fromSolar(year, month, day)
    yTG = day.getYearGZ(True)
    mTG = day.getMonthGZ()
    dTG = day.getDayGZ()
    hTG = sxtwl.getShiGz(dTG.tg, hour)
    isInJi = False
    for i in range(18):
        if day.hasJieQi():
            JQ = JQMC[day.getJieQi()]
            if JQ in ['立春', '立夏', '立秋', '立冬']:
                isInJi = True
                break
        day = day.after(1)
    return [TianGan[yTG.tg], DiZhi[yTG.dz], TianGan[mTG.tg], DiZhi[mTG.dz], TianGan[dTG.tg], DiZhi[dTG.dz], TianGan[hTG.tg], DiZhi[hTG.dz]], isInJi

def _getShiShen(wuxingA, yinyangA, wuxingB, yinyangB):
    # 印
    ShiShenName, ShiShenAlias = '', ''
    if WuXingSheng[wuxingB] == wuxingA:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '正印', '印'
        else:
            ShiShenName, ShiShenAlias = '偏印', '枭'
    # 食伤
    elif WuXingSheng[wuxingA] ==  wuxingB:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '伤官', '伤'
        else:
            ShiShenName, ShiShenAlias = '食神', '食'
    # 财
    elif WuXingKe[wuxingA] == wuxingB:
        if yinyangA != yinyangB:
            ShiShenName, ShiShenAlias = '正财', '才'
        else:
            ShiShenName, ShiShenAlias = '偏财', '财'
    # 官杀
    elif WuXingKe[wuxingB] == wuxingA:
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
def getShiShen(tianganA, tianganB, flag=False):
    if flag and tianganA == tianganB:
        return ['身主']
    wuxingA, yinyangA = WuXingTianGan[tianganA]
    wuxingB, yinyangB = WuXingTianGan[tianganB]
    return _getShiShen(wuxingA, yinyangA, wuxingB, yinyangB)[:2]


def _getWuXing(D, K):
    wuxing, yiyang = D[K]
    yiyang = '阳' if yiyang else '阴'
    return [wuxing, yiyang]

def getTianGanWuXing(tiangan):
    return _getWuXing(WuXingTianGan, tiangan)

def getDiZhiWuXing(dizhi):
    return _getWuXing(WuXingDiZhi, dizhi)


def getCangGan(dizhi):
    return list(DiZhiCangGan[dizhi])


def isPairInDict(keys, D):
    results = set()
    n = len(keys)
    for i in range(n-1):
        k1 = keys[i]
        for j in range(i+1, n):
            k2 = keys[j]
            for item in it.permutations([k1, k2]):
                t_item = tuple(item)
                if t_item in D:
                    results.add(t_item + (D[t_item], ))
    return list(results)


def isTripletInDict(keys, D):
    results = set()
    n = len(keys)
    for i in range(n-2):
        k1 = keys[i]
        for j in range(i+1, n-1):
            k2 = keys[j]
            for k in range(j+1, n):
                k3 = keys[k]
                for item in it.permutations([k1, k2, k3]):
                    t_item = tuple(item)
                    if t_item in D:
                        results.add(t_item + (D[t_item], ))
    return list(results)


def replaceNoneByKey(datas, key):
    rdata = []
    for item in datas:
        item = list(item)
        if item[-1] is None:
            item[-1] = key
        rdata.append(item)
    return rdata

def getTianGanHeChong(tiangans):
    He = isPairInDict(tiangans, TianGanWuHe)
    Chong = isPairInDict(tiangans, TianGanSiChong)
    He = replaceNoneByKey(He, '合')
    Chong = replaceNoneByKey(Chong, '冲')
    return He, Chong


def getDiZhiHeChongXingHai(dizhis):
    He = isPairInDict(dizhis, DiZhiLiuHe)
    Chong = isPairInDict(dizhis, DiZhiLiuChong)
    Hai = isPairInDict(dizhis, DiZhiLiuHai)
    Xing = isPairInDict(dizhis, DiZhiSiXing)
    He = replaceNoneByKey(He, '合')
    Chong = replaceNoneByKey(Chong, '冲')
    Hai = replaceNoneByKey(Hai, '害')
    Xing = replaceNoneByKey(Xing, '刑')

    return He, Chong, Hai, Xing


def getDiZhiHuiFang(dizhis):
    return isTripletInDict(dizhis, DiZhiSiHuiFang)


def getDiZhiHuiJu(dizhis):
    HuiJu = isTripletInDict(dizhis, DiZhiWuHuiJu)
    BanHuiJu = isPairInDict(dizhis, DiZhiBanHuiJu)
    return HuiJu, BanHuiJu


def isDeLing(RG, YZ, isInJi):
    wuxing, _ = getTianGanWuXing(RG)
    wuxing_YZ, _ = getDiZhiWuXing(YZ)
    wangshi = WuXingSiShi[wuxing]['旺']
    if wangshi == '季':
        if isInJi:
            return True, [YZ, wuxing_YZ, '旺']
        else:
            return False, None
    siji = DiZhiSiJi[wangshi]
    if YZ in siji:
        return True, [YZ, wuxing_YZ, '旺']
    xiangshi = WuXingSiShi[wuxing]['相']
    if xiangshi == '季':
        if isInJi:
            return True,[YZ, wuxing_YZ, '相']
        else:
            return False, None
    siji = DiZhiSiJi[xiangshi]
    if YZ in siji:
        return True, [YZ, wuxing_YZ, '相']
    return False, None


def isDeDi(RG, dizhis):
    changsheng = ShiErChangSheng[RG]['长生']
    lu = ShiErChangSheng[RG]['临官']
    yangren = ShiErChangSheng[RG]['帝旺']
    D = {
        changsheng: '长生',
        lu: '禄',
        yangren: '羊刃',
    }
    NZ, YZ, SZ = dizhis[0], dizhis[1], dizhis[3]
    DiInfo = {}
    for i in [NZ, YZ, SZ]:
        if i in D:
            wuxing, _ = getDiZhiWuXing(i)
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
        GWX, _ = _getWuXing(WuXingTianGan, G)
        wuxing_tiangan.append(GWX)
    RGWX = wuxing_tiangan.pop(-2)
    wuxing_tiangan.insert(-1, '')
    for Z in dizhis:
        ZWX, _ = _getWuXing(WuXingDiZhi, Z)
        wuxing_dizhi.append(ZWX)

    for k in WuXingSheng:
        if WuXingSheng[k] == RGWX:
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
        GWX, _ = _getWuXing(WuXingTianGan, G)
        wuxing_tiangan.append(GWX)
    RGWX = wuxing_tiangan.pop(-2)
    wuxing_tiangan.insert(-1, '')
    for Z in dizhis:
        ZWX, _ = _getWuXing(WuXingDiZhi, Z)
        wuxing_dizhi.append(ZWX)
    if '弱' in body:
        for k in WuXingSheng:
            if WuXingSheng[k] == RGWX:
                SRGWX = k
                break
        valid_keys = [RGWX, SRGWX]
    else:

        for k in WuXingKe:
            if WuXingKe[k] == RGWX:
                KRGWX = k
                break
        valid_keys = [KRGWX, WuXingSheng[RGWX], WuXingKe[RGWX]]

    YongShen = []
    for idx, WX in enumerate(wuxing_tiangan):
        if WX in valid_keys:
            G = tiangans[idx]
            YongShen.append([G] + getTianGanWuXing(G))
    for idx, WX in enumerate(wuxing_dizhi):
        if WX in valid_keys:
            Z = dizhis[idx]
            YongShen.append([Z] + getDiZhiWuXing(Z))
    return len(YongShen) > 0, YongShen










