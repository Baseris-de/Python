# lowercase
# letters=[]
# for c in range(97, 123):     
#     letters.append(chr(c)) 
# print(letters) 
#  
def name_value(my_list):
    s = "abcdefghijklmnopqrstuvwxyz"
    result=[]
    for i in my_list:
        sum=0
        for j in i:
            sum+=s.index(j)+1
        
        result.append(sum)
    print(result)
    for i in range(len(result)):
        result[i] = result[i]*(i+1)
    print(result)    
name_value(["codewars","abc","xyz"])
name_value(["abc","abc","abc","abc"])
