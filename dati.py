import sqlite3

conn = sqlite3.connect("dati.db", check_same_thread=False)

def atzimju_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE atzime(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skolens INTEGER NOT NULL,
        subject INTEGER NOT NULL,
        grade INTEGER NOT NULL
        )
        """
    )
    conn.commit()

def tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE skolotaju(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL
        )
        """
    )
    conn.commit()

# tabulas_izveide()

def pievienot_skolenu(vards, uzvards):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO skoleni(vards, uzvards) VALUES("{vards}","{uzvards}")
        """
    )
    conn.commit()

def pievienot_skolotaju(vards, uzvards):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO skolotaju(vards, uzvards) VALUES("{vards}","{uzvards}")
        """
    )
    conn.commit()

def pievienot_atzime(vards, subject, grade):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO atzime(vards, subject, grade) VALUES("{vards}","{subject}","{grade}")
        """
    )
    conn.commit()

def iegut_skolenus():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT vards, uzvards FROM skoleni
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_skolotaju():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT vards, uzvards FROM skolotaju
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_atzime():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT vards, subject, grade FROM atzime
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati