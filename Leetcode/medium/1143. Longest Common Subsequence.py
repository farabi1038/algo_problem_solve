class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        sub_array=[[0]*(len(text2)+1) for n in range(len(text1)+1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                    if text1[i-1]==text2[j-1]:
                        sub_array[i][j]=sub_array[i-1][j-1]+1
                    else:
                        sub_array[i][j]=max(sub_array[i-1][j],sub_array[i][j-1])   
        return sub_array[len(text1)][len(text2)]

        