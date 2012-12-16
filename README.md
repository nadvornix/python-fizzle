## python-fizzle

Damerau–Levenshtein distance (fuzzy string matching) for python with support of unicode and custom edit costs

## Examples:
```python
#basic usage:
>>> from fizzle import *
>>> print dl_distance('Levenshtein', 'Lenevshtein')
2

# custom edit costs:
>>> editCosts=[('a','e',0.4),	#(default edit costs are 1)
		   ('e','a',0.65),
		   ('i','y',0.3),
		   ('m','n',0.5),
		   ('t','p',1.5)
		   ]
>>> dl_distance('Levenshtein', 'Lenevshtein', substitutions=editCosts,symetric=False)
2

#picking TOP 2 matches from list:
>>> misspellings = ["Levenshtain","Levenstein","Levinstein","Levistein","Levenshtein"]
>>> pick_N("Levenshtein", misspellings, 2)
[(1, 'Levemshtein'), (1, 'Levenshtain')]

#picking only best:
>>> pick_one("Levenshtein", misspellings)
(1, 'Levemshtein')

#Distance between word and words from list
>>> match_list("Levenshtein", misspellings,substitutions=editCosts,symetric=False)
[(0.65, 'Levenshtain'), (1, 'Levenstein'), (2, 'Levinstein'), (3, 'Levistein'), (1, 'Levemshtein')]

```

### LICENSE: MIT License
### AUTHOR: Jiri Nadvornik: nadvornik.jiri@gmail.com
