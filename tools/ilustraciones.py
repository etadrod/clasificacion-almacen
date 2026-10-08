# Genera las ilustraciones SVG de los artículos añadidos (no proceden del inventario fotografiado).
import pathlib
OUT = pathlib.Path(__file__).resolve().parent / "ilustraciones"
OUT.mkdir(exist_ok=True)
K="#22252b"; G="#7d8590"; LG="#c5ccd6"; Y="#f2b705"; O="#f06a1d"; R="#d4342b"; W="#ffffff"; B="#1f5fa8"; LB="#7fb2e5"; DG="#3b4048"
S = 'stroke="#22252b" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
def hose(d, c=K): return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round"/>'
A = {}
# ---------- ACCIDENTE DE TRÁFICO ----------
A[122] = ("Separador hidráulico", f'''
<rect x="90" y="250" width="170" height="100" rx="18" fill="{Y}" {S}/>
<rect x="40" y="275" width="60" height="50" rx="10" fill="{DG}" {S}/>
<path d="M250 280 L520 170 L530 190 L270 300 Z" fill="{G}" {S}/>
<path d="M250 320 L520 430 L530 410 L270 300 Z" fill="{G}" {S}/>
<path d="M505 160 l35 20 l-12 22 Z M505 440 l35 -20 l-12 -22 Z" fill="{K}"/>
<path d="M140 250 q0 -70 70 -70 h40" fill="none" {S} />
{hose("M70 325 q-40 80 30 140 t120 40")}''')
A[123] = ("Cizalla hidráulica", f'''
<rect x="60" y="250" width="180" height="100" rx="18" fill="{Y}" {S}/>
<path d="M230 290 C330 150 470 140 540 190 C460 200 360 240 260 310 Z" fill="{G}" {S}/>
<path d="M230 310 C330 450 470 460 540 410 C460 400 360 360 260 290 Z" fill="{G}" {S}/>
<circle cx="250" cy="300" r="22" fill="{DG}" {S}/>
<path d="M110 250 q0 -70 70 -70 h30" fill="none" {S}/>
{hose("M70 340 q-30 90 60 130 t120 20")}''')
A[124] = ("Cilindro de rescate", f'''
<rect x="70" y="255" width="250" height="90" rx="14" fill="{Y}" {S}/>
<rect x="320" y="270" width="190" height="60" rx="10" fill="{LG}" {S}/>
<path d="M510 250 h40 v100 h-40 M560 260 l20 -15 M560 340 l20 15" fill="{G}" {S}/>
<path d="M70 250 h-30 v100 h30" fill="{G}" {S}/>
<path d="M150 255 q0 -60 60 -60 h40 q20 0 20 20 v40" fill="none" {S}/>
{hose("M120 345 q-20 100 80 120 t140 -10")}''')
A[125] = ("Herramienta combinada", f'''
<rect x="70" y="250" width="190" height="100" rx="18" fill="{O}" {S}/>
<path d="M250 285 L470 200 Q540 190 545 230 L280 305 Z" fill="{G}" {S}/>
<path d="M250 315 L470 400 Q540 410 545 370 L280 295 Z" fill="{G}" {S}/>
<path d="M330 265 l150 -50 M330 335 l150 50" stroke="{W}" stroke-width="5"/>
<path d="M120 250 q0 -70 70 -70 h40" fill="none" {S}/>
{hose("M80 340 q-30 90 60 130 t120 20")}''')
A[126] = ("Grupo motobomba hidráulico", f'''
<rect x="110" y="170" width="380" height="250" rx="12" fill="none" stroke="{K}" stroke-width="14"/>
<rect x="150" y="220" width="170" height="150" rx="14" fill="{R}" {S}/>
<rect x="340" y="250" width="110" height="120" rx="10" fill="{DG}" {S}/>
<circle cx="235" cy="295" r="40" fill="{DG}" {S}/>
<rect x="355" y="210" width="70" height="40" rx="8" fill="{Y}" {S}/>
<circle cx="150" cy="440" r="26" fill="{K}"/><circle cx="450" cy="440" r="26" fill="{K}"/>
{hose("M490 300 q80 0 70 90 t-60 90", O)}{hose("M490 340 q60 10 50 80 t-40 70", B)}''')
A[127] = ("Calzos escalonados de estabilización", f'''
<path d="M90 430 V370 H190 V310 H290 V250 H390 V190 H490 V430 Z" fill="{Y}" {S}/>
<path d="M90 430 l30 30 H520 l-30 -30" fill="#c99500" {S}/>
<path d="M190 370 H490 M290 310 H490 M390 250 H490" stroke="#c99500" stroke-width="4"/>
<rect x="110" y="390" width="60" height="16" fill="{K}" rx="3"/>''')
A[128] = ("Puntales de estabilización", f'''
<rect x="150" y="440" width="120" height="25" rx="5" fill="{DG}" {S}/>
<rect x="190" y="150" width="40" height="295" rx="6" fill="{LG}" {S}/>
<rect x="197" y="250" width="26" height="190" fill="{R}"/>
<path d="M175 150 h70 l-15 -40 h-40 Z" fill="{DG}" {S}/>
<rect x="340" y="440" width="120" height="25" rx="5" fill="{DG}" {S}/>
<rect x="380" y="190" width="40" height="255" rx="6" fill="{LG}" {S}/>
<rect x="387" y="270" width="26" height="170" fill="{R}"/>
<path d="M365 190 h70 l-15 -40 h-40 Z" fill="{DG}" {S}/>
<path d="M230 330 L380 360" stroke="{Y}" stroke-width="14"/>''')
A[129] = ("Protector de airbag", f'''
<circle cx="300" cy="300" r="190" fill="none" stroke="{K}" stroke-width="34"/>
<rect x="290" y="300" width="20" height="190" fill="{K}"/>
<circle cx="300" cy="300" r="120" fill="{R}" {S}/>
<text x="300" y="315" font-family="Arial" font-weight="700" font-size="42" fill="{W}" text-anchor="middle">AIRBAG</text>
<path d="M180 300 H105 M420 300 H495" stroke="{Y}" stroke-width="22"/>
<path d="M300 180 V110" stroke="{Y}" stroke-width="22"/>''')
A[130] = ("Cortacinturones y rompecristales", f'''
<rect x="170" y="230" width="270" height="90" rx="40" fill="{O}" {S} transform="rotate(-25 300 275)"/>
<path d="M410 160 q70 -20 90 40 q-40 -10 -60 20 Z" fill="{G}" {S}/>
<circle cx="455" cy="190" r="10" fill="{LG}"/>
<path d="M160 360 l-60 40 l20 20 l50 -45 Z" fill="{G}" {S}/>
<path d="M95 405 l-12 12" stroke="{K}" stroke-width="10"/>''')
A[131] = ("Cojines neumáticos de elevación", f'''
<rect x="110" y="180" width="320" height="320" rx="30" fill="{K}" transform="skewX(-12)" {S}/>
<rect x="190" y="280" width="160" height="110" rx="10" fill="{Y}" transform="skewX(-12)"/>
<text x="220" y="350" font-family="Arial" font-weight="700" font-size="46" fill="{K}">12 t</text>
<path d="M140 470 l20 -20 M480 470 l-20 -20" stroke="{G}" stroke-width="6"/>
{hose("M420 260 q90 -20 110 80 t-30 150", Y)}''')
A[132] = ("Sierra para vidrio laminado", f'''
<path d="M110 330 L430 230 L450 290 L130 390 Z" fill="{LG}" {S}/>
<path d="M130 390 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26 l20 20 l15 -26" fill="none" stroke="{K}" stroke-width="5"/>
<path d="M430 230 l90 -30 q30 10 25 50 l-15 40 l-50 15 Z" fill="{O}" {S}/>
<path d="M130 340 l-30 -80 l40 -10 l20 70" fill="{LG}" {S}/>''')
A[133] = ("Protectores de aristas cortantes", f'''
<path d="M80 200 h200 v40 h-160 v40 h160 v40 h-200 Z" fill="{R}" {S}/>
<path d="M320 300 h200 v40 h-160 v40 h160 v40 h-200 Z" fill="{Y}" {S}/>
<path d="M120 380 h140 v30 h-140 Z" fill="{R}" {S}/>
<circle cx="150" cy="260" r="10" fill="{DG}"/><circle cx="230" cy="260" r="10" fill="{DG}"/>
<circle cx="400" cy="360" r="10" fill="{DG}"/><circle cx="470" cy="360" r="10" fill="{DG}"/>''')
# ---------- RESCATE ACUÁTICO ----------
A[134] = ("Chaleco salvavidas", f'''
<path d="M180 120 h70 q20 60 50 60 q30 0 50 -60 h70 l40 70 v300 q0 20 -20 20 h-280 q-20 0 -20 -20 v-300 Z" fill="{O}" {S}/>
<path d="M300 180 V510" stroke="{K}" stroke-width="6"/>
<rect x="160" y="300" width="280" height="22" fill="{LG}"/><rect x="160" y="400" width="280" height="22" fill="{LG}"/>
<rect x="282" y="295" width="36" height="32" rx="5" fill="{K}"/><rect x="282" y="395" width="36" height="32" rx="5" fill="{K}"/>''')
A[135] = ("Aro salvavidas", f'''
<circle cx="300" cy="300" r="175" fill="none" stroke="{W}" stroke-width="90"/>
<circle cx="300" cy="300" r="175" fill="none" stroke="{R}" stroke-width="90" stroke-dasharray="137.4 137.4"/>
<circle cx="300" cy="300" r="222" fill="none" {S}/><circle cx="300" cy="300" r="128" fill="none" {S}/>
<path d="M120 300 q-30 120 60 200 q100 60 200 20 q120 -60 100 -220" fill="none" stroke="{Y}" stroke-width="8" stroke-dasharray="4 10"/>''')
A[136] = ("Tubo de rescate", f'''
<rect x="70" y="250" width="420" height="100" rx="50" fill="{R}" {S}/>
<text x="280" y="315" font-family="Arial" font-weight="700" font-size="40" fill="{W}" text-anchor="middle">RESCUE</text>
<path d="M490 300 q60 0 70 -60 q5 -60 -40 -80" fill="none" stroke="{Y}" stroke-width="10"/>
<path d="M70 285 l-30 -10 v50 l30 -10" fill="{K}"/>''')
A[137] = ("Boya torpedo", f'''
<path d="M80 300 Q80 200 300 200 Q520 200 540 300 Q520 400 300 400 Q80 400 80 300 Z" fill="{O}" {S}/>
<path d="M170 210 v-40 h80 v40 M350 210 v-40 h80 v40 M170 390 v40 h80 v-40 M350 390 v40 h80 v-40" fill="none" {S}/>
<path d="M540 300 q50 0 40 -80" fill="none" stroke="{Y}" stroke-width="10"/>''')
A[138] = ("Bolsa de lanzamiento con cuerda", f'''
<rect x="170" y="180" width="200" height="290" rx="30" fill="{R}" {S}/>
<rect x="170" y="230" width="200" height="30" fill="{LG}"/>
<ellipse cx="270" cy="180" rx="100" ry="25" fill="{DG}" {S}/>
<path d="M270 180 C300 60 450 80 430 200 S520 360 470 470" fill="none" stroke="{Y}" stroke-width="12"/>
<circle cx="470" cy="480" r="16" fill="none" stroke="{Y}" stroke-width="10"/>''')
A[139] = ("Aletas", f'''
<path d="M150 470 C120 330 140 200 200 110 L290 110 C330 210 320 340 270 470 Z" fill="{B}" {S}/>
<path d="M330 470 C300 330 320 200 380 110 L470 110 C510 210 500 340 450 470 Z" fill="{B}" {S}/>
<ellipse cx="210" cy="430" rx="55" ry="45" fill="{K}"/><ellipse cx="390" cy="430" rx="55" ry="45" fill="{K}"/>''')
A[140] = ("Traje de neopreno", f'''
<path d="M240 90 h120 l90 60 l40 170 l-40 10 l-40 -130 v360 h-60 l-50 -230 l-50 230 h-60 v-360 l-40 130 l-40 -10 l40 -170 Z" fill="{K}" {S}/>
<path d="M200 230 h200 v30 h-200 Z" fill="{B}"/>
<circle cx="300" cy="100" r="40" fill="{DG}" {S}/>''')
A[141] = ("Casco de rescate acuático", f'''
<path d="M120 360 Q120 150 300 150 Q480 150 480 360 Z" fill="{R}" {S}/>
<path d="M100 360 h400 v30 h-400 Z" fill="{DG}" {S}/>
<circle cx="230" cy="250" r="16" fill="{K}"/><circle cx="300" cy="230" r="16" fill="{K}"/><circle cx="370" cy="250" r="16" fill="{K}"/>
<path d="M160 390 q140 120 280 0" fill="none" stroke="{K}" stroke-width="10"/>''')
A[142] = ("Tabla de rescate", f'''
<path d="M70 300 Q120 200 300 200 L470 210 Q560 240 560 300 Q560 360 470 390 L300 400 Q120 400 70 300 Z" fill="{Y}" {S}/>
<path d="M100 300 H540" stroke="{R}" stroke-width="22"/>
<rect x="200" y="215" width="40" height="22" rx="8" fill="{K}"/><rect x="330" y="215" width="40" height="22" rx="8" fill="{K}"/>
<rect x="200" y="363" width="40" height="22" rx="8" fill="{K}"/><rect x="330" y="363" width="40" height="22" rx="8" fill="{K}"/>''')
A[143] = ("Máscara y tubo de buceo", f'''
<path d="M120 230 h300 q30 0 30 30 v80 q0 30 -30 30 h-90 l-40 -40 l-40 40 h-100 q-30 0 -30 -30 v-80 q0 -30 30 -30 Z" fill="{LB}" {S}/>
<path d="M90 280 h-40 M450 280 h40" stroke="{K}" stroke-width="18"/>
<path d="M500 420 V120 q0 -30 30 -30" fill="none" stroke="{O}" stroke-width="24" stroke-linecap="round"/>
<path d="M500 420 q0 50 -50 50 h-40" fill="none" stroke="{K}" stroke-width="24" stroke-linecap="round"/>''')
A[144] = ("Pértiga de rescate", f'''
<path d="M80 520 L450 150" stroke="{Y}" stroke-width="24" stroke-linecap="round"/>
<path d="M80 520 L180 420" stroke="{K}" stroke-width="28" stroke-linecap="round"/>
<path d="M450 150 q60 -60 100 -10 q30 50 -40 80" fill="none" stroke="{G}" stroke-width="18" stroke-linecap="round"/>''')
A[145] = ("Camilla de rescate acuático flotante", f'''
<path d="M70 260 h460 l-30 120 h-400 Z" fill="{O}" {S}/>
<path d="M120 260 v120 M180 260 v120 M240 260 v120 M300 260 v120 M360 260 v120 M420 260 v120 M480 260 v120" stroke="{K}" stroke-width="4"/>
<rect x="60" y="230" width="490" height="34" rx="17" fill="{Y}" {S}/>
<rect x="90" y="380" width="430" height="34" rx="17" fill="{Y}" {S}/>''')
# ---------- TRANSMISIONES ----------
def radio(x,y,s=1.0,col=K):
    return f'''<g transform="translate({x} {y}) scale({s})">
<rect x="-12" y="-150" width="22" height="130" rx="10" fill="{K}"/>
<rect x="-60" y="-30" width="140" height="280" rx="22" fill="{col}" {S}/>
<rect x="-40" y="0" width="100" height="60" rx="6" fill="{LB}"/>
<g fill="{G}"><rect x="-38" y="90" width="26" height="20" rx="4"/><rect x="-3" y="90" width="26" height="20" rx="4"/><rect x="32" y="90" width="26" height="20" rx="4"/>
<rect x="-38" y="125" width="26" height="20" rx="4"/><rect x="-3" y="125" width="26" height="20" rx="4"/><rect x="32" y="125" width="26" height="20" rx="4"/>
<rect x="-38" y="160" width="26" height="20" rx="4"/><rect x="-3" y="160" width="26" height="20" rx="4"/><rect x="32" y="160" width="26" height="20" rx="4"/></g>
<rect x="-72" y="40" width="14" height="60" rx="4" fill="{O}"/></g>'''
A[146] = ("Equipo portátil de radio (walkie)", radio(300,200,1.25))
A[147] = ("Emisora móvil de vehículo", f'''
<rect x="80" y="220" width="360" height="130" rx="16" fill="{DG}" {S}/>
<rect x="110" y="250" width="160" height="50" rx="6" fill="{LB}"/>
<circle cx="380" cy="285" r="30" fill="{G}" {S}/>
<g fill="{G}"><rect x="110" y="310" width="34" height="18" rx="4"/><rect x="155" y="310" width="34" height="18" rx="4"/><rect x="200" y="310" width="34" height="18" rx="4"/></g>
<rect x="450" y="300" width="70" height="120" rx="20" fill="{K}" {S}/>
<path d="M440 330 C400 420 470 440 450 470 C430 500 480 510 485 420" fill="none" stroke="{K}" stroke-width="6"/>''')
A[148] = ("Emisora base", f'''
<rect x="60" y="230" width="380" height="180" rx="14" fill="{G}" {S}/>
<rect x="90" y="260" width="200" height="60" rx="6" fill="{LB}"/>
<circle cx="370" cy="290" r="36" fill="{DG}" {S}/>
<g fill="{DG}"><rect x="90" y="340" width="40" height="22" rx="4"/><rect x="145" y="340" width="40" height="22" rx="4"/><rect x="200" y="340" width="40" height="22" rx="4"/><rect x="255" y="340" width="40" height="22" rx="4"/></g>
<ellipse cx="510" cy="450" rx="60" ry="18" fill="{K}"/>
<path d="M510 450 V300" stroke="{K}" stroke-width="10"/>
<rect x="485" y="250" width="50" height="70" rx="22" fill="{K}"/>''')
A[149] = ("Antena con base magnética", f'''
<path d="M300 430 V70" stroke="{K}" stroke-width="10" stroke-linecap="round"/>
<path d="M300 300 m-14 0 a14 6 0 1 0 28 0 a14 6 0 1 0 -28 0" fill="{K}"/>
<ellipse cx="300" cy="450" rx="110" ry="34" fill="{DG}" {S}/>
<rect x="280" y="410" width="40" height="40" fill="{G}" {S}/>
{hose("M380 460 q120 20 140 -60", K)}''')
A[150] = ("Batería de radio portátil", f'''
<rect x="200" y="110" width="200" height="380" rx="24" fill="{K}" {S}/>
<rect x="225" y="200" width="150" height="120" rx="8" fill="{Y}"/>
<text x="300" y="250" font-family="Arial" font-weight="700" font-size="32" fill="{K}" text-anchor="middle">Li-ion</text>
<text x="300" y="295" font-family="Arial" font-weight="700" font-size="28" fill="{K}" text-anchor="middle">7,4 V</text>
<rect x="245" y="400" width="24" height="40" rx="4" fill="{Y}"/><rect x="288" y="400" width="24" height="40" rx="4" fill="{Y}"/><rect x="331" y="400" width="24" height="40" rx="4" fill="{Y}"/>''')
A[151] = ("Cargador múltiple de equipos portátiles", f'''
<path d="M50 420 h500 l-30 80 h-440 Z" fill="{DG}" {S}/>
{radio(130,300,0.7)}{radio(250,300,0.7)}{radio(370,300,0.7)}{radio(490,300,0.7)}
<g fill="#38c172"><circle cx="130" cy="470" r="9"/><circle cx="250" cy="470" r="9"/><circle cx="370" cy="470" r="9"/></g><circle cx="490" cy="470" r="9" fill="{R}"/>''')
A[152] = ("Teléfono vía satélite", f'''
<rect x="200" y="200" width="200" height="320" rx="30" fill="{DG}" {S}/>
<rect x="330" y="60" width="50" height="160" rx="20" fill="{K}" {S}/>
<rect x="230" y="230" width="140" height="90" rx="6" fill="{LB}"/>
<g fill="{G}"><rect x="232" y="345" width="36" height="24" rx="5"/><rect x="282" y="345" width="36" height="24" rx="5"/><rect x="332" y="345" width="36" height="24" rx="5"/>
<rect x="232" y="385" width="36" height="24" rx="5"/><rect x="282" y="385" width="36" height="24" rx="5"/><rect x="332" y="385" width="36" height="24" rx="5"/>
<rect x="232" y="425" width="36" height="24" rx="5"/><rect x="282" y="425" width="36" height="24" rx="5"/><rect x="332" y="425" width="36" height="24" rx="5"/></g>''')
A[153] = ("Megáfono", f'''
<path d="M180 250 L470 130 V470 L180 350 Z" fill="{W}" {S}/>
<ellipse cx="470" cy="300" rx="40" ry="170" fill="{R}" {S}/>
<rect x="110" y="245" width="80" height="110" rx="14" fill="{R}" {S}/>
<path d="M200 350 v120 h50 v-100" fill="{K}" {S}/>
<path d="M520 220 q40 80 0 160 M550 190 q60 110 0 220" fill="none" stroke="{G}" stroke-width="8"/>''')
A[154] = ("Micrófono altavoz de mano", f'''
<rect x="210" y="150" width="180" height="250" rx="40" fill="{K}" {S}/>
<g fill="{G}">{''.join(f'<rect x="245" y="{y}" width="110" height="10" rx="5"/>' for y in range(190,330,24))}</g>
<rect x="190" y="230" width="20" height="80" rx="6" fill="{O}"/>
<path d="M300 400 c0 40 -60 30 -60 70 s60 30 60 70 s-60 30 -60 50" fill="none" stroke="{K}" stroke-width="8"/>''')
A[155] = ("Repetidor portátil", f'''
<rect x="90" y="250" width="420" height="230" rx="20" fill="{Y}" {S}/>
<rect x="120" y="280" width="360" height="130" rx="8" fill="{DG}"/>
<rect x="140" y="300" width="150" height="40" rx="4" fill="{LB}"/>
<g fill="#38c172"><circle cx="330" cy="320" r="10"/><circle cx="365" cy="320" r="10"/></g>
<path d="M150 430 h300" stroke="{K}" stroke-width="8"/>
<path d="M180 250 V90 M420 250 V90" stroke="{K}" stroke-width="10" stroke-linecap="round"/>''')
A[156] = ("Kit auricular con pulsador (PTT)", f'''
<path d="M160 120 q-60 0 -60 70 q0 60 60 60 h20 v-130 Z" fill="{K}" {S}/>
<path d="M175 200 C260 220 230 320 300 330" fill="none" stroke="{LG}" stroke-width="10"/>
<path d="M300 330 c40 10 20 60 60 70 s20 60 60 70" fill="none" stroke="{K}" stroke-width="8"/>
<rect x="400" y="440" width="110" height="70" rx="16" fill="{DG}" {S}/>
<circle cx="455" cy="475" r="20" fill="{O}"/>''')
A[157] = ("Mástil telescópico de antena", f'''
<path d="M300 420 L180 520 M300 420 L420 520 M300 420 V520" stroke="{K}" stroke-width="12" stroke-linecap="round"/>
<rect x="282" y="250" width="36" height="180" fill="{G}" {S}/>
<rect x="288" y="150" width="24" height="110" fill="{LG}" {S}/>
<rect x="293" y="80" width="14" height="80" fill="{LG}" {S}/>
<path d="M300 80 V30 M250 70 L300 40 L350 70" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>''')

