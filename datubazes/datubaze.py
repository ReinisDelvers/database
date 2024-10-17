import sqlite3
import tkinter as tk
from tkinter import ttk

conn = sqlite3.connect("datubazes/faili/my.db")

def kverijs(vaicajums):
    cur = conn.cursor()
    cur.execute(vaicajums)
    conn.commit()

tabulas_dzesana = "DROP TABLE skoleni"

tabulas_izveide = """
CREATE TABLE IF NOT EXISTS skoleni(
    id_skolenam INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT,
    uzvards TEXT,
    vecums INT
)

"""

datu_pievienosana = """
INSERT INTO skoleni(vards, uzvards, vecums)
VALUES('Anna', 'Bērziņa', 17)

"""
def datu_pieliksana(tabula, kolonnas, dati):
    vaicajums = f"""
INSERT INTO {tabula}{kolonnas}
VALUES{dati}

"""

datu_pieliksana("skoleni", ("vards", "uzvards", "vecums"), ("Jānis", "Bērziņš","16"))









# root = tk.Tk()
# root.title('Datu bāze')
# root.geometry('1280x720')
# root.resizable(False, False)

# frame = ttk.Frame(root)

# options = {'padx': 5, 'pady': 5}



# frame.grid(padx=10, pady=10)

# root.mainloop()