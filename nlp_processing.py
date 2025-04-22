import nltk
nltk.download('punkt')
nltk.download('stopwords')


def text_preprocessing(text):
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Lowercasing
    tokens = [token.lower() for token in tokens]
    
    # Stopword removal
    stopwords = set(nltk.corpus.stopwords.words('spanish'))
    tokens = [token for token in tokens if token not in stopwords]
    
    # Lemmatization
    steammer = nltk.stem.SnowballStemmer("spanish")
    tokens = [steammer.stem(token) for token in tokens]
    
    return tokens

def reminders_preprocessing(text):
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Stopword removal
    stopwords = set(nltk.corpus.stopwords.words('spanish'))
    tokens = [token for token in tokens if token not in stopwords]

    return " ".join(tokens)
