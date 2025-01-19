import pandas as pd
import re

def clean_html(content):
    clean_text = re.sub(r'<(?!a\s|/a)[^>]+>', '', content)
    clean_text = re.sub(r'<a href="([^"]+)".*?>(.*?)</a>', r'\2 (\1)', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df['Problem'] = df['Problem'].apply(clean_html)
    df.to_csv(output_file, index=False)

def split_problems(text):
    problems = []
    pattern = re.compile(r'(\d+) ([^\(]+)\s+\(([^)]+)\) ([A-Z]) ([\d\.]+)(?: Vid \(([^)]*)\))? ?(?:/ Code \(([^)]*)\))?')
    matches = pattern.findall(text)

    for match in matches:
        problem = {
            'name': match[1].strip(),
            'link': match[2].strip(),
            'difficulty': match[3].strip() + ' ' + match[4].strip(),
            'video': match[5].strip() if match[5] else None, 
            'code': match[6].strip() if match[6] else None
        }
        problems.append(problem)

    return problems

def clean_data(file_path):
    df = pd.read_csv(file_path)
    records = []

    for _, row in df.iterrows():
        topic = row['Topic']
        company = row['Company']
        problem_text = row['Problem']

        if isinstance(problem_text, str):
            problems = split_problems(problem_text)

            for problem in problems:
                records.append({
                    'Topic': topic,
                    'Company': company,
                    'Problem Name': problem['name'],
                    'Difficulty': problem['difficulty'],
                    'Link': problem['link'],
                    'Video': problem.get('video', ''),  
                    'Code': problem.get('code', '') 
                })

    return pd.DataFrame(records)

if __name__ == '__main__':
    clean_csv('results.csv', 'clean_res.csv')
    cleaned_df = clean_data('clean_res.csv')
    cleaned_df.to_csv('clean_res.csv', index=False)


