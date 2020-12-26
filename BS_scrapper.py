# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 08:01:11 2020

@author: Saurabh Singh
"""
#Scrapping
#There are 3 libraries used in python for scrapping
#Beautifulsoup, Scrappy and Selenium
#BEauftiful soup is good for HTML and XML files and easy to understand but is inefficient
#Selenuium is good for projects with Javascript, used for automation as well and a bit Difficult to understand, slow for large amount of data
#Scrappy is used for large chunks of data, works on all os, not user friendly
#bs4 can be used for scrapping data from wiki, bank account, job portal, shopping sites , etc.
#In html all the information are created using tags

!pip install beautifulsoup4
#When you work with beatiful soup library you have to specify the method you are going to parse to convert html files into objects
#parser will take the raw html and convert it to more readable format
#There are different methods to parse your codes, the best one is lxml to parse your code
#if we are using default html parser it will not work well with broken html codes
#We have to install lxml parser library.
!pip install lxml

#now we have to import all packages
from bs4 import BeautifulSoup
import os
os.getcwd()


with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('div', class_ ='card')

    for i in tags:
        course_name = i.h5.text
        course_price = i.a.text.split()[-1] #split and get last element
        #use f string to include both
        print(f'{course_name} costs {course_price}')
 



#---------------------------------------------------------------------#
#Scarpping jobs website

import time
def find_jobs():   
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=', verify=False).text
    soup =BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    print('ENter a skill that you are not familiar with ')
    unfamiliar_skill = input('>')
    print(f"Filtering out {unfamiliar_skill} skill")
    for index,job in enumerate(jobs):  #enumerate will allows us to iterate over index as well as content.
        publish_date = job.find('span',class_ = 'sim-posted' ).span.text
        if 'few' in publish_date:
            location = job.find('span' ).text
            extra_info = job.header.h2.a['href']
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ','')
            skills = job.find( 'span',class_ = "srp-skills" ).text.replace(' ','')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f: #w stands for writing the file
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills Required: {skills.strip()} \n")
                    f.write(f"location: {location.strip()} \n")
                    f.write(f"extra_info: {extra_info}] n")
                print('file saved {index}.txt')
if __name__ == '__main__':
    while True:  #run only when this function is called
        find_jobs() # run the function
        time_wait = 2
        print(f"Waiting for {time_wait} seconds.....")
        time.sleep(time_wait * 10)# specify time to run
    
