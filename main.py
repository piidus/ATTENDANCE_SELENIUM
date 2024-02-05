import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, math
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

user = os.getenv('USER')
# Open main url
main_url = os.getenv('URL')

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)




def login():
    '''
        It complete login  process
    '''
    driver.get(main_url)
    driver.maximize_window()
    # time.sleep(3)
    user_name = driver.find_element(By.ID, 'user_name').send_keys(user)
    password = driver.find_element(By.ID, 'user_pass').send_keys(os.getenv('PWD'))
    main_window = driver.current_url
    driver.find_element(By.ID, 'user_capcha').send_keys(Keys.TAB)
    print('in starting main window ::', main_window)
    #  
    for _ in range(30): 
        ''' if new window not equal first window then it return 1'''
        time.sleep(1)
        new_window = driver.current_url
        if new_window != main_window:
            main_window = new_window
            print(main_window)
            break

    return 1

def accept_all_application():
    # Find the table element by its ID
    table = driver.find_element(By.ID, "example")

    # Find all rows in the table
    rows = table.find_elements(By.TAG_NAME, "tr")
    original_window = driver.current_window_handle
    # Iterate through each row and get the value of the 5th td element
    for row in rows:
        # Find all td elements in the current row
        cells = row.find_elements(By.TAG_NAME, "td")
        
        
        # Check if the row has at least 5 td elements
        if len(cells) >= 8:
            # Get the value of the 5th td element (index 4)
            print('sterp 1')
            sixth_td_value = cells[7].text
            print(sixth_td_value)
            # Check if the value is equal to 'View'
            if sixth_td_value == "Approved/Reject":
                # Click the sixth td element
                print('sterp 2') 
                try:
                    cells[7].click()
                    try:
                        # Wait for the modal to appear (assuming it has a class like "modal" and "fade")
                        modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal.fade")))
                    
                        # Find the "OK" button inside the modal by its class
                        ok_button = modal.find_element(By.CSS_SELECTOR, "input[type='submit'][value='OK']")  

                        # Click on the "OK" button
                        ok_button.click()

                    except Exception as e:
                        print('coukd not click', e)
                    # alert.accept()
                    time.sleep(1)
                    
                except Exception as e:
                    print(e, ' error in clicking')
                time.sleep(5)
                print('sterp 3')
                # break
            
            # driver.switch_to.window(original_window)    # #Switch back to the old tab or window
            print("Value of the 5th td in this row:", sixth_td_value)
    time.sleep(1)


def find_and_accept():
    # for left span
    driver.find_element(By.XPATH, '//*[@id="master_directory"]/a/span').click()

    driver.find_element(By.ID, "pending_common").click()
    time.sleep(1)

    # Find the table element by its ID
    table = driver.find_element(By.ID, "example")

    # Find all rows in the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Iterate through each row and get the value of the 5th td element
    for row in rows:
        # Find all td elements in the current row
        cells = row.find_elements(By.TAG_NAME, "td")
        
        # Check if the row has at least 5 td elements
        if len(cells) >= 5:
            # Get the value of the 5th td element (index 4)
            fifth_td_value = cells[4].text
            
            print("Value of the 5th td in this row:", fifth_td_value)
            # Check if the value is not equal to 0
            if fifth_td_value != "0":
                # Click the 5th td element
                cells[4].click()
                time.sleep(5)
                # Now run accept function
                accept_all_application()
                break
    time.sleep(5)





if __name__ == '__main__':
    
    
    try:
        login = login()
        
    except Exception as e:
        print(e)
    else:
        if login == 1:
            print('start loop')
            find_and_accept()
    finally:
        driver.quit()
