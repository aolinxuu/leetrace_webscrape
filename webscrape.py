import csv
from selenium import webdriver
from util import set_questions, set_difficulty, set_topics, set_companies, clear_topics, clear_companies, get_results

topics = [
    "array", "backtracking", "binary-indexed-tree", "binary-search", "binary-search-tree",
    "binary-tree", "bit-manipulation", "bitmask", "breadth-first-search", "combinatorics",
    "counting", "depth-first-search", "design", "divide-and-conquer", "dynamic-programming",
    "enumeration", "geometry", "graph", "greedy", "hash-function", "hash-table", "heap-priority-queue",
    "linked-list", "math", "matrix", "memoization", "monotonic-stack", "number-theory", "ordered-set",
    "prefix-sum", "queue", "recursion", "rolling-hash", "segment-tree", "shortest-path",
    "simulation", "sliding-window", "sorting", "stack", "string", "string-matching", "topological-sort",
    "tree", "trie", "two-pointers", "union-find"
]

companies = [
    "accenture", "adobe", "affirm", "agoda", "airbnb", "amazon", "anduril", "apple",
    "arista-networks", "atlassian", "blackrock", "bloomberg", "bytedance", "capital-one",
    "cisco", "citadel", "databricks", "datadog", "de-shaw", "doordash", "epic-systems",
    "facebook", "goldman-sachs", "google", "grammarly", "ibm", "infosys", "intuit",
    "linkedin", "lyft", "microsoft", "nvidia", "oracle", "palantir-technologies",
    "paypal", "phonepe", "pinterest", "roblox", "salesforce", "servicenow", "snowflake",
    "tcs", "tiktok", "turing", "uber", "visa", "walmart-labs", "wix", "yandex", "zoho"
]

driver = webdriver.Chrome()
driver.get("https://leetracer.com/screener")

with open('results.csv', mode='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['Topic', 'Company', 'Problem'])

    try:
        set_questions(driver)
        set_difficulty(driver, ["medium", "hard"])

        for topic in topics:
            clear_topics(driver)
            set_topics(driver, [topic])

            for company in companies:
                clear_companies(driver)
                set_companies(driver, [company])

                results = get_results(driver)
                html_content = results.get_attribute('outerHTML')
                writer.writerow([topic, company, html_content])

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()