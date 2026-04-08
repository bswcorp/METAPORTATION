import math,os
def run():
 C,G,Y,R,W,RESET='[96m','[92m','[93m','[91m','[97m','[0m'
 os.system('clear')
 print(f'{Y}========================================{RESET}')
 print(f'{C}🏛️  STG BANK SENTRAL : UNIT 008{RESET}')
 print(f'{W}👑 ARCHITECT: ANDI M. HARPIANTO{RESET}')
 print(f'{Y}========================================{RESET}')
 print(f'{G}[#] STATUS: ANGKA BULAT TERKUNCI UTUH{RESET}')
 print(f'{G}[#] STATUS: KOMA DILEPAS UNTUK JAJAN{RESET}')
 print(f'{W}----------------------------------------{RESET}')
 v=114.0
 for i in range(1,4):
  n=v*math.sqrt(2)
  w=math.floor(n)
  k=n-w
  print(f' T{i}: BULAT={G}{w}{RESET} | KOMA={C}{k:.4f}{RESET}')
  v=float(w)
 print(f'{W}----------------------------------------{RESET}')
 print(f'{R}[!] JUJUR ITU BAIK, ITULAH STG{RESET}')
 input('
Tekan Enter...')
if __name__=='__main__':run()
