from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
from nltk.corpus import brown
import nltk

posts = nltk.corpus.nps_chat.xml_posts([
    '10-19-20s_706posts.xml','10-19-30s_705posts.xml',
'10-19-40s_686posts.xml',

'10-19-adults_706posts.xml',

'10-24-40s_706posts.xml',

'10-26-teens_706posts.xml',

'11-06-adults_706posts.xml',

'11-08-20s_705posts.xml',

'11-08-40s_706posts.xml',

'11-08-adults_705posts.xml',

'11-08-teens_706posts.xml',

'11-09-20s_706posts.xml',

'11-09-40s_706posts.xml',

'11-09-adults_706posts.xml',

'11-09-teens_706posts.xml'
])


# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance
i=0
for sentence in brown.sents(categories=['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance',
'science_fiction']):
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1
for sentence in posts:
    for w1, w2, w3 in trigrams(sentence.text, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1
 
# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count
# default test case
sentence="find the nearest medical shop to center of arizona"
sentence=sentence.split(" ")
for i in range(0,len(sentence)-1):
    r=dict(model[sentence[i],sentence[i+1]])
    print(sentence[i],sentence[i+1])
    print(r)
    for j in r:
        if i+2<len(sentence):
            if j==sentence[i+2]:
                print(j)
                r=brown.categoories()
                if j in r:
                    print(r)
        
        

