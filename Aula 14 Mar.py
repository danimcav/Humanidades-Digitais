# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load Portuguese tokenizer, tagger, parser and NER
nlp = spacy.load("pt_core_news_lg")

# Process whole documents
text = ("Bom dia Alvaro. Onde é que nasceste?")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)