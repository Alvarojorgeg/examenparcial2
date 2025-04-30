import tkinter as tk
from tkinter import ttk, messagebox
from clases.book import Book
from clases.book_genre import BookGenre

class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        self.libros = []

        self.setup_widgets()

    def setup_widgets(self):
        frame_registro = ttk.LabelFrame(self.root, text="Registrar Libro")
        frame_registro.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame_registro, text="Título:").grid(row=0, column=0, sticky="w")
        self.entry_titulo = ttk.Entry(frame_registro)
        self.entry_titulo.grid(row=0, column=1)

        ttk.Label(frame_registro, text="Autor:").grid(row=1, column=0, sticky="w")
        self.entry_autor = ttk.Entry(frame_registro)
        self.entry_autor.grid(row=1, column=1)

        ttk.Label(frame_registro, text="Género:").grid(row=2, column=0, sticky="w")
        self.combo_genero = ttk.Combobox(frame_registro, values=[g.name for g in BookGenre], state="readonly")
        self.combo_genero.grid(row=2, column=1)
        self.combo_genero.current(0)

        ttk.Button(frame_registro, text="Agregar Libro", command=self.agregar_libro).grid(row=3, column=0, columnspan=2, pady=5)

        frame_lista = ttk.LabelFrame(self.root, text="Lista de Libros")
        frame_lista.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(frame_lista, columns=("Título", "Autor", "Género", "Estado"), show="headings")
        for col in ("Título", "Autor", "Género", "Estado"):
            self.tree.heading(col, text=col)
        self.tree.grid(row=0, column=0, columnspan=2)

        ttk.Button(frame_lista, text="Prestar", command=self.prestar_libro).grid(row=1, column=0, sticky="ew", pady=5)
        ttk.Button(frame_lista, text="Devolver", command=self.devolver_libro).grid(row=1, column=1, sticky="ew", pady=5)

    def agregar_libro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        genero_str = self.combo_genero.get()

        if not titulo or not autor:
            messagebox.showwarning("Campos Vacíos", "Todos los campos son obligatorios.")
            return

        try:
            genero = BookGenre[genero_str]
        except KeyError:
            messagebox.showerror("Género inválido", f"No se reconoce el género: {genero_str}")
            return

        libro = Book(titulo, autor, genero)
        self.libros.append(libro)
        self.actualizar_lista()

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for idx, libro in enumerate(self.libros):
            self.tree.insert('', 'end', iid=idx, values=(
                libro.get_titulo(),
                libro.get_autor(),
                libro.get_genero().value,
                "Disponible" if libro.is_available() else "Prestado"
            ))

    def prestar_libro(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            idx = int(seleccionado[0])
            if self.libros[idx].prestar():
                self.actualizar_lista()
            else:
                messagebox.showinfo("No Disponible", "El libro ya está prestado.")

    def devolver_libro(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            idx = int(seleccionado[0])
            self.libros[idx].devolver()
            self.actualizar_lista()

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()