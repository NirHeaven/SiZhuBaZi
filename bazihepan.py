
from utils import *

def baziAnalysis(m_info=None, f_info=None, m_bazi=None, f_bazi=None):
    if m_bazi is None:
        m_year, m_month, m_day, m_hour, m_minute, m_zone = m_info
        m_bazi, m_isInJi = getGanZhi(m_year, m_month, m_day, m_hour, m_minute, m_zone)
    if f_bazi is None:
        f_year, f_month, f_day, f_hour, f_finute, f_zone = f_info
        f_bazi, f_isInJi = getGanZhi(f_year, f_month, f_day, f_hour, f_finute, f_zone)

    mNZ, mYZ, mRG, mRZ, mSZ = m_bazi[1], m_bazi[3], m_bazi[4], m_bazi[5], m_bazi[7]
    fNZ, fYZ, fRG, fRZ, fSZ = f_bazi[1], f_bazi[3], f_bazi[4], f_bazi[5], f_bazi[7]
    mSX = C_ShengXiaoEmoji[C_DiZhi.index(mNZ)]
    fSX = C_ShengXiaoEmoji[C_DiZhi.index(fNZ)]

    # 十二生肖是否入对日支
    MIsFSXBeiWei = getDiZhiRelation(mNZ, fRZ)
    FIsMSXBeiWei = getDiZhiRelation(fNZ, mRZ)

    # 十二生肖合克
    SXRelation = getDiZhiRelation(mNZ, fNZ)

    # 日主关系
    RGRelation = getTianGanRelation(mRG, fRG)

    # 夫妻宫关系
    RZRelation = getDiZhiRelation(mRZ, fRZ)

    # 年纳音关系
    MNayin, FNayin, NNaYinRelation = getNaYinRelation(m_bazi[:2], f_bazi[:2])

    # 晚年关系
    SZRelation = getDiZhiRelation(mSZ, fSZ)

    format_mbazi = [mSX + '  ' + Format(list(map(lambda a: Format(a, sep='', align=None), m_bazi)), n=2, sep='||', align=None)]
    format_fbazi = [fSX + '  ' + Format(list(map(lambda a: Format(a, sep='', align=None), f_bazi)), n=2, sep='||', align=None)]
    format_mshengxiaoruwei = [
        Format([mNZ, '(', mSX, ')'], sep='', color_idx=0, align=None) + Format([fRZ], sep='', color_idx=0,
                                                                               align=None) + '⋅' + MIsFSXBeiWei]
    format_fshengxiaoruwei = [
        Format([fNZ, '(', fSX, ')'], sep='', color_idx=0, align=None) + Format([mRZ], sep='', color_idx=0,
                                                                               align=None) + '⋅' + FIsMSXBeiWei]
    format_shengxiaoheke = [
        Format([mNZ, '(', mSX, ')'], sep='', color_idx=0, align=None) + Format([fNZ, '(', fSX, ')'], sep='', color_idx=0,
                                                                               align=None) + '⋅' + SXRelation]

    format_rizhurelation =[
        Format([mRG], sep='', color_idx=0, align=None) + Format([fRG], sep='', color_idx=0, align=None) + '⋅' + RGRelation]

    format_fuqirelation = [
        Format([mRZ], sep='', color_idx=0, align=None) + Format([fRZ], sep='', color_idx=0, align=None) + '⋅' + RZRelation]

    format_mnayin = [Format(MNayin, color_idx=2)]
    format_fnayin = [Format(FNayin, color_idx=2)]
    format_nayinrelation = [NNaYinRelation]

    format_wannianrelation = [
        Format([mSZ], sep='', color_idx=0, align=None) + Format([fSZ], sep='', color_idx=0, align=None) + '⋅' + SZRelation]
    print_str = [
        ['=================================================================='],
        ['男主'] + format_mbazi + format_mnayin,
        ['女主'] + format_fbazi + format_fnayin,
        ['------------------------------------------------------------------'],
        ['男入女位'] + format_mshengxiaoruwei,
        ['女入男位'] + format_fshengxiaoruwei,
        ['生肖合克'] + format_shengxiaoheke,
        ['------------------------------------------------------------------'],
        ['日主'] + format_rizhurelation,
        ['------------------------------------------------------------------'],
        ['夫妻宫'] + format_fuqirelation,
        ['------------------------------------------------------------------'],
        # ['年纳音'] + format_nayinrelation,
        # ['------------------------------------------------------------------'],
        ['晚年关系'] + format_wannianrelation,
        ['------------------------------------------------------------------'],
        ['备注：无代表没有合冲刑亥']
    ]
    for idx, s in enumerate(print_str):
        print(Format(list(map(lambda a:Format(a, sep='', align_w=12, color_idx=None), s)), sep='    ', color_idx=None))
        pass

if __name__ == '__main__':
    # baziAnalysis([1993, 5, 13, 19, 5, '襄樊'], f_bazi='甲戌丙子己丑丁卯')
    baziAnalysis(m_bazi='癸酉乙卯丙申甲午', f_bazi='己卯乙亥丁亥甲辰')
    # baziAnalysis(m_bazi='丙子丙申乙酉戊寅', f_bazi='乙亥丙戌丁酉丁未')


