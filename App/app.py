#----------------------------------------------------
# TODO
#----------------------------------------------------
# None

#----------------------------------------------------
# GLOBAL VARIABLES
#----------------------------------------------------
# None

#----------------------------------------------------
# IMPORTS
#----------------------------------------------------
import sys
sys.path.append('../Code/Modules/')
import helper
import graphing

#----------------------------------------------------
# MAIN
#----------------------------------------------------
def main():
    helper.st.title("Discord Analyser")


    uploaded_file = helper.st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = helper.pd.read_csv(uploaded_file)

        if helper.st.button("Display activity levels"):
            graphing.create_histogram(df)
            helper.st.image('../Images/Average_Posts.png')
        
        if helper.st.button("Display average word counts"):
            graphing.create_boxplot(df)
            helper.st.image('../Images/Average_Word_Count.png')

        if helper.st.button("Display average post reception"):
            graphing.create_reaction_chart(df)
            helper.st.image('../Images/Average_Post_Reactions.png')

if __name__ == "__main__":
    main()