import streamlit as st
import time
from maze_solver import MAZE, START, END, solve_maze_bfs, solve_maze_dfs, solve_maze_astar

# Configuración de página simple
st.set_page_config(page_title="Visualizador de Laberinto", layout="centered")

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

# --- FUNCIÓN DE RENDERIZADO (Estilo exacto) ---
def render_maze(maze, path=None):
    if path is None:
        path = []
    
    path_set = set(path)
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀")
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")
            elif (r_idx, c_idx) in path_set:
                display_row.append("🔹")
            elif col == 1:
                display_row.append("⬛")
            else:
                display_row.append("⬜")
        
        display_maze.append("".join(display_row))
    
    st.markdown(
        f"""
        <div style="line-height: 1.0; font-size: 20px; text-align: center; white-space: nowrap;">
            {'<br>'.join(display_maze)}
        </div>
        """, 
        unsafe_allow_html=True
    )

# --- SIDEBAR DE OPCIONES ---
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS (Amplitud)", "DFS (Profundidad)", "A* (A-Star)"])
solve_button = st.sidebar.button("Resolver Laberinto")

# --- LÓGICA PRINCIPAL ---
if solve_button:
    path = None
    
    # 1. Medir tiempo de inicio
    start_time = time.perf_counter()
    
    # 2. Ejecutar algoritmo
    if "BFS" in algorithm:
        path = solve_maze_bfs(MAZE, START, END)
    elif "DFS" in algorithm:
        path = solve_maze_dfs(MAZE, START, END)
    elif "A*" in algorithm:
        path = solve_maze_astar(MAZE, START, END)
    
    # 3. Medir tiempo final
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # Convertir a milisegundos

    if path:
        st.success(f"¡Camino encontrado con {algorithm}!")
        
        # 4. Mostrar métricas (Tiempo y Pasos)
        col1, col2 = st.columns(2)
        col1.metric("⏱️ Tiempo de ejecución", f"{elapsed_time:.4f} ms")
        col2.metric("👣 Pasos totales", len(path))
        
        render_maze(MAZE, path)
    else:
        st.error("No se encontró un camino.")
        render_maze(MAZE)
else:
    render_maze(MAZE)