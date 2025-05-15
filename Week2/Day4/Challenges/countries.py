import requests
import random
import json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def fetch_random_countries():
    try:
        
        response = requests.get('https://restcountries.com/v3.1/all')
        response.raise_for_status()  
        
        all_countries = response.json()
        
        
        total_countries = len(all_countries)
        random_indices = random.sample(range(total_countries), min(10, total_countries))
        
        random_countries = []
        for index in random_indices:
            country = all_countries[index]
            
            
            random_countries.append({
                "name": country["name"]["common"],
                "capital": country["capital"][0] if "capital" in country and country["capital"] else "N/A",
                "flag": country["flags"]["svg"],
                "subregion": country["subregion"] if "subregion" in country else "N/A",
                "population": country["population"]
            })
        
        return random_countries
    except requests.RequestException as e:
        print(f"Error fetching countries: {e}")
        return []

def store_countries_in_db():
    try:
        
        connection = psycopg2.connect(
            dbname="public",
            user="imad",
            password="",  
            host="localhost",  
            port="5432"        
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            capital VARCHAR(100),
            flag TEXT,
            subregion VARCHAR(100),
            population BIGINT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        
        countries = fetch_random_countries()
        
        
        for country in countries:
            cursor.execute("""
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s);
            """, (
                country["name"],
                country["capital"],
                country["flag"],
                country["subregion"],
                country["population"]
            ))
        
        print(f"Successfully inserted {len(countries)} countries into the database.")
        
        
        cursor.execute("SELECT id, name, capital, subregion, population FROM countries ORDER BY id DESC LIMIT 10;")
        rows = cursor.fetchall()
        print("\nRecently added countries:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Capital: {row[2]}, Subregion: {row[3]}, Population: {row[4]}")
        
        
        cursor.close()
        connection.close()
        
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False

if __name__ == "__main__":
    store_countries_in_db()