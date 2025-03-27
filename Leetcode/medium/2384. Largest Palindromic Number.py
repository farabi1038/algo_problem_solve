class Solution:
    def largestPalindromic(self, num: str) -> str:

        #Count the occurance:
        string_builder=[]
        text_count = Counter(num)
        
        middle=''
        for i in sorted(text_count.keys(), reverse=True):
            j=text_count[i]
            if j%2==1 and middle=='':
                middle=i
            string_builder.append(i*(j//2))

        left= ''.join(string_builder).lstrip('0')
        if left=='' and middle== '':
            return '0'
        return left+middle+left[::-1]        
            

        
