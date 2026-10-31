def ijobiy_yigindi(*sonlar):
    jami = 0

    for son in sonlar:
        if son > 0:
            jami += son

    return jami


n = int(input("n kiriting: "))

sonlar = list(map(int, input().split()))

print(ijobiy_yigindi(*sonlar))