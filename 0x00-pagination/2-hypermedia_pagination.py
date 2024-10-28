#!/usr/bin/env python3
"""This module contains a simple pagination function"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct page from the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing the following key-value pairs:
        - page_size - the length of the returned dataset page
        - page - the current page number
        - data - the dataset  page (equivalent to return from previous task)
        - next_page - the next page number in the dataset (None if no further pages)
        - prev_page - the previous page number in the dataset (None if no further pages)
        - total_pages - the total number of pages in the dataset as an integer
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = []

        with open("Popular_Baby_Names.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        data = data[1:]

        total_pages = math.ceil(len(data) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": data[(page - 1) * page_size : page * page_size],
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
