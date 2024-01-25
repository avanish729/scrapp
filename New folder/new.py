import requests
from bs4 import BeautifulSoup
import csv # To store the data in a CSV file


# URL of Swiggy's restaurant page
url = 'https://www.swiggy.com/city/gorakhpur/best-restaurants'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
try :

    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")


    csv_file = open('csv/Pune.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(['Restaurant Name', 'Rating'])





# Check if the request was successful
    if response.status_code == 200:
       
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())

        restaurant_element = soup.find_all('div', class_='styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp')

        
        
        if restaurant_element:
        
            for restaurant in restaurant_element:
                
                restaurant_name = restaurant.find('div', class_='sc-beySbM cwvucc').text.strip()
                rating = restaurant.find('span', class_='sc-beySbM evFhcR').text[0:3].strip()
            

                print(f'Restaurant Name: {restaurant_name}')
                print(f'Rating: {rating}')

                writer.writerow([name, rating])
                
            
            
            # write the data to csv file
        else:  
            print('Failed to retrieve the webpage.')

except requests.exceptions.HTTPError as err:
     print(f"HTTP Error Occured: {err}")
     
     print(err)

 