# naive bayes implementation on IMDB dataset from scratch, without using pandas, numpy, or sklearn

from collections import defaultdict
import re

with open('ds-ai-ml/IMDB Dataset.csv', 'r') as f:
    lines = f.readlines()

n = int(0.8 * (len(lines)-1))

train_set = lines[1:n]
test_set = lines[n:]

train_neg_count=0
train_pos_count=0

pos_bog = defaultdict(int)
neg_bog = defaultdict(int)

vocab = []

for i in range(len(train_set)):
    if 'negative' in train_set[i].split(',')[-1]:
        for w in train_set[i].split()[:1]:
            alpha_num = re.sub(r'[^a-zA-Z0-9]', '', w)
            alpha_num = alpha_num.lower()
            neg_bog[alpha_num] += 1
            if alpha_num not in vocab:
                vocab.append(alpha_num)
        train_neg_count += 1
    elif 'positive' in train_set[i].split(',')[-1]:
        for w in train_set[i].split()[:1]:
            alpha_num = re.sub(r'[^a-zA-Z0-9]', '', w)
            alpha_num = alpha_num.lower()
            pos_bog[alpha_num] += 1
            if alpha_num not in vocab:
                vocab.append(alpha_num)
        train_pos_count += 1


prior_prob_neg = train_neg_count/(train_neg_count+train_pos_count)
prior_prob_pos = train_pos_count/(train_neg_count+train_pos_count)

# print(prior_prob_neg, '---', prior_prob_pos)

# print(len(vocab))
# print(len(pos_bog))
# print(len(neg_bog))


prob_pos_words = defaultdict(int)
prob_neg_words = defaultdict(int)

for w in pos_bog:
    prob_pos_words[w] = (pos_bog[w] + 1 ) / (len(pos_bog) + len(vocab))

for w in neg_bog:
    prob_neg_words[w] = (neg_bog[w] + 1 ) / (len(neg_bog) + len(vocab))


# print(prob_neg_words['the'])

#### Testing begins

test_docs = defaultdict(int)

actual = []
predicted = []

for i in range(len(test_set)):
    if 'negative' in test_set[i].split(',')[-1]:
        actual.append(0)
    elif 'positive' in test_set[i].split(',')[-1]:
        actual.append(1)

for i in range(len(test_set)):
    temp_prob_pos = 1
    temp_prob_neg = 1
    for w in test_set[i].split()[:1]:
        alpha_num = re.sub(r'[^a-zA-Z0-9]', '', w)
        alpha_num = alpha_num.lower()
        temp_prob_pos *= prob_pos_words[alpha_num]
        temp_prob_neg *= prob_neg_words[alpha_num]
    temp_prob_pos *= prior_prob_pos
    temp_prob_neg *= prior_prob_neg

    if temp_prob_neg > temp_prob_pos:
        predicted.append(0)
    else:
        predicted.append(1)

crct = 0

for i in range(len(actual)):
    if actual[i] == predicted[i]:
        crct += 1

print(f"Accuracy: {crct/len(predicted)}")

