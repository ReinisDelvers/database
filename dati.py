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
        SELECT vards, uzvards, subject, grade 
        FROM
        (atzime JOIN skoleni ON skoleni.id = atzime.vards_id)
        JOIN prieksmeti ON prieksmeti.id = atzime.subject_id
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
        SELECT vards, uzvards, subject 
        FROM
        (prieksmetiunskolotaji JOIN skolotaju ON skolotaju.id = prieksmetiunskolotaji.vards_id)
        JOIN prieksmeti ON prieksmeti.id = prieksmetiunskolotaji.subject_id
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

def iegut_videjas_atzimes(orderby="skoleni.uzvards"):
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT skoleni.vards, skoleni.uzvards, prieksmeti.subject, AVG(atzime.grade), skoleni.id 
        FROM
        (skoleni LEFT JOIN atzime ON skoleni.id = atzime.vards_id)
        LEFT JOIN prieksmeti ON prieksmeti.id = atzime.subject_id
        GROUP BY skoleni.id, prieksmeti.id
        ORDER BY {orderby} ASC
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def dzest_skolenu(id):
    cur = conn.cursor()
    cur.execute(
        f"""
        DELETE FROM skoleni
        WHERE id = "{id}"
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def dzest_skolotaju(id):
    cur = conn.cursor()
    cur.execute(
        f"""
        DELETE FROM skolotaju
        WHERE id = "{id}"
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def dzest_prieksmeti(id):
    cur = conn.cursor()
    cur.execute(
        f"""
        DELETE FROM prieksmeti
        WHERE id = "{id}"
        """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati