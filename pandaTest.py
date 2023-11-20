import pandas as pd

# Your dictionary
data = {
    '1': ['Van Cortlandt Park-242', '238 St', '231 St', 'Marble Hill-225 St', '215 St', '207 St', 'Dyckman St', '191 St', '181 St', '168 St', '157 St', '145 St', '137 St-City College', '125 St', '116 St-Columbia University', 'Cathedral Pkwy (110 St)', '103 St', '96 St', '86 St', '79 St', '72 St', '66 St-Lincoln Center', '59 St-Columbus Circle', '50 St', 'Times Sq-42 St', '34 St-Penn Station', '28 St', '23 St', '18 St', '14 St', 'Christopher St-Sheridan Sq', 'Houston St', 'Canal St', 'Franklin St', 'Chambers St', 'WTC Cortlandt', 'Rector St', 'South Ferry'],
    '2': ['Wakefield-241 St', 'Nereid Av', '233 St', '225 St', '219 St', 'Gun Hill Rd', 'Burke Av', 'Allerton Av', 'Pelham Pkwy', 'Bronx Park East', 'E 180 St', 'West Farms Sq-E Tremont Av', '174 St', 'Freeman St', 'Simpson St', 'Intervale Av', 'Prospect Av', 'Jackson Av', '3 Av-149 St', '149 St-Grand Concourse', '135 St', '125 St', '116 St', 'Central Park North (110 St)', '96 St', '72 St', 'Times Sq-42 St', '34 St-Penn Station', '14 St', 'Chambers St', 'Park Place', 'Fulton St', 'Wall St', 'Clark St', 'Borough Hall', 'Hoyt St', 'Nevins St', 'Atlantic Av-Barclays Ctr', 'Bergen St', 'Grand Army Plaza', 'Eastern Pkwy-Brooklyn Museum', 'Franklin Av-Medgar Evers College', 'President St-Medgar Evers College', 'Sterling St', 'Winthrop St', 'Church Av', 'Beverly Rd', 'Newkirk Av-Little Haiti', 'Flatbush Av-Brooklyn College']
}

# Convert the dictionary to a DataFrame
# df = pd.DataFrame.from_dict(data, orient='index', columns=['Station'] * len(data['1']))

df = pd.DataFrame.from_dict(data, orient='index')

print(df)
print(df.info)
new_df = df.transpose()
print(new_df)
print(new_df.info)

# Save the DataFrame to a CSV file
new_df.to_csv('subway_stations.csv', index=False)

print("CSV file created successfully.")