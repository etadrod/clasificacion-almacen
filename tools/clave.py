# Clave de corrección: ID -> [categoría correcta, alternativas también válidas...]
# Editar aquí y ejecutar tools/build.py para regenerar public/index.html
EPI="EPIs"; IF="Incendio Forestal"; IU="Incendio Urbano"; RT="Rescate Tierra"; SAN="Sanitario"
LOG="Logística"; SEG="Seguridad"; SEN="Señalización"; HER="Herramientas y ferretería"; EXT="Extinción de Incendios"; AT="Accidente de Tráfico"
K = {}
for i in range(1,8): K[i]=[EPI,SEN]           # chalecos (alta visibilidad / identificación)
K[8]=[EPI,LOG]                                   # camisetas de uniformidad
for i in (9,10,11,12,13,14): K[i]=[EPI]          # botas, pantalón, cinturón, guantes
K[15]=[HER,EPI,SEN]                              # linterna frontal
K[16]=[EPI,RT]; K[17]=[EPI,IF,RT]; K[18]=[EPI]; K[19]=[EPI,IF]; K[20]=[EPI,IF]; K[21]=[EPI,IU]  # cascos
K[22]=[IF,EXT]                                   # mochila de extinción
K[23]=[LOG,EPI,IF]                               # camel back (hidratación)
for i in (24,25,26,27,28): K[i]=[IF]             # herramienta forestal
K[29]=[IF,HER]                                   # pico
K[30]=[EPI,IU]; K[31]=[EPI,IU]                   # trajes de bombero
for i in (32,33,34,35,36): K[i]=[EPI]            # trajes de intervención, casco
K[37]=[RT,EPI]                                   # material de cuerda
for i in (38,39,41): K[i]=[EPI]                  # gafas, viseras
K[40]=[SAN]; K[42]=[SAN]                         # oxígeno, equipo de emergencias
K[43]=[HER,LOG]                                  # destructora de papel
K[44]=[SAN]; K[45]=[IF,EPI]; K[46]=[SAN]; K[47]=[SEN]; K[48]=[SAN]   # maniquí RCP, fire shelter, DEA, señales, kit RCP
for i in range(49,55): K[i]=[SAN,AT]             # collarines
K[55]=[SAN]; K[56]=[EPI]; K[57]=[EPI]
for i in (58,59,60,62): K[i]=[LOG]               # raciones
K[61]=[EPI]; K[63]=[LOG,SAN]; K[64]=[EPI]; K[65]=[RT]; K[66]=[SAN]
K[67]=[SEN]; K[68]=[EPI]; K[69]=[SEN]; K[70]=[EPI]
K[71]=[RT]; K[72]=[RT,EPI]; K[73]=[SEN]; K[74]=[EPI,LOG]
for i in range(75,100): K[i]=[RT]                # material de rescate en altura
K[100]=[EXT,EPI,IU]                              # Dräger
K[101]=[HER]; K[102]=[HER,SEG]; K[103]=[RT]
K[104]=[LOG]; K[105]=[LOG]                       # mesa de simulación, pizarras GOM
K[106]=[IF,EPI]; K[107]=[IU,EPI]                 # maniquíes uniformados
for i in range(108,121): K[i]=[SEG]
K[110]=[SEG,EPI]; K[113]=[SEG,HER]; K[114]=[SEG,EPI]
K[121]=[SEN,SEG]                                 # cono de linterna
