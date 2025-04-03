class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cn = Counter(s)
        print(cn)
        result =''
        used =set()
        for i in order:
            result+=i*cn[i]
            used.add(i)
      

        for i in s:
            if i not in used:
                result+=i 
        return result           

        