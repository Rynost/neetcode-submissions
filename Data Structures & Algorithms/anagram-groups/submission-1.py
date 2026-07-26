class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myhash = defaultdict(list)

        for s in strs: #loop through strings
            count = [0] * 26 #creates string num map

            for c in s: #loop through chars
                count[(ord(c) - ord("a"))] += 1 #counts
            myhash[tuple(count)].append(s)
        return list(myhash.values())
             