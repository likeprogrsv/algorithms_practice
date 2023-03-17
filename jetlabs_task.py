from typing import List, Union
import pytest


data = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"},
        {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]


class DeleteDuplicates:
    """
        Delete duplicates entities
    """
    def del_dict_duplicates(self, input: Union[list, tuple]) -> List[dict]:
        """
        Delete duplicate dictionaries in lists or tuples
        """
        # Check type on input
        if not isinstance(input, (list, tuple,)):
            raise TypeError("Input must be list or tuple")
        result: list = []
        checked: set = set()
        for value in input:
            if tuple(value.items()) not in checked:
                checked.add(tuple(value.items()))
                result.append(value)
        return result


test_del_duplic = DeleteDuplicates()


@pytest.mark.parametrize('list, answer', [
    (data, [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}, {},
            {'key2': 'value2'}]),
    ([{'key2': 'value2'}, {'key2': 'value2'}], [{'key2': 'value2'}]),
    ([{'key2': 'value2'}, {}, {}, {}], [{'key2': 'value2'}, {}]),
    ])
def test_del_dict_duplic(list: List[dict], answer: List[dict]):
    assert test_del_duplic.del_dict_duplicates(list) == answer



'''
def del_dict_duplicates(self, input: Union[list, tuple]) -> List[dict]:
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
    '''