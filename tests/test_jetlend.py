import pytest
from typing import List
from jetlabs_task import DeleteDuplicates

data = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"},
        {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

test_del_duplic = DeleteDuplicates()


@pytest.mark.parametrize('list, answer', [
    (data, [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}, {},
            {'key2': 'value2'}]),
    ([{'key2': 'value2'}, {'key2': 'value2'}], [{'key2': 'value2'}]),
    ([{'key2': 'value2'}, {}, {}, {}], [{'key2': 'value2'}, {}]),
    ])
def test_del_dict_duplic(list: List[dict], answer: List[dict]):
    assert test_del_duplic.del_dict_duplicates(list) == answer
