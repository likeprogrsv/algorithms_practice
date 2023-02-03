from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i in range(len(strs[0])):
            for x in strs:
                try:
                    if strs[0][i] == x[i]:
                        continue
                    else:
                        return pref
                except:
                    return pref
            pref += strs[0][i]
        return pref
