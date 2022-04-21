import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion. This is another sentence.")


# tokenize and print all info
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

# named entities
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# get sentences
for sent in doc.sents:
    print(sent.text)

# noun chunks:
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)

# similarity (also works on sentences, words etc)
doc2 = nlp("A spectre is haunting Europe.")
print(doc.similarity(doc2))

# counting words
word_frequencies = Counter([token.text for token in doc])
print(word_frequencies.most_common(10))

# counting nouns
noun_frequencies = Counter([token.text for token in doc if token.pos_ == "NOUN"])
print(noun_frequencies.most_common(10))
