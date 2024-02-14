from jjcli import *

for n in range(13,17):
    comando= f'wget -r -c -l 2 "https://www.comumonline.com/page/{n}/?s=entrevista"'
    qxsystem (comando)