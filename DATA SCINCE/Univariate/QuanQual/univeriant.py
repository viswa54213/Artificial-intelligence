class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
    def freqTable(i,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cusum"])
        freqTable["Unique_Values"]=dataset[i].value_counts().index
        freqTable["Frequency"]=dataset[i].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cusum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable
    
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                                   "Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for i in quan:
            descriptive[i]["Mean"]=dataset[i].mean()
            descriptive[i]["Median"]=dataset[i].median()
            descriptive[i]["Mode"]=dataset[i].mode()[0]
            descriptive[i]["Q1:25%"]=dataset.describe()[i]["25%"]
            descriptive[i]["Q2:50%"]=dataset.describe()[i]["50%"]
            descriptive[i]["Q3:75%"]=dataset.describe()[i]["75%"]
            descriptive[i]["99%"]=np.percentile(dataset[i],99)
            descriptive[i]["Q4:100%"]=dataset.describe()[i]["max"]
            descriptive[i]["IQR"]=descriptive[i]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[i]["1.5rule"]=1.5*descriptive[i]["IQR"]
            descriptive[i]["Lesser"]=descriptive[i]["Q1:25%"]-descriptive[i]["1.5rule"]
            descriptive[i]["Greater"]=descriptive[i]["Q3:75%"]+descriptive[i]["1.5rule"]
            descriptive[i]["Min"]=dataset[i].min()
            descriptive[i]["Max"]=dataset[i].max()
            return descriptive
        
    def replacementoutliers():
        for t in lesser:
        dataset[t][dataset[t]<descriptive[t]["Lesser"]]=descriptive[t]["Lesser"]
        for column in greater:
        dataset[t][dataset[t]>descriptive[t]["Greater"]]=descriptive[t]["Greater"]
        
    def outliers columns():
        lesser=[]
        greater=[]
        for i in quan:
            if (descriptive[i]["Min"]<descriptive[i]["Lesser"]):
                lesser.append(i)
            if(descriptive[i]["Max"]>descriptive[i]["Greater"]):
                greater.append(i)

            return lesser, greater 
    
    
    