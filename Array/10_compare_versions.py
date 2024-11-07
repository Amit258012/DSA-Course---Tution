# https://leetcode.com/problems/compare-version-numbers/

"""
To solve this, we can split each version string into parts using the dot (.) separator, convert each part to an integer, and compare the corresponding parts one by one. If a part is missing in one version (due to unequal lengths of the versions), we treat it as 0. Based on the comparison of the parts, we return:

1 if version1 is greater,
-1 if version2 is greater,
0 if both versions are equal.

Time Complexity: O(max(n, m))
Space Complexity: O(n + m)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 1) Split the version strings based on "." and store them in lists
        v1, v2 = version1.split("."), version2.split(".")

        # Get the lengths of the two version arrays
        n = len(v1)
        m = len(v2)

        # 2) Initialize two pointers to traverse both version arrays
        i = j = 0

        # 3) Traverse both version arrays while either has elements left
        while i < n or j < m:
            # Extract the integer from version1 if available, otherwise treat it as 0
            r1 = int(v1[i]) if i < n else 0
            # Extract the integer from version2 if available, otherwise treat it as 0
            r2 = int(v2[j]) if j < m else 0

            # Compare the current parts of both versions
            if r1 < r2:
                return -1  # version1 is smaller than version2
            elif r1 > r2:
                return 1  # version1 is greater than version2
            # Move to the next parts
            i += 1
            j += 1

        # If we finish the loop and find no difference, the versions are equal
        return 0
