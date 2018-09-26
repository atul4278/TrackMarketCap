import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_market_data(baseurl):
    logging.info("Fetching Stock Data from Google Finance...")
    stock = []
    temp = []
    counter = 0
    try:
        logging.info("Launching Google Finance...")
        driver = webdriver.Firefox()
        driver.get(baseurl)
        world_mkt_elements = driver.find_element_by_xpath(r'//div[@class="rit-block"]/div[2]')
        content = world_mkt_elements.text
        stock_data = content.split('\n')[1:]
        logging.info("Parsing retrived data...")
        for val in stock_data:
            temp.append(val)
            counter+=1
            if counter == 4:
                stock.append(temp)
                temp = list()
                counter = 0
        logging.info(f"Parsing Complete.Data: {stock}")
        return stock
    except Exception as e:
        logging.exception(f'ERROR: {e}')
    finally:
        driver.quit()

def get_stock_data(baseurl):
    try:
        logging.info("Launching Google Finance...")
        driver = webdriver.Firefox()
        driver.get(baseurl)
        stropen = driver.find_element_by_xpath("//td[text()='Open']/following-sibling::td").text.replace(',','')
        strhigh = driver.find_element_by_xpath("//td[text()='High']/following-sibling::td").text.replace(',','')
        strlow = driver.find_element_by_xpath("//td[text()='Low']/following-sibling::td").text.replace(',','')
        symbol = baseurl.split('+')[1]
        return [float(stropen),float(strhigh),float(strlow),symbol]
    except NoSuchElementException as e:
        logging.error(f"ERROR: {e} for {baseurl}")
        return [None, None, None, None]
    except Exception as E:
        raise Exception(f"ERROR: {E}")
    finally:
        driver.quit()
