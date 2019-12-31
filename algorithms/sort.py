"""Sorting algorithms for lists."""

from math import ceil


class ListSort(list):
    """Built-in list class augmented with sort algorithms."""

    #  Quicksort helper methods

    @staticmethod
    def choose_median(a_list):
        """Choose index of median of first, last, and middle entries.

        Assumes entries are comparable orderable types.

        Parameters
        ----------
        a_list : list
            List to choose median from


        Returns
        -------
        median_index : int
            Index of median of first, last and middle entries
        """
        len_list = len(a_list)
        # first, last, and middle entries
        p1 = a_list[0]
        p2 = a_list[ceil((len_list / 2) - 1)]
        p3 = a_list[len_list - 1]
        # if middle entry is between first and last
        if (p1 <= p2 <= p3) or (p3 <= p2 <= p1):
            median_index = ceil((len_list / 2) - 1)
        # else if first entry is between middle and last
        elif (p2 <= p1 <= p3) or (p3 <= p1 <= p2):
            median_index = 0
        # else last entry is between first and middle
        else:
            median_index = len_list - 1
        return median_index

    @staticmethod
    def partition(a_list, left_index, right_index):
        """Partition list around pivot entry at left index.

        Partitions list in place and returns new index of pivot.

        Parameters
        ----------
        left_index : int
            Index to pivot around. All smaller entries in list will end up
            to left of entry at this index.
        right_index : int
            Index to end partitioning. All entries to the right of this index
            will not be included in partitioning.

        Returns
        -------
        new_index : int
            Index of pivot entry after partitioning
        """
        # pivot is entry at left index
        p = a_list[left_index]
        # begin new index iterating from location of pivot entry
        i = left_index + 1
        # for all other entries between indices
        for j in range(left_index + 1, right_index + 1):
            # if entry is less than pivot
            if a_list[j] < p:
                # swap entry with entry at new index
                a_list[i], a_list[j] = a_list[j], a_list[i]
                # incremement new index
                i += 1
        # swap pivot with rightmost entry smaller than pivot
        new_index = i - 1
        a_list[left_index], a_list[new_index] = (a_list[new_index],
                                                 a_list[left_index])
        return new_index

    def quicksort(self, choose_pivot=choose_median.__func__):
        """Recursive quicksort.

        Parameters
        ----------
        choose_pivot : function, default choose_median
            Method for choosing pivot.

        Returns
        -------
        self_sorted : ListSort
            sorted copy of self
        """
        self_sorted = self.copy()
        # list length
        len_list = len(self_sorted)
        # base case
        if len_list == 0 or len_list == 1:
            pass
        # recursive case
        else:
            # choose pivot index and swap with first element
            index_p = choose_pivot(self_sorted)
            self_sorted[0], self_sorted[index_p] = (self_sorted[index_p],
                                                    self_sorted[0])

            # partition around pivot (first element)
            index_p = ListSort.partition(self_sorted, 0, len_list - 1)

            # get left and right lists and lengths
            left_list = ListSort(self_sorted[:index_p])
            right_list = ListSort(self_sorted[index_p + 1:])

            # recurse on both sides of pivot
            left_list = left_list.quicksort(choose_pivot)
            right_list = right_list.quicksort(choose_pivot)

            self_sorted = ListSort(left_list + [self_sorted[index_p]] +
                                   right_list)
        return self_sorted

    # mergesort helper method

    @classmethod
    def merge(cls, list1, list2):
        """Merge two sorted lists into sorted list.

        Assumes both lists are non-empty.

        Parameters
        ----------
        list1 : list
            First list to merge
        list2: list
            Second list to merge

        Returns
        -------
        merged_list : list
            Merged list
        """
        # check lists are non-empty
        assert list1 and list2, "Both lists should be non-empty"

        # initialize return list
        merged_list = []

        # iterate through one list
        while list1:
            if list1[0] < list2[0]:
                merged_list += [list1.pop(0)]
            else:
                merged_list += [list2.pop(0)]
            if not list2:
                break

        # add remainders of lists (possibly empty)
        merged_list += (list1 + list2)
        return cls(merged_list)

    def mergesort(self):
        """Recursive mergesort.

        Returns
        -------
        self_sorted : ListSort
            sorted copy of self
        """
        self_sorted = self.copy()
        # base case -- list has length 1
        if len(self_sorted) == 1:
            pass
        # recursive case -- uses merge helper function
        else:
            # index of middle entry
            mid = len(self_sorted) // 2
            # get left and right hand lists
            left = ListSort(self_sorted[:mid])
            right = ListSort(self_sorted[mid:])
            # recursively merge left and right lists
            left = left.mergesort()
            right = right.mergesort()
            # merge left and right sorted lists
            self_sorted = ListSort.merge(left, right)
        return self_sorted
