def get_even_dict(raw_data: dict) -> dict:
    print(raw_data)
    raw_data = {key: value for key, value in raw_data.items() if isinstance(value, int) and value % 2 == 0}
    print(raw_data)
    return raw_data

def get_dict_consisting_of_string(raw_data: dict) -> dict:
    raw_data = {str.lower(key): value for key, value in raw_data.items() if isinstance(key, str) and key.isalpha()}
    return raw_data


def get_not_none_value_dict(raw_data: dict) -> dict:
    raw_data = {key: value for key, value in raw_data.items() if value}
    print(raw_data)
    return raw_data
