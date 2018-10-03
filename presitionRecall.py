class PresitionRecall:
    def __init__(self, relevance_dict, rankings):
        self.relevance_dict = relevance_dict
        self.rankings = rankings
        self.recall = [0,10,20,30,40,50,60,70,80,90,100]
        self.presition_recall_data = []

    def calculate_presition(self):
        presition_recall = []
        for query in range(1, len(self.rankings)+1):
            relevant = self.relevance_dict[query]
            retrieved = set()
            #presition_recall = []
            for doc in self.rankings[query-1][1]:
                retrieved.add(doc)
                if doc in relevant:
                    presition = int((len(retrieved & relevant)/len(retrieved))*1000)/10
                    recall = int((len(retrieved & relevant)/len(relevant))*10)*10
                    presition_recall.append((query, recall, presition))
                    print(f"Q: {query} -- Recall:{recall} -- Presition: {presition}")
        return sorted(presition_recall)



