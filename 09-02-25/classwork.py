def find_value_by_key(list_of_dicts, key):
    values = []
    for dictionary in reversed(list_of_dicts):
        if key in dictionary:
            values.append(dictionary[key])
    return values

def evaluate(value, names):
    if isinstance(value, (int, float)):
        return value

    elif isinstance(value, str):
        if value in names:
            return names[value]

    elif isinstance(value, dict):
        if not (isinstance(value, dict) and ("function" in value or "macro" in value)):
            return "Error"
        if "function" in value:
            key = "function"
        else:
            key = "macro"
        return find_value_by_key(value, key)
