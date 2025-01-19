from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# click all questions
def set_questions(driver):
    wait = WebDriverWait(driver, 20)
    questions = ["neet150", "grind75", "grind169", "blind75", "all_problems"]
    for q in questions:
        question_checkbox = wait.until(EC.element_to_be_clickable((By.ID, q)))
        if not question_checkbox.is_selected():
            question_checkbox.click()

# click medium and hard difficulties
def set_difficulty(driver, difficulties):
    wait = WebDriverWait(driver, 20)
    all_difficulties = ["easy", "medium", "hard"]
    for d in all_difficulties:
        difficulty_checkbox = wait.until(EC.element_to_be_clickable((By.ID, d)))
        if d in difficulties:
            if not difficulty_checkbox.is_selected():
                difficulty_checkbox.click()
        else:
            if difficulty_checkbox.is_selected():
                difficulty_checkbox.click()

def set_topics(driver, topics):
    wait = WebDriverWait(driver, 20)
    topic_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownMenuButton1")))
    topic_dropdown.click()

    for t in topics:
        topic_checkbox = wait.until(EC.element_to_be_clickable((By.ID, t)))
        if not topic_checkbox.is_selected():
            topic_checkbox.click()
    # close dropdown        
    topic_dropdown.click()

def set_companies(driver, companies):
    wait = WebDriverWait(driver, 20)
    company_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownMenuButton2")))
    company_dropdown.click()

    for c in companies:
        company_checkbox = wait.until(EC.element_to_be_clickable((By.ID, c)))
        if not company_checkbox.is_selected():
            company_checkbox.click()
    # close dropdown        
    company_dropdown.click()

def clear_topics(driver):
    wait = WebDriverWait(driver, 20)
    topic_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownMenuButton1")))
    topic_dropdown.click()
    topic = wait.until(EC.element_to_be_clickable((By.ID, "NONE1")))
    topic.click()
    # close dropdown
    topic_dropdown.click()
    
def clear_companies(driver):
    wait = WebDriverWait(driver, 20)
    company_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownMenuButton2")))
    company_dropdown.click()
    company = wait.until(EC.element_to_be_clickable((By.ID, "NONE2")))
    company.click()
    # close dropdown
    company_dropdown.click()

def get_results(driver):
    wait = WebDriverWait(driver, 20)
    update_settings = wait.until(EC.element_to_be_clickable((By.NAME, "button_settings")))
    update_settings.click()
    
    wait.until(EC.visibility_of_element_located((By.ID, "results")))
    return driver.find_element(By.CSS_SELECTOR, "#results > tbody")
    