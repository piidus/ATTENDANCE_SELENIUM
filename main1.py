from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, math
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
# from selenium.exception import StaleElementReferenceException
import os, time
from cliock_test import clickable
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def login_to_main_page(driver):
    """
    It will login to the main page of pm poshan website
    
    Parameters:
    driver (obj): The webdriver object
    
    Returns:
    None
    """
    user = os.getenv('USER')
    pwd = os.getenv('PWD')
    url = 'https://pmposhan.wb.gov.in/login'


    driver.get(url)
    driver.maximize_window()
    # check url change or not
    while True:
        current_url = driver.current_url
        if current_url == url:
            # check user name and password values if none send values
            user_name = driver.find_element(By.ID, 'user_name').get_attribute('value')
            password = driver.find_element(By.ID, 'user_pass').get_attribute('value')
            if user_name == '':        
                user_name = driver.find_element(By.ID, 'user_name').send_keys(user)
            if password == '':
                password = driver.find_element(By.ID, 'user_pass').send_keys(pwd)
            time.sleep(2)
        else:
            print(current_url)
            break

def open_attendance_page(driver):
    """
    This function opens the attendance page by getting the specific url and clicking on it
    
    Parameters:
    driver (obj): The webdriver object
    
    Returns:
    None
    """
    url = "https://pmposhan.wb.gov.in/blockwise_summary_report?district_code=a7c812f386d5eaf61ed5e704fec8dc8c518ed84eb37cfb8b3c58b6afd8fed3f229b90c92ef3b80f2a9633e46b6b0c84c326ce916013b061afed4e19d2e609235nQlAXMxntoJ45ZdU0ImGcl7TRIoMwrMeQiVlUOpksOk%3D"
    # find url and click
    driver.get(url)
    time.sleep(1)

def accept_all_application(driver):
    # Find the table element by its ID
    """
    This function finds the table element by its ID, finds all rows in the table, 
    and iterates through each row to get the value of the 5th td element. It then
    checks if the row has at least 5 td elements and if the value of the 5th td element
    is not equal to 0. If the condition is met, it clicks on the 7th td element which
    is a link to the application details page. It then clicks on the back button to go
    back to the blockwise summary report page.

    Parameters:
    driver (obj): The webdriver object

    Returns:
    None
    """
    _table = driver.find_element(By.ID, "example")
    print('_table')
    # Find all rows in the table
    __rows = _table.find_elements(By.TAG_NAME, "tr")
    # pass first 2 rows
    __rows = __rows[2:]
    print('rows')
    time.sleep(3)
    row = __rows[0]
        # Find all td elements in the current row
    cells = row.find_elements(By.TAG_NAME, "td")
    # Iterate through each row and get the value of the 5th td element
    for _ in __rows:
        print('length of rows', len(__rows))
        
        # print(cells)
        print('length of cells', len(cells))
        # Check if the row has at least 5 td elements
        if len(cells) >= 7:
            print('[cell hited]')
            # get herf on 7th td and click on it
            _link = driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr/td[8]/a')
            # _link.get_attribute('href').click()
            _link.click()

           
            try:
                # alert = WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
                # # accept alert
                # alert.accept()
                clickable()
                # driver.find_element(By.NAME, "submit").click()
            except Exception as e:  
                print(e)

    # after for loop click on back button
    url = "https://pmposhan.wb.gov.in/blockwise_summary_report?district_code=95973e786c85bef28b117e0f0e27de9132ff014d2ad0caa16f2aa06c383ae76b6cbdb1b5e9b1de2e6c8940315881657360e517676b5dd55836f590c22806d042cCewrq1SS30d91LNAX5%2FFfjCZed6%2Fty8ojGkGcM6R7c%3D" 
    driver.get(url)
block_table =None
block_rows = None
# def find_school(driver):
#     global block_table, block_rows
#     table_id = 'table_th'
#     # find table body and loop every row print it
#     # Find the table element by its ID
#     block_table = driver.find_element(By.ID, "example")

#     # Find all rows in the table
#     block_rows = block_table.find_elements(By.TAG_NAME, "tr")

#     # Iterate through each row and get the value of the 5th td element
#     for _row in block_rows:
#         # Find all td elements in the current row
#         # cells_ = _row.find_elements(By.TAG_NAME, "td")
#         try:
#             cells_ = _row.find_elements(By.TAG_NAME, "td")
#         except Exception as e:
#             print("Row is stale, skipping...")
#             continue

#         # Check if the row has at least 5 td elements
#         if len(cells_) >= 5:
#             # Get the value of the 5th td element (index 4)
#             fifth_td_value = int(cells_[4].text)            

#             # print("Value of the 5th td in this row:", fifth_td_value)
#             if fifth_td_value > 0:
#                 # get herf and click on it
#                 cells_[4].click()
#                 try:
#                     accept_all_application(driver)
#                 except Exception as e:
#                     print(e)
#                 time.sleep(3)

    
def find_school(driver):
    

    """
    This function finds the table element by its ID, finds all rows in the table, 
    and iterates through each row to get the value of the 5th td element. It then
    checks if the row has at least 5 td elements and if the value of the 5th td element
    is greater than 0. If the condition is met, it clicks on the 4th td element which
    is a link to the school details page. It then clicks on the back button to go
    back to the blockwise summary report page.

    Parameters:
    driver (obj): The webdriver object

    Returns:
    None
    """
    total = 0
    
    try:
        block_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "example")))
        block_rows = block_table.find_elements(By.TAG_NAME, "tr")

        for _row in block_rows:
            cells_ = _row.find_elements(By.TAG_NAME, "td")
            total += 1
            if len(cells_) >= 5:
                fifth_td_value = int(cells_[4].text)

                if fifth_td_value > 0:
                    cells_[4].click()
                    try:
                        accept_all_application(driver)
                        if total > 50:
                            driver.quit()
                        find_school(driver)
                    except Exception as e:
                        print("Error in accept_all_application:", e)
                    time.sleep(3)
    except Exception as e:
        print("Error in find_school:", e)
        
    else:
        total += 1
        print(f"Total attempts: {total}")
        if total == 50:
            driver.quit()





if __name__ == '__main__':
    login_to_main_page(driver)
    open_attendance_page(driver)
    find_school(driver)
    driver.quit()