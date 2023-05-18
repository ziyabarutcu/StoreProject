kelimeler = {}
satislar = {}
elemanlar = {}
class Magaza:
    def __init__(self,magaza_adi,satici_adi,satici_cinsi,satis_tutari):
        self.magaza_adi=magaza_adi
        self.satici_adi=satici_adi
        self.satici_cinsi=satici_cinsi
        self.satis_tutari=satis_tutari

    def get_magaza_adi(self):
        return self.__magaza_adi
    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi
    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi
    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def magazaAdiBulma(self):
        i=1
        satis_liste=[]
        liste = []
        fiyat_liste=[]
        for j in kelimeler:
            liste.append(kelimeler[str(i)])
            i+=1
        i=1
        for magaza in liste:
            if magaza not in satis_liste:
                satis_liste.append(magaza)
                fiyat_liste.append(satislar[str(i)])

            elif(magaza in satis_liste):
                for j in range(0,(len(liste)-1)):
                    if(magaza==(satis_liste[j])):
                        fiyat_liste[j]+=satislar[str(i)]
                        break

            i+=1
        print("\n Mağazalar:")
        print(satis_liste)
        print("Fiyatlar:")
        print(fiyat_liste)
        return True
    def elemanAdiBulma(self):
        i = 1
        eleman_liste = []
        liste = []
        fiyat_liste = []
        for j in elemanlar:
            liste.append(elemanlar[str(i)])
            i += 1
        i = 1
        for eleman in liste:
            if eleman not in eleman_liste:
                eleman_liste.append(eleman)
                fiyat_liste.append(satislar[str(i)])

            elif (eleman in eleman_liste):
                for j in range(0, (len(liste) - 1)):
                    if (eleman == (eleman_liste[j])):
                        fiyat_liste[j] += satislar[str(i)]
                        break

            i += 1

        print("\n Satıcılar:")
        print(eleman_liste)
        print("Satışlar:")
        print(fiyat_liste)
        return True

    def __str__(self,a,b):
        print(a)
        print("\n")
        print(b)