import requests
import mysql.connector
from datetime import datetime


# Step 1: Call the Rick and Morty API
url = "https://rickandmortyapi.com/api/character"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
        content = response.content
        #print content in file google.html
        file = open('characters.json', 'wb')
        file.write(content)
        file.close()

# Step 2: Connect to MySQL database
db_config = {
    'user': 'root',
    'password': 'new-password',
    'host': 'localhost',
    'database': 'cartoons'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Step 3: Create table if it does not exist
create_table_query = """
CREATE TABLE IF NOT EXISTS characters (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(50),
    species VARCHAR(100),
    type VARCHAR(100),
    gender VARCHAR(50),
    origin VARCHAR(100),
    location VARCHAR(100),
    image VARCHAR(255),
    url VARCHAR(255),
    created DATETIME
)
"""
cursor.execute(create_table_query)

# Step 4: Insert data into table
insert_character_query = """
INSERT INTO characters (id, name, status, species, type, gender, origin, location, image, url, created)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for character in data['results']:
    # Convert the datetime string to a format that MySQL can accept
    created_datetime = datetime.strptime(character['created'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
    
    character_data = (
        character['id'],
        character['name'],
        character['status'],
        character['species'],
        character['type'],
        character['gender'],
        character['origin']['name'],
        character['location']['name'],
        character['image'],
        character['url'],
        created_datetime
    )
    cursor.execute(insert_character_query, character_data)


# Commit and close the connection
conn.commit()
cursor.close()
conn.close()
