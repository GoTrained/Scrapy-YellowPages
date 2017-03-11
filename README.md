# Scrapy YellowPages Spider

Using Scrapy to scrape YellowPages.

This code starts with a search result URL after you open yellowpages.com, type a search keyword and select a location.

## Running the Scrapy Spider

To run this spider, download the whole repository into your machine, open your Terminal, navigate to its folder, and then type:

```
scrapy crawl ylp
```
If you rather want to generate an CSV file of the data scraped by Scrapy, type the following:

```
scrapy crawl ylp -o filename.csv
```


