#############check the greatest in three digit num####


def greatest_num():
    aaa=int(input("First num   :   "))
    bbb=int(input("First sec   :   "))
    ccc=int(input("First third :   "))
    if aaa>=bbb and aaa>=ccc:
        print(aaa,"is the greatest number")
    elif bbb>=ccc and bbb>=aaa:
        print(bbb,"is the greatest number")
    else:
        print(ccc,"is the greatest number")
greatest_num()
