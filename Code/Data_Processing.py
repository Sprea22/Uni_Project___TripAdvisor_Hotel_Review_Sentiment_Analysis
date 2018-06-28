import re
import nltk
from nltk.corpus import stopwords


def preProcessing(Reviews):
    ######################## ASCII ########################
    for i in range(0, len(Reviews)):
        x = Reviews.iloc[i].encode('ascii', errors = 'ignore').decode()
    ######################## LOWER CASE ########################
    Reviews = Reviews.apply(lambda row: row.lower())

    ######################## DIGITS + STUFFS ########################
    Reviews = Reviews.apply(lambda row: re.sub("[0,1,2,3,4,5,6,7,8,9,),(,-,,\,/,$,|,#]", '', row))

    ######################## NOT ########################
    # It allows to mantain the 'not' token even after the stopword remove
    Reviews = Reviews.apply(lambda row: re.sub("n't", ' not', row))

    ######################## STRING TO TOKEN ########################
    Token_Reviews = Reviews.apply(lambda row: nltk.word_tokenize(row))

    ######################## STOPWORDS ########################
    stop = stopwords.words("english")
    stop.remove("not")
    Reviews = Token_Reviews.apply(lambda row: [w for w in row if not w in stop])

    ######################## TOKEN TO STRING ########################
    # Join each review's tokens together in order to get back a string for each review
    for idx in range(0,len(Reviews)):
        Stemmed_Review_temp = []
        for word in Reviews.iloc[idx]:
            Stemmed_Review_temp.append((word))
        Reviews.iloc[idx] = Stemmed_Review_temp
        Reviews.iloc[idx] = ' '.join(Reviews.iloc[idx])

    ######################## PUNTACTION TO REPLACE ########################
    # The following code allow to substitute the "toReplace" list of values with the '.' character within the Reviews dataset
    toReplace = ['?','!',';',',']
    for idx_review in range(0, len(Reviews)):
        for i in toReplace:
            Reviews[idx_review] = Reviews[idx_review].replace(i, '.')

    return Reviews
