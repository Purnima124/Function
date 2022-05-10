# Ab aapko kuchh questions solve krna hai pre-define function ka use kr ke. Q1 . 
# Aapko max function ka use krke di hue list me se sbse bada value print krvani hai. Input
# numbers = [3, 5, 7, 34, 2, 89, 2, 5] 
# Output :- 89 Q2. Aapko sum function ka use krke di hue list 
# ke element ka sum print krvana hai. Input
def max():
    number=[3,5,7,34,2,89,2,5]
    i=0
    b=number[i]
    while i<len(number):
        if number[i]>b:
            b=number[i]
        i=i+1
    print(b)
max()