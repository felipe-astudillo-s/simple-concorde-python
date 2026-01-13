import random
from concorde_solver import ConcordeSolver

def main():
    # 1. Configuración
    CANTIDAD_CIUDADES = 50
    NOMBRE_ARCHIVO = "mis_datos" # Sin extensión
    
    # 2. Generar datos de prueba (Simulando tus datos reales)
    print(f"--- Generando {CANTIDAD_CIUDADES} ciudades aleatorias ---")
    coordenadas = []
    for _ in range(CANTIDAD_CIUDADES):
        x = random.uniform(0, 1000) # Usamos float para ser más realistas
        y = random.uniform(0, 1000)
        coordenadas.append((x, y))

    # 3. Inicializar el Solver
    try:
        solver = ConcordeSolver(executable_path="./concorde")
    except FileNotFoundError as e:
        print(e)
        return

    # 4. Crear el archivo TSP
    tsp_file = solver.create_tsp_file(coordenadas, f"{NOMBRE_ARCHIVO}.tsp")
    print(f"Archivo TSP creado en: {tsp_file}")

    # 5. Resolver
    print("Ejecutando Concorde...")
    sol_file = solver.run_solver(tsp_file)

    if sol_file:
        # 6. Leer y mostrar resultados
        tour_indices = solver.read_solution(sol_file)
        
        print("\n✅ ¡Ruta Óptima Encontrada!")
        print(f"Orden de visita (índices): {tour_indices}")
        
        # Opcional: Reconstruir la ruta con coordenadas para usarla después
        ruta_final = [coordenadas[i] for i in tour_indices]
        print(f"Primera ciudad: {ruta_final[0]}")
        print(f"Última ciudad: {ruta_final[-1]}")
        
        # 7. Limpieza (Opcional, si quieres borrar los archivos generados)
        # solver.cleanup(NOMBRE_ARCHIVO) 
        # print("\nArchivos temporales eliminados.")
    else:
        print("❌ No se pudo encontrar la solución.")

if __name__ == "__main__":
    main()
