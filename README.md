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

## The Spider ylp Code

It assumes the search results are only on one page. We make it a separate spider to make it easier to understand it if you are new to Scrapy.

The *parse* function starts with *companies* which is a list that includes all the *div* tags with class *info*.

```
companies = response.xpath('//*[@class="info"]')
```

To see how it looks like, open the URL in Chrome browser, right-click a company title, select *Inspect*, and then move the mouse arrow until its on ```<div class="info">``` to notice how it highlights the whole box where the company details are listed.

After that, we loop on this list to extract the details of each company. Note that in XPath, we complete as if we are adding to the first XPath of companies.

```
for company in companies:
     name = company.xpath('h3/a/span[@itemprop="name"]/text()').extract_first()
     phone = company.xpath('div/div[@class="phones phone primary"]/text()').extract_first()
     website = company.xpath('div/div[@class="links"]/a/@href').extract_first()
```

Finally, we *yield* these variables in the same for loop. It is a dictionary. If you are saving the output to CSV, it will appear as columns.

```
yield{'Name':name,'Phone':phone, 'Website':website}
```




