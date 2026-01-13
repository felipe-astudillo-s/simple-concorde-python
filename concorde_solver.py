import subprocess
import os
import shutil

class ConcordeSolver:
    def __init__(self, executable_path="./concorde"):
        self.executable = executable_path
        # Verificamos que el ejecutable exista al iniciar
        if not os.path.exists(self.executable):
            raise FileNotFoundError(f"No se encuentra el ejecutable en: {self.executable}")

    def create_tsp_file(self, points, filename="problem.tsp"):
        """
        Toma una lista de tuplas (x, y) y genera un archivo formateado TSPLIB.
        Ejemplo points: [(0,0), (10,5), (3,8)...]
        """
        num_points = len(points)
        with open(filename, 'w') as f:
            f.write(f"NAME: {filename}\n")
            f.write("TYPE: TSP\n")
            f.write(f"DIMENSION: {num_points}\n")
            f.write("EDGE_WEIGHT_TYPE: EUC_2D\n") # Distancia Euclideana 2D estándar
            f.write("NODE_COORD_SECTION\n")
            for i, (x, y) in enumerate(points):
                # Concorde usa índices empezando en 1 para el archivo TSP
                f.write(f"{i+1} {x} {y}\n")
            f.write("EOF\n")
        
        return os.path.abspath(filename)

    def run_solver(self, tsp_filename):
        """
        Ejecuta Concorde sobre el archivo TSP dado.
        Retorna el path del archivo de solución (.sol) si tiene éxito.
        """
        if not os.path.exists(tsp_filename):
            raise FileNotFoundError(f"No se encuentra el archivo de datos: {tsp_filename}")

        # Ejecutamos Concorde (sin banderas raras para máxima compatibilidad)
        # qsopt.a debe estar en la misma carpeta para problemas grandes
        comando = [self.executable, tsp_filename]
        
        try:
            # subprocess.PIPE captura la salida para que no ensucie la terminal
            result = subprocess.run(
                comando, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            # Nombre esperado del archivo de solución
            sol_filename = tsp_filename.replace(".tsp", ".sol")
            
            if result.returncode == 0 and os.path.exists(sol_filename):
                return sol_filename
            else:
                print("Error ejecutando Concorde:")
                print(result.stdout)
                return None
                
        except Exception as e:
            print(f"Error crítico: {e}")
            return None

    def read_solution(self, sol_filename):
        """Lee el archivo .sol y devuelve la lista de índices ordenados."""
        with open(sol_filename, 'r') as f:
            lines = f.read().split()
            # El primer número es la cantidad de nodos (lo saltamos)
            # El resto son los índices del tour (0-based)
            tour = [int(n) for n in lines[1:]]
        return tour

    def cleanup(self, filename_base):
        """Limpia los archivos temporales generados por Concorde."""
        extensions = ['.tsp', '.sol', '.mas', '.pul', '.sav', '.res']
        for ext in extensions:
            f = filename_base + ext
            if os.path.exists(f):
                os.remove(f)
