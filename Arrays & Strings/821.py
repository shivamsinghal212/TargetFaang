"""
Author: Shivam Singhal
Date Attempted: 08-Aug-23
Time Taken: 40 mins
Status: Accepted
Link: https://leetcode.com/problems/shortest-distance-to-a-character/
"""
from typing import List


def shortestToChar(s: str, c: str) -> List[int]:
    c_arr_loc = []
    sol_arr = []

    i = 0
    while i < len(s):
        if s[i] == c:
            c_arr_loc.append(i)
        i += 1

    j = 0
    new_min_pos = 0

    while j < len(s):
        if len(c_arr_loc) == 1:
            diff = abs(c_arr_loc[new_min_pos] - j)
            sol_arr.append(diff)
            j += 1
        elif len(c_arr_loc) > 1:
            diff1 = abs(c_arr_loc[new_min_pos] - j)
            if len(c_arr_loc) - 1 == new_min_pos:
                diff2 = abs(c_arr_loc[new_min_pos] - j)
            else:
                diff2 = abs(c_arr_loc[new_min_pos + 1] - j)

            if diff2 < diff1:
                new_min_pos += 1
            sol_arr.append(min(diff1, diff2))
            j += 1
    return sol_arr


print(shortestToChar("aaabaaadbaaa", "a"))
