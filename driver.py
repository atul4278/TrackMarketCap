import logging
from Library.get_finance_data import *
from Library.my_database import *
from Utilities.my_logger import initialize_logger
import sqlite3
from time import sleep


def main():
    logger = initialize_logger(logging.DEBUG)
    url = 'https://finance.google.com/finance'
    create_database()
    logger.info(url)
    dataset = get_market_data(url) # Get Stock Data from Google Finance
    # print(dataset)

    for i,data in enumerate(dataset): # Parse Fetched data in expected format
        dataset[i][1] = float(dataset[i][1].replace(',',''))
        dataset[i][3] = dataset[i][3].split(' ')[0]

    sql = ''' INSERT INTO WORLD_MKT (SYMBOL, PRICE, DESCRIPTION, CHANGE) VALUES (?,?,?,?)'''
    insert_into_db(sql,dataset)  # inserting fetched data into DB
    table_data = fetch_db_data("Select Symbol from WORLD_MKT")
    print(table_data)

    # Fetching data Specific to stocks
    index_url = 'https://www.google.com/search?safe=active&tbm=fin&q=INDEX:+'
    dataset_stock = []
    for s in table_data:
        dataset_stock.append(get_stock_data(index_url+s[0]))
        # issue with Steps as cannot fetch data

    print(dataset_stock)
    sql = '''UPDATE WORLD_MKT SET OPEN=?, HIGH=?, LOW=? WHERE SYMBOL=?'''
    # sql = ''' INSERT INTO WORLD_MKT (OPEN, HIGH, LOW) VALUES (?,?,?)'''
    insert_into_db(sql, dataset_stock)  # inserting fetched data into DB

    table_data = fetch_db_data("Select * from WORLD_MKT")
    print(table_data)

if __name__=='__main__':
    main()

