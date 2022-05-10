# Ab aapko kuchh questions solve krna hai pre-define function ka use kr ke. Q1 . 
# Aapko max function ka use krke di hue list me se sbse bada value print krvani hai. Input
# numbers = [3, 5, 7, 34, 2, 89, 2, 5] 
# Output :- 89 Q2. Aapko sum function ka use krke di hue list 
# ke element ka sum print krvana hai. Input
def max():
    number=[3,5,7,34,2,89,2,5]
    i=0
    b=number[0]
    while i<len(number):
        if number[i]>b:
            b=number[i]
        i=i+1
    print(b)
max()
    
    # Question 2
# function_print_lines naam ka ek function 
# likho jo 2 strings leta ho, aur 
# unko neeche diye hue dhang se print karta ho. 
# Jaise agar hum usko "Mera naam Rishabh hai." aur 
# "Main NavGurukul ka co-Founder hun." denge 
# toh woh yeh print karega
def function_print_lines():
    print("mera name purnima hai")
    print("aur Main NavGurukul ka co-Founder hun.")
function_print_lines()
