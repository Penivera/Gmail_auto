# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from unidecode import unidecode
import csv
from datetime import datetime
import string

# Chrome options
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
]

# Randomly select a User-Agent
user_agent = random.choice(user_agents)
proxy = 'gw.dataimpulse.com:823:cb2d17f151aaa9e9e4dd__cr.us:b8ef63825804bedf' #replace with required proxy

chrome_options = ChromeOptions()
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument(f"user-agent={user_agent}")
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options,service=service ) 
#chrome_options.add_argument(f'--proxy-server={proxy}')
green,red= lambda text: f'\033[32m{text}\033[0m',lambda text: f'\033[31m{text}\033[0m'
yellow = lambda text: f'\033[33m{text}\033[0m'
# WebDriver service




def name_reader(file_name):
    names = []
    with open(file_name,'r',newline='') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            names.extend([name.strip() for name in row if name.strip()])
    name = [unidecode(name) for name in names]        
    return name

first_names = name_reader('f_names.csv')
last_names = name_reader('L_names.csv')


# Randomly select a first name and a last name
your_first_name = random.choice(first_names)
your_last_name = random.choice(last_names)

# Generate a random number
random_number = random.randint(1000, 9999)

# Retirer les accents des prénoms et nom de famille
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()


your_username = f'{your_first_name_normalized}.{your_last_name_normalized}{random_number}'

def generate_random_date():
    while True:
        try:
            # Generate random day, month, and year
            day = random.randint(1, 31)
            month = random.randint(1, 12)
            year = random.randint(1900, 2006)
            
            # Validate and format the date
            date = datetime(year, month, day)
            return date.strftime('%d %#m %Y')  # Use this for windows"
            #return date.strftime('%d %-m %Y')  # On Linux remove comment
        except ValueError:
            # If the date is invalid (e.g., 30 Feb), retry
            continue

def generate_password(length=16):
    # Define the character pool
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool
    password = ''.join(random.choices(all_characters, k=length))
    return password



your_birthday = generate_random_date() #dd m yyyy exp : 24 11 2003
your_gender = '1' # 1:F 2:M 3:Not say 4:Custom
your_password =  generate_password()
debug_mode = True #Set to false in production

def out_save(email,password,app_pass):
    headers = ['emails','passwords','app passwords']
    with open('login_info.csv','a',newline='') as file:
        writer = csv.DictWriter(file,fieldnames= headers)
        writer.writeheader()
        writer.writerow({'emails': email, 'passwords': password,'app passwords': app_pass})


def fill_form(driver):
    try:
        driver.get('https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp')

        # Fill in name fields
        first_name = driver.find_element(By.NAME, 'firstName')
        last_name = driver.find_element(By.NAME, 'lastName')
        first_name.clear()
        first_name.send_keys(your_first_name)
        last_name.clear()
        last_name.send_keys(your_last_name)
        next_button = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe')
        next_button.click()

        # Wait for birthday fields to be visible
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, 'day')))

        # Fill in birthday
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, 'month'))
        month_dropdown.select_by_value(birthday_elements[1])
        day_field = driver.find_element(By.ID, 'day')
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, 'year')
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender
        gender_dropdown = Select(driver.find_element(By.ID, 'gender'))
        gender_dropdown.select_by_value(your_gender)
        next_button = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe')
        next_button.click()

        
       # Create custom email
        time.sleep(2)
        if driver.find_elements(By.ID, 'selectionc4') :
            create_own_option = wait.until(EC.element_to_be_clickable((By.ID,'selectionc4') ))
            create_own_option.click()
        
        create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, 'Username')))
        username_field = driver.find_element(By.NAME, 'Username')
        username_field.clear()
        username_field.send_keys(your_username)
        next_button = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe')
        next_button.click()
        
        # Enter and confirm password
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd')))
        password_field.clear()
        password_field.send_keys(your_password)
        # Locate the parent div element with the ID 'confirm-passwd'
        confirm_passwd_div = driver.find_element(By.ID, 'confirm-passwd')
         #Find the input field inside the parent div
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, 'PasswdAgain')
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        next_button = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe')
        next_button.click()

        # Skip phone number and recovery email steps
        skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button span.VfPpkd-vQzf8d')))
        for button in skip_buttons:
            try:
                button.click()
            except Exception as e:
                print(yellow('Warning some buttons were not clicked'))

        # Agree to terms
        try:
            next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Next']]")))
            next_button.click()
        except Exception as e:
            print(yellow('Suppressed Click Error'))
        out_save(f'{your_username}.@gmail.com',your_password)

        print(green(f'Your Gmail successfully created:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}'))

    except Exception as e:
        print(red(f'Failed to create your Gmail\n{e}'))
    finally:
        if debug_mode:
            app_pass = input('Press any key To close\n').strip()
        out_save(f'{your_username}.@gmail.com',your_password,app_pass)
        driver.quit()


def main():
    fill_form(driver)

# Execute the function to fill out the form

if __name__ == '__main__':
    main()