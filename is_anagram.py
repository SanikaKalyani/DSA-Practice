#problem : is_anagram

class Solution:
    def is_anagram(self,s,t):
        if sorted(s)==sorted(t):
            return True
        else:
            return False

#test cases

#1.s="sanika"  sorted(s)=['s','a','n','i','k','a']
#  t="aksani"  sorted(t)=['a','k','s','a','n','i]
#  sorted(s)==sorted(t)  is_anagram= True

#2.s="sanu"  sorted(s)=['s','a','n','u']
#  t="aksani"  sorted(t)=['a','k','s','a','n','i]
#  sorted(s)==sorted(t)  is_anagram= False
