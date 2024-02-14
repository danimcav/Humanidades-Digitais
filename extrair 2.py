from jjcli import *

for n in range(1,53):
    comando= f'wget -r -c -l 2 "https://www.comumonline.com/page/{n}/?s=entrevista"'
    qxsystem (comando)