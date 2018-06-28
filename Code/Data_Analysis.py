import sys
import json
import string
import itertools
import xlrd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import namedtuple
from vocabulary.vocabulary import Vocabulary as vb

####################################################################################
########################        Implemented functions       ########################
####################################################################################
from Data_Processing import preProcessing
from Topics_Polarity import topics_Polarity
from Performance_Evaluation import performance_Evaluation
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

####################################################################################
########################              LOAD DATA             ########################
####################################################################################
#data = pd.read_csv("Reviews.csv")
#####
xl = pd.ExcelFile("Test_Reviews.xlsx")
data = xl.parse("Sheet1")

####################################################################################
########################        DATA PRE-PRE-PROCESSING     ########################
####################################################################################
# SELECTED TOPICS: Rooms, Cleanliness, Location, Service
# Aggregate the Topics range from (1,2,3,4,5) to (1,3,5) | VTA = Variable To Aggregate
VTA = "Rooms"
data[VTA] = data[VTA].replace(2, 1)
data[VTA] = data[VTA].replace(4, 5)
#data = data[data["Rooms"] != - 1]
#data = data.drop(columns=["Date", "No. Reader", "No. Helpful", "Hotel_ID", "Author"])
data = data.iloc[0:1000]
data.index = range(0,len(data))
Reviews = data["Content"]

####################################################################################
######################## PRE-PROCESSING ON THE REVIEWS DATA ########################
####################################################################################
# ASCII characters
# Lower case
# Digits and symbols
# Manage 'Not' term
# Remove STOPWORDS
# Replace punctuations with '.'

Reviews = preProcessing(Reviews)

####################################################################################
########################    TOPICS POLARITY ESTIMATION      ########################
####################################################################################
# The searchfor_list contains all the synonymous of a single topic that are searched into the reviews
searchfor_list = ["room", "rooms", "apartment", "place", "chamber", "suit", "bed", "toilette", "bedroom"]
polarity_results = []
notnull_polarity_list = []

# For each review: Look for that sentences (each sentence are considered splitted by the char '.') that contains on of the words in searchfor_list
# For each sentence: calculate the polarity value using TextBlob
# For each review: aggregate all the sentences polarities (mean)
polarity_results, notnull_polarity_list, min_polarity, mean_polarity, max_polarity = topics_Polarity(Reviews, searchfor_list)


####################################################################################
########################     PERFORMANCE EVALUTION ???      ########################
####################################################################################

performance_Evaluation(data, polarity_results)
