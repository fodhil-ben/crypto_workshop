from Crypto.Util.number import getPrime, bytes_to_long
from flag import FLAG2

primes = []
n = 1
e = 65537
while len(primes) != 32:
    tmp = getPrime(10)
    print(tmp)
    if tmp not in primes:
        n *= tmp
        primes.append(tmp)

m = bytes_to_long(FLAG2)
c = pow(m, e, n)
print(f'{n=}')
print(f'{e=}')
print(f'{c=}')

# n=102276369704640839630060455250719684637490634382082133780033051769428454756135375671827059173
# e=65537
# c=17521772226817481212411625777640035344169153092516205939759562959547518270984721354985216349


