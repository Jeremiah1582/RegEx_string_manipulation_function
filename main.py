# this function uses REGEX to find a word at a specific occurrence in a string and replace that word with a new word.
from re import finditer

sentence="A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."

change = input('what word would you like to replace?: ')
replacementWord =input(f'what word would you like to replace "{change}" with?: ')
occurrence = int(input(f'at what occurrence would you like the word "{change}" to change?: '))


def replaceWord_func(repWord:str,newWord:str,occurrence:int,longString:str): #specifying the types of input
    allMatches = finditer(repWord,longString)#returns a callable_iterable 
    count=0
    for i in allMatches:
        count+=1
        if i.group() ==repWord and count==occurrence:
            start_Idx= i.start() #store start index 
            end_idx=i.end()#store end index
            return longString[:start_Idx] + newWord + longString[end_idx:] #reconstruct and return new string 
    
print(replaceWord_func(change,replacementWord,occurrence,sentence))