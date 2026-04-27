import requests
API_KEY = '2394ceb479e01f28ff48046577fc4e10'  
city = 'Mumbai'
url = f"http://api.openweathermap.org/data/2.5/weather?
q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print(f"Failed to retrieve data. Status code: 
{response.status_code}, Reason: {response.reason}")
City: Mumbai
Temperature: 27.99°C
Weather: haze
import requests
import matplotlib.pyplot as plt
API_KEY = '2394ceb479e01f28ff48046577fc4e10'
city = 'Mumbai'
url = f"http://api.openweathermap.org/data/2.5/weather?
q={'Mumbai'}&appid={'2394ceb479e01f28ff48046577fc4e10'}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    labels = ['Temperature', 'Feels Like', 'Humidity']
    values = [temp, feels_like, humidity]
    plt.bar(labels, values)
    plt.title(f"Weather Data for {city}")
    plt.ylabel("Values")
    plt.show()
else:
    print("Error fetching data")





