This program scrapes the Focused Compounding websites free section using requests and Beautiful Soup 4. This program is meant to collect all the free articles to put them in a single readable file. Please support Focused Compounding if you like their content.

Be nice to their website, maybe dont send too many requests in a short timespan.

Uncomment the function to run.
Run linkgetter() to get a list of all the links for the scraper to read from. 
If linkgetter() does not save all links, increase the number of pages it scrapes in range(85).
linkgetter() will not work if the url changes from https://focusedcompounding.com/free-content/page/

Run postscraper() to get all the text from the posts.
postscraper() puts all the text from each post into a html document and adds page breaks before every heading. It might duplicate the first page of links.

For readability I suggest saving the file as a pdf or something.