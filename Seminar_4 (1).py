#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
import numpy as np
a=list(range(50,101))
print(np.array(a))


# In[ ]:





# In[3]:


#2
b=[]
c=[]
d=[]
k=1
l=0
m=6
for i in range(10):
    b.append(k)
    c.append(l)
    d.append(m)
print(np.array(b))
print(np.array(c))
print(np.array(d))


# In[4]:


#3
data = list(range(20,32))
print(data)
data1 = np.array(data)
print(data1)
k = np.reshape(data1,(3,4))
print(k)


# In[5]:


#4
x=np.eye(3)
print(x)
y=np.zeros((3,3))
np.fill_diagonal(y,1)
print(y)


# In[6]:


#5
c = np.zeros((5,5))
np.fill_diagonal(c,[1,2,3,4,5])
print(c)


# In[7]:


#6
a=np.random.randn(2,5)
print(a)
print('total sum')
print(np.sum(a))
print('sum of columns')
print(np.sum(a,1))
print('sum of rows')
for i in range(5):
    k=a[0,i]+a[1,i]
    print(k)


# In[10]:


#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014", "2015", "2016", "2017", "2018","2019", "2020"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9, "2015":10, "2016":11, "2017":12, "2018":13, "2019":14, "2020":15}

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}

#Salaries
KobeBryant_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000,25000000,0,0,0,0,0]
JoeJohnson_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790,22309344,11000000,10254904,0,0,0]
LeBronJames_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400,22970500,30963450,33285709,35654150,37436858,39219566]
CarmeloAnthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000,22875000,24559380,26243760,27928140,2159029,2564753]
DwightHoward_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271,22359364,23180275,23500000,24256725,5603850,2564753]
ChrisBosh_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400,22192730,23741060,25289390,26837720,0,0]
ChrisPaul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563,21468695,22868827,24268959,35645150,38506482,41358814]
KevinDurant_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624,20158622,26540100,25000000,30000000,37199000,40108950]
DerrickRose_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875,20093064,21323252,2533488,2176260,7317074,7682926]
DwayneWade_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000,20000000,17878652,2328652,2393887,0,0]
#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
import warnings as w
w.filterwarnings('ignore')
print('Total sum ',np.sum(Salary))
print('Total sum of Rows',np.sum(Salary, 0))
print('Total sum of Columns',np.sum(Salary, 1))
#Games 
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35,66,0,0,0,0,0]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80,81,78,55,0,0,0]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69,76,74,82,55,67,45]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40,72,74,78,10,58,69]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41,71,74,81,9,69,69]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44,53,0,0,0,0,0]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82,74,61,58,58,70,70]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27,72,62,68,78,0,35]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51,66,64,25,51,50,50]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62,74,60,67,72,0,0]
#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])
import warnings as w
w.filterwarnings('ignore')
print('Total sum ',np.sum(Games))
print('Total sum of Rows',np.sum(Games, 0))
print('Total sum of Columns',np.sum(Games, 1))
#Minutes Played
KobeBryant_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207,1863,0,0,0,0,0]
JoeJohnson_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791,2703,1843,1205,0,0,0]
LeBronJames_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493,2709,2794,3026,1937,2316,1504]
CarmeloAnthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428,2530,2538,2501,294,1902,1690]
DwightHoward_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223,2280,2199,2463,230,1306,1196]
ChrisBosh_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556,1778,0,0,0,0,0]
ChrisPaul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857,2420,1921,1847,1857,2208,2199]
KevinDurant_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913,2578,2070,2325,2702,1157,1459]
DerrickRose_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530,2097,2082,420,1392,1298,1279]
DwayneWade_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971,2258,1792,1536,1885,0,0]
#Matrix
MinutesPlayed = np.array([KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP, KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])
import warnings as w
w.filterwarnings('ignore')
print('Total sum ',np.sum(MinutesPlayed))
print('Total sum of Rows',np.sum(MinutesPlayed, 0))
print('Total sum of Columns',np.sum(MinutesPlayed, 1))
#Field Goals
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266,398,0,0,0,0,0]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446,377,273,146,0,0,0]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624,737,736,857,558,643,422]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358,567,602,472,49,336,327]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251,372,388,506,43,202,178]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343,358,0,0,0,0,0]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568,515,374,367,302,434,439]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238,698,551,630,721,0,324]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338,447,460,81,363,369,287]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509,540,414,299,416,0,0]
#Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])
import warnings as w
w.filterwarnings('ignore')
print('Total sum ',np.sum(FieldGoals))
print('Total sum of Rows',np.sum(FieldGoals, 0))
print('Total sum of Columns',np.sum(FieldGoals, 1))
#Field Goal Attempts
KobeBryant_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713,1113,0,0,0,0,0]
JoeJohnson_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025,859,626,360,0,0,0]
LeBronJames_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279,1416,1344,1580,1095,1303,823]
CarmeloAnthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806,1307,1389,1168,121,782,777]
DwightHoward_FGA = [881,873,974,979,834,1044,726,813,800,423,600,613,911,69,277,303]
ChrisBosh_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745,767,0,0,0,0,0]
ChrisPaul_FGA = [947,871,1291,1255,637,928,890,856,870,1170,1114,785,798,720,887,879]
KevinDurant_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467,1381,1026,1222,1383,0,603]
DerrickRose_FGA = [436,436,436,1208,1373,1597,695,0,164,835,1048,977,186,753,753,611]
DwayneWade_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084,1183,955,682,960,0,0]
#Matrix
FieldGoalAttempts = np.array([KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA, ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])
import warnings as w
w.filterwarnings('ignore')
print('Total sum ',np.sum(FieldGoalAttempts))
print('Total sum of Rows',np.sum(FieldGoalAttempts, 0))
print('Total sum of Columns',np.sum(FieldGoalAttempts, 1))
#Points
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782,1161,0,0,0,0,0]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154,992,715,372,0,0,0]
LeBronJames_PTS = [2132,2250,2304,2258,2111,1683,2036,2089,1743,1920,1954,2251,1505,1698,1126,1426]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966,1573,1659,1261,134,895,924]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646,976,1002,1347,115,517,482]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928,1010,0,0,0,0,0]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564,1446,1104,1081,906,1232,1149]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686,2029,1555,1792,2027,0,943]
DerrickRose_PTS = [597,597,1361,1619,2026,852,0,159,904,1080,1154,209,917,904,734,311]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331,1409,1096,765,1083,0,0]
#Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])             
import warnings as w
w.filterwarnings('ignore')
print('Total sum ',np.sum(Points))
print('Total sum of Rows',np.sum(Points, 0))
print('Total sum of Columns',np.sum(Points, 1))


# In[ ]:




