import json
import yaml


exclude = [
    "id",
]


def create_github_issue_form(schema_data):
    issue_form = {
        "name": "Digital Edition Entry",
        "description": "Submit a new digital edition to the catalog",
        "title": "[New Entry]: ",
        "labels": ["new-entry"],
        "body": [],
    }

    for field in schema_data:
        if field["name"] in exclude:
            continue
        # Process help_text to ensure proper YAML escaping while preserving markdown
        help_text = field["help_text"]
        # if "\n" in help_text:  # If multiline, use YAML literal block scalar
        #     help_text = f"{help_text}"

        # Changed logic: use dropdown if values exist
        field_type = (
            "dropdown" if "values" in field
            else "input" if field["type"] == "string"
            else "textarea"
        )

        form_element = {
            "type": field_type,
            "id": field["name"],
            "attributes": {
                "label": field["verbose_name"],
                "description": help_text,
            },
            "validations": {"required": not field.get("optional", False)},
        }

        # Add options for dropdown fields
        if "values" in field:
            form_element["attributes"]["options"] = field["values"]
            form_element["attributes"]["default"] = 0

        issue_form["body"].append(form_element)

    return issue_form


# Read the schema
with open("schema.json", "r", encoding="utf-8") as fp:
    schema_data = json.load(fp)

# Create the issue form
issue_form = create_github_issue_form(schema_data)


# Write the YAML file with custom dumper settings
class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


with open(".github/ISSUE_TEMPLATE/new-edition.yml", "w", encoding="utf-8") as fp:
    yaml.dump(issue_form, fp, allow_unicode=True, sort_keys=False, Dumper=MyDumper)
