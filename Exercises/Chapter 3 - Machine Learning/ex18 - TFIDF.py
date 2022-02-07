text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    def distance(row1, row2):
        distance = []
        for i in range(len(row1)):
            distance.append(abs(row1[i]-row2[i]))
            i+=1
        total=0
        for ele in range(0, len(distance)):
            total = total + distance[ele]
        if total==0:
            total=np.inf
        return total

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]
    docs = [line.lower().split() for line in text.split('\n')]
    
    N=len(docs)
    uniqueWords = list(set(text.lower().split()))
##    print(uniqueWords)


    # 2. go over each unique word and calculate its term frequency, and its document frequency
    #term frequency
    tf={}
    #document frequency
    df={}

    for word in uniqueWords:
        tf[word] = [line.count(word)/len(line) for line in docs]
        df[word] = sum([word in doc for doc in docs])/N
#        print(word,df[word])
    
#    print('DF LOOKS LIKE', df)
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    total_tfidf=[]

    for index, line in enumerate(docs):
        tfidf=[]
        for word in uniqueWords:
            tfidf.append(tf[word][index]*math.log(1/df[word],10))
        total_tfidf.append(tfidf)
#    print(total_tfidf)
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    dist=[[distance(sent1, sent2) for sent1 in total_tfidf] for sent2 in total_tfidf]
    full = np.asarray(dist).astype('float')
    print(np.unravel_index(np.nanargmin(full), full.shape))

main(text)
