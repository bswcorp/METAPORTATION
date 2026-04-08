import os,time
def menu():
 C,G,Y,R,W,M,RESET = '[96m','[92m','[93m','[91m','[97m','[95m','[0m'
 while True:
  os.system('clear')
  print(f'{Y}===================================={RESET}')
  print(f'{C}🏛️ STG-OS : EXECUTIVE HUB (BROADCAST){RESET}')
  print(f'{W}👑 ARCHITECT: ANDI M. HARPIANTO | 114 BT{RESET}')
  print(f'{Y}===================================={RESET}')
  print(f'{G} [001] VETO ROOT    [008] BANK SENTRAL{RESET}')
  print(f'{G} [111] SALDO TRUST  [222] CENTRAL HUB{RESET}')
  print(f'{R} [212] MILITER      [666] AXIS 114 BT{RESET}')
  print(f'{M} [810] SHOWROOM     [999] SIRI/AIGARTH{RESET}')
  print(f'{W} [000] PARKIR EXIT{RESET}')
  print(f'{Y}===================================={RESET}')
  p = input(f'{C}👉 PILIH UNIT: {RESET}')
  if p=='001':os.system('python3 stg_shell.py')
  elif p=='008':os.system('python3 bank_stg_core.py')
  elif p=='111':os.system('python3 sonar_gas_recovery.py')
  elif p=='222':os.system('python3 reality_checker.py')
  elif p=='212':os.system('python3 real_laser_sovereign.py')
  elif p=='666':os.system('python3 koordinat_114.py')
  elif p=='810':os.system('bash ~/METAPORTATION/panggil_senjata.sh')
  elif p=='999':os.system('python3 aigarth.py')
  elif p=='000':break
  else:time.sleep(1)
if __name__ == '__main__': menu()
