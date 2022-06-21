PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE pirates(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
INSERT INTO pirates VALUES(1,'Admiral','Wade');
INSERT INTO pirates VALUES(2,'Winter','Greybeard');
INSERT INTO pirates VALUES(3,'Jonas','Rattler');
INSERT INTO pirates VALUES(4,'Wyatt','Gold');
INSERT INTO pirates VALUES(5,'Hunter','Brendan');
INSERT INTO pirates VALUES(6,'Sugar-Tongue','Shelley');
INSERT INTO pirates VALUES(7,'David','Death');
INSERT INTO pirates VALUES(8,'Liza','Mcgee');
INSERT INTO pirates VALUES(9,'Jilly','Buckets');
INSERT INTO pirates VALUES(10,'One-Tooth','John');
INSERT INTO pirates VALUES(11,'Vicky','Fishmonger');
INSERT INTO pirates VALUES(12,'Brent','Seadog');
INSERT INTO pirates VALUES(13,'Admiral','Simpson');
INSERT INTO pirates VALUES(14,'Vera','Sparrow');
INSERT INTO pirates VALUES(15,'Ella','Treasures');
INSERT INTO pirates VALUES(16,'Pearl','Bailey');
INSERT INTO pirates VALUES(17,'Glory','Jones');
INSERT INTO pirates VALUES(18,'Pete','Blackbeard');
INSERT INTO pirates VALUES(19,'Bill','Bones');
INSERT INTO pirates VALUES(20,'John','Blackeye');
INSERT INTO pirates VALUES(21,'Poopdeck','Pete');
INSERT INTO pirates VALUES(22,'Maximus','Dark-Skull');
INSERT INTO pirates VALUES(23,'Musclemouth','Mike');
INSERT INTO pirates VALUES(24,'Chipper','Goldheart');
INSERT INTO pirates VALUES(25,'Crimson','Seadog');
INSERT INTO pirates VALUES(26,'Toothless','Pete');
INSERT INTO pirates VALUES(27,'Thunder','Dave');
INSERT INTO pirates VALUES(28,'Pete','Plank');
INSERT INTO pirates VALUES(29,'Mad','Michael');
INSERT INTO pirates VALUES(30,'Rascal','Jimmy');
INSERT INTO pirates VALUES(31,'Cannonball','Conner');
INSERT INTO pirates VALUES(32,'Barnacle','Bill');
INSERT INTO pirates VALUES(33,'Silver-Tooth','Samuel');
INSERT INTO pirates VALUES(34,'Pete','Peg-Leg');
INSERT INTO pirates VALUES(35,'Jason','Sea-Legs');
INSERT INTO pirates VALUES(36,'Old-Time','Sammy');
INSERT INTO pirates VALUES(37,'Lazy-Eye','Louie');
INSERT INTO pirates VALUES(38,'Paddy','Sparrow');
INSERT INTO pirates VALUES(39,'Vince','PuffyPants');
INSERT INTO pirates VALUES(40,'Jack','Red-Locks');
INSERT INTO pirates VALUES(41,'Gordon','Rough');
INSERT INTO pirates VALUES(42,'Oscar','Foul');
INSERT INTO pirates VALUES(43,'Wyatt','Gold');
INSERT INTO pirates VALUES(44,'Edwin','Mables');
INSERT INTO pirates VALUES(45,'Theo','Stinkalot');
INSERT INTO pirates VALUES(46,'George','Balding');
INSERT INTO pirates VALUES(47,'Jonas','Rattler');
INSERT INTO pirates VALUES(48,'Jacob','Cutter');
INSERT INTO pirates VALUES(49,'Wade','Wilds');
INSERT INTO pirates VALUES(50,'Randell','Rummy');
INSERT INTO pirates VALUES(51,'Garrick','Roach');
INSERT INTO pirates VALUES(52,'Malvo','Razor-Face');
INSERT INTO pirates VALUES(53,'Roger','Starky');
INSERT INTO pirates VALUES(54,'Finn',"O'Fish");
INSERT INTO pirates VALUES(55,'Dirty','Danny');
INSERT INTO pirates VALUES(56,'Churchhill','Evans');
INSERT INTO pirates VALUES(57,'Celia','Tyde');
INSERT INTO pirates VALUES(58,'Elnora','Neale');
INSERT INTO pirates VALUES(59,'Shiverin','Shelley');
INSERT INTO pirates VALUES(60,'Mighty','Mary');
INSERT INTO pirates VALUES(61,'Kellie','Strong-Heart');
INSERT INTO pirates VALUES(62,'Misty','Winters');
INSERT INTO pirates VALUES(63,'Voodo','Wendy');
INSERT INTO pirates VALUES(64,'Salty','Sarah');
INSERT INTO pirates VALUES(65,'Shark-Fin','Suzie');
INSERT INTO pirates VALUES(66,'Penelope','Precious');
INSERT INTO pirates VALUES(67,'Sivera','Snake-Eyes');




CREATE TABLE ships(
    boat_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    crew_number INTEGER,
    captain_id INTEGER,
    FOREIGN KEY (captain_id) REFERENCES pirates(id) ON DELETE CASCADE ON UPDATE CASCADE
);
COMMIT;
