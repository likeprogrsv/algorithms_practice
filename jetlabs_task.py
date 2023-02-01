data = ({"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, \
          {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"})


from typing import List, Union

def del_dict_duplicates(input: Union[list, tuple]) -> List[dict]: 
    """
    Delete duplicate dictionaries in lists or tuples
    """  
    # Check type on input
    if not isinstance(input, (list, tuple,)):
        raise TypeError("Input must be list or tuple")
    
    result: list = []
    checked: dict = {}
    for indx, value in enumerate(input):
        if tuple(value.items()) not in checked.keys():            
            # Reducing memory usage by assignment int type value in dict
            checked[tuple(value.items())] = indx
            result.append(value)
    return result

print(del_dict_duplicates(data))
