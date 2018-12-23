#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver


def scrape():
    executable_path = {"executable_path":"chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless = False)

    
    mars_facts_data = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    #scrapping latest news about mars from nasa
    news_title = soup.find("div", class_="content_title").text
    news_description = soup.find("div", class_="article_teaser_body").text
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_paragraph'] = news_description

    #Mars Featured Image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
    browser.visit(image_url)

    #get image url using BeautifulSoup
    html_image = browser.html
    soup = bs(html_image, "html.parser")
    image_url = soup.find('a', class_ = "button fancybox")['data-fancybox-href']
    base_url = 'https://www.jpl.nasa.gov/'
    full_img_url = base_url + image_url
    mars_facts_data["featured_image"] = full_img_url

    # #### Mars Weather

    #get mars weather's latest tweet from the website
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    mars_weather = soup.find(
        'div', class_='js-tweet-text-container').text.strip()
    mars_facts_data["mars_weather"] = mars_weather

    # #### Mars Facts

    url_facts = "https://space-facts.com/mars/"

    table = pd.read_html(url_facts)
    table[0]

    facts_df = table[0]
    facts_df.columns = ["Parameter", "Values"]
    clean_table = facts_df.set_index(["Parameter"])
    mars_html_table = clean_table.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_facts_data["mars_facts_table"] = mars_html_table

    # #### Mars Hemisperes

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    #Getting the base url
    hemi_base_url = 'https://astrogeology.usgs.gov/'
    hemisphere_img_urls = []
    hemisphere_img_urls

    # #### Cerberus-Hemisphere-image-url

    hemisphere_img_urls = []
    results = browser.find_by_xpath(
        "//*[@id='product-section']/div[2]/div[1]/a/img").first.click()
    cerberus_open = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    complete_cerberus = hemi_base_url + cerberus_url
    cerberus_title = soup.find("h2", class_="title").text
    cerberus = {'url': complete_cerberus, 'title': cerberus_title}
    hemisphere_img_urls.append(cerberus)

    #Go Back To Homescreen
    back = browser.find_by_xpath(
        "//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()

    # #### Schiaparelli-Hemisphere-image-url
    results = browser.find_by_xpath(
        "//*[@id='product-section']/div[2]/div[2]/a/img").first.click()
    schiaparelli_open = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, 'html.parser')
    schiaparelli_url = soup.find('img', class_='wide-image')['src']
    complete_schiaparelli = hemi_base_url + schiaparelli_url
    schiaparelli_title = soup.find('h2', class_='title').text
    schiaparelli = {'url': complete_schiaparelli, 'title': schiaparelli_title}
    hemisphere_img_urls.append(schiaparelli)

    #Go Back To Homescreen
    back = browser.find_by_xpath(
        "//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()

    # #### Syrtis Major Hemisphere
    results = browser.find_by_xpath(
        "//*[@id='product-section']/div[2]/div[3]/a/img").first.click()
    syrtis_open = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    syrtis_image = browser.html
    soup = bs(syrtis_image, 'html.parser')
    syrtis_url = soup.find('img', class_='wide-image')['src']
    complete_syrtis = hemi_base_url + syrtis_url
    syrtis_title = soup.find('h2', class_='title').text
    syrtis = {'url': complete_syrtis, 'title': syrtis_title}
    hemisphere_img_urls.append(syrtis)

    #Go Back To Homescreen
    back = browser.find_by_xpath(
        "//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()

    # #### Valles Marineris Hemisphere

    results = browser.find_by_xpath(
        "//*[@id='product-section']/div[2]/div[4]/a/img").first.click()
    valles_open = browser.find_by_xpath("//*[@id='wide-image-toggle']").first.click()
    valles_image = browser.html
    soup = bs(valles_image, 'html.parser')
    valles_url = soup.find('img', class_='wide-image')['src']
    complete_valles = hemi_base_url + valles_url
    valles_title = soup.find('h2', class_='title').text
    valles = {'url': complete_valles, 'title': valles_title}
    hemisphere_img_urls.append(valles)

    #Go Back To Homescreen
    back = browser.find_by_xpath(
        "//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").first.click()

    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls

    
