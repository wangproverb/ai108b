import sys
sys.path.insert(0, '..')

import collections
import re

with open('../data/timemachine.txt', 'r') as f:
    lines = f.readlines()
    raw_dataset = [re.sub('[^A-Za-z]+', ' ', st).lower().split()
                   for st in lines]

for st in raw_dataset[8:12]:
    print('tokens:', len(st), st)

counter = collections.Counter([t for s in raw_dataset for t in s])
print("frequency of 'traveller':", counter['traveller'])

print(counter.most_common(10))

from matplotlib import pyplot as plt

wordcounts = [count for i,count in counter.most_common()]
plt.loglog(wordcounts)
plt.show()

wseq = [tk for st in raw_dataset for tk in st]
word_pairs = [pair for pair in zip(wseq[:-1], wseq[1:])]
print('Beginning of the book\n', word_pairs[:10])

counter_pairs = collections.Counter(word_pairs)
print('Most common word pairs\n', counter_pairs.most_common(10))

word_triples = [triple for triple in zip(wseq[:-2], wseq[1:-1], wseq[2:])]
counter_triples = collections.Counter(word_triples)

print('Most common word triples\n', counter_triples.most_common(10))

bigramcounts = [count for _,count in counter_pairs.most_common()]
triplecounts = [count for _,count in counter_triples.most_common()]
plt.loglog(wordcounts, label='word counts')
plt.loglog(bigramcounts, label='bigram counts')
plt.loglog(triplecounts, label='triple counts')
plt.legend()
plt.show()

