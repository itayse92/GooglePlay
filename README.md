# Google Play Store Apps' Details Extractor

#### Extract/scrape details of every app in search results pages of google play store. The output is a csv file with the following information for each app: app name, URL, category, company, ratings, installs.

## INSTALLATION
Make sure you are ready to scrape:
1. Download Firefox (our web driver)
2. Install relevant packages (pip/pip3 install…):

   * webdriver 
   * sys 
   * unittest 
   * time 
   * re 
   * requests 
   * webbrowser 
   * bs4
   * xlsxwriter
   * csv

In order to install webdriver package, you need to download selenium first:
  * Go to https://www.seleniumhq.org/download/ and download the latest version of Mozilla GeckoDriver.
  * Copy 'geckodriver' to the folder with your python code.

## ADJUSTMENTS

List your queries in the following format: 'query': 'relevant part of url'

**For example:** 
 ```python
 # ENTER URL'S WITH THE FOLLOWING FORMAT: 'NAME': 'SEARCH QUERY(PASTE FROM URL)'
urls = {
    'Flights': '/search?q=flights%20booking&c=apps',
    'Hotels': '/search?q=hotel%20booking&c=apps'
}
 ```
and paste them in "urls" dictionary.
 
## AFTER RUN
Open "apps_output.csv" (in the same folder of the .py file) and remove black rows:
  *	Select the data.
  *	Press the F5 key.
  *	In the Go to dialog box, click on the Special button.
  *	In the Go to Special dialog box, select Blanks.
  *	Delete selected rows

## NOTE
Please let me know if you have any questions or problems and I will be more than happy to help.

## License
[MIT](https://choosealicense.com/licenses/mit/)
