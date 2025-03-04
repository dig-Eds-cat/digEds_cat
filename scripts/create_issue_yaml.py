import json
import yaml


def create_github_issue_form(schema_data):
    issue_form = {
        "name": "Digital Edition Entry",
        "description": "Submit a new digital edition to the catalog",
        "title": "[New Entry]: ",
        "labels": ["new-entry"],
        "body": [],
    }

    for field in schema_data:
        # Process help_text to ensure proper YAML escaping while preserving markdown
        help_text = field["help_text"]
        if "\n" in help_text:  # If multiline, use YAML literal block scalar
            help_text = f"|\n{help_text}"

        form_element = {
            "type": (
                "input"
                if field["type"] == "string"
                else "dropdown" if "values" in field else "textarea"
            ),
            "id": field["name"],
            "attributes": {
                "label": field["verbose_name"],
                "description": help_text,
            },
            "validations": {"required": not field.get("optional", False)},
        }

        # Add values for dropdown fields
        if "values" in field:
            form_element["attributes"]["options"] = field["values"]

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
