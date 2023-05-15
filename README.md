TV-Doggy Web Scraper
====================

![alt text](https://imgur.com/78IiR5w)

TV-Doggy is a Python web scraper that extracts the latest episodes of your favorite TV shows from the internet and provides you with a list of links to download the latest episode torrents or watch them online. It uses various web scraping techniques to extract the latest episode information from popular TV show databases and video hosting sites.

Requirements
------------

Before you can run TV-Doggy, you will need to have Python 3 installed on your computer. You will also need to install the following Python libraries:

-   requests
-   BeautifulSoup4
-   tabulate
-   transmissionrpc

You can install these libraries by running the following command in your terminal:

python

`pip install requests beautifulsoup4 tabulate transmissionrpc`

Usage
-----

To use TV-Doggy, simply run the `WebSkrepa.py` script in your terminal using the following command:

python

`python WebSkrepa.py`

This will extract the latest episode information for the shows listed in the `myshows` list in the script and display a table of the results in your terminal.

You can also customize the `myshows` list to include your own favorite TV shows by editing the list in the script.

By default, TV-Doggy will display a table of the latest episode information for your favorite TV shows. You can also choose to download the latest episode torrents or watch them online by following the links provided in the table.

To download the latest episode torrents, you will need to have a torrent client such as Transmission installed on your computer. TV-Doggy uses Transmission's RPC interface to download the torrents.

Credits
-------

TV-Doggy was created by [your name here]. It uses various open-source libraries and APIs, including:

-   [Python Requests](https://requests.readthedocs.io/en/master/)
-   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-   [Tabulate](https://pypi.org/project/tabulate/)
-   [Transmission RPC](https://github.com/mrpapercut/transmissionrpc)

License
-------

TV-Doggy is licensed under the [MIT License](https://github.com/%5Byour-github-username%5D/tv-doggy/blob/main/LICENSE).