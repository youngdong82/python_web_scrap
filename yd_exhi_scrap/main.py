from kukje import move_current_page as extract_kukje
from sonje import move_current_page as extract_sonje
from kukje import move_current_page as extract_arko


kukje = extract_kukje()
sonje = extract_sonje()
arko = extract_arko()

exhibitions = kukje + sonje + arko

for i in exhibitions:
  print(i)
  
print(len(exhibitions))