#import subprocess

#for n in range(1148, 1150):
    #comando = f'wget -r -c -l 2 "http://www.nos.uminho.pt/History.aspx?id={n}"'
   # subprocess.run(comando, shell=True)

from jjcli import*

for n in range(1067, 1150):
    comando = f'wget -r -c -l2 "http://www.nos.uminho.pt/History.aspx?id={n}"'
    subprocess.run(comando, shell=True)

