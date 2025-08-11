# naive bayes implementation on IMDB dataset from scratch, without using pandas, numpy, or sklearn

from collections import defaultdict

with open('ds-ai-ml/IMDB Dataset.csv', 'r') as f:
    lines = f.readlines()

n = int(0.8 * (len(lines)-1))

train_set = lines[1:n]
test_set = lines[n:]

train_neg_count=0
train_pos_count=0

for i in range(len(train_set)):
    if 'negative' in train_set[i].split(',')[-1]:
        train_neg_count += 1
    elif 'positive' in train_set[i].split(',')[-1]:
        train_pos_count += 1

prior_prob_neg = train_neg_count/(train_neg_count+train_pos_count)
prior_prob_pos = train_pos_count/(train_neg_count+train_pos_count)

print(prior_prob_neg, '---', prior_prob_pos)

