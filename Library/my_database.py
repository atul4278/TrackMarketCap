import logging
import sqlite3
import sqlite3

def create_database():
    """
    Create Database and Required Table(s)

    :return:
    """
    logging.info('Creating Database...')
    try:
        db = sqlite3.connect('STOCKDATA')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE WORLD_MKT '
                       '(SYMBOL TEXT PRIMARY KEY, DESCRIPTION TEXT, PRICE FLOAT, CHANGE TEXT, OPEN FLOAT, HIGH FLOAT, LOW FLOAT)')
        db.commit()
    except Exception as E:
        try:
            if 'table WORLD_MKT already exists' == E:
                cursor.execute('''delete from WORLD_MKT''')
                db.commit()
        except Exception as E:
            raise Exception('Failed to create DB')
    finally:
        if 'db' in globals():
            db.close()

def insert_into_db(sql, dataset):
    """
    Insert Multiple dataser Records in DB as per provided query

    :param sql: Insert Query in format for executemany method
    :param dataset: dataset to be inserted
    :return:
    """
    logging.info('Inserting data into STOCKDATA...')
    try:
        db = sqlite3.connect('STOCKDATA')
        cursor = db.cursor()
        cursor.executemany(sql,dataset)
    except sqlite3.IntegrityError:
        logging.info(f' Data already Present.')
    except Exception as E:
        logging.error(f'Error While Inserting Data: {E}')
        return False
    else:
        logging.info('data inserted successfully in database table')
        db.commit()
        return True
    finally:
        if 'db' in globals():
            db.close()

def fetch_db_data(sql):
    """
    Fetch Data from STOCKDATA as per given query

    :param sql: Select Query to fetch data
    :return: Fetched data or None
    """
    logging.info('Feting Data from STOCKDATA')
    try:
        db = sqlite3.connect('STOCKDATA')
        cursor = db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as E:
        logging.error(f'Error While Fetching Data: {E}')
        return
    finally:
        if 'db' in globals():
            db.close()