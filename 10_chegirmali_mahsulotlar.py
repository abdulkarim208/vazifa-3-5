n = int(input("Mahsulotlar sonini kiriting: "))
narxlar = list(map(int, input("Narxlarni kiriting: ").split()))

tanlangan = list(filter(lambda x: x >= 15000, narxlar))

natija = list(map(lambda x: x - 3000, tanlangan))

print(natija)