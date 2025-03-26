class Solution:
    def minTimeToType(self, word: str) -> int:
        time=0
        current = 'a'
        for i in range(len(word)):
            curr_val = ord(current)-65
            word_value = ord(word[i])-65

            dis = abs(curr_val-word_value)
            time+=min(dis,26-dis)+1
            current =word[i]
        return time    


        