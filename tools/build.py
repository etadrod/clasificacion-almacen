# Uso: python3 tools/build.py  (desde la raíz del repo) -> genera public/index.html
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root/"tools"))
from clave import K
items = json.loads((root/"tools/articulos.json").read_text(encoding="utf-8"))
items = [{"id":it["id"], "n":it["n"], "k":K[it["id"]]} for it in items]  # solo nombre: sin marca, modelo ni stock
assert len(items)==187 and all(it.get("k") for it in items)
src = (root/"app.html").read_text(encoding="utf-8")
(root/"public/index.html").write_text(src.replace("/*ITEMS*/[]", json.dumps(items, ensure_ascii=False, separators=(",",":"))), encoding="utf-8")
print("OK", len(items))
