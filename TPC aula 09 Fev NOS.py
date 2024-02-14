from jjcli import *

for n in range(1088, 1095):
    comando = f'wget --no-check-certificate -r -c -l 2 "http://www.nos.uminho.pt/History.aspx?id={n}"'
    qxsystem(comando)