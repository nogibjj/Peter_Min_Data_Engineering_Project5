# Mini_Project_3
[![CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project3/actions/workflows/cicd.yml)

This is the README for my Mini Project 3 for the IDS706 - Data Engineering Systems class at Duke University.

## Dataset
The dataset comes from Kaggle, a public machine learning and data science community. It contains a CSV file of detailed information regarding the most-streamed Spotify songs in 2023. Link: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data

## Techniques Applied
In addition to [Pandas](https://pandas.pydata.org/) for convenience with drawing figures, I have integrated [Polars](https://pola.rs) for more convenience in data preparation. Compared to Pandas, Polars is faster and more expressive in terms of mimicking the behaviors of data wranling syntax.

## Data Visualization
For the visualization, I analyzed and visualized the 10 hottest artists by their stream counts.

![alt text](top_10_artist_by_stream_count.png)

## Summary Statistics
Here is a glimpse into the summary statistics for certain columns from the dataset by running `dataframe.describe()`:

![alt text](summary_statistics.png)

## Extra Credit
If you examine the [one of the latest commits by myself](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project3/actions/runs/10977799956/job/30480175871) in GitHub, you will see that both the HTML descriptive data analytics file from the `ProfileReport` and the markdown descriptive statistics file are built automatically at each push from the CI/CD pipeline. PDF file format is not supported by this package so HTML has to be used here.
