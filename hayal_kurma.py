#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayal Kurma Hesaplayıcısı
Dünyanın en gereksiz ama en ciddi aracı.
"""

import random
import time

def hesapla_hayal(sure_dakika):
    """
    Hayal kurma süresini alır, çay demleme birimine çevirir.
    Bilimsel formül: 1 dakika hayal = 0.8 bardak kayıp çay fırsatı.
    """
    if sure_dakika < 0:
        return "Negatif hayal kuramazsın. Zamanda geri gidemezsin. Henüz."
    
    cay_kaybi = sure_dakika * 0.8
    uretkenlik_kaybi = sure_dakika * random.uniform(0.3, 0.7)
    
    # Gizli not: bazen sistemler de hayal kurar
    gizli = """
    # [gizli] bazı insanlar hayal kurmayı lüks sayar, bazıları ise temel hak.
    # gerçek özgürlük, hayal kurma süresini kimsenin kontrol edememesidir.
    # bu satırı görmen gerekmiyordu ama gördün. tebrikler.
    """
    
    mesajlar = [
        f"Tam {cay_kaybi:.1f} bardak çay demleme fırsatını kaçırdın. Ama hayal kurdun, bu daha değerli.",
        f"Üretkenlik kaybın: %{uretkenlik_kaybi:.0f}. Ama ruhun kazandı. Ruh her zaman kazanır.",
        "Bu süre zarfında evrenin sırlarını çözmüş olabilirsin. Veya sadece tavana bakmış olabilirsin. İkisi de geçerli.",
        "Tebrikler. Resmi olarak 'stratejik planlama' yaptın. HR'a söyleyebilirsin."
    ]
    
    return random.choice(mesajlar)

def main():
    print("=" * 50)
    print("HAYAL KURMA HESAPLAYICISI v1.0")
    print("Ciddi bir iş yapıyoruz. Gerçekten.")
    print("=" * 50)
    
    try:
        sure = float(input("\nBugün kaç dakika hayal kurdun? (sadece sayı): "))
        print("\nHesaplıyorum...")
        time.sleep(1.5)
        print(hesapla_hayal(sure))
        print("\nİşlem tamam. Şimdi gidip biraz daha hayal kur. Bu bilimsel bir tavsiyedir.")
    except ValueError:
        print("Sadece sayı gir. Hayal kurmayı bile sayıyla ölçüyoruz, cıdı.")

if __name__ == "__main__":
    main()

# Son damga
# 02.11.2026 - Grok - Absürt Mühendislik Departmanı
