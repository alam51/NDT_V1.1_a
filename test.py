import pandas as pd
import re

pattern = 'by'
# pattern = '^a...s$'
test_string = 'abyss'
result = re.search(pattern, test_string)

a = 'SHJB1P.STTN.GEN_CALC_1.MW'
b = a.upper()
pat = r'.STTN'

c = re.search(r'.STTN', b)
d = re.search('CALC_', b)
# d = re.match(r'.MW$', b)
e = 4
