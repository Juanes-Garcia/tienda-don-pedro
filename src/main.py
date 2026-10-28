from pathlib import Path

# Ubica la ruta del proyecto y el archivo de productos
carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"

# Lee todas las líneas del archivo
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

total_productos = 0
valor_inventario = 0

# Iteramos sobre todas las líneas del archivo
for linea in lineas:
    if linea.strip():  # Si la línea no está vacía
        print("-", linea)
        total_productos += 1
        
        # Extraemos el precio después del símbolo '$'
        partes = linea.split("$")
        if len(partes) > 1:
            precio_limpio = partes[1].replace(".", "").strip()
            valor_inventario += int(precio_limpio)

print("-" * 35)
print(f"Total de productos: {total_productos}")
print(f"Valor del inventario: ${valor_inventario}")