# MovieAnalysis
Data Engineering Project

The following are helpful links for project,

1. [Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
2. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
3. [Requests](http://docs.python-requests.org/en/master/)
4. [plotly](https://plot.ly/python/)
5. [Dataset](https://grouplens.org/datasets/movielens/)
6. [OMDB API](http://www.omdbapi.com/)


**PROJECT IMPLEMENTATION STEPS:**

1. Run the filteringDataset.ipynb to filter the dataset and remove duplicate ID’s. After executing we get 
datasetWithoutBoxOffice.csv

2. Run extractBoxOffice.ipynb copies to extract box office using WebCrawl class present in webcrawl.py. After executing the latter file we get datasetWithBoxOffice.csv

**Optional(but suggested):** We have made 10 copies of extractBoxOffice.ipynb with 1000 entries each, and then using mergeCSV.ipynb we have merged all the csv's to get datasetWithBoxOffice.csv.

3. Run extractTicketInflationPrice.ipynb to extract table of ticket inflation price by year. After executing we get ticketPriceInflation.csv 

4. Run adjustTicketPriceInflation.ipynb. After executing we get finalDataset.csv

5. Run plotDataset1.ipynb, plotDataset2.ipynb to visualise the dataset.

[For Windows when converting to csv use encoding as UTF-8]
