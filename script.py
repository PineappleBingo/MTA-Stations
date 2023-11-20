import string
import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_stations(line):
    # Define Url by given line number
    url = "https://new.mta.info/maps/subway-line-maps/" + str(line).lower() + "-line"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing the station names using the specified data-title attribute
        station_elements = soup.select('td[data-title*="Subway Station"]' )

        # Extract station names from the elements
        stations = [station.text.strip() for station in station_elements]
        # print("\nstations[" + str(line) + "]:", stations)

        return stations

    else:
        print(f"Error: Unable to fetch the webpage (Status Code: {response.status_code})")
        return None

def scrape_shuttle_stations(line):
    # Define Url by given line number
    url = "https://new.mta.info/maps/subway-line-maps/" + str(line).lower() + "-line"

    # Send a GET request to the URL
    response = requests.get(url)

    shuttle_stations_dic = {}

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find Manhattan Shuttle
        m_station_elements = soup.select('h2[id="42-st-shuttle-manhattan"] ~ div table tr td[data-title*="Subway Station"]')
        b_station_elements = soup.select('h2[id="franklin-shuttle-brooklyn"] ~ div table tr td[data-title*="Subway Station"]')
        q_station_elements = soup.select('h2[id="rockaway-shuttle-queens"] ~ div table tr td[data-title*="Subway Station"]')

        # Extract station names from the elements
        m_stations = [station.text.strip() for station in m_station_elements]
        b_stations = [station.text.strip() for station in b_station_elements]
        q_stations = [station.text.strip() for station in q_station_elements]
        
        shuttle_stations = m_stations + b_stations + q_stations
        print("\nstations[" + str(line) + "]:", shuttle_stations, type(shuttle_stations))

        shuttle_stations_dic["GS"] = m_stations
        shuttle_stations_dic["FS"] = b_stations
        shuttle_stations_dic["S"] = q_stations
        
        return shuttle_stations_dic

    else:
        print(f"Error: Unable to fetch the webpage (Status Code: {response.status_code})")
        return None

stations_by_ruotes = {}

# # # Get Station Names from line 1 ~ 7
# for line in range(1, 8):
#     stations_by_ruotes[str(line)] = scrape_stations(line)  

# # Get Station Names Letter Lines
# lines = ["A", "B", "C", "D", "E", "F", "G", "J", "L", "M", "N", "Q", "R", "W", "Z"]
# for line in lines:
#     stations_by_ruotes[line] = scrape_stations(line) 

scrape_shuttle_stations("S")

# print("\n\nstations_by_ruotes:", stations_by_ruotes)


# # Convert Dict to dataframe
# df = pd.DataFrame.from_dict(stations_by_ruotes, orient='index')

# # Transpose coloumns and rows
# new_df = df.transpose()
# print("\n\n-------- Stations DF --------\n", new_df)

# # Save the DataFrame to a CSV file
# new_df.to_csv('subway_stations.csv', index=False)

# print("CSV file created successfully.")


# Scrape station names
# station_names = scrape_station_names(1)

# # Print the result
# if station_names:
#     print("Station Names:")
#     for index, station in enumerate(station_names, start=1):
#         print(f"{index}. {station}")
