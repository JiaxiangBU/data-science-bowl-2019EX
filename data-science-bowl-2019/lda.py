#AUTOGENERATED! DO NOT EDIT! File to edit: dev/lda.ipynb (unless otherwise specified).

__all__ = ['parse', 'getDF', 'freq_words']

#Cell
def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

#Cell
def freq_words(x, terms = 30, x_label_size = 12, x_rotation_degree = 45):
    all_words = ' '.join([str(text) for text in x])
    # hold elements str.
    all_words = all_words.split()

    fdist = FreqDist(all_words)
    words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})

    # selecting top 20 most frequent words
    d = words_df.nlargest(columns="count", n = terms)
    plt.figure(figsize=(20,5))
    ax = sns.barplot(data=d, x= "word", y = "count")
    ax.set(ylabel = 'Count')

    plt.xlabel('Events', size = x_label_size)
    plt.xticks(rotation = x_rotation_degree)
    plt.show()