# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    del list_to_remove_elements[4:6]
    del list_to_remove_elements[0:1]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    return ['Pink'] + list_to_add_elements + ['Yellow']

def is_empty(list_to_check):
    return not len(list_to_check)

def check_lists(list_to_compare1, list_to_compare2):
    return list_to_compare1[2:3] == list_to_compare2[2:3]

def list_of_lists(list_of_lists_to_modify):
    
    return [
        list_of_lists_to_modify[0][:2],
        list_of_lists_to_modify[1][1:4],
        list_of_lists_to_modify[2][-2:]
    ]
    
