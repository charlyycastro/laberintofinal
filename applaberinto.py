import streamlit as st
import time
from maze_solver import MAZE, START, END, solve_maze_bfs, solve_maze_dfs, solve_maze_astar

# Configuración de página simple
st.set_page_config(page_title="Visualizador de Laberinto", layout="centered")

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

# --- FUNCIÓN DE RENDERIZADO IDÉNTICA A TU IMAGEN ---
def render_maze(maze, path=None):
    if path is None:
        path = []
    
    # Convertimos el camino a un set para verificar rápido
    path_set = set(path)
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            # Lógica exacta de tus emojis originales
            if (r_idx, c_idx) == START:
                display_row.append("🚀")  # Inicio (Cohete)
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")  # Fin (Bandera)
            elif (r_idx, c_idx) in path_set:
                display_row.append("🔹")  # Camino resuelto (Rombo azul pequeño)
            elif col == 1:
                display_row.append("⬛")  # Muro (Cuadro negro grande)
            else:
                display_row.append("⬜")  # Camino libre (Cuadro blanco grande)
        
        display_maze.append("".join(display_row))
    
    # Usamos un estilo de línea ajustado para que los cuadros se vean pegados como en la imagen
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
    
    # Ejecutamos el algoritmo seleccionado
    if "BFS" in algorithm:
        path = solve_maze_bfs(MAZE, START, END)
    elif "DFS" in algorithm:
        path = solve_maze_dfs(MAZE, START, END)
    elif "A*" in algorithm:
        path = solve_maze_astar(MAZE, START, END)

    if path:
        st.success(f"¡Camino encontrado con {algorithm}!")
        render_maze(MAZE, path)
    else:
        st.error("No se encontró un camino.")
        render_maze(MAZE)
else:
    # Estado inicial (sin resolver)
    render_maze(MAZE)