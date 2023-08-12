#----------------------------------------------------
# TODO
#----------------------------------------------------
# Have a look at function body comments.
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
    # the above is called a docstring. ive created this one as an example, and its good to get in the habit of maintaing clean/informative code


    # df = helper.pd.read_csv(user_CSV)
    df = user_CSV

    author_post_counts = df['Author'].value_counts()
    helper.plt.figure()
    author_post_counts.plot(kind='bar')
    # try using matplotlib to do the barplot. pandas graphing is very limited/nonrobust

    helper.plt.title('Number of Posts by Each Author', fontsize=15)
    helper.plt.xlabel('Author', fontsize=12)
    helper.plt.ylabel('Number of Posts', fontsize=12)
    # fontsize should not be hardcoded. we save these in our helper.py!
    # in helper.py, under GLOBAL VARAIBLES, you can create variables like
    # TITLE_FONT_SIZE = 15
    # AXES_FONT_SIZE = 12
    # and then here, set it as fontsize=helper.TITLE_FONT_SIZE 

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


def create_boxplot(user_CSV):
    # along with the notes from the first function, try to sort the boxplots by their average. the highest average should be the first entry
    
    # df = helper.pd.read_csv(user_CSV)
    df = user_CSV

    df['WordCount'] = df['Content'].apply(lambda x: len(str(x).split()))
    word_counts_by_user = [df[df['Author'] == user]['WordCount'].tolist() for user in df['Author'].unique()]

    helper.plt.figure()
    helper.plt.boxplot(word_counts_by_user, vert=False, patch_artist=True, boxprops=dict())
    helper.plt.title('Distribution of Word Counts per Post by Users')
    helper.plt.xlabel('Word Count')
    helper.plt.yticks(range(1, len(df['Author'].unique()) + 1), df['Author'].unique())
    helper.plt.tight_layout()


    # helper.plt.show()


#----------------------------------------------------
# MAIN
#----------------------------------------------------
def main():
    create_histogram("../../Data/news_ai.csv")
    return None

if __name__ == "__main__":
    main()