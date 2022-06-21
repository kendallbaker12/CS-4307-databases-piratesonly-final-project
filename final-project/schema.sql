CREATE TABLE pirates(
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE ships(
    boat_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    crew_number INTEGER, 
    captain_id INTEGER,
    FOREIGN KEY(captain_id) REFERENCES pirates(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE pirate_details(
    pirate_id INTEGER NOT NULL,
    pirate_hobbies TEXT,
    fav_place_to_plunder TEXT,
    fav_pirate_music TEXT,
    pirate_age INTEGER NOT NULL,
    FOREIGN KEY (pirate_id) REFERENCES pirates(id) ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE crew(
    boat_id INTEGER NOT NULL,
    pirate_id INTEGER NOT NULL,
    job_title TEXT,
    FOREIGN KEY (boat_id) REFERENCES ships(boat_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (pirate_id) REFERENCES pirates(id) ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE hearties(
    pirate_id INTEGER NOT NULL,
    matched_id INTEGER NOT NULL,
    FOREIGN KEY (pirate_id) REFERENCES pirates(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (matched_id) REFERENCES pirates(id) ON DELETE CASCADE ON UPDATE CASCADE
);





