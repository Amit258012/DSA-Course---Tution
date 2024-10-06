# https://leetcode.com/problems/group-anagrams/description/

"""
The goal is to group words (strings) that are anagrams of each other. Anagrams are words that have the same characters but in a different order (e.g., "bat" and "tab"). To group the anagrams, we can sort each string's characters to form a key and store the original strings in a hash map (hmap) using the sorted string as the key. All strings with the same sorted key are anagrams and will be grouped together in the hash map.

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams, where the key is the sorted version of the string
        hmap = {}

        # Iterate over each string in the list
        for s in strs:
            # Sort the string to form a key that will be the same for all anagrams
            k = "".join(sorted(s))

            # If the sorted key exists in the dictionary, append the original string to its list
            if k in hmap:
                hmap[k].append(s)
            else:
                # Otherwise, create a new list with the string
                hmap[k] = [s]

        # Collect all the anagram groups from the dictionary
        res = []
        for val in hmap.values():
            res.append(val)

        # Return the list of anagram groups
        return res
