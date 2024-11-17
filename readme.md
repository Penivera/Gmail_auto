
---

# Gmail Account Creation Automation Script - Version 1.1.0

This Python script automates the process of creating Gmail accounts. It leverages the **Selenium WebDriver** to interact with the Google Sign-Up page and performs the following tasks:

- Randomly generates a first name, last name, username, and password.
- Fills in the registration form with these details, including a randomly generated birthday and gender.
- Automatically skips optional fields (such as phone number and recovery email).
- Saves the newly created email addresses and passwords to a CSV file for future reference.
WRITTEN BY PENIEL @ http://github.com/SpiDher

## Prerequisites

To run this script, you need to install the following dependencies:

1. **Selenium WebDriver**: This is the core library used for automating the browser.
2. **Unidecode**: For removing accents from names.
3. **Threading**: For running multiple account creations simultaneously.

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

Additionally, you need to download the **ChromeDriver** executable, which is required to control the Chrome browser. Ensure the version of ChromeDriver matches the version of Chrome installed on your machine.

## Features

- **Random Name and Email Generation**: The script randomly selects names from CSV files containing first and last names.
- **Customizable User Agent**: The script randomly selects one of several user agents to mimic different devices and prevent detection by Google.
- **Multi-threading**: The script supports multi-threaded execution, allowing you to create multiple Gmail accounts simultaneously.
- **Proxy Support**: The script includes a proxy setup, which can be configured for different regions or anonymity.
- **Debug Mode**: When enabled, the script will pause after each account creation and allow you to check the results before closing the browser.

## How to Use

1. **CSV Files**: 
   - `f_names.csv`: A file containing a list of first names.
   - `L_names.csv`: A file containing a list of last names.

2. **Run the Script**:
   - The script accepts two arguments: 
     - `run_no`: Number of Gmail accounts to create.
     - `no_threads`: Number of threads (parallel processes) to run for account creation.

Example usage:

```bash
python script_name.py 5 2
```

This command will attempt to create 5 Gmail accounts using 2 threads (parallel processes).

## Debug Mode

- **Enabled (default)**: The script will pause after completing each account creation. A message will display with the new Gmail account and password. You can press any key to close the script and browser.
- **Disabled**: The script will run without pausing and will automatically close the browser after completing the tasks.

To disable debug mode, set the `debug_mode` variable to `False` in the script:

```python
debug_mode = False
```

This is useful for running the script in production or when you don't need to manually verify each created account.

## Notes

- **Proxy**: If you need to use a proxy for account creation, replace the `proxy` variable with your desired proxy settings.
- **Threading**: The `multi_run` function allows you to run the script in parallel using multiple threads. Be mindful that too many threads might slow down your system or result in IP blocks from Google.
- **Security**: Make sure you're using this script responsibly and not violating any terms of service from Google or any other service provider.

## Saving Account Information

The script saves the generated Gmail accounts and passwords to a CSV file named `login_info.csv`. This file contains the following headers:

- `emails`: The generated Gmail account address.
- `passwords`: The generated password for that account.

## Troubleshooting

If the script encounters any issues during the account creation process (e.g., element not found, network issues), it will print an error message. These errors can often be caused by changes to Google's sign-up process or issues with the browser driver.

---

Feel free to modify the configuration or debug settings based on your needs!