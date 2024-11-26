import tkinter as tk
from me_tehendo_app import METeendoApp

# Alkalmazás indítása
if __name__ == "__main__":
    gyoker = tk.Tk()  # Létrehozzuk a fő Tkinter ablakot
    app = METeendoApp(gyoker)  # Az alkalmazás létrehozása
    gyoker.mainloop()  # A Tkinter fő ciklusának elindítása
