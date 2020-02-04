#### (1) A function that can take a string and return a list of bigrams

```python
sentence = "In non-functional linguistics, a sentence is a textual unit consisting of one or more words that are grammatically linked."
[biagram for biagram in zip(sentence.split(" ")[:-1], sentence.split(" ")[1:])]
```

#### (2) Remove Stop words
```python
stopwords = [
    'I', 
    'as', 
    'to', 
    'you', 
    'your', 
    'but', 
    'be', 
    'a',
]

paragraph = 'I want to figure out how I can be a better data scientist'

" ".join([i for i in paragraph.split(" ") if i not in stopwords])
```

#### (3) Finding missing number with O(n) complexity

Subtract all numbers from sum. If list starts with 0 then sum = [n*(n+1)/2] else sum = [(n+1)*(n+2)/2]
```python
nums = [0,1,2,4,5]
n = len(nums)

missing_no = n*(n+1)/2 - sum(nums)
```

#### (4) An elevator in a building starts with 5 passengers and stops at seven 7 floors. If each passenger is equally likely to get an any floor and all the passengers leave independently of each other, what is the probability that no two passengers will get off at the same floor?

```
The number of ways to assing 7 floors to 5 passengers is 7⋅7⋅7⋅7⋅7 beacuse for each passenger you can choose one of the 7 floors.

The number of ways to assign 7 floors to 5 passengers without repetition of floors is 7⋅6⋅5⋅4⋅3 because for the first passenger
you have 7 option, for the second you will have 6 and so on. Note that this number count all possible orders betwen passengers too.

Then, you will guess it, the result is (7⋅6⋅5⋅4⋅3)/(7^5).
```

#### (5) Reverse a string
```python
a = 'abcdefg'

a[::-1]

"".join(reversed(a))

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str
reverse(a)
```

#### (6) Fibonacci Numbers
```python
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
print(Fibonacci(9)) 
```

#### (7) Roman Numbers

```python
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman
```
