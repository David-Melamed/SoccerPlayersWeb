import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="soccer_players"
)
cursor = mydb.cursor()

stmt = "SHOW TABLES LIKE 'my_app_teams'"
cursor.execute(stmt)
result = cursor.fetchone()
if not result:
    create_teams_table = "CREATE TABLE my_app_teams (name varchar(100) NOT NULL,country varchar(50) NOT NULL,start_date " \
                   "datetime(6) DEFAULT NULL,League varchar(50) DEFAULT NULL,coach_name varchar(50) DEFAULT NULL, " \
                   "picture varchar(255) DEFAULT NULL, slug varchar(45) NOT NULL, url varchar(255) NOT NULL, " \
                   "PRIMARY KEY (name))"
    cursor.execute(create_teams_table)


stmt = "SHOW TABLES LIKE 'my_app_positions'"
cursor.execute(stmt)
result = cursor.fetchone()
if not result:
    create_positions_table = "CREATE TABLE my_app_positions (role varchar(100) NOT NULL,position varchar(20) DEFAULT " \
                             "NULL,PRIMARY KEY (role)) ENGINE=InnoDB DEFAULT CHARSET=utf8; "
    cursor.execute(create_positions_table)

stmt = "SHOW TABLES LIKE 'my_app_players'"
cursor.execute(stmt)
result = cursor.fetchone()
if not result:
    create_players_table = "CREATE TABLE my_app_players (id int(11) NOT NULL AUTO_INCREMENT,first_name varchar(50) NOT NULL,last_name varchar(50) NOT NULL,start_date datetime DEFAULT NULL,role_id varchar(100) NOT NULL,salary int(11) NOT NULL,picture varchar(100) NOT NULL,team_id varchar(100) NOT NULL,url varchar(255) NOT NULL,PRIMARY KEY (id),KEY my_app_players_team_id_e05b90f8 (team_id),KEY my_app_players_position_id_8100dcdd (role_id),CONSTRAINT my_app_players_team_id_e05b90f8_fk_my_app_teams_city FOREIGN KEY (team_id) REFERENCES my_app_teams (name)) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;"
    cursor.execute(create_players_table)

json_data = open('json/my_app_positions.json').read()
json_obj = json.loads(json_data)

for item in json_obj:
    role = item.get("role")
    position = item.get("position")

    # query = "INSERT INTO my_app_players (first_name, last_name, start_date, role_id, salary, picture, team_id, " \
    #         "url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); "
    query = "INSERT INTO my_app_positions (role, position) VALUES (%s, %s);"
    cursor.execute(query, (role, position))

json_data = open('json/my_app_teams.json').read()
json_obj = json.loads(json_data)

for item in json_obj:
    name = item.get("name")
    country = item.get("country")
    start_date = item.get("start_date")
    League = item.get("League")
    coach_name = item.get("coach_name")
    slug = item.get("slug")
    url = item.get("url")
    # query = "INSERT INTO my_app_players (first_name, last_name, start_date, role_id, salary, picture, team_id, " \
    #         "url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); "
    query = "INSERT INTO my_app_teams (name, country, start_date, League, coach_name, slug, url ) VALUES (%s, %s, %s, " \
            "%s, %s, %s, %s); "
    cursor.execute(query, (name, country, start_date, League, coach_name, slug, url))

json_data = open('json/my_app_players.json').read()
json_obj = json.loads(json_data)

for item in json_obj:
    player_id = item.get("id")
    first_name = item.get("first_name")
    last_name = item.get("last_name")
    start_date = item.get("start_date")
    role_id = item.get("role_id")
    salary = item.get("salary")
    picture = item.get("picture")
    team_id = item.get("team_id")
    url = item.get("url")
    # query = "INSERT INTO my_app_players (first_name, last_name, start_date, role_id, salary, picture, team_id, " \
    #         "url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); "
    query = "INSERT INTO my_app_players (id, first_name, last_name, start_date, role_id, salary, picture, team_id, " \
            "url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (player_id, first_name,last_name, start_date, role_id, salary, picture, team_id, url))



mydb.commit()
mydb.close()
