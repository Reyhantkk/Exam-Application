class Soru:
    def __init__(self, metin, secenekler, cevap):
        self.metin = metin
        self.secenekler = secenekler
        self.cevap = cevap

    def cevabi_kontrol_et(self, kullanici_cevabi):
        return self.cevap == kullanici_cevabi

# Soruların oluşturulması
soru_listesi = [
    Soru("Python programlama dilinin kurucusu kimdir?", ['A) Guido van Rossum', 'B) Elon Musk', 'C) Bill Gates', 'D) Mark Zuckerberg'], 'A'),
    Soru("Hangisi Python'da bir veri tipidir?", ['A) list', 'B) array', 'C) table', 'D) object'], 'A'),
    Soru("Python dosya uzantısı nedir?", ['A) .pyth', 'B) .pt', 'C) .py', 'D) .python'], 'C'),
]

# Sınavın çalıştırılması
def sinavi_calistir(sorular):
    puan = 0
    for soru in sorular:
        print(soru.metin)
        for secenek in soru.secenekler:
            print(secenek)
        cevap = input("Cevabınız (A, B, C, D): ")
        if soru.cevabi_kontrol_et(cevap.upper()):
            print("Doğru!")
            puan += 1
        else:
            print("Yanlış!")
    print(f"Sınavı tamamladınız. Puanınız: {puan}/{len(sorular)}")

# Sınavı başlat
sinavi_calistir(soru_listesi)
