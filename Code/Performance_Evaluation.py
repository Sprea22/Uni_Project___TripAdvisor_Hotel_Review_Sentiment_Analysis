
def performance_Evaluation(data, polarity_results):
    cont_tot = 0
    cont_1_ok = 0
    cont_3_ok = 0
    cont_5_ok = 0

    for i in range(0, len(polarity_results)):
        if(polarity_results[i] != 0.123454321):
            cont_tot = cont_tot + 1
            #print(data["Content"].T.values[i], " | \n ", polarity_results[i], " | ", data["Rooms"].T.values[i])
            if(polarity_results[i] == data["Rooms"].T.values[i]):
                if(polarity_results[i] == 1):
                    cont_1_ok = cont_1_ok + 1
                if(polarity_results[i] == 3):
                    cont_3_ok = cont_3_ok + 1
                if(polarity_results[i] == 5):
                    cont_5_ok = cont_5_ok + 1

    print("----------------------")
    print("Total reviews: ", len(polarity_results))
    print("Predicted reviews: ", cont_tot, "\n---")
    print("Label 1 correct prediction: ", cont_1_ok, "\n---")
    print("Label 3 correct prediction: ", cont_3_ok, "\n---")
    print("Label 5 correct prediction: ", cont_5_ok)
    print("----------------------")
    print
    print("Accuracy: ", float(cont_1_ok + cont_3_ok + cont_5_ok)/float(cont_tot))

    return ""
