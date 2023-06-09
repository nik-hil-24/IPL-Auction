# Importing Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# Website URL
url = 'https://www.iplt20.com/auction'
r = requests.get(url)


# Extracting HTML
soup = BeautifulSoup(r.content, 'html.parser')


# Classes
section_class = 'ih-points-table-sec position-relative'
team_name_class = 'ih-t-left align-center'
table_class = 'ih-td-tab auction-tbl'


# Finding sections wih table
main_section = soup.find_all('section', class_ = section_class)
# DataFrame Header
header = ['TEAM']
create_df = True


for section in main_section:
    # getting table name
    team_name = (section.find('h2')).text
    # Getting Table
    table = section.find('table', class_ = table_class)
    # Creating DataFrame and setting headers
    if create_df == True:
        headings = table.find_all('th')
        for head in headings:
            header.append(head.text)
            df = pd.DataFrame(columns = header)
        create_df = False
    # Getting data from table
    rows = table.find_all('tr')
    for row in rows[1:]:
        # Creating a row of data ['Team Name', 'Player Name', 'Nationality', 'Type', 'Price']
        row_data = [team_name]
        data = row.find_all('td')
        for td in data:
            row_data.append(td.text)
        # Adding row to DataFrame
        df.loc[len(df)] = row_data
        
# Saving to csv
df.to_csv('ipl_data.csv', index = False)