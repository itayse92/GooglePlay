from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import unittest, time, re
import requests, webbrowser, bs4, xlsxwriter, csv


# ENTER URL'S WITH THE FOLLOWING FORMAT: 'NAME': 'SEARCH QUERY(PASTE FROM URL)'
urls = {
    'Flights': '/search?q=flights%20booking&c=apps',
    'Hotels': '/search?q=hotel%20booking&c=apps'
}


def is_contain(text, string):
    if text.find(string) >= 0:
            return True
    return False


class Sel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://play.google.com/store"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sel(self):

        # prepare excel output
        csv_file = open('apps_output.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['App Name', 'App Company', 'URL', 'Category', 'Ratings', 'Installs', 'Search-Genre'])

        for genre, URL in urls.items():
            # prepare driver
            driver = self.driver
            delay = 3
            driver.get(self.base_url + URL)

            # scroll down - change the range to scroll more/less times
            for i in range(1, 10):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)

            # go back to the top of the page
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

            html_source = driver.page_source
            data = html_source.encode('utf-8')

            # scrape details
            apps = driver.find_elements_by_class_name("Vpfmgd")
            app_counter = 0
            for app in apps:
                app_counter = app_counter + 1
                print(f'App Number : {app_counter}')

                # get url
                site_url = app.find_element_by_tag_name("a").get_attribute("href")
                print(f'URL: {site_url}')

                # enter to url and get more details
                result = requests.get(site_url)
                result.raise_for_status()
                soup2 = bs4.BeautifulSoup(result.text, "html.parser")
                first_block = soup2.find('div', class_='oQ6oV')

                # get app name
                name_block = soup2.find('h1', class_='AHFaub')
                app_name = name_block.text
                print(f'App Name: {app_name}')

                # get category
                second_block = first_block.find_all('a', href=True)
                for a in second_block:
                    if is_contain(a['href'], 'apps/category/'):
                        category = a.text
                        break
                print(f'App Category: {category}')

                # get company
                second_block = first_block.find_all('a', href=True)
                for a in second_block:
                    if is_contain(a['href'], 'apps/dev?id='):
                        app_company = a.text
                        break
                print(f'App Company: {app_company}')

                # get ratings
                third_block = first_block.find('div', class_='dNLKff')
                ratings = third_block.text
                print(f'App Ratings: {ratings}')

                # get installs
                fourth_block = soup2.find('div', class_='IxB2fe')
                fifth_block = fourth_block.find_all('div', class_='hAyfc')
                for parameter in fifth_block:
                    if is_contain(parameter.text, 'Installs'):
                        installs_string = parameter.text
                        installs = installs_string[8:]
                        print(f'App Installs: {installs}')

                print(f'Searched Genre: {genre}')
                print('\n')
                try:
                    csv_writer.writerow([app_name, app_company, site_url, category, ratings, installs, genre])
                except:
                    print("There was an error with this specific app")

        csv_file.close()


if __name__ == "__main__":
    unittest.main()
