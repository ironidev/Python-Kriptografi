################################################################
# Meretas sandi Caesar dengan Brute-force
# Editor : Matius Celcius Sinaga
# Author : # http://inventwithpython.com/hacking (BSD Licensed)
#################################################################

pesan = 'RWMXWNBRJ AJHJ'
HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for kunci in range(len(HURUF)):

    ubah = ''

    for symbol in pesan:
        if symbol in HURUF:

            nomor = HURUF.find(symbol)
            nomor = nomor - kunci

            if nomor < 0:

                nomor = nomor + len(HURUF)

            ubah = ubah + HURUF[nomor]

        else:

            ubah = ubah + symbol

    print('Key #%s: %s' % (kunci, ubah))