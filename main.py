from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Link:
    def __init__(self, location, links):
        self.location = location
        self.links = links

    def update_links(self, new_links):
        combined_links = self.links + new_links
        self.links = get_unique_links(combined_links)


def start_driver():
    return webdriver.Firefox(executable_path="/bin/geckodriver")
    # Starts the web browser using Firefox (namely, gecko)


def end_driver(driver):
    driver.quit()
    # Closes the web browser


def get_links(driver):
    tmp = []

    links = driver.find_elements_by_css_selector('a[href]:not(article a)')
    for link in links:
        link = link.get_attribute('href')
        link = trim_link(link)
        tmp.append(link)
    return tmp
    # Returns a list of objects, each pointing to a link, a[href], that is not an article


def get_unique_links(links):
    unique_links = []
    for link in links:
        if link not in unique_links:
            unique_links.append(link)
    return unique_links


def trim_link(link):
    cleaned_link = link
    if 'http' in cleaned_link:
        cleaned_link = link.split('//', 2)[1]
        cleaned_link = "https://" + cleaned_link
    if cleaned_link[-1] == '/':
        cleaned_link = cleaned_link[0:-1]
    return cleaned_link


if __name__ == "__main__":
    seed = 'https://www.vnq.org.au/'
    browser = start_driver()

    browser.get(seed)

    links = get_links(browser)
    unique_links = get_unique_links(links)
    print(unique_links)

    links_to_check = unique_links
    links_checked = []
    # for link in links_to_check:
    #     browser.get(link)
    #
    #     new_links = get_links(browser)
    #     new_unique_links = get_unique_links(new_links)
    #
    #     links_checked.append(link)
    #     links_to_check.pop(0)
    browser.quit()
