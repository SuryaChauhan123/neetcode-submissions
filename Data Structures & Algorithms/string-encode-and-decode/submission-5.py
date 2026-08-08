class Solution:

    def encode(self, strs: List[str]) -> str:
        string=''
        if strs==[]:
            return ''
        else:
            for i in strs:
                string+=i
                string+="@breaker@"
            return string


    def decode(self, s: str) -> List[str]:
        if s=='':
            return []
        else:
            string=s[0:len(s)-9]
            lst=string.split('@breaker@')
            return lst
