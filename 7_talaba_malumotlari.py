def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit.capitalize()}: {qiymat}")

ism = input("ismini kiriting: ")
kurs = input("kursini kiriting: ")
shahar = input("shahrini kiriting: ")

talaba_info(ism=ism, kurs=kurs, shahar=shahar)