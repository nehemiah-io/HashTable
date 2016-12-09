#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size

        Θ(n) running time to initialize n empty linked lists"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table

        Θ(1) running time to loop over entire list within list to print"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored

        Θ(1) running time to do operations (unless hash function is not constant time)"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets

        Θ(n) running time to loop over entire bucket list"""
        count = 0

        for bucket in self.buckets:
            # bucket should be a list containing the key value pairs
            count += bucket.length()

        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False

        Best case running time: Ω(1) if key is near the head
       Worst case running time: O(n) if key is the tail or not in the list"""
        # TODO: Check if the given key exists in a bucket

        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]
        for node in bucket:
            if node.data[0] == key:
                return True

            # current = bucket.head

            # while current.next is not None:
            #     if current.data == key:
            #         return True
            #     current = current.next

        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError

         Best case running time: Ω(1) if item is near the head of the list.
       Worst case running time: O(n) if item is near the tail of the list or
       not present and we need to loop through all n nodes in the list"""
        # TODO: Check if the given key exists and return its associated value
        bucket = self.buckets[self._bucket_index(key)]
        data = bucket.find(lambda node: node[0] == key)
        if data is not None:
            return data[1]


            # current = bucket.head

            # while current.next is not None:
            #     if current.data[0] == key:
            #         return current.data[1]
            #     current = current.next

        raise KeyError

    def set(self, key, value):
        """Insert or update the given key with its associated value

        Best case running time: Ω(1) if item is near the head of the list.
       Worst case running time: O(n) if item is near the tail of the list or
       not present and we need to loop through all n nodes in the list"""
        # TODO: Insert or update the given key-value entry into a bucket
        hashKey = hash(key) % len(self.buckets)
        bucket = self.buckets[hashKey]
        if bucket.find(lambda node: node[0] == key):
            for node in bucket:
                if node.data[0] == key:
                    bucket.delete(node.data)
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError

        Best case running time: Ω(1) if item is near the head of the list.
       Worst case running time: O(n) if item is near the tail of the list or
       not present and we need to loop through all n nodes in the list"""
        # TODO: Find the given key and delete its entry if found

        # get the bucket by using the hash

        bucketIndex = hash(key) % len(self.buckets)
        bucket = self.buckets[bucketIndex]
        for node in bucket:
            if key == node.data[0]:
                bucket.delete(node.data)
                return


        # current = bucket.head

        # while current.next is not None:
        #     if current.data[0] == key:
        #         #remove key val pair from hash table
        #     current = current.next

        raise KeyError

    def keys(self):
        """Return a list of all keys in this hash table

        Θ(n+b) running time to loop over entire list within list"""
        keys = []
        for bucket in self.buckets:
            for node in bucket:
                keys.append(node.data[0])

        return keys

    def values(self):
        """Return a list of all values in this hash table

        Θ(n+b) running time to loop over entire list within list"""
        # TODO: Collect all values in each of the buckets
        values = []
        for bucket in self.buckets:
            for node in bucket:
                values.append(node.data[1])

        return values

    def items(self):
        """Return a list of all key, value pairs in the hash table


        Θ(n) running time to loop over entire list within list"""
        keys = self.keys()
        values = self.values()
        items = []

        for i in range(len(keys)):
            items.append((keys[i], values[i]))

        return items

    def __iter__(self):
        """Make linked list iterable

        Best case running time: Ω(1) if iteration is broken from the other side
       Worst case running time: O(n) if iteration continues for the length of the list"""
        for node in self.buckets:
            yield node
