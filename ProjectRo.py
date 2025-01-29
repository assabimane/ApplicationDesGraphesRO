import tkinter as tk
from tkinter import Toplevel, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import random
from collections import defaultdict

class GraphVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualization Program")
        self.root.geometry("600x400")

        # Main menu with two buttons: "Start" and "Exit"
        self.main_menu()

    def main_menu(self):
        # Create a title label
        title_label = tk.Label(self.root, text="Bienvenue dans le Programme de Visualisation de Graphe", font=("Arial", 16))
        title_label.pack(pady=30)

        # Create a smaller subtitle label
        subtitle_label = tk.Label(self.root, text="Sélectionnez une option ci-dessous", font=("Arial", 12))
        subtitle_label.pack(pady=10)

        # Create the "Start Program" button
        start_button = tk.Button(self.root, text="Entrer dans le programme", width=25, height=2, command=self.start_program)
        start_button.pack(pady=10)

        # Create the "Exit Program" button
        exit_button = tk.Button(self.root, text="Quitter", width=25, height=2, command=self.root.quit)
        exit_button.pack(pady=10)

        # Add another title at the bottom of the page
        additional_title = tk.Label(self.root, text="Projet relisé par : Assab Imane et encadré par : Prof El Mkhalet Mouna", font=("Arial", 10))
        additional_title.pack(side='bottom', pady=10)

    def start_program(self):
        # Switch to the graph visualization interface when "Start Program" is clicked
        self.clear_screen()
        self.graph_interface()

    def clear_screen(self):
        # Clear all widgets from the main menu to prepare for the new interface
        for widget in self.root.winfo_children():
            widget.destroy()

    def graph_interface(self):
        # Set up the graph creation and visualization interface
        self.graphs = {
            "Welsh Powell": {
                'A': {'B': 1, 'C': 1, 'D': 1, 'E': 1},
                'B': {'A': 1, 'C': 1, 'E': 1, 'F': 1},
                'C': {'A': 1, 'B': 1, 'D': 1, 'F': 1},
                'D': {'A': 1, 'C': 1, 'E': 1, 'F': 1},
                'E': {'A': 1, 'B': 1, 'D': 1},
                'F': {'B': 1, 'C': 1, 'D': 1}
            },
            "Nord Ouest": {
                'S1': {'D1': 10, 'D2': 12, 'D3': 15},
                'S2': {'D1': 8, 'D2': 9, 'D3': 11},
                'S3': {'D1': 6, 'D2': 7, 'D3': 8},
                'D1': {},
                'D2': {},
                'D3': {}
            },
            "Dijkstra": {
                'A': {'B': 1, 'C': 4, 'D': 3, 'F': 8},
                'B': {'C': 2, 'D': 5, 'E': 6},
                'C': {'D': 1, 'E': 4, 'F': 2},
                'D': {'E': 3, 'F': 5},
                'E': {'F': {}} ,
                'F': {}
            },
            "Moindre Cout": {
                'A': {'B': 3, 'C': 2, 'D': 5},
                'B': {'A': 3, 'C': 1, 'D': 4},
                'C': {'A': 2, 'B': 1, 'D': 6},
                'D': {'A': 5, 'B': 4, 'C': 6}
            }
        }

        # Create a label for the interface title
        self.title_label = tk.Label(self.root, text="Choisissez un Algorithme", font=("Arial", 14))
        self.title_label.pack(pady=10)

        # Create a button to input the number of vertices
        self.vertex_label = tk.Label(self.root, text="Nombre de sommets:")
        self.vertex_label.pack(padx=10, pady=10)
        
        self.vertex_entry = tk.Entry(self.root)
        self.vertex_entry.pack(padx=10, pady=10)
        
        self.create_graph_button = tk.Button(
            self.root, text="Créer Graphe", command=self.create_graph
        )
        self.create_graph_button.pack(pady=10)
        
        algorithms = [
            "Welsh Powell", "Dijkstra", "Potentiel Metra", "Kruskal",
            "Bellman Ford", "Ford Fulkerson", "Nord Ouest", "Stepping Stone", 
            "Moindre Cout"
        ]
        
        for algo in algorithms:
            btn = tk.Button(
                self.root,
                text=algo,
                width=20,
                height=2,
                command=lambda a=algo: self.show_graph(a)
            )
            btn.pack(pady=5)

        # Create "Back" button to return to the main menu
        back_button = tk.Button(
            self.root,
            text="Retour au menu principal",
            command=self.main_menu,
            width=20,
            height=2
        )
        back_button.pack(pady=10)

    def create_graph(self):
        num_vertices = self.vertex_entry.get()
        try:
            num_vertices = int(num_vertices)
            if num_vertices < 2:
                raise ValueError("Le nombre de sommets doit être supérieur ou égal à 2.")
        except ValueError as e:
            messagebox.showerror("Erreur", f"Entrée invalide: {e}")
            return

        # Create a simple graph with the specified number of vertices
        self.graph = {f'V{i}': {} for i in range(num_vertices)}

        # Step 1: Make the graph connected by creating a spanning tree (connected path)
        for i in range(num_vertices - 1):
            self.graph[f'V{i}'][f'V{i+1}'] = random.randint(1, 10)
            self.graph[f'V{i+1}'][f'V{i}'] = self.graph[f'V{i}'][f'V{i+1}']  # Bidirectional connection

        # Step 2: Add random edges to make the graph more interesting, but still keep it connected
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if random.random() < 0.3:  # 30% chance of adding an extra edge
                    weight = random.randint(1, 10)
                    self.graph[f'V{i}'][f'V{j}'] = weight
                    self.graph[f'V{j}'][f'V{i}'] = weight  # Bidirectional

        messagebox.showinfo("Graph Created", f"Un graphe connexe avec {num_vertices} sommets a été créé.")
        
    def show_graph(self, algo_name):
        if not hasattr(self, 'graph') or not self.graph:
            messagebox.showinfo("Info", "Veuillez d'abord créer un graphe.")
            return
        
        graph_window = Toplevel(self.root)
        graph_window.title(f"Visualisation - {algo_name}")
        graph_window.geometry("800x600")
        
        G = nx.DiGraph()
        graph_data = self.graph if algo_name != "Moindre Cout" else self.graphs["Moindre Cout"]
        
        for node, edges in graph_data.items():
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        
        pos = nx.spring_layout(G)
        
        nx.draw(
            G, pos,
            with_labels=True,
            node_color='skyblue',
            node_size=1500,
            font_size=12,
            font_weight='bold',
            ax=ax
        )
        
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        
        close_button = tk.Button(
            graph_window,
            text="Fermer",
            command=graph_window.destroy
        )
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualizerApp(root)
    root.mainloop()
