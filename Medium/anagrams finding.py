#anagrams finding

from collections import Counter

def groupAnagrams(words):
    anagram={}
    for i in words:
        hashKey= frozenset(Counter(i).items())
        if hashKey not in anagram:
            anagram[hashKey]=[]
        anagram[hashKey].append(i)
        
    return list(anagram.values())
    
