################################################################
# Dekripsi dengan sandi Transposisi
# Editor : Matius Celcius Sinaga
# Author : # http://inventwithpython.com/hacking (BSD Licensed)
# ################################################################

import math, pyperclip

def main():
    pesanSaya = 'Iaakn nudRa:oahIny ReaATs iAiTr|'
    kunciSaya = 8
    teksawal = dekripsiPesan(kunciSaya, pesanSaya)
    print(teksawal + '|')
    pyperclip.copy(teksawal)

def dekripsiPesan(kunci, pesan):
    jumlahKolom = math.ceil(len(pesan) / kunci)
    jumlahBaris = kunci
    jumlahKotakyangTerisi = (jumlahKolom * jumlahBaris) - len(pesan)
    teksawal = [''] * jumlahKolom
    kolom = 0
    baris = 0

    for symbol in pesan:
        teksawal[kolom] += symbol
        kolom += 1

        if (kolom == jumlahKolom) or (kolom == jumlahKolom - 1 and baris >= jumlahBaris - jumlahKotakyangTerisi):
            kolom = 0
            baris += 1

    return ''.join(teksawal)

if __name__=='__main__':
    main()