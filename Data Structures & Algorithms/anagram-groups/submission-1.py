class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sett={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in sett:
                sett[key]=[]
            sett[key].append(i)
        return list(sett.values())
        
                    


        