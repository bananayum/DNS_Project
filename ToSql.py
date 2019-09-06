import pymysql

def run(sha256,family_result):
    Sample_HASH=sha256

    if ('ALYac' in family_result.keys()):
        ALYac=family_result['ALYac']
    else:
        ALYac = None

    if ('APEX' in family_result.keys()):
        APEX=family_result['APEX']
    else:
        APEX = None

    if ('AVG' in family_result.keys()):
        AVG = family_result['AVG']
    else:
        AVG = None

    if ('Acronis' in family_result.keys()):
        Acronis = family_result['Acronis']
    else:
        Acronis = None

    if ('Ad-Aware' in family_result.keys()):
        Ad_Aware = family_result['Ad-Aware']
    else:
        Ad_Aware = None

    if ('AegisLab' in family_result.keys()):
        AegisLab = family_result['AegisLab']
    else:
        AegisLab = None

    if ('AhnLab-V3' in family_result.keys()):
        AhnLab_V3 = family_result['AhnLab-V3']
    else:
        AhnLab_V3 = None

    if ('ALYac' in family_result.keys()):
        Alibaba = family_result['Alibaba']
    else:
        Alibaba = None

    if ('Antiy-AVL' in family_result.keys()):
        Antiy_AVL = family_result['Antiy-AVL']
    else:
        Antiy_AVL = None

    if ('Arcabit' in family_result.keys()):
        Arcabit = family_result['Arcabit']
    else:
        Arcabit = None

    if ('Avast' in family_result.keys()):
        Avast = family_result['Avast']
    else:
        Avast = None

    if ('Avast-Mobile' in family_result.keys()):
        Avast_Mobile = family_result['Avast-Mobile']
    else:
        Avast_Mobile = None

    if ('Avira' in family_result.keys()):
        Avira = family_result['Avira']
    else:
        Avira = None

    if ('Babable' in family_result.keys()):
        Babable = family_result['Babable']
    else:
        Babable = None

    if ('Baidu' in family_result.keys()):
        Baidu = family_result['Baidu']
    else:
        Baidu = None

    if ('BitDefender' in family_result.keys()):
        BitDefender = family_result['BitDefender']
    else:
        BitDefender = None

    if ('Bkav' in family_result.keys()):
        Bkav = family_result['Bkav']
    else:
        Bkav = None

    if ('CAT_QuickHeal' in family_result.keys()):
        CAT_QuickHeal = family_result['CAT-QuickHeal']
    else:
        CAT_QuickHeal = None

    if ('CMC' in family_result.keys()):
        CMC = family_result['CMC']
    else:
        CMC = None

    if ('ClamAV' in family_result.keys()):
        ClamAV = family_result['ClamAV']
    else:
        ClamAV = None

    if ('Comodo' in family_result.keys()):
        Comodo = family_result['Comodo']
    else:
        Comodo = None

    if ('CrowdStrike' in family_result.keys()):
        CrowdStrike = family_result['CrowdStrike']
    else:
        CrowdStrike = None

    if ('Cybereason' in family_result.keys()):
        Cybereason = family_result['Cybereason']
    else:
        Cybereason = None

    if ('Cylance' in family_result.keys()):
        Cylance = family_result['Cylance']
    else:
        Cylance = None

    if ('Cyren' in family_result.keys()):
        Cyren = family_result['Cyren']
    else:
        Cyren = None

    if ('DrWeb' in family_result.keys()):
        DrWeb = family_result['DrWeb']
    else:
        DrWeb = None

    if ('ESET-NOD32' in family_result.keys()):
        ESET_NOD32 = family_result['ESET-NOD32']
    else:
        ESET_NOD32 = None

    if ('Emsisoft' in family_result.keys()):
        Emsisoft = family_result['Emsisoft']
    else:
        Emsisoft = None

    if ('Endgame' in family_result.keys()):
        Endgame = family_result['Endgame']
    else:
        Endgame = None

    if ('F-Prot' in family_result.keys()):
        F_Prot = family_result['F-Prot']
    else:
        F_Prot = None

    if ('F-Secure' in family_result.keys()):
        F_Secure = family_result['F-Secure']
    else:
        F_Secure = None

    if ('FireEye' in family_result.keys()):
        FireEye = family_result['FireEye']
    else:
        FireEye = None

    if ('Fortinet' in family_result.keys()):
        Fortinet = family_result['Fortinet']
    else:
        Fortinet = None

    if ('GData' in family_result.keys()):
        GData = family_result['GData']
    else:
        GData = None

    if ('Ikarus' in family_result.keys()):
        Ikarus = family_result['Ikarus']
    else:
        Ikarus = None

    if ('Invincea' in family_result.keys()):
        Invincea = family_result['Invincea']
    else:
        Invincea = None

    if ('Jiangmin' in family_result.keys()):
        Jiangmin = family_result['Jiangmin']
    else:
        Jiangmin = None

    if ('K7AntiVirus' in family_result.keys()):
        K7AntiVirus = family_result['K7AntiVirus']
    else:
        K7AntiVirus = None

    if ('K7GW' in family_result.keys()):
        K7GW = family_result['K7GW']
    else:
        K7GW = None

    if ('Kaspersky' in family_result.keys()):
        Kaspersky = family_result['Kaspersky']
    else:
        Kaspersky = None

    if ('Kingsoft' in family_result.keys()):
        Kingsoft = family_result['Kingsoft']
    else:
        Kingsoft = None

    if ('MAX' in family_result.keys()):
        MAX = family_result['MAX']
    else:
        MAX = None

    if ('Malwarebytes' in family_result.keys()):
        Malwarebytes = family_result['Malwarebytes']
    else:
        Malwarebytes = None

    if ('MaxSecure' in family_result.keys()):
        MaxSecure = family_result['MaxSecure']
    else:
        MaxSecure = None

    if ('McAfee' in family_result.keys()):
        McAfee = family_result['McAfee']
    else:
        McAfee = None

    if ('McAfee-GW-Edition' in family_result.keys()):
        McAfee_GW_Edition = family_result['McAfee-GW-Edition']
    else:
        McAfee_GW_Edition = None

    if ('MicroWorld-eScan' in family_result.keys()):
        MicroWorld_eScan = family_result['MicroWorld-eScan']
    else:
        MicroWorld_eScan = None

    if ('Microsoft' in family_result.keys()):
        Microsoft = family_result['Microsoft']
    else:
        Microsoft = None

    if ('NANO-Antivirus' in family_result.keys()):
        NANO_Antivirus = family_result['NANO-Antivirus']
    else:
        NANO_Antivirus = None

    if ('Paloalto' in family_result.keys()):
        Paloalto = family_result['Paloalto']
    else:
        Paloalto = None

    if ('Panda' in family_result.keys()):
        Panda = family_result['Panda']
    else:
        Panda = None

    if ('Qihoo-360' in family_result.keys()):
        Qihoo_360 = family_result['Qihoo-360']
    else:
        Qihoo_360 = None

    if ('Rising' in family_result.keys()):
        Rising = family_result['Rising']
    else:
        Rising = None

    if ('SUPERAntiSpyware' in family_result.keys()):
        SUPERAntiSpyware = family_result['SUPERAntiSpyware']
    else:
        SUPERAntiSpyware = None

    if ('SentinelOne' in family_result.keys()):
        SentinelOne = family_result['SentinelOne']
    else:
        SentinelOne = None

    if ('Sophos' in family_result.keys()):
        Sophos = family_result['Sophos']
    else:
        Sophos = None

    if ('Symantec' in family_result.keys()):
        Symantec = family_result['Symantec']
    else:
        Symantec = None

    if ('SymantecMobileInsight' in family_result.keys()):
        SymantecMobileInsight = family_result['SymantecMobileInsight']
    else:
        SymantecMobileInsight = None

    if ('TACHYON' in family_result.keys()):
        TACHYON = family_result['TACHYON']
    else:
        TACHYON = None

    if ('Tencent' in family_result.keys()):
        Tencent = family_result['Tencent']
    else:
        Tencent = None

    if ('TotalDefense' in family_result.keys()):
        TotalDefense = family_result['TotalDefense']
    else:
        TotalDefense = None

    if ('Trapmine' in family_result.keys()):
        Trapmine = family_result['Trapmine']
    else:
        Trapmine = None

    if ('TrendMicro' in family_result.keys()):
        TrendMicro = family_result['TrendMicro']
    else:
        TrendMicro = None

    if ('TrendMicro-HouseCall' in family_result.keys()):
        TrendMicro_HouseCall = family_result['TrendMicro-HouseCall']
    else:
        TrendMicro_HouseCall = None

    if ('Trustlook' in family_result.keys()):
        Trustlook = family_result['Trustlook']
    else:
        Trustlook = None

    if ('VBA32' in family_result.keys()):
        VBA32 = family_result['VBA32']
    else:
        VBA32 = None

    if ('VIPRE' in family_result.keys()):
        VIPRE = family_result['VIPRE']
    else:
        VIPRE = None

    if ('ViRobot' in family_result.keys()):
        ViRobot = family_result['ViRobot']
    else:
        ViRobot = None

    if ('Webroot' in family_result.keys()):
        Webroot = family_result['Webroot']
    else:
        Webroot = None

    if ('Yandex' in family_result.keys()):
        Yandex = family_result['Yandex']
    else:
        Yandex = None

    if ('Zillya' in family_result.keys()):
        Zillya = family_result['Zillya']
    else:
        Zillya = None

    if ('ZoneAlarm' in family_result.keys()):
        ZoneAlarm = family_result['ZoneAlarm']
    else:
        ZoneAlarm = None

    if ('Zoner' in family_result.keys()):
        Zoner = family_result['Zoner']
    else:
        Zoner = None


    db=pymysql.connect("localhost","root","xebszw7lllg","samplefamily",charset="UTF8")
    cursor=db.cursor()

    sql="INSERT INTO virus_family(Sample_HASH,ALYac,APEX,AVG,Acronis,Ad_Aware,AegisLab,AhnLab_V3,Alibaba,Antiy_AVL,Arcabit," \
        "Avast,Avast_Mobile,Avira,Babable,Baidu,BitDefender,Bkav,CAT_QuickHeal,CMC,ClamAV,Comodo,CrowdStrike,Cybereason,Cylance,Cyren,DrWeb," \
        "ESET_NOD32,Emsisoft,Endgame,F_Prot,F_Secure,FireEye,Fortinet,GData,Ikarus,Invincea,Jiangmin,K7AntiVirus,K7GW,Kaspersky,Kingsoft,MAX," \
        "Malwarebytes,MaxSecure,McAfee,McAfee_GW_Edition,MicroWorld_eScan,Microsoft,NANO_Antivirus,Paloalto,Panda,Qihoo_360,Rising,SUPERAntiSpyware," \
        "SentinelOne,Sophos,Symantec,SymantecMobileInsight,TACHYON,Tencent,TotalDefense,Trapmine,TrendMicro,TrendMicro_HouseCall,Trustlook,VBA32,VIPRE,ViRobot," \
        "Webroot,Yandex,Zillya,ZoneAlarm,Zoner) " \
        "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
        "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
        "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(Sample_HASH,ALYac,APEX,AVG,Acronis,Ad_Aware,AegisLab,AhnLab_V3,Alibaba,Antiy_AVL,Arcabit,
        Avast,Avast_Mobile,Avira,Babable,Baidu,BitDefender,Bkav,CAT_QuickHeal,CMC,ClamAV,Comodo,CrowdStrike,Cybereason,Cylance,Cyren,DrWeb,ESET_NOD32,Emsisoft,Endgame,
        F_Prot,F_Secure,FireEye,Fortinet,GData,Ikarus,Invincea,Jiangmin,K7AntiVirus,K7GW,Kaspersky,Kingsoft,MAX,Malwarebytes,MaxSecure,McAfee,McAfee_GW_Edition,MicroWorld_eScan,
        Microsoft,NANO_Antivirus,Paloalto,Panda,Qihoo_360,Rising,SUPERAntiSpyware,SentinelOne,Sophos,Symantec,SymantecMobileInsight,TACHYON,Tencent,TotalDefense,Trapmine,
        TrendMicro,TrendMicro_HouseCall,Trustlook,VBA32,VIPRE,ViRobot,Webroot,Yandex,Zillya,ZoneAlarm,Zoner)

    cursor.execute(sql)
    db.commit()
    db.close()