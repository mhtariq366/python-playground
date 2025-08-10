with open('ds-ai-ml/input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("no. of characters: ", len(text))

unique_char = sorted(list(set(text)))

print(''.join(unique_char))

def encode(s):
    l=[]
    for c in s:
        l.append(unique_char.index(c))
    return l

def decode(l):
    s=''
    for n in l:
        s += unique_char[n]
    return s

