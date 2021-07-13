def process_numbers(unprocessed_list):

    processed_list = []
    
    if not isinstance(unprocessed_list, list):
        return processed_list
    
    for item in unprocessed_list:
        if isinstance(item, int):
            processed_list.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                converted_item = int(item)
                processed_list.append(converted_item)

    processed_list.sort()

    return processed_list


def process_names(unprocessed_list):

    processed_list = []

    if not isinstance(unprocessed_list, list):
        return processed_list

    for item in unprocessed_list:
        if isinstance(item, str):
            if not item.isnumeric():
                processed_list.append(item)

    processed_list.sort()

    return processed_list