# ---------- EXTINCIÓN DE INCENDIOS ----------
def ext(col, label, horn=False):
    h = f'<path d="M330 150 q90 0 110 120 l40 30 l-20 25 l-50 -30" fill="{K}" {S}/>' if horn else f'<path d="M330 150 q100 10 110 130" fill="none" stroke="{K}" stroke-width="14"/><path d="M430 270 l20 40 l-30 5 Z" fill="{K}"/>'
    return f'''<rect x="210" y="170" width="180" height="340" rx="60" fill="{col}" {S}/>
<rect x="240" y="270" width="120" height="130" rx="8" fill="{W}"/>
<text x="300" y="350" font-family="Arial" font-weight="700" font-size="40" fill="{K}" text-anchor="middle">{label}</text>
<rect x="270" y="120" width="60" height="55" fill="{DG}" {S}/>
<path d="M260 120 h120 l-10 -25 h-90 Z" fill="{K}"/>
<circle cx="300" cy="150" r="12" fill="{LG}"/>{h}'''
A[158] = ("Extintor de polvo ABC", ext(R,"ABC"))
A[159] = ("Extintor de CO2", ext(R,"CO2",True))
A[160] = ("Manguera de 45 mm enrollada", f'''
<circle cx="300" cy="300" r="190" fill="{R}" {S}/>
{''.join(f'<circle cx="300" cy="300" r="{r}" fill="none" stroke="#a52520" stroke-width="5"/>' for r in range(60,190,26))}
<circle cx="300" cy="300" r="50" fill="{LG}" {S}/>
<rect x="470" y="270" width="70" height="60" rx="8" fill="{LG}" {S}/>''')
A[161] = ("Manguera de 70 mm", f'''
<path d="M90 470 C90 300 500 380 480 200 C470 120 380 110 360 150" fill="none" stroke="{K}" stroke-width="58" stroke-linecap="round"/>
<path d="M90 470 C90 300 500 380 480 200 C470 120 380 110 360 150" fill="none" stroke="{Y}" stroke-width="46" stroke-linecap="round"/>
<rect x="45" y="460" width="90" height="60" rx="8" fill="{LG}" {S}/>
<rect x="320" y="110" width="80" height="60" rx="8" fill="{LG}" {S} transform="rotate(-30 360 140)"/>''')
A[162] = ("Lanza de caudal variable", f'''
<rect x="110" y="270" width="230" height="70" rx="14" fill="{LG}" {S}/>
<path d="M340 260 h120 l40 -20 v130 l-40 -20 h-120 Z" fill="{R}" {S}/>
<path d="M500 240 l60 -40 M500 305 h70 M500 370 l60 40" stroke="{B}" stroke-width="8" stroke-dasharray="10 10"/>
<path d="M190 340 v100 h60 v-100" fill="{K}" {S}/>
<path d="M240 270 l40 -60 h40" fill="none" stroke="{K}" stroke-width="14" stroke-linecap="round"/>
<rect x="60" y="275" width="60" height="60" rx="6" fill="{G}" {S}/>''')
A[163] = ("Bifurcación", f'''
<rect x="90" y="270" width="140" height="70" rx="10" fill="{LG}" {S}/>
<path d="M230 260 h80 l120 -100 l40 45 l-100 85 v20 l100 85 l-40 45 l-120 -100 h-80 Z" fill="{LG}" {S}/>
<rect x="420" y="130" width="70" height="60" rx="8" fill="{G}" {S} transform="rotate(-40 455 160)"/>
<rect x="420" y="410" width="70" height="60" rx="8" fill="{G}" {S} transform="rotate(40 455 440)"/>
<circle cx="350" cy="190" r="22" fill="{R}" {S}/><circle cx="350" cy="410" r="22" fill="{R}" {S}/>''')
A[164] = ("Llave de racores", f'''
<path d="M120 470 L400 190" stroke="{G}" stroke-width="40" stroke-linecap="round"/>
<path d="M400 190 m-70 0 a90 90 0 1 1 90 90 l-30 -40 a45 45 0 1 0 -45 -45 Z" fill="{G}" {S}/>
<circle cx="140" cy="450" r="16" fill="{K}"/>''')
A[165] = ("Hidrante y llave de hidrante", f'''
<rect x="200" y="200" width="160" height="290" rx="20" fill="{R}" {S}/>
<path d="M190 200 q90 -110 180 0 Z" fill="{R}" {S}/>
<rect x="150" y="300" width="60" height="60" rx="8" fill="{LG}" {S}/><rect x="350" y="300" width="60" height="60" rx="8" fill="{LG}" {S}/>
<rect x="170" y="480" width="220" height="30" rx="6" fill="{DG}" {S}/>
<path d="M440 140 h120 M500 140 v220" stroke="{K}" stroke-width="20" stroke-linecap="round"/>''')
A[166] = ("Lanza de espuma", f'''
<path d="M120 260 h200 l200 -40 v160 l-200 -40 h-200 Z" fill="{LG}" {S}/>
<rect x="60" y="270" width="70" height="60" rx="8" fill="{G}" {S}/>
<circle cx="250" cy="300" r="14" fill="{K}"/>
<path d="M250 314 C240 400 300 420 330 480" fill="none" stroke="{K}" stroke-width="8"/>
<g fill="{W}" stroke="{G}" stroke-width="3"><circle cx="545" cy="250" r="16"/><circle cx="560" cy="300" r="20"/><circle cx="545" cy="350" r="16"/></g>''')
A[167] = ("Bidón de espumógeno", f'''
<path d="M160 170 h280 v320 q0 20 -20 20 h-240 q-20 0 -20 -20 Z" fill="{Y}" {S}/>
<rect x="190" y="120" width="70" height="50" rx="6" fill="{K}"/>
<path d="M330 170 v-50 h80 v50" fill="none" {S}/>
<rect x="190" y="260" width="220" height="120" rx="8" fill="{W}"/>
<text x="300" y="310" font-family="Arial" font-weight="700" font-size="34" fill="{K}" text-anchor="middle">ESPUMA</text>
<text x="300" y="352" font-family="Arial" font-weight="700" font-size="28" fill="{K}" text-anchor="middle">AFFF 3%</text>''')
# ---------- INCENDIO URBANO ----------
A[168] = ("Hacha de bombero", f'''
<path d="M140 500 L410 150" stroke="#9c6b3c" stroke-width="30" stroke-linecap="round"/>
<path d="M360 110 l120 -20 q40 60 -10 130 l-110 -40 Z" fill="{LG}" {S}/>
<path d="M370 150 l-80 -50 l20 -30 Z" fill="{G}" {S}/>
<path d="M140 500 L190 435" stroke="{R}" stroke-width="34" stroke-linecap="round"/>''')
A[169] = ("Barra de entrada forzada (Halligan)", f'''
<path d="M140 460 L450 150" stroke="{G}" stroke-width="30" stroke-linecap="round"/>
<path d="M450 150 l60 -10 l-10 30 Z M430 130 l20 -70 l25 15 Z" fill="{G}" {S}/>
<path d="M140 460 l-40 30 q-20 10 -10 -15 l30 -45" fill="{G}" {S}/>
<path d="M120 470 l-30 -60" stroke="{K}" stroke-width="6"/>''')
A[170] = ("Gancho de techo", f'''
<path d="M120 520 L420 120" stroke="{Y}" stroke-width="22" stroke-linecap="round"/>
<path d="M420 120 l40 -50 M420 120 q60 10 50 70 l-30 -10" fill="none" stroke="{G}" stroke-width="18" stroke-linecap="round"/>
<path d="M120 520 L170 455" stroke="{K}" stroke-width="28" stroke-linecap="round"/>''')
A[171] = ("Ventilador de presión positiva", f'''
<circle cx="300" cy="270" r="190" fill="{DG}" {S}/>
<circle cx="300" cy="270" r="160" fill="none" stroke="{LG}" stroke-width="6"/>
{''.join(f'<path d="M300 270 q{40} -110 {0} -140 q-40 30 0 140" fill="{G}" transform="rotate({a} 300 270)"/>' for a in range(0,360,60))}
<circle cx="300" cy="270" r="26" fill="{R}" {S}/>
<path d="M150 450 l-30 70 h360 l-30 -70" fill="none" {S}/>''')
A[172] = ("Cámara térmica", f'''
<rect x="140" y="160" width="320" height="230" rx="34" fill="{Y}" {S}/>
<rect x="180" y="195" width="240" height="160" rx="10" fill="{K}"/>
<rect x="190" y="205" width="220" height="140" rx="6" fill="#4a1d6b"/>
<ellipse cx="300" cy="275" rx="45" ry="55" fill="#f0a020"/><ellipse cx="300" cy="275" rx="22" ry="28" fill="#fff07a"/>
<rect x="260" y="390" width="80" height="120" rx="16" fill="{K}" {S}/>''')
A[173] = ("Escalera de ganchos", f'''
<path d="M230 520 V140 M370 520 V140" stroke="#9c6b3c" stroke-width="22" stroke-linecap="round"/>
{''.join(f'<path d="M230 {y} H370" stroke="#9c6b3c" stroke-width="12"/>' for y in range(180,520,50))}
<path d="M230 140 q0 -70 70 -70 q60 0 40 60" fill="none" stroke="{G}" stroke-width="16" stroke-linecap="round"/>''')
A[174] = ("Cortina portátil antihumo", f'''
<rect x="170" y="90" width="260" height="420" fill="none" stroke="{K}" stroke-width="12"/>
<rect x="182" y="102" width="236" height="300" fill="{R}"/>
<path d="M182 402 h236" stroke="{K}" stroke-width="6"/>
<text x="300" y="270" font-family="Arial" font-weight="700" font-size="34" fill="{W}" text-anchor="middle">HUMO</text>
<path d="M200 470 q50 -40 100 0 t100 0" fill="none" stroke="{G}" stroke-width="10"/>''')
A[175] = ("Abrepuertas hidráulico", f'''
<rect x="110" y="250" width="260" height="90" rx="16" fill="{Y}" {S}/>
<path d="M370 260 h120 l40 15 v40 l-40 15 h-120 Z" fill="{G}" {S}/>
<path d="M490 260 l60 -20 v110 l-60 -20" fill="{LG}" {S}/>
<rect x="150" y="200" width="70" height="50" rx="8" fill="{K}"/>
<path d="M180 200 V140 h120" fill="none" stroke="{K}" stroke-width="12"/>''')
A[176] = ("Ariete de entrada forzada", f'''
<rect x="100" y="240" width="400" height="120" rx="20" fill="{DG}" {S}/>
<rect x="480" y="225" width="60" height="150" rx="10" fill="{K}"/>
<path d="M200 240 v-60 h80 v60 M330 240 v-60 h80 v60" fill="none" stroke="{Y}" stroke-width="16"/>''')
A[177] = ("Detector multigás", f'''
<rect x="200" y="130" width="200" height="340" rx="30" fill="{Y}" {S}/>
<rect x="230" y="170" width="140" height="110" rx="8" fill="{K}"/>
<text x="300" y="215" font-family="Arial" font-weight="700" font-size="24" fill="#38c172" text-anchor="middle">O2 20,9</text>
<text x="300" y="255" font-family="Arial" font-weight="700" font-size="24" fill="#38c172" text-anchor="middle">CO 0</text>
<circle cx="300" cy="350" r="34" fill="{DG}" {S}/>
<rect x="250" y="410" width="100" height="22" rx="6" fill="{R}"/>''')

def svg(body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
<rect width="600" height="600" fill="#eef1f5"/>{body}
<text x="584" y="586" font-family="Arial" font-size="18" fill="#8a93a0" text-anchor="end">Imagen ilustrativa</text></svg>'''
for i,(n,b) in A.items(): (OUT/f"{i}.svg").write_text(svg(b), encoding="utf-8")
NAMES = {i:n for i,(n,b) in A.items()}
if __name__=="__main__": print(len(A))
