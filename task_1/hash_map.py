from typing import Hashable


# This class contains a constructor with key, value, next properties of a hash table.
class Item:
    def __init__(self, key: Hashable, value: any):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self, size=100):
        """
        Initialize data structure.
        """
        # Size is defined by our (default=100). Can define it anything size.
        self.size: int = size
        # The size of the items is dependent on our size
        self.items: list[Item | None] = [None] * size

    # This method helps to calculate the index of the hash table.
    def _get_index(self, key: Hashable) -> int:
        return hash(key) & self.size - 1

    # This method helps to add a new key, value pair into the hash table.
    def put(self, key: Hashable, value: any) -> None:
        """
        value will always be non-negative.
        :type key: Hashable
        :type value: any
        :rtype: None
        """
        # get the index
        index = self._get_index(key)
        item = self.items[index]
        # There are three(3) conditions to consider:
        # 1. If there is no key, value pair existing in the index, then create a new node to the index in hash table.
        if item is None:
            self.items[index] = Item(key, value)
        # If the key present in the index, then
        else:
            # If the key is same, then update the value.
            if item.key == key:
                item.value = value
            else:
                # Iterate through the loop while if the key is not same
                while True:
                    # 2. We check if the item has the same key as the new item, then we update the value and return.
                    if item.key == key:
                        item.value = value
                        return
                    else:
                        # 3. If not item have next item, then we add the new item to the next item.
                        if not item.next:
                            item.next = Item(key, value)
                            return
                        # 4. Else we move to the next item
                        item = item.next

    def get(self, key: Hashable) -> any:
        """
        Returns the value to which the specified key is mapped, or raise ValueError if this map contains no mapping for the key
        :type key: Hashable
        :rtype: any
        """
        # get the index
        index = self._get_index(key)
        # 1. Check if the key is present
        if self.items[index] is None:
            raise ValueError
        item = self.items[index]
        # Iterate through the loop while if the key is not same
        while True:
            # 2. We check if the item has the same key as the new item, then we update the value and return.
            if item.key == key:
                return item.value
            else:
                # 3. If item have next item, then we move to the next item
                if item.next:
                    item = item.next
                # 4. Elif item have no next item, we raise ValueError
                else:
                    raise ValueError
