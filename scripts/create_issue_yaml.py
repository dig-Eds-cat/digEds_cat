import json
import yaml


exclude = [
    "id",
]


def create_github_issue_form(schema_data):
    """Creates a GitHub issue form template for submitting new digital edition entries.
    This function takes schema data and converts it into a structured GitHub issue form template.
    The form includes input fields for various metadata about digital editions, with support
    for different field types (dropdown, input, textarea) based on the schema.
    Args:
        schema_data (list): A list of dictionaries containing the schema fields configuration.
            Each field dictionary should contain:
            - name (str): Field identifier
            - verbose_name (str): Display label for the field
            - help_text (str): Description/help text for the field
            - type (str): Data type of the field
            - optional (bool, optional): Whether field is required
            - values (list, optional): List of options for dropdown fields
    Returns:
        dict: A GitHub issue form template with the following structure:
            {
                "name": str,
                "description": str,
                "title": str,
                "labels": list,
                "body": list of form elements
    Note:
        Fields listed in the 'exclude' global variable will be skipped during form generation.
    """

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
        help_text = field["help_text"]
        field_type = (
            "dropdown"
            if "values" in field
            else "input" if field["type"] == "string" else "textarea"
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
        if "values" in field:
            form_element["attributes"]["options"] = field["values"]
            form_element["attributes"]["default"] = 0

        issue_form["body"].append(form_element)

    return issue_form


with open("schema.json", "r", encoding="utf-8") as fp:
    schema_data = json.load(fp)

issue_form = create_github_issue_form(schema_data)

with open(".github/ISSUE_TEMPLATE/new-edition.yml", "w", encoding="utf-8") as fp:
    yaml.dump(issue_form, fp, allow_unicode=True, sort_keys=False)
