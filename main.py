import subprocess
import os
import random

# CONFIGURACIÓN
EJECUTABLE = "./concorde"
ARCHIVO_TSP = "demo.tsp"
ARCHIVO_SOL = "demo.sol"
CANTIDAD_CIUDADES = 50  # Número de ciudades para la prueba

def generar_tsp_random(filename, n):
    """Genera un archivo TSP con coordenadas aleatorias."""
    print(f"[1] Generando {n} ciudades aleatorias en {filename}...")
    with open(filename, 'w') as f:
        f.write(f"NAME: Demo\nTYPE: TSP\nDIMENSION: {n}\n")
        f.write("EDGE_WEIGHT_TYPE: EUC_2D\nNODE_COORD_SECTION\n")
        for i in range(1, n + 1):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            f.write(f"{i} {x}.0 {y}.0\n")
        f.write("EOF\n")

def correr_concorde():
    """Ejecuta Concorde llamando al proceso del sistema."""
    if not os.path.exists(EJECUTABLE):
        print(f"ERROR: No se encuentra el archivo {EJECUTABLE}")
        return False

    print(f"[2] Ejecutando Concorde...")
    try:
        # Usamos la configuración compatible para Python 3.6 hasta el más nuevo
        # Quitamos -x y -o para imitar el comando manual que sí funcionó
        comando = [EJECUTABLE, ARCHIVO_TSP]
        # -x: borra archivos temporales
        # -o: define nombre de salida explícito
        
        resultado = subprocess.run(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        if resultado.returncode == 0:
            print("    -> Concorde terminó con éxito.")
            return True
        else:
            print("    -> Error interno de Concorde.")
            print(resultado.stderr)
            return False

    except PermissionError:
        print(f"ERROR: Permiso denegado. Ejecuta: chmod +x {EJECUTABLE}")
        return False
    except Exception as e:
        print(f"ERROR inesperado: {e}")
        return False

def leer_solucion():
    """Lee el archivo .sol generado."""
    if not os.path.exists(ARCHIVO_SOL):
        print("ERROR: No se generó el archivo de solución.")
        return

    print(f"[3] Leyendo solución...")
    with open(ARCHIVO_SOL, 'r') as f:
        lines = f.read().split()
        # La primera línea es el número de nodos
        num_nodos = lines[0]
        # El resto es la ruta
        ruta = lines[1:]
        
    print(f"\n✅ RESULTADO FINAL:")
    print(f"   Ruta óptima encontrada para {num_nodos} ciudades:")
    print(f"   {ruta}")

# --- FLUJO PRINCIPAL ---
if __name__ == "__main__":
    if os.path.exists(ARCHIVO_SOL): os.remove(ARCHIVO_SOL) # Limpieza previa
    
    generar_tsp_random(ARCHIVO_TSP, CANTIDAD_CIUDADES)
    if correr_concorde():
        leer_solucion()
