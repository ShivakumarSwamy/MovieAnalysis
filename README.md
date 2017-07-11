# MovieAnalysis

The following are helpful links for project,

1. [Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
2. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
3. [Requests](http://docs.python-requests.org/en/master/)
4. [plotly](https://plot.ly/python/)
5. [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
6. [OMDB API](http://www.omdbapi.com/)
7. [Markdown Quick Tutorial](http://commonmark.org/help/)

## Pleases don't use the dataset for commercial purpose.

We have filtered the dataset for year 1990-2014, country as USA, language as English


## Project Implementation Steps:

1. Run the `filteringDataset.ipynb` to filter the dataset and remove duplicate ID’s. After executing we get 
`datasetWithoutBoxOffice.csv`

2. Run `extractBoxOffice.ipynb` to extract box office using WebCrawl class present in `webcrawl.py`. After executing we get `datasetWithBoxOffice.csv`

**Optional(but suggested):** We have made 10 copies of `extractBoxOffice.ipynb` with 1000 entries each, and then using `mergeCSV.ipynb` we have merged all the csv's to get `datasetWithBoxOffice.csv`.

> Alternatively, you can run `extractBoxOfficeAllEntries.ipynb` to extract box office for all entries, but consumes lot of time (in hrs)

3. Run `extractTicketInflationPrice.ipynb` to extract table of ticket inflation price by year. After executing we get `ticketPriceInflation.csv` 

4. Run `adjustTicketPriceInflation.ipynb`. After executing we get `finalDataset.csv`

5. Run `plotDataset1.ipynb`, `plotDataset2.ipynb` to visualise the dataset.

**For Windows when converting to csv use encoding as UTF-8**


