from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Set up your LinkedIn credentials
LINKEDIN_USERNAME = "8446274030"
LINKEDIN_PASSWORD = "Ashugore75@"

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    
    # Wait for the username field and input the username
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys(LINKEDIN_USERNAME)
    
    # Enter the password
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    
    # Press Enter to submit
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    
    # Wait for the feed page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "feed-nav"))
    )
    print("Logged in successfully")

def get_email_from_profile(profile_url):
    driver.get(profile_url)
    
    # Wait until the profile page loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='pv-contact-info']"))
    )
    
    email = None
    try:
        # Click the "Contact Info" button
        contact_info_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'contact-info')]"))
        )
        contact_info_button.click()

        # Wait for the email to appear
        email_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'ci-email')]//a"))
        )
        
        # Extract the email
        email = email_element.text
        print(f"Extracted Email: {email}")
    except Exception as e:
        print(f"No email found or access restricted: {e}")
    
    return email

def save_email_to_json(email):
    if email:
        # Save email to a JSON file
        data = {"email": email}
        with open('email_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Email saved to email_data.json")
    else:
        print("No email to save.")

# Main execution
def main():
    login_to_linkedin()
    
    # Replace with a valid LinkedIn profile URL
    profile_url = "https://www.linkedin.com/in/someone-profile/"
    email = get_email_from_profile(profile_url)
    
    # Save the extracted email to JSON
    save_email_to_json(email)
    
    # Close the browser after execution
    driver.quit()

# Execute the main function
if __name__ == "__main__":
    main()
