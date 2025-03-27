import re
import requests
import pandas as pd

ISSUE_NR = 409


def parse_issue_body(body):
    sections = re.split(r'###\s+', body)
    sections = [s.strip() for s in sections if s.strip()]
    parsed_data = {}
    for section in sections:
        lines = section.split('\n', 1)
        if len(lines) == 2:
            key = lines[0].strip()
            value = lines[1].strip()
            parsed_data[key] = value

    return parsed_data


df = pd.read_csv("digEds_cat.csv")
url = f"https://api.github.com/repos/dig-Eds-cat/digEds_cat/issues/{ISSUE_NR}"

response = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})

if response.status_code == 200:
    issue_data = response.json()
    parsed_issue = parse_issue_body(issue_data["body"])
    parsed_issue["id"] = 99999
    new_row = pd.DataFrame([parsed_issue])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("digEds_cat.csv", index=False)
