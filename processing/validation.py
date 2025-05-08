from bson import ObjectId


def validate_dataset(data, validation_rules):
    valid_entries = []
    for entry in data:
        is_valid = validate_entry(entry, validation_rules)
        if is_valid:
            valid_entries.append(entry)
    return valid_entries


def validate_entry(entry, validation_rules):
    for field_path, rules in validation_rules.items():
        # Den tatsächlichen/kleinsten Wert holen
        value = get_nested(entry, field_path)
        if not validate_field(value, rules):
            return False
    return True


def get_nested(d: dict, path: str):
    keys = path.split(".")
    for key in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(key)
    return d


def validate_field(value, validation_rules):
    # 0. Prüfung auf ObjectID
    if isinstance(value, (str, ObjectId)):
        value = str(value)

    # 1. Pflichtfeld
    if validation_rules.get("required"):
        if value in (None, ""):
            return False

    # 2. Alphanumerisch
    if validation_rules.get("alphanumeric"):
        if not value.isalnum():
            return False

    # 3. Numeric
    if validation_rules.get("numeric"):
        if not isinstance(value, int):
            return False

    # 4. Boolean
    if validation_rules.get("bool"):
        if not isinstance(value, bool):
            return False

    # 5. Länge
    if "length" in validation_rules:
        expected_length = validation_rules["length"]
        value = str(value)
        if not len(value) == expected_length:
            return False

    # 6. Min
    if validation_rules.get("min"):
        if value < validation_rules["min"]:
            return False

    # 7. Max
    if validation_rules.get("max"):
        if value > validation_rules["max"]:
            return False

    return True
