# SaucePlz

## Description

SaucePlz stalks possible fakes by searching for source and copies of a given image's url.

The spider use Google Reverse Image Search and scrap the url of every images of the list.

To extract the data, SaucePlz uses the open source and collaborative framework [Scrapy](https://github.com/scrapy/scrapy).

## Origin of the name

The word "sauce" is sometimes used in all caps along with "plz", is a slang version of the word "source".

It is used (usually in a pleading tone) as a request to someone who posted a claim, a picture or anything that raises interest but is unsourced/not complete. Its goal is to prove it, confirm it and to see more information/pictures/anything from the initial content. [source](http://knowyourmeme.com/memes/sauce)


## Installation

To download the script, type the code below in a shell :

```shell
git clone https://github.com/wbwlkr/sauce-plz.git
```

## Getting started

Run the sauceplz.py spider using the runspider command:

```shell
scrapy runspider sauceplz.py -o fakes.json
```

For each copy fount, the data related to the following columns will be written in a json file or csv:

```
'domain' (the domain of the image's url)
'image'  (the url of the image)
'sauce' (the "source" url of the page where the image was found)
```

## Requirements

 * Python3
 * Scrapy==1.4.0

## Author

* **[WebWalker](https://github.com/wbwlkr)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
