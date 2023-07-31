def transform(legacy_data: dict) -> dict:
    result = dict()

    for score, chars in legacy_data.items():
        for char in chars:
            result[char.lower()] = score

    return result
