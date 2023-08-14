#----------------------------------------------------
# TODO
#----------------------------------------------------

# If you want to enrich the graphing functionality, can you think of other types of user inputs?
# Maybe user wants to graph top 5 posters instead of seeing ALL posters?
# You can also directly ask your dad what kinds of visuals + optional configs he'd want!

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
    
    # by strict convention Python, caps are reserved for Classes
    # Create_Histogram -> create_histogram
    # if you give caps to your functions, other ppl will wrongly interpret your functions as somethign they are not

    # variables in python also follow snake_case (user_CSV -> user_csv)
    # global or constant variables are the only varaibles that are all capitalized (eg. PI = 3.1415 or GLOBAL_USERNAME = "will")

    # liekwise, ive added type hints (user_csv -> user_csv: helper.pd.DataFrame) to make it clear what formats are acceptable
    # return hint which is the "-> None" hwich tells the user what this function outputs
    

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
    
    # In general, you want to programmatically save your files
    # do this for the other function as well!
    # Also, you don't want any white spaces in your folder names "Data Visualization". Some systems (for eg. CLI/powershell)
    # cannot parse white spaces without additional formatting, which is a big headache.
    # Folder names without white spaces just overall make your program the most compatible with everything
    # Also, by convention python file names will use underscores instead of dashes (snake case) "Average-Word" vs "Average_Word"
    # helper.plt.show()
    

def create_boxplot(user_csv: helper.pd.DataFrame) -> None:
    
    # df = helper.pd.read_csv(user_CSV)
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

    # helper.plt.show()

def create_reaction_chart(user_csv: helper.pd.DataFrame) -> None:

    df = user_csv

    def total_reaction_count(reaction_str):
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