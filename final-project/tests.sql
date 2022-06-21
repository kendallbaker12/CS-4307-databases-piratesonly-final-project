SELECT p.first_name,p.last_name,p2.first_name,p2.last_name,details.fav_pirate_music
FROM pirates AS p
JOIN pirate_details AS details on p.id = details.pirate_id 
JOIN hearties AS matches ON matches.pirate_id  = p.id 
JOIN pirates AS p2 ON p2.id = matches.pirate_id
JOIN pirate_details AS details2 ON p2.id = details2.pirate_id
WHERE details.fav_pirate_music = detaiails2.fav_pirate_music
OR details.pirate_hobbies = details2.pirate_hobbies
OR details.fav_place_to_plunder = details2.fav_place_to_plunder

pirates to details
pirates to matches
matches to pirates
pirates to details


SELECT pirates.first_name,pirates.last_name,p.first_name,p.last_name 
FROM pirates 
JOIN hearties ON hearties.pirate_id = pirates.id 
JOIN pirates AS p ON p.id = hearties.matched_id 
WHERE pirates.id = ?

SELECT pirate_details.fav_pirate_music,p.first_name,p.last_name
FROM pirate_details
JOIN pirates AS p ON pirate_details.pirate_id = p.id 
WHERE pirate_details = type of music?