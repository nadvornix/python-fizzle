## python-fizzle

Damerau–Levenshtein distance and fuzzy substring matching for python with support of unicode and custom edit costs

Cost for each insertion, deletion and character transposition is 1.

## Examples:
```python
#basic usage:
>>> from fizzle import *
>>> print dl_distance('Levenshtein', 'Lenevshtein')
2

# custom edit costs:
>>> editCosts=[('a','e',0.4),	#default edit costs are 1
		   ('e','a',0.65),
		   ('i','y',0.3),
		   ('m','n',0.5),
		   ('t','p',1.5)
		   ]
>>> dl_distance('Levenshtein', 'Lenevshtein', substitutions=editCosts,symetric=False)
2

#picking top 2 matches from list:
>>> misspellings = ["Levenshtain","Levenstein","Levinstein","Levistein","Levenshtein"]
>>> pick_N("Levenshtein", misspellings, 2)
[(1, 'Levemshtein'), (1, 'Levenshtain')]

#picking only best match:
>>> pick_one("Levenshtein", misspellings)
(1, 'Levemshtein')

#Distance between word and words from list
>>> match_list("Levenshtein", misspellings,substitutions=editCosts,symetric=False)
[(0.65, 'Levenshtain'), (1, 'Levenstein'), (2, 'Levinstein'), (3, 'Levistein'), (1, 'Levemshtein')]

# Default cost of transposition is 1:
>>> print dl_distance('AB', 'BA')
1

# LD distance without transposition is Levenshtein distance:
>>> print dl_distance('AB', 'BA', transposition=False)
2
```

#### Fuzzy substring search
```python
from fizzle import *

#fuzzy find substring
>>> substring_search("aabcegf","aa aaWbcdefg a")
'aaWbcdef'

#fuzzy find substring, returns (distance, (start, end))
>>> substring_match("aabcegf","aa aaWbcdefg a", substitutions=editCosts)
(3, (3, 11))

```
substring_position and substring_score is same as substring_match but returs only position or distance respectively

#### Named parameters (work for all functions):
* substitutions (default []) - List of triples (A,B,c) meaning edit A->B have cost C. Default cost is 1

* symetric (defualt True) - If edit A->B have same cost as B->A 

* nonMatchingEnds (defualt False) - True=substring matching

* transposition (defualt True) -  True=use Damerau–Levenshtein. False=compute Levenshtein distance 

* secondHalfDiscount (defualt False) - Edits in second half of string will be discounted

* printMatrix (defualt False)	- Print matrix of edit distances

#### Similar projects:
* [python-Levenshtein](https://github.com/ztane/python-Levenshtein/)
* [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)

### LICENSE: MIT License
### AUTHOR: Jiri Nadvornik: nadvornik.jiri@gmail.com
