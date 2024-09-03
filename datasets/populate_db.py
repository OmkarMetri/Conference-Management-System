import pandas as pd
import sqlite3
import csv


def populate_all_conferences(database):
    """
    Path of DB
    :param database: SQLite DB path
    :return:
    """
    create_table = """ CREATE TABLE IF NOT EXISTS all_conferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT NOT NULL,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                organizer TEXT NOT NULL,
                category TEXT NOT NULL,
                location TEXT NOT NULL,
                country TEXT NOT NULL,
                website TEXT NOT NULL,
                organizer_email TEXT NOT NULL,
                deadline TEXT NOT NULL,
                about_conf TEXT
                ); """

    insert = """INSERT INTO all_conferences 
                (date, link, name, organizer, category, location, country, website, organizer_email, deadline, about_conf) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?);"""

    conn = sqlite3.connect(database)
    if not conn:
        return "Could not connect to database"

    c = conn.cursor()
    c.execute(create_table)

    for row in all_conferences:
        try:
            c.execute(insert, row)
        except:
            continue

    conn.commit()
    conn.close()


def populate_top_conferences(database):
    """
    Path of DB
    :param database: SQLite DB path
    :return:
    """
    create_table = """ CREATE TABLE IF NOT EXISTS top_conferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                link TEXT NOT NULL,
                name TEXT NOT NULL,
                organizer TEXT NOT NULL,
                location TEXT NOT NULL,
                country TEXT NOT NULL,
                website TEXT NOT NULL,
                deadline TEXT NOT NULL,
                hindex INTEGER NOT NULL
                ); """

    insert = """INSERT INTO top_conferences 
                    (date, link, name, organizer, location, country, website, deadline, hindex) 
                    VALUES(?,?,?,?,?,?,?,?,?)"""

    conn = sqlite3.connect(database)
    if not conn:
        return "Could not connect to database"

    c = conn.cursor()
    c.execute(create_table)

    for row in top_conferences:
        try:
            c.execute(insert, row)
        except:
            continue

    conn.commit()
    conn.close()


def populate_university_programs(database):
    """
    Path of DB
    :param database: SQLite DB path
    :return:
    """
    create_table = """ CREATE TABLE IF NOT EXISTS university_programs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                college TEXT NOT NULL,
                courses TEXT NOT NULL
                ); """

    insert = """INSERT INTO university_programs (college, courses) VALUES(?,?)"""

    # create a database connection
    conn = sqlite3.connect(database)
    if not conn:
        return "Could not connect to database"

    c = conn.cursor()
    c.execute(create_table)

    for row in university_programs:
        try:
            c.execute(insert, row)
        except Exception as e:
            print(str(e))
            continue
    conn.commit()
    conn.close()


def read_csv(filename):
    """
    Read the CSV file
    :param filename: path of the CSV file
    :return: list of tuples, i.e., [row-1, row-2 . . .]
    """
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        data = [tuple(row) for row in reader]

    return data


if __name__ == "__main__":
    db = "conf_hub.db"

    # read the data from CSV files
    all_conferences = read_csv("all_conferences.csv")
    top_conferences = read_csv("top_conferences.csv")
    university_programs = read_csv("university_programs.csv")

    # populate database
    populate_all_conferences(db)
    populate_top_conferences(db)
    populate_university_programs(db)

    print("SQLite: Database populated!!!")
