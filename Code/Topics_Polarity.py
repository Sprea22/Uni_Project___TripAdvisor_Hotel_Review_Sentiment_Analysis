import numpy as np
from textblob import TextBlob

def topics_Polarity(Reviews, searchfor_list):
    ######################## TOPIC SELECTION ########################
    polarity_results = []
    notnull_polarity_list = []
    for review in Reviews:
        flag = False
        review_polarity_temp = []
        review = review.split('.')
        for sentence in review:
            for word in searchfor_list:
                if word in sentence:
                    flag = True
                    review_polarity_temp.append(TextBlob(sentence).sentiment.polarity)
                    #print(sentence ," | ", TextBlob(sentence).sentiment.polarity)
                    break
        if(flag):
            polarity_results.append(np.mean(review_polarity_temp))
        else:
            polarity_results.append(-2)
    # Append to the "notnull_polarity_list" all the reviews polarity that has been calculted (so the one different by -2)
    polarity_results = np.array(polarity_results)
    for i in range(0, len(polarity_results)):
        if(polarity_results[i] != -2):
            notnull_polarity_list.append(polarity_results[i])
    # Compute the min, mean and max polarity about the reviews in the "notnull_polarity_list"
    min_polarity = min(notnull_polarity_list)
    mean_polarity = np.mean(notnull_polarity_list)
    max_polarity = max(notnull_polarity_list)

    # Compute the polarity threshold in order to labelize each single review
    # The labels are:
    # -2 = Impossible to calculate the sentiment because the reivew doesn't containt the searched topic
    # 1, 2, 5 = Labels as the tripadvisor metadata
    threshold_NEG = -(abs(min_polarity/5))
    threshold_POS = abs(max_polarity/5)
    print("----------------------")
    print("Min polarity: ", min_polarity)
    print("Avg polarity: ", mean_polarity)
    print("Max polarity: ", max_polarity)
    print("----------------------")
    print("Negative threshold: ", threshold_NEG)
    print("Positive threshold: ", threshold_POS)

    for i in range(0, len(polarity_results)):
        if(polarity_results[i] != -2):
            if(polarity_results[i] > threshold_POS):
                polarity_results[i] = 5
            elif(polarity_results[i] < threshold_NEG):
                polarity_results[i] = 1
            else:
                polarity_results[i] = 3

    return polarity_results, notnull_polarity_list, min_polarity, mean_polarity, max_polarity
