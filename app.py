def get_middle(word):
    length=len(word)
    middle_index=length//2
    
    if length%2==0:
        return word[middle_index-1:middle_index+1]
    else:
        return word[middle_index]
    
input=str(input("ENTER YOUR WORD "))
result=get_middle(input)
print("INPUT: ",input,"\nOUTPUT: ",result)