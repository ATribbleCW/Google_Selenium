from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# Set up the webdriver 
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

def search_and_get_first_element(query):
   
    driver.get("https://www.google.com")

    # Find the search box, enter the query, and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query + Keys.RETURN)

    # Attempt to locate the first visible element in the search results
    try:
        # Find the first result by checking for <h3> and other possible elements
        first_result = driver.find_element(By.CSS_SELECTOR, "h3, .g, .BNeawe")
        element_tag = first_result.tag_name
        print(f"First result element tag: {element_tag}")
        print("Content:", first_result.text)
    except Exception as e:
        print("Could not find the first result element:", e)

# Prompt the user to enter a search term
search_term = input("Enter a search term: ")
search_and_get_first_element(search_term)

# Close the browser
driver.quit()