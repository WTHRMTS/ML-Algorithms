a = [1,1,1,2,2,3,4,5,6]
from collections import Counter
most_common = Counter(a).most_common(1)
print(most_common)