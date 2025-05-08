def drop_fields(data, fields_to_drop):
    for session in data:
        for field in fields_to_drop:
            if "." in field:
                drop_nested_field(session, field)
            else:
                session.pop(field, None)
    return data

def drop_nested_field(d, field_path):
    keys = field_path.split(".")
    # Bis zum vorletzten dict gehen, um das letzte zu löschen
    for key in keys[:-1]:
        d = d.get(key, {})
    d.pop(keys[-1], None)