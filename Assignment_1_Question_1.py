#!/usr/bin/env python
# coding: utf-8

# Question 1
# 
# Python List Manipulation Task
# 
# Python List Manipulation Task
# 
# 
# 
# Task Description:
# 
# Create a class named ListManipulator with the following methods:
# __init__: Initializes an empty list.
# add_elements: Takes a list of elements as a parameter and appends them to the internal list.
# remove_duplicates: Removes duplicate elements from the internal list.
# reverse_list: Reverses the order of elements in the internal list.
# sort_list: Sorts the elements in the internal list in ascending order.
# get_unique_elements: Returns a new list containing only the unique elements from the internal list.
# remove_element: Takes an element as a parameter and removes its first occurrence from the internal list.
# get_list: Returns the current state of the internal list.

# In[1]:


class ListManipulator:
    def __init__(self):
        self.internal_list = []

    def add_elements(self, elements):
        self.internal_list.extend(elements)

    def remove_duplicates(self):
        self.internal_list = list(set(self.internal_list))

    def reverse_list(self):
        self.internal_list.reverse()

    def sort_list(self):
        self.internal_list.sort()

    def get_unique_elements(self):
        return list(set(self.internal_list))

    def remove_element(self, element):
        if element in self.internal_list:
            self.internal_list.remove(element)

    def get_list(self):
        return self.internal_list

# Example usage:
lm = ListManipulator()
lm.add_elements([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
print("Original List:", lm.get_list())

lm.remove_duplicates()
print("List after removing duplicates:", lm.get_list())

lm.reverse_list()
print("Reversed List:", lm.get_list())

lm.sort_list()
print("Sorted List:", lm.get_list())

unique_elements = lm.get_unique_elements()
print("Unique Elements:", unique_elements)

lm.remove_element(3)
print("List after removing element 3:", lm.get_list())


# In[ ]:




