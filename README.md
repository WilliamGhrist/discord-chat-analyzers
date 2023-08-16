# Discord-Chat-Analyzer

Analyze and visualize user activity and engagement metrics from exported Discord chat data.

## Table of Contents
- [Discord-Chat-Analyzer](#discord-chat-analyzer)
- [Executive Summary](#executive-summary)
- [Project Description](#project-description)
- [Install and Run the Project](#install-and-run-the-project)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Usage](#usage)
- [Built Using](#built-using)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)


## Executive Summary
Discord is a primary platform for community interaction and online communities to stay connected and engauged.  This project provides a tool for server administrators and community managers to gauge user activity, and the quality of interactions on their servers.  It allows them to input data from their server channels, and generate insights and visalizations from this data for use in better managing the community.   


## Project Description

This project provides tools to extract insights from exported Discord chat data. With the help of Python and its powerful data processing and visualization libraries, users can generate charts that represent metrics such as user activity, average word count per post, and reaction distributions.

### Features

- User Activity Analysis: Generate a histogram displaying the number of posts made by each user.

- Word Count Analysis: Produce a boxplot showing the distribution of average word counts per post by user.

- Reaction Analysis: Visualize the distribution of reactions received by each user.

## Install and Run the Project 
### Prerequisites
- Ensure you have Python 3.x installed on your system.
- A Discord server from which chat data can be exported.
### Setup
install requirments

```
pip install matplotlib
pip install steramlit
pip install pandas
```

Clone repo

`git clone git@github.com:WilliamGhrist/discord-chat-analyzers.git`

Download Tyrrrz's Discord channel exporter tool.

`https://github.com/Tyrrrz/DiscordChatExporter/releases/tag/2.40.4`

### Usage

1. Use the Discorde channel exporter tool to export your desired channel to CSV format.

2. Navigate to the project directory and run the streamlit app:

    `streamlit run app.py`

3. upload your CSV and generate visualizations.


## Built Using

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-008080?style=for-the-badge&logo=matplotlib&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.

## Acknowledgments

Thanks to @Tyrrrz for the Discord channel exporter tool.

[GitHub](https://github.com/Tyrrrz)

## Contact 
William Ghrist  
[Linkedin](https://www.linkedin.com/in/william-ghrist-736509203)

Christopher Denq 

[Linkedin](https://www.linkedin.com/in/christopherdenq) 

[GitHub](https://github.com/cdenq)
