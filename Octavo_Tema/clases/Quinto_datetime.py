from datetime import datetime

despierta = datetime(2024, 10 , 5 , 8, 30)
duerme = datetime(2024, 10, 5, 23, 50)
vigilia = duerme - despierta

print(vigilia.seconds)


