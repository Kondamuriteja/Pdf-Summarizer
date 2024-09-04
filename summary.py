import re
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def search_in_text(text, query):
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    matches = []

    for match in pattern.finditer(text):
        start = match.start()
        end = match.end()
        context_start = max(0, start - 50)
        context_end = min(len(text), end + 50)
        context = text[context_start:context_end]
        matches.append(context)

    return matches

def process_question(question):
    doc = nlp(question)
    return [(token.text, token.pos_) for token in doc]

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join([str(sentence) for sentence in summary])
