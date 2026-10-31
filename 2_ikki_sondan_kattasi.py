def katta_son(a, b):
    return a if a > b else b


a, b = map(int, input("a va b ni kiriting: ").split())
print("katta son:", katta_son(a, b))