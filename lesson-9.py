#################################################################
# Meretas Sandi Transposisi                                     #
# Editor : Matius Celcius Sinaga                                #
# Author : http://inventwithpython.com/hacking (BSD Licensed)   #
# ###############################################################

import pyperclip

from helper import deteksibahasa
from helper import dekripsitransposisi

def main():
    pesanSaya = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu plri ch nitaalr eiuengiteehb(e1 hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad l t oisn sit u1rnd stara nvhn fsedbh ee,n e necrg6 8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po droB wtinue r Pieno nc ayieeto'lulcih sfnc ownaSserbereiaSm-eaiah, nnrttgcC maciiritvledastinideI nn rms iehn tsigaBmuoetcetias rn"""
    pesanSaya = retasTransposisi(pesanSaya)

    if pesanSaya == None:
        print('Gagal melakukan peretasan pada enkripsi.')
    else:
        print('Menyalin pesan yang teretas ke dalam layar:')
        print(pesanSaya)
    # pyperclip harus berada satu folder dengan program
    # pyperclip.copy(pesanYangTeretas)

def retasTransposisi(pesan):
    print('Sedang meretas...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    for kunci in range(1, len(pesan)):
        print('Mencoba kunci #%s...' % (kunci))
        pesanTerdekripsi = dekripsitransposisi.dekripsiPesan(kunci, pesan)

        if deteksibahasa.cekBahasa(pesanTerdekripsi):
            print()
            print('Kemungkinan dapat di retas:')
            print('Kunci %s: %s' % (kunci, pesanTerdekripsi[:100]))
            print()
            print('Tekan D untuk berhenti dan Enter untuk melanjutkan peretasan:')
            respon = input('> ')

            if respon.strip().upper().startswith('D'):
                return pesanTerdekripsi

    return None

if __name__ == '__main__':
    main()