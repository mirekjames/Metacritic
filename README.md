#Metacritic-Scraper

This scraper automatically scrolls down the Metacritic page for a given game and gets the username of the reviewer, the date of the review, the score, and the text of the review.
It exports to a .csv file.

##To Use:

1. Go to the user review page for the game. (ex. https://www.metacritic.com/game/baldurs-gate-3/user-reviews/)
2. Change the 'game' variable to the name of the game as it appears in the url (ex. baldurs-gate-3)
3. Change the 'scroll' variable to an appropriate number. This dictates how many times the scraper attempts to scroll the page down. So if there are a lot of reviews and you want them all, this will need to be a big number. For Starfield's 10000+ reviews, I used a scroll of 600000.
4. Run the scraper either through the command line or with a text editor like Thonny.
