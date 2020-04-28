################################################################
# Membalikkan Sandi
# Editor : Matius Celcius Sinaga
# Author : http://inventwithpython.com/hacking (BSD Licensed)
################################################################

pesan = 'Indonesia Raya'
ubah = ''
i = len(pesan) - 1

while i >= 0:
    ubah = ubah + pesan[i]
    i = i - 1

print(ubah)

