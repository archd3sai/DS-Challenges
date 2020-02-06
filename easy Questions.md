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

#### (8) If X ~ N (3, 2²) and Y ~ N(1, 2²) what is the distribution of 2X-Y ?
```
mean = (3*2 - 1) = 5

Var(2X−Y) = 2^2*Var(X) + 1^2*Var(Y) − 2*2*1*Cov(X,Y)
          = 4*Var(X) + Var(Y) − 0
          = 4*4 + 4 
          = 20

Distribution of (2X-Y) ~ N(5,20)
```

#### (9) Alice and Bob take turns in rolling a fair dice. Whoever  gets "6" first wins the game. Alice starts the game. What are the chances that Alice wins.
```
First Round:
P(Alice Win) = 1/6
P(Bob Win) = 5/6 * 1/6 = 5/6 * P(Alice Win)

P(Alice Win) + P(Bob Win) = 1
x + 5/6 * x = 1
x = 6/11
```

#### (10) The product costs 100 dollars per month, averages 10% in monthly churn, and the average customer sticks around for around 3.5 months. Calculate the formula for the average lifetime value.
```
LTV = Average Revenue Per Account / Churn Rate 
    = 100/0.1
    = 1000
```

#### (11) Explain results of a model when cofficients are not available

```
Partial Dependence plots and Explainable AI (LIME, SHAP)
```

#### (12) In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour?

```
We can model this as a Poisson distribution with rate λ.

Probability of seeing no shooting star = exp(-15*λ)*(λt^0)/0!
                                  P(0) = exp(-15*λ) 
                               1 - 0.2 = exp(-15*λ)    
                                       => λ
                                       
Probability of seeing at lease one shooting star in 60 min, P = 1 - P(0)
                                                              = 1 - exp(-60*λ)
```

#### (13) Print First Non-repeating Character. "aaabccdd" -> "b", "abcbad" -> "c", "abcabc" -> -1
```python
a = 'aaabbcdc'
b = list(a)
c = [x for x in b if b.count(x)==1]
print(c[0] if len(c) >= 1 else -1)
```
