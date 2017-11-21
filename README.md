# Fake Hunter

## Description

Fake Hunter stalks possible fakes by searching for copies of a given image's url.

The spider use Google Reverse Image Search and scrap the url of every images of the list.

To extract the data, Fake Hunter uses the open source and collaborative framework [Scrapy](https://github.com/scrapy/scrapy).

## Installation

To download the script, type the code below in a shell :

```shell
git clone git@github.com:wbwlkr/fake-hunter.git
```

## Getting started

Run the lebonscrap.py spider using the runspider command:

```shell
scrapy runspider hunt.py -o fakes.json
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
