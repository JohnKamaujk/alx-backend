#!/usr/bin/env python3
"""Simple pagination module.
"""

import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None  # Added this line

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves info about a page from a given index and with a
        specified size.
        """
        assert isinstance(index, int)
        assert 0 <= index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(index, page_size)
        next_index = end_index

        data_page = [self.__indexed_dataset[i] for i in range
                     (start_index, end_index)
                     if i in self.__indexed_dataset]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data_page),
            "data": data_page,
        }
