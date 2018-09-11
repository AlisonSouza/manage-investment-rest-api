
import re

def alison(literatureText, wordsToExclude):
    splited = re.sub("[^a-zA-Z\d\s]", " ",  literatureText).split()

    totals = {}

    for word in splited:
       totals[word] = splited.count(word)
       v=list(totals.values())
       k=list(totals.keys())
       maxx = k[v.index(max(v))]
    print(maxx)
#[^a-zA-Z\d\s]
#dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#{'sape': 4139, 'jack': 4098, 'guido': 4127}

alison("Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's  favorite favorite favorite food.", ["and", "he", "the", "to", "is", "Jack", "Jill"])
