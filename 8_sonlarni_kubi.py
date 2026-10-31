n = int(input("Nechta son kiritasiz: "))
sonlar = list(map(int, input("Sonlarni kiriting: ").split()))

natija = list(map(lambda x: x ** 3, sonlar))

print(natija)