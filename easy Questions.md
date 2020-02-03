#### (1) A function that can take a string and return a list of bigrams

```
sentence = "In non-functional linguistics, a sentence is a textual unit consisting of one or more words that are grammatically linked."
[biagram for biagram in zip(sentence.split(" ")[:-1], sentence.split(" ")[1:])]
```

#### (2) Remove Stop words
```
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
```
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
