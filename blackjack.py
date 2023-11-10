import random

class BlackjackGame:
    def __init__(self):
        self.deste = self.oyun_destesi_olustur()
        self.oyuncu_el = []
        self.krupiye_el = []

    def oyun_destesi_olustur(self):
        renkler = ['Kupa', 'Karo', 'Sinek', 'Maça']
        degerler = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        destede_kartlar = [{'renk': renk, 'deger': deger} for renk in renkler for deger in degerler]
        random.shuffle(destede_kartlar)
        return destede_kartlar

    def kart_cek(self):
        return self.deste.pop()

    def el_toplam(self, el):
        toplam = 0
        as_sayisi = 0
        for kart in el:
            if kart['deger'] in ['K', 'Q', 'J']:
                toplam += 10
            elif kart['deger'] == 'A':
                toplam += 11
                as_sayisi += 1
            else:
                toplam += int(kart['deger'])
        
        while toplam > 21 and as_sayisi:
            toplam -= 10
            as_sayisi -= 1
        
        return toplam

    def oyun_bitti_mi(self):
        return self.el_toplam(self.oyuncu_el) > 21 or self.el_toplam(self.krupiye_el) > 21

    def oyun_sonucu(self):
        oyuncu_toplam = self.el_toplam(self.oyuncu_el)
        krupiye_toplam = self.el_toplam(self.krupiye_el)

        if oyuncu_toplam > 21:
            return 'Oyuncu battı, krupiye kazandı!'
        elif krupiye_toplam > 21:
            return 'Krupiye battı, oyuncu kazandı!'
        elif oyuncu_toplam > krupiye_toplam:
            return 'Oyuncu kazandı!'
        elif oyuncu_toplam < krupiye_toplam:
            return 'Krupiye kazandı!'
        else:
            return 'Berabere!'

    def oyunu_baslat(self):
        self.oyuncu_el.append(self.kart_cek())
        self.oyuncu_el.append(self.kart_cek())
        self.krupiye_el.append(self.kart_cek())

        while True:
            print(f"\nOyuncu El: {self.oyuncu_el}, Toplam: {self.el_toplam(self.oyuncu_el)}")
            print(f"Krupiye'nin Açık Kartı: {self.krupiye_el[0]}")

            if input("Başka bir kart çekmek ister misiniz? (E/H): ").lower() == 'e':
                self.oyuncu_el.append(self.kart_cek())
            else:
                break

            if self.oyun_bitti_mi():
                break

        while self.el_toplam(self.krupiye_el) < 17:
            self.krupiye_el.append(self.kart_cek())

        print("\nOyun Sonu!")
        print(f"Oyuncu El: {self.oyuncu_el}, Toplam: {self.el_toplam(self.oyuncu_el)}")
        print(f"Krupiye El: {self.krupiye_el}, Toplam: {self.el_toplam(self.krupiye_el)}")
        print(self.oyun_sonucu())

        return input("Yeniden oynamak ister misiniz? (E/H): ").lower() == 'e'

if __name__ == "__main__":
    while True:
        oyun = BlackjackGame()
        if not oyun.oyunu_baslat():
            break
