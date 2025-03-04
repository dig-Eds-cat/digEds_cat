import json
import os


with open("schema.json", "r", encoding="utf-8") as fp:
    data = json.load(fp)

with open("scripts/CONTRIBUTING_template.md", "r", encoding="utf-8") as fp:
    text = fp.read()

for x in data:
    heading = f"#### {x["verbose_name"]}\n\n"
    body = f'{x["help_text"]}\n\n'
    text += heading
    text += body

with open(os.path.join(".github", "CONTRIBUTING.md"), "w", encoding="utf-8") as fp:
    fp.write(text)
