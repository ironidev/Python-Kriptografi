###############################################################
# Deteksi Bahasa #
# Editor : Matius Celcius Sinaga #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)
###############################################################

HurufBESAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Huruf_Dan_Spasi = HurufBESAR + HurufBESAR.lower() + ' \t\n'


def memuatKamus():
    fileKamus = open('dictionary.txt')
    cekKata = {}
    for kata in fileKamus.read().split('\n'):
        cekKata[kata] = None
        fileKamus.close()
        return cekKata

KATA_BAHASA = memuatKamus()


def hitungJumlahKata(pesan):
    pesan = pesan.upper()
    pesan = bukanKata(pesan)
    kemungkinanKata = pesan.split()

    if kemungkinanKata == []:
        return 0.0
    cocok = 0

    for kata in kemungkinanKata:
        if kata in KATA_BAHASA:
            cocok += 1
    return float(cocok) / len(kemungkinanKata)

def bukanKata(pesan):
    hurufSaja = []
    for symbol in pesan:
        if symbol in Huruf_Dan_Spasi:
            hurufSaja.append(symbol)
    return ''.join(hurufSaja)

def cekBahasa(pesan, IjinkanJumlahKata=20, IjinkanJumlahHuruf=85):
    kataYangCocok = hitungJumlahKata(pesan) * 100 >= IjinkanJumlahKata
    nomorHuruf = len(bukanKata(pesan))
    IjinkanJumlahKalimat = float(nomorHuruf) / len(pesan) * 100
    hurufYangCocok = IjinkanJumlahKalimat >= IjinkanJumlahHuruf
    return kataYangCocok and hurufYangCocok