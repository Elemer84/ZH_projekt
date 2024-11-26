import tkinter as tk
from me_fuggvenyek import me_teendo_hozzaadas, me_teendo_torles, me_teendok_mentese

class METeendoApp:
    def __init__(self, gyoker):
        self.gyoker = gyoker
        self.gyoker.title("Teendő Nyilvántartó")  # Az ablak címe

        # Teendők listája
        self.teendok = []

        # Felhasználói felület létrehozása
        self.felulet_letrehozas()

    def felulet_letrehozas(self):
        # Felhasználó név mező
        self.felhasznalo_mezo = tk.Entry(self.gyoker, width=40)
        self.felhasznalo_mezo.pack(pady=5)

        # Címke a teendő mezőhöz
        self.cimke = tk.Label(self.gyoker, text="Új teendő:")
        self.cimke.pack(pady=5)

        # Beviteli mező a teendőhöz
        self.teendo_mezo = tk.Entry(self.gyoker, width=40)
        self.teendo_mezo.pack(pady=5)

        # Hozzáadás gomb
        self.hozzaadas_gomb = tk.Button(self.gyoker, text="Hozzáadás", command=lambda: me_teendo_hozzaadas(self))
        self.hozzaadas_gomb.pack(pady=5)

        # Törlés gomb
        self.torles_gomb = tk.Button(self.gyoker, text="Törlés", command=lambda: me_teendo_torles(self))
        self.torles_gomb.pack(pady=5)

        # Mentés gomb
        self.mentes_gomb = tk.Button(self.gyoker, text="Mentés fájlba", command=lambda: me_teendok_mentese(self))
        self.mentes_gomb.pack(pady=5)

        # Teendők listája megjelenítés
        self.teendo_lista = tk.Listbox(self.gyoker, width=50, height=10)
        self.teendo_lista.pack(pady=5)
