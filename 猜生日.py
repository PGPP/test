a,b,c,d,e=2,2,2,2,2
print("以下会通过几个问题，得到你的生日是请按1，不是请按0：")
while a!='1' and a!='0':
    a=input("""1号问题你的生日在这里面吗？
    1  3  5  7
    9 11 13 15
    17 19 21 23
    25 27 29 31
    """)
while b!="1"and b!="0":
    b=input("""2号问题你的生日在里面吗？
    2  3  6  7
    10 11 14 15
    18 19 22 23
    26 27 30 31
    """)
while c!="1"and c!="0":
    c=input("""3号问题你的生日在里面吗？
     4  5  6  7
     12 13 14 15
     20 21 22 23
     28 29 30 31
    """)
while d!="1"and d!="0":
    d=input("""4号问题你的生日在里面吗？
    8  9 10 11
    12 13 14 15
    24 25 26 27
    28 29 30 31
    """)
while e!='1'and e!="0":
    e=input("""5号问题你的生日在里面吗？
    16 17 18 19
    20 21 22 23
    24 25 26 27
    28 29 30 31
    """)
sun=a+b+c+d+e
print(sun)
day,power=0,0
for i in list(sun):
    i=int(i)
    day=day+i*2**power
    power+=1
print("你的生日是：%d号"%day)
