# Welcome to RequestSoup!

RequestSoup was created with the goal to make Python web-scraping easier. The package interfaces both requests and BeautifulSoup, making them easier to use in conjunction with one another.

# Installation
The installation process for RequestSoup is pretty easy! Just enter the following command in your terminal:

`pip install RequestSoup`

# Usage
Usage of the package is almost identical to the indiviual use of requests and BeautifulSoup. Here is an example:

    import RequestSoup as scraper

    r = scraper.get("https://google.com")
    # The Variable r is a Request Response Object

	elements = scraper.findAll("a",{"href":"/"})
	#elements will now be a list of all "a" elements on the page with an herf that points to "/"
For more detailed usage check out: add read the docs link

# Sessions
The package also features the ability to create Request Sessions. An example of this is provided here:

    import RequestSoup as scraper

	session = scraper.Session()
	session.get("https://google.com")
	#The session object makes it much easier to work with and send multiple requests to the same website
# Feedback
This is my first public python package and I would appreciate any user feedback. For feature requests or changes, feel free to create an issue or pull request on the GitHub repo. 
