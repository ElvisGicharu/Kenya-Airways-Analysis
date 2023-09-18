from bs4 import BeautifulSoup
import requests
import pandas as pd
dates=[]
comments=[]
ratings=[]
flight_class=[]
countries=[]



for page in range(1,5):
    page=f'https://www.airlinequality.com/airline-reviews/kenya-airways/page/{page}/'
    response= requests.get(page)
    response=response.content
    soup=BeautifulSoup(response,'html.parser')
    # print(soup)
    
    # foundations
    # find because this is the outer cover
    brackets=soup.find('article',class_='comp comp_reviews-airline querylist position-content')
    
    # rating
    # Find all because there are alot of ratings in the cover
    for rating in brackets.find_all('div',class_='rating-10'):
        ratin=rating.span.text
        ratings.append(ratin)
        # print(ratin)
        
        # Date
    for date in brackets.find_all('div',class_='body'):
        time=date.time.text
        dates.append(time)
        # print(time)
        
        # find flight_class
    for flight in brackets.find_all('table',class_='review-ratings'): #finds all table elements
        table_row=flight.find_all('tr')
        table_data=table_row[1].find_all('td')
        flight_classs=table_data[1].text
        flight_class.append(flight_classs)
        
        # print(flight_class)
        
        # review
    for comment in brackets.find_all('div',class_='text_content'):
        comm=comment.text
        comments.append(comm)
        # print(comm)
        
    for countr in brackets.find_all('h3',class_='text_sub_header userStatusWrapper'):
        country=countr.span.next_sibling.text.strip(' ()')
        countries.append(country)
    
        
    



# make sure they all have the same length
# print('Ratings')
# print(len(ratings))

# print("dates")
# print(len(dates))

# print("comm nts")
# print(len(comment))

# print('Ratings')
# print(len(ratings))

# print('flight class')
# print(len(flight_class))

print(len(countries))

# Here we are setting a limit of a list of 40
dates=dates[:40]
comments=comments[:40]
ratings=ratings[:40]
flight_class=flight_class[:40]
countries=countries[:40]
# print(len(comments))

# Create dataframe
data=pd.DataFrame({"Dates": dates, "ratings":ratings, "countries":countries, "flight_class":flight_class, "reviews":comments})

# print(data)
data.to_csv('datasets/reviews.csv')
