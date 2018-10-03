class PresitionRecall:
    def __init__(self, relevance_dict, rankings):
        self.relevance_dict = relevance_dict
        self.rankings = rankings
        self.recall = [100,90,80,70,60,50,40,30,20,10,0]
        self.presition_recall_data = []

    def calculate_presition(self):
        for query in range(1, len(self.rankings)+1):
            relevant = self.relevance_dict[query]
            retrieved = set()
            partial_p_r = {}
            presition_recall = []
            for doc in self.rankings[query-1][1]:
                retrieved.add(doc)
                if doc in relevant:
                    presition = int((len(retrieved & relevant)/len(retrieved))*1000)/10
                    recall = int((len(retrieved & relevant)/len(relevant))*10)*10
                    #presition_recall.append()
                    partial_p_r[recall] = presition
                    # print(f"Q: {query} -- Recall:{recall} -- Presition: {presition}")
            for i in self.recall:
                if i in partial_p_r:
                    presition_recall.insert(0, (i, partial_p_r[i]))
                else:
                    if presition_recall == []:
                        presition_recall.insert(0, (i, 0))
                    else:
                        presition_recall.insert(0, (i, presition_recall[0][1]))
            self.presition_recall_data.append(presition_recall)

    def calculate_Average(self):
        average = []
        recall = self.recall
        for i in range(len(self.presition_recall_data[0])):
            res = 0
            for j in range(len(self.presition_recall_data)):
                res += self.presition_recall_data[j][i][1]
            avg = int((res/len(self.presition_recall_data))*100)/100
            average.append(avg)
            recall.reverse()
        self.presition_recall_data.append(list(zip(recall, average)))


    def get_PresitionRecallData(self):
        return self.presition_recall_data




