import extract
import transform
import sqlalchemy
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"

if __name__ == "__main__":

    # Importing the songs_df from the Extract.py
    load_df = extract.return_dataframe()
    if (transform.data_quality(load_df) == False):
        raise ("Failed at Data Validation")
    transformed_df = transform.transform_df(load_df)
    # The Two Data Frame that need to be Loaded in to the DataBase

    # Loading into Database
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('../my_played_tracks.sqlite')
    cursor = conn.cursor()

    # SQL Query to Create Played Songs
    sql_query_1 = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """
    # SQL Query to Create Most Listened Artist
    sql_query_2 = """
    CREATE TABLE IF NOT EXISTS fav_artist(
        timestamp VARCHAR(200),
        ID VARCHAR(200),
        artist_name VARCHAR(200),
        count VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (ID)
    )
    """
    cursor.execute(sql_query_1)
    conn.commit()
    cursor.execute(sql_query_2)
    conn.commit()

    print("Opened database successfully")

    # We need to only Append New Data to avoid duplicates
    try:
        load_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")
    try:
        transformed_df.to_sql("fav_artist", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database2")

    # cursor.execute('DROP TABLE my_played_tracks')
    # cursor.execute('DROP TABLE fav_artist')

    conn.close()
    print("Close database successfully")

