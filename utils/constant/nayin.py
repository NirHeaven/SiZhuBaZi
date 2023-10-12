
C_NaYinD = {
    '海中金': ['甲子', '乙丑'],
    '炉中火': ['丙寅', '丁卯'],
    '大林木': ['戊辰', '己巳'],
    '路旁土': ['庚午', '辛未'],
    '剑锋金': ['壬申', '癸酉'],
    '山头火': ['甲戌', '乙亥'],
    '涧下水': ['丙子', '丁丑'],
    '城头土': ['戊寅', '己卯'],
    '白蜡金': ['庚辰', '辛巳'],
    '杨柳木': ['壬午', '癸未'],
    '泉中水': ['甲申', '乙酉'],
    '屋上土': ['丙戌', '丁亥'],
    '霹雳火': ['戊子', '己丑'],
    '松柏木': ['庚寅', '辛卯'],
    '长流水': ['壬辰', '癸巳'],
    '沙中金': ['甲午', '乙未'],
    '山下火': ['丙申', '丁酉'],
    '平地木': ['戊戌', '己亥'],
    '壁上土': ['庚子', '辛丑'],
    '金箔金': ['壬寅', '癸卯'],
    '覆灯火': ['甲辰', '乙巳'],
    '天河水': ['丙午', '丁未'],
    '大驿土': ['戊申', '己酉'],
    '钗钏金': ['庚戌', '辛亥'],
    '桑柘木': ['壬子', '癸丑'],
    '大溪水': ['甲寅', '乙卯'],
    '沙中土': ['丙辰', '丁巳'],
    '天上火': ['戊午', '己未'],
    '石榴木': ['庚申', '辛酉'],
    '大海水': ['壬戌', '癸亥'],
}
C_NaYin = {}
for k in C_NaYinD:
    for v in C_NaYinD[k]:
        C_NaYin[v] = k

# key 为男
C_NNayinHeHui = {
    '木': {
        '木':'木命夫妻争不休，子女因此添忧愁，阴木要能胸宽广，子孙昌盛财富厚。',
        '火':'男木女火情深厚，起家致富是能手，子女知书又达理，福寿无边乐悠悠。',
        '土':'男木女土难聚就，灾祸疾病最堪忧，多是中年分东西，夫妻无缘财不留。',
        '金':'男木女金难长久，夫硬妻刚不到头，妻若柔情温如水，财丁两旺定富有。',
        '水':'鸳鸯夫妻不易求，恩恩爱爱无忧愁，子孝孙贤多富贵，小儿登科住高楼。',
    },
    '火': {
        '木': '火木夫妻命相生，全家浸在幸福中，子女聪明通义理，六畜兴旺田园丰。',
        '火': '火火相并一世穷，妻离子算总是凶，妻若晓理胸怀大，子孙兴旺财兴隆。',
        '土': '火土夫妻情意浓，相处总是初恋情，家业兴旺财运好，子子孙孙榜有名。',
        '金': '男火女金最为凶，女刚从来无长命，夫妻能晓此中理，百业兴旺家不穷。',
        '水': '火水相见不留情，阴盛阳衰孤独命，里里外外生事端，皆因水火不相容。',
    },
    '土': {
        '木': '土木夫妻是灾难，同房同床处难同眠，财空家冷子难留，皆因克夫家不全。',
        '火': '土火夫妻真美满，夫枕妻怀福中眠，更有子孙多财宝，幸福快乐伴苍天。',
        '土': '硬土软土成一片，夫唱妇随好姻缘，丁财两旺六畜兴，子子孙孙大团圆。',
        '金': '土金夫妻好姻缘，强男娇妻合的欢，子孙成群财满门，更有福寿到百年。',
        '水': '土水很难成姻缘，昼夜吵声哭连连，子女意冷离家去，夫妻分手中年。',
    },
    '金': {
        '木': '金男女木不相当，曾是成婚不久长，命理相伤不为吉，终久难眠同一处。',
        '火': '男金女火不为良，当心妻把丈夫伤，火能安来亦富有，火旺败家不相当。',
        '土': '金土夫妻比鸳鸯，阴生阳长福寿长，神仙羡慕好伴侣，世代富贵大吉昌。',
        '金': '金命夫妻不相让，中年难眠同一处，昼夜争斗无休止，老来必定守空房。',
        '水': '金水夫妻最为上，恩恩爱爱日子强，子孝孙贤文章好，财丁两旺福寿康。',
    },
    '水': {
        '木': '水木相生心相连，神仙都说好姻缘，多子多孙又多财，田园兴旺福寿添。',
        '火': '水火从来不相见，若为夫妻实难安，烈妻从来不相让，败家破财人不全。',
        '土': '水土夫妻难久全，男烦女嫌家难安，贫苦相怨无出路，时到中年夫妻散。',
        '金': '天生一对好姻缘，好男又与内助贤，六畜兴旺子孙昌，天伦之乐赛神仙。',
        '水': '男水女水好姻缘，水水交融招人羡，丁财两旺多富贵，夫妻恩爱到百年。',
    },
}
NNayinHeHuiL = {

}