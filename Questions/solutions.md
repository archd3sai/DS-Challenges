#### A function that can take a string and return a list of bigrams

```
sentence = "In non-functional linguistics, a sentence is a textual unit consisting of one or more words that are grammatically linked."
[biagram for biagram in zip(sentence.split(" ")[:-1], sentence.split(" ")[1:])]
```

#### Remove Stop words
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

#### Finding missing number with O(n) complexity

Subtract all numbers from sum. If list starts with 0 then sum = [n*(n+1)/2] else sum = [(n+1)*(n+2)/2]
```
nums = [0,1,2,4,5]
n = len(nums)

missing_no = n*(n+1)/2 - sum(nums)
```
