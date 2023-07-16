def toplama_ulas(hedef, sayilar, secilenler=[]):
    if hedef == 0:
        return secilenler
    if hedef < 0 or not sayilar:
        return None

    for i, sayi in enumerate(sayilar):
        kalan = hedef - sayi
        alt_dizi = toplama_ulas(kalan, sayilar[i+1:], secilenler + [sayi])
        if alt_dizi is not None:
            return alt_dizi

    return None
print("Programın sonucu vermesi bazı sayılar için uzun sürebilir bunun sebebi çok fazla kombinasyon olması...")
sayilar = list(range(1, 200))
print("Kullanılacak Dizi: ",sayilar)
hedef_sayi = int(input("Hedef sayıyı girin: (Max 20100) "))


sonuc = toplama_ulas(hedef_sayi, sayilar)

if sonuc:
    print("Hedef sayıya ulaşmak için seçilen sayılar:", sonuc)
    print("Toplam:", sum(sonuc))
else:
    print("Hedef sayıya ulaşılamadı.")
