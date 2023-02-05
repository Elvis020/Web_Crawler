<h1 align="center">
Web Crawler

![Web_Crawler_CI](https://github.com/Elvis020/Web_Crawler/actions/workflows/python-app.yml/badge.svg)
<a href="https://www.python.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/python-3.7.x%20|%203.8.x|%203.9.x-brightgreen.svg" alt="Python supported"></a>

</h1>

<h3 align="center">

[Installation](https://github.com/Elvis020/Web_Crawler#installation) - [Overview](https://github.com/Elvis020/Web_Crawler#overview) - [Features](https://github.com/Elvis020/Web_Crawler#features) - [Quickstart](https://github.com/Elvis020/Web_Crawler#quickstart) - [Libraries](https://github.com/Elvis020/Web_Crawler#libraries)

</h3>

## Installation
To install the web crawler<br>
* ```git clone https://github.com/Elvis020/Web_Crawler.git```
* ```cd Web_Crawler/```
* ```pip install -r requirements```

## Overview
This program accepts an input url, and perform a web crawl on the URL, without using any external library.

It lists all URL’s that are on the page of that URL, and then subsequently crawls the URLs within that same domain,  
until all URL’s under the supplied domain have been crawled. 

It then creates a file, called ```results``` containing all the URLs, obtained from the execution. This includes all the URLs, whether domain-related or not.

Example: If we crawl https://turntabl.io, we can find https://medium.com/@turntabl.io listed as it’s on that page, 
however we don't crawl it. We will list and crawl https://turntabl.io/our-services.html.

## Features
- [x] Validation checks and error handling (done)
- [x] Scalability of running the application on large domains
- [x] Concurrency
- [x] Sufficient unit tests
- [x] Presenting the results into a file

## Libraries
* BeautifulSoup
* ArgParse
* Pytest


## Quickstart
  * After cloning the crawler, you will need to know if your website/url is crawl-able  
    * The app is executed using the command <br> ```python app.py -u url-name```.  <br>This executes it without any deepcrawl, it just gathers the links on the webpage and is suitable for webpages with all links leading to the same webpage. An example of such website is: http://turntabl.io
    * If you have a domain/website with crawl-able links eg:http://books.toscrape.com, you can run it with the following command <br> ```python app.py -u url-name -d``` or ```python app.py -u url-name --deepcrawl```
  * For more information, you can use the command: ```python -h```





