import helper 

######Histogram######
def Create_Histogram(user_CSV):

    helper.df = helper.pd.read_csv(user_CSV)

    author_post_counts = helper.df['Author'].value_counts()
    helper.plt.figure()
    author_post_counts.plot(kind='bar')

    helper.plt.title('Number of Posts by Each Author', fontsize=15)
    helper.plt.xlabel('Author', fontsize=12)
    helper.plt.ylabel('Number of Posts', fontsize=12)

    helper.plt.xticks(rotation=45)
    helper.plt.tight_layout()
    helper.plt.show()


######BoxPlot######
def Create_BoxPlot(user_CSV):
    
    helper.df = helper.pd.read_csv(user_CSV)

    helper.df['WordCount'] = helper.df['Content'].apply(lambda x: len(str(x).split()))
    word_counts_by_user = [helper.df[helper.df['Author'] == user]['WordCount'].tolist() for user in helper.df['Author'].unique()]

    helper.plt.figure()
    helper.plt.boxplot(word_counts_by_user, vert=False, patch_artist=True, boxprops=dict())
    helper.plt.title('Distribution of Word Counts per Post by Users')
    helper.plt.xlabel('Word Count')
    helper.plt.yticks(range(1, len(helper.df['Author'].unique()) + 1), helper.df['Author'].unique())
    helper.plt.tight_layout()
    helper.plt.show()


#----------------------------------------------------
# Module Checking
#----------------------------------------------------
def main():
    return None

if __name__ == "__main__":
    main()