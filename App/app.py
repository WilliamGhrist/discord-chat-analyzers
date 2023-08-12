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
            # matplotlib doesnt have a gui interface, but we can get around that by graphing the function, then saving it
            # and then displaying that saved png!
        
        if helper.st.button("Display average word counts"):
            graphing.create_boxplot(df)


if __name__ == "__main__":
    main()