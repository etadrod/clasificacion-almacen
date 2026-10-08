# Clasificación del almacén

App web para el alumnado del Módulo 1510 *Gestión de recursos de emergencias y protección civil* (CFGS Coordinación de Emergencias y Protección Civil, Canarias). Actividad preparatoria del registro de artículos del almacén.

- A cada alumno se le asignan 30 artículos al azar de 157 (121 del inventario con foto real y 36 con imagen ilustrativa para Accidente de Tráfico, Rescate Acuático y Transmisiones), repartidos por turnos entre las categorías para que todas las que tienen material estén representadas.
- Clasificación en 13 categorías: ficha con foto (teclas A–M), tabla de revisión, glosario.
- «Finalizar y corregir» bloquea las respuestas, muestra la solución y la nota (aciertos/30 × 10) y genera el informe PDF para Moodle.

Estructura:
- `app.html`: fuente de la app.
- `tools/articulos.json`: artículos del inventario. `tools/clave.py`: clave de corrección (categoría correcta y alternativas válidas).
- `python3 tools/build.py` genera `public/index.html` (sitio estático publicado en Render).
- `tools/ilustraciones.py`: genera las ilustraciones SVG de los artículos 122–157 (`tools/ilustraciones/`).
- `public/img/`: fotos (`<ID>.jpg` y miniatura `<ID>_t.jpg`). `public/vendor/`: jsPDF y jsPDF-AutoTable (MIT).
