import sys
sys.path.append('../Code')
from Code import helper 
from Code import graphing
from Code.graphing import Create_Histogram, Create_BoxPlot

def main():
    helper.st.title("Discord Analyser")


    uploaded_file = helper.st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = helper.pd.read_csv(uploaded_file)

        if helper.st.button("Display activity levels"):
            Create_Histogram(df)
        
        if helper.st.button("Display average word counts"):
            Create_BoxPlot(df)


if __name__ == "__main__":
    main()