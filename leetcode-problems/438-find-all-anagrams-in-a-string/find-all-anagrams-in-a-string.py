class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        txt = s
        pat = p
        i = 0
        j = 0
        count = 0
        k = len(pat)
        N= len(txt)
        pat_dict = dict(Counter(pat))
        cnt = len(pat_dict)
        ans = []
        while j<N:
            if txt[j] in pat_dict:
                pat_dict[txt[j]]-=1
                if pat_dict[txt[j]] == 0:
                    cnt -=1
            
            if j-i+1 < k:
                j+=1
            elif j-i+1==k:
                if cnt == 0:
                    ans.append(j-k+1)
                if txt[i] in pat_dict:
                    pat_dict[txt[i]]+=1
                    if pat_dict[txt[i]]==1:
                        cnt+=1
                i+=1
                j+=1
        return ans
        