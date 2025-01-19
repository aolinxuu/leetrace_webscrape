import pandas as pd
from bs4 import BeautifulSoup

def clean_html(row):
    soup = BeautifulSoup(row, 'html.parser')
    rows = soup.find_all('tr')
    cleaned_rows = []
    for tr in rows:
        cells = tr.find_all('td')
        entry = {
            "Problem ID": cells[0].text.strip(),
            "Problem Name": cells[1].text.strip(),
            "Difficulty": cells[2]['class'][0] if cells[2]['class'] else "Not classified",
            "Score": cells[3].text.strip(),
            "Resources": ' / '.join([a['href'] for a in cells[4].find_all('a')])
        }
        cleaned_rows.append(entry)
    return cleaned_rows

# Example DataFrame
data = {
    "Topic": ["array", "array"],
    "Company": ["accenture", "adobe"],
    "Problem": [
        # Add your actual HTML content here
        "<tbody>...</tbody>",
        "<tbody>...</tbody>"
    ]
}

df = pd.DataFrame(data)
df['Cleaned Data'] = df['Problem'].apply(clean_html)
print(df['Cleaned Data'].values.tolist())