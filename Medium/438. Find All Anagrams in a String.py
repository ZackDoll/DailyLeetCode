class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #hashmaps
        counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        curr_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        
        for c in p:
            counts[c] += 1

        indexes = []
        
        if len(p) > len(s):
            return []
        #initialize substring
        end = len(p) - 1
        sub = s[:end + 1]
        for c in sub:
            curr_counts[c] += 1

        for i in range(len(s)):
            if end == len(s):
                continue
            else:
                if counts == curr_counts:
                    indexes.append(i)

                end += 1
                if end != len(s):
                    curr_counts[s[end]] += 1
                
                curr_counts[s[i]] -= 1
                
        return indexes




            
        
            
            
