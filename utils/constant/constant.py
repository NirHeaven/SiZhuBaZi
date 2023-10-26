
C_JQMC = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]


C_ZHU = {
    0: '年',
    1: '月',
    2: '日',
    3: '时'
}

C_DayPerMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


C_SanQi = {
    ('甲', '戊', '庚'): '天上三奇',
    ('乙', '丙', '丁'): '地上三奇',
    ('壬', '癸', '辛'): '人中三奇',
}

C_KuiGang = ['庚辰', '壬辰', '庚戌', '戊戌']

C_GeJu = {
    '正官格': {
        '优': '稳重，正直，负责，重纪律',
        '劣': '不积极，保守，优柔寡断',
        '成': '身强见财，身弱见印',
        '破': '见伤官，无印克制',
        '备注': '身强方能驭财；逢官看财'
    },
    '正财格': {
        '优': '安分守己，刻苦耐劳，惜金，节俭，守信，对家庭负责',
        '劣': '吝啬，做事虎头蛇尾，憨直',
        '成': '身强见食，身弱见官',
        '破': '见比， 财轻比重',
        '备注': '身强方能驭财；逢财看杀'
    },
    '正印格': {
        '优': '宽厚仁慈，重名誉，讲人情，追求学问，自远小人，易接近宗教',
        '劣': '依赖心重，思想不切实际，不善察言观色，死要面子',
        '成': '身旺印多，需财伐印',
        '破': '印轻逢财，在杀生印的情况下更忌',
        '备注': '逢印看官'
    },
    '食神格': {
        '优': '聪明，温和，举止儒雅，思想脱俗，感性，喜文艺，计长远，擅烹饪',
        '劣': '易疲劳，喜幻想，喜无拘无束，内心易感空虚，自命不凡，易发胖，肠胃弱反消瘦，',
        '成': '身旺，只许一位，喜财',
        '破': '见偏印',
        '备注': ''
    },
    '七杀格': {
        '优': '进取，果断，嫉恶如仇，创新，领导',
        '劣': '偏激，易猜忌，粗鲁，阴沉好杀，酒色',
        '成': '食神制杀；喜印，身弱杀旺尤甚',
        '破': '逢财无制',
        '备注': '有杀先论杀，无杀始论用；逢杀看印'
    },
    '偏财格': {
        '优': '精力充沛，不折不挠，豪迈慷慨，做事速战速决',
        '劣': '不珍惜金钱，圆滑，易得金钱和女人，也易失去',
        '成': '身强见食，身弱见官',
        '破': '众人之财，怕比劫分夺，需官星',
        '备注': '非妻所带，众人之财也；偏财身旺方能驭财，趋求商贾之人'
    },
    '偏印格': {
        '优': '悟性，洞察，好学，喜创造，喜怒不形于色，与异性安全感',
        '劣': '缺乏耐心，多学少成，内向多疑，孤僻，过多则与家人无缘',
        '成': '身强喜财，以财克偏印，但会弃祖业',
        '破': '偏印克食神，食神为善，因此忌见食神',
        '备注': '弃印就财，舍轻用重'
    },
    '伤官格': {
        '优': '多才，长相秀丽，悟性强，追求完美，独裁倔强，易成为奇迹似的英雄人物',
        '劣': '博而不精，易恃才傲物，为达目的不择手段，好管闲事，财难平衡。男应注意克制私欲，女应注意内外兼修',
        '成': '见印, 身强喜财',
        '破': '见官，日主火土尤甚，金木水可不忌',
        '备注': '务要伤尽; 旺者用财，弱者用印'
    },

    '建禄格': {
        '优': '意志坚定，自尊自信，乐观，明分寸，知进退，重情义但很自我',
        '劣': '以自我为中心，固执己见，知心朋友少，对部署和亲人严厉刻薄',
        '成': '半成格，需见官，喜财',
        '破': '无财官透杀印',
        '备注': '',
    },
    '羊刃格': {
        '优': '个性强而突出，口才好，应变力强，能在社交场合制造气氛',
        '劣': '脾气执拗，野心大，不服输，嫉妒，双重性格，不善理财，对妻子不够体贴，劫财多则行事粗鲁',
        '成': '半成格，需见杀',
        '破': '无官杀',
        '备注': '羊刃架杀'
    },
}
C_ShengZhengKuL = {
    ('寅', '申', '巳', '亥'): '四生',
    ('子', '午', '卯', '酉'): '四正',
    ('辰', '戌', '丑', '未'): '四库',
}
C_ShengZhengKu = {}
for k in C_ShengZhengKuL:
    C_ShengZhengKu[tuple(sorted(list(k)))] = C_ShengZhengKuL[k]