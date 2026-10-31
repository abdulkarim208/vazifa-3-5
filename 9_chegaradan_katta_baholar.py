baholar = list(map(int, input("Baholarni kiriting: ").split()))

natija = list(filter(lambda x: x > 70, baholar))

print(natija)