###############################################################
# Sandi Caesar
# Editor : Matius Celcius Sinaga
# Author : # http://inventwithpython.com/hacking (BSD Licensed)
###############################################################

import pyperclip

pesan = 'Indonesia Raya'
kunci = 9
mode = 'encrypt'
HURUF ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ubah = ''

pesan = pesan.upper()

for symbol in pesan:
    if symbol in HURUF:

        nomor = HURUF.find(symbol)

        if mode == 'encrypt':
            nomor = nomor + kunci
        elif mode == 'decrypt':
            nomor = nomor - kunci

        if nomor >= len(HURUF):
            nomor = nomor - len(HURUF)
        elif nomor < 0:
            nomor = nomor + len(HURUF)

        ubah = ubah + HURUF[nomor]

    else:

        ubah = ubah + symbol

print(ubah)

print(range(len(HURUF)))

#menyalin hasil enkripsi/dekripsi pada penyimpanan sementara
pyperclip.copy(ubah)

























