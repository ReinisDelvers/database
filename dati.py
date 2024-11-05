import sqlite3

conn = sqlite3.connect("dati.db", check_same_thread=False)

def atzimju_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        # "DROP TABLE atzime"
        """
        CREATE TABLE atzime(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (vards_id) REFERENCES skoleni(id),
        FOREIGN KEY (subject_id) REFERENCES subject(id)
        )
        """
    )
    conn.commit()
# atzimju_tabulas_izveide()

def prieksmetiunskolotaji_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        # "DROP TABLE prieksmetiunskolotaji"
        """
        CREATE TABLE prieksmetiunskolotaji(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        FOREIGN KEY (vards_id) REFERENCES skolotaji(id),
        FOREIGN KEY (subject_id) REFERENCES subject(id)
        )
        """
    )
    conn.commit()
# prieksmetiunskolotaji_tabulas_izveide()

def tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        # "DROP TABLE prieksmeti"
        """
        CREATE TABLE prieksmetiunskolotaji(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NO NULL,
        subject TEXT NOT NULL
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
        INSERT INTO atzime(vards_id, subject_id, grade) VALUES("{vards}","{subject}","{grade}")
        """
    )
    conn.commit()

def pievienot_prieksmeti(subject):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO prieksmeti(subject) VALUES("{subject}")
        """
    )
    conn.commit()

def pievienot_prieksmetiunskolotaji(vards, subject):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO prieksmetiunskolotaji(vards_id, subject_id) VALUES("{vards}", "{subject}")
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
        SELECT vards_id, subject_id, grade FROM atzime
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_prieksmeti():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT subject FROM prieksmeti
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_prieksmetiunskolotaji():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT vards_id, subject_id FROM prieksmetiunskolotaji
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_prieksmeti_id():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id, subject FROM prieksmeti
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_skoleni_id():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id ,vards, uzvards FROM skoleni
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_skolotaji_id():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id ,vards, uzvards FROM skolotaju
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati