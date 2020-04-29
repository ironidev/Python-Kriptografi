###############################################################
# Transposisi File sandi #
# Editor : Matius Celcius Sinaga #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)
# #############################################################

import time, os, sys
from helper import enkripsitransposisi
from helper import dekripsitransposisi

def main():

    masukkanNamaFile = 'matiuscelciussinaga.txt'
    namaFileKeluaran = 'matiuscelciussinaga.encrypted.txt'
    kunciSaya = 10
    modeSaya = 'encrypt'

    if not os.path.exists(masukkanNamaFile):
        print('File %s yang dimaksud tidak ada. Silahkan keluar...' % (masukkanNamaFile))
        sys.exit()

    if os.path.exists(namaFileKeluaran):
        print('Tulis ulang file %s. (C)ontinue atau (Q)uit?' % (namaFileKeluaran))
        response = input('> ')

        if not response.lower().startswith('c'):
            sys.exit()

    objekFile = open(masukkanNamaFile)
    isi = objekFile.read()
    objekFile.close()

    print('%sing...' % (modeSaya.title()))

    waktuAwal = time.time()
    if modeSaya == 'encrypt':
        ubah = enkripsitransposisi.enkripsiPesan(kunciSaya, isi)
    elif modeSaya == 'decrypt':
        ubah = dekripsitransposisi.dekripsiPesan(kunciSaya, isi)
    jumlahWaktu = round(time.time() - waktuAwal, 2)
    print('%sion time: %s seconds' % (modeSaya.title(), jumlahWaktu))

    FileObjekKeluaran = open(namaFileKeluaran, 'w')
    FileObjekKeluaran.write(ubah)
    FileObjekKeluaran.close()

    print('Done %sing %s (%s characters).' % (modeSaya, masukkanNamaFile, len(isi)))
    print('%sed file is %s.' % (modeSaya.title(), namaFileKeluaran))

if __name__ == '__main__':
    main()



















