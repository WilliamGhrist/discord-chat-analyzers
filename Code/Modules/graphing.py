#----------------------------------------------------
# TODO
#----------------------------------------------------
# 

#----------------------------------------------------
# GLOBAL VARIABLES
#----------------------------------------------------
# None

#----------------------------------------------------
# IMPORTS
#----------------------------------------------------
import helper 

#----------------------------------------------------
# FUNCTION BODY
#----------------------------------------------------
def create_histogram(user_csv: helper.pd.DataFrame) -> None:  
    
    """ 
    Plots the frequency of user posts.

    user_CSV -> helper.pd.DataFrame
        The given data (in Pandas DataFrame format) to graph on

    Return -> None
        Saves file as .png in Images folder.
    """
    df = user_csv

    author_post_counts = df['Author'].value_counts()
    helper.plt.figure()
    helper.plt.bar(author_post_counts.index, author_post_counts.values)
    helper.plt.title('Number of Posts by Each Author', fontsize=helper.TITLE_FONT_SIZE)
    helper.plt.xlabel('Author', fontsize=helper.AXES_FONT_SIZE)
    helper.plt.ylabel('Number of Posts', fontsize=helper.AXES_FONT_SIZE)
    helper.plt.xticks(rotation=45)
    helper.plt.tight_layout()
    helper.plt.savefig(f"../Images/Average_Posts.png")
    

def create_boxplot(user_csv: helper.pd.DataFrame) -> None:
    """ 
    Plots the average words per user.

    user_CSV -> helper.pd.DataFrame
        The given data (in Pandas DataFrame format) to graph on

    Return -> None
        Saves file as .png in Images folder.
    """
    df = user_csv

    df['WordCount'] = df['Content'].apply(lambda x: len(str(x).split()))

    average_word_counts = df.groupby('Author')['WordCount'].mean().sort_values(ascending=False)
    word_counts_by_user_sorted = [df[df['Author'] == user]['WordCount'].tolist() for user in average_word_counts.index]

    helper.plt.figure()
    helper.plt.boxplot(word_counts_by_user_sorted, vert=False, patch_artist=True, boxprops=dict())
    helper.plt.title('Distribution of Word Counts per Post by Users')
    helper.plt.xlabel('Word Count')

    helper.plt.yticks(range(1, len(average_word_counts) + 1), average_word_counts.index)
    
    helper.plt.tight_layout()
    helper.plt.savefig(f"../Images/Average_Word_Count.png")



def create_reaction_chart(user_csv: helper.pd.DataFrame) -> None:
    """ 
    Plots the average reactions per user.

    user_CSV -> helper.pd.DataFrame
        The given data (in Pandas DataFrame format) to graph on

    Return -> None
        Saves file as .png in Images folder.
    """
    df = user_csv

    def total_reaction_count(reaction_str: str) -> int:
        
        if not isinstance(reaction_str, str):
            return 0
        
        total = 0
        num = ""
        for char in reaction_str:
            if char.isdigit():
                num += char
            elif num:
                total += int(num)
                num = ""
        
        if num:
            total += int(num)
            
        return total


    df['Total_Reactions'] = df['Reactions'].apply(total_reaction_count)

    user_avg_reactions = df.groupby('Author')['Total_Reactions'].mean()

    user_avg_reactions = user_avg_reactions.sort_values(ascending=False)

    helper.plt.figure()
    helper.plt.barh(user_avg_reactions.index, user_avg_reactions.values, color='skyblue')
    helper.plt.xlabel('Average Number of Reactions per Post')
    helper.plt.ylabel('User')
    helper.plt.title('Overall Average Reactions per Post by User')
    helper.plt.gca().invert_yaxis()  
    helper.plt.tight_layout()
    helper.plt.savefig(f"../Images/Average_Post_Reactions.png")


#----------------------------------------------------
# MAIN
#----------------------------------------------------
def main():
    create_histogram("../../Data/news_ai.csv")
    return None

if __name__ == "__main__":
    main()
