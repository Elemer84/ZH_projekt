import os
from tkinter import messagebox

def me_teendok_beolvasasa(app):
    """Teendők beolvasása fájlból."""
    file_path = "teendok.txt"  # A fájl elérési útja
    if os.path.exists(file_path):  # Csak akkor próbál beolvasni, ha a fájl létezik
        try:
            with open(file_path, "r", encoding="utf-8") as fajl:
                for sor in fajl:
                    sor = sor.strip()
                    if ": " in sor:  # Ellenőrzi, hogy helyes-e a formátum
                        felhasznalo, teendo = sor.split(": ", 1)
                        app.teendok.append((felhasznalo, teendo))  # Adatok hozzáadása a listához
                        app.teendo_lista.insert("end", f"{felhasznalo}: {teendo}")  # GUI frissítése
        except Exception as e:
            messagebox.showerror("Hiba", f"Nem sikerült a teendők beolvasása: {e}")  # Hiba esetén üzenet

def me_teendo_hozzaadas(app):
    """Új teendő hozzáadása a listához."""
    uj_teendo = app.teendo_mezo.get()  # Az új teendő beviteli mező tartalma
    felhasznalo = app.felhasznalo_mezo.get()  # Felhasználó név mező tartalma
    if uj_teendo.strip():  # Ha a teendő nem üres
        app.teendok.append((felhasznalo, uj_teendo))  # A felhasználó és teendő párosítása
        app.teendo_lista.insert("end", f"{felhasznalo}: {uj_teendo}")  # Teendő hozzáadása a listához
        app.teendo_mezo.delete(0, "end")  # A beviteli mező törlése
    else:
        messagebox.showwarning("Figyelmeztetés", "A teendő mező nem lehet üres!")  # Figyelmeztetés, ha üres mezőt próbálnak hozzáadni

def me_teendo_torles(app):
    """Kijelölt teendő törlése a listából."""
    try:
        kivalasztott_index = app.teendo_lista.curselection()[0]  # A kiválasztott teendő indexének lekérése
        app.teendok.pop(kivalasztott_index)  # A teendő törlése a listából
        app.teendo_lista.delete(kivalasztott_index)  # A GUI-ból való eltávolítás
    except IndexError:
        messagebox.showwarning("Figyelmeztetés", "Nincs kijelölt teendő!")  # Ha nincs kijelölt teendő, figyelmeztetés

def me_teendok_mentese(app):
    """Teendők mentése fájlba."""
    file_path = "teendok.txt"  # A fájl alapértelmezett elérési útja

    # Ellenőrizzük, hogy létezik-e a fájl, ha nem, akkor létrehozzuk
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            pass  # Csak létrehozza a fájlt üresen, ha nem létezik

    try:
        # A fájl megnyitása írásra
        with open(file_path, "w", encoding="utf-8") as fajl:
            for felhasznalo, teendo in app.teendok:  # A teendők listájának bejárása
                fajl.write(f"{felhasznalo}: {teendo}\n")  # Teendők kiírása fájlba
        messagebox.showinfo("Siker", "A teendők sikeresen elmentve a 'teendok.txt' fájlba.")  # Üzenet, ha sikerült
    except Exception as e:
        messagebox.showerror("Hiba", f"Nem sikerült a teendők mentése: {e}")  # Hibaüzenet, ha valami elromlik