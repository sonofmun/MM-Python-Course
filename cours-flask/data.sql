BEGIN TRANSACTION;
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
	`user_id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_nom`	TINYTEXT NOT NULL,
	`user_login`	VARCHAR ( 45 ) NOT NULL,
	`user_email`	TINYTEXT NOT NULL,
	`user_password`	VARCHAR ( 100 ) NOT NULL
);
DROP TABLE IF EXISTS `place`;
CREATE TABLE IF NOT EXISTS `place` (
	`place_id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`place_nom`	TINYTEXT NOT NULL,
	`place_description`	TEXT,
	`place_longitude`	NUMERIC NOT NULL,
	`place_latitude`	NUMERIC NOT NULL,
	`place_type`	TINYTEXT NOT NULL
);
DROP TABLE IF EXISTS `variante`;
CREATE TABLE IF NOT EXISTS `variante` (
	`variante_id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`variante_nom`	TINYTEXT NOT NULL,
	`variante_lang_code`	VARCHAR ( 45 ) NOT NULL,
	`variante_place_id`	integer NOT NULL,
	FOREIGN KEY(variante_place_id) REFERENCES place(place_id)
);
DROP TABLE IF EXISTS `authorship`;
CREATE TABLE IF NOT EXISTS `authorship` (
	`authorship_id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`authorship_user_id`	integer NOT NULL,
	`authorship_place_id`	integer NOT NULL,
	`authorship_date`	DATETIME DEFAULT current_timestamp,
	FOREIGN KEY(authorship_user_id) REFERENCES user(user_id),
	FOREIGN KEY(authorship_place_id) REFERENCES place(place_id)
);
DROP INDEX IF EXISTS `fk_authorship_2_idx`;
CREATE INDEX IF NOT EXISTS `fk_authorship_2_idx` ON `authorship` (
	`authorship_user_id`	ASC
);
DROP INDEX IF EXISTS `fk_authorship_1_idx`;
CREATE INDEX IF NOT EXISTS `fk_authorship_1_idx` ON `authorship` (
	`authorship_place_id`	ASC
);
COMMIT;

BEGIN TRANSACTION;

INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (0, 'Hippana', 'Ancient settlement in the western part of Sicily, probably founded in the seventh century B.C.', 37.7018481, 13.4357804, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (1, 'Nicomedia', 'Nicomedia was founded in 712/11 BC as a Megarian colony named Astacus and was rebuilt by Nicomedes I of Bithynia in 264 BC. The city was an important administrative center of the Roman Empire.', 40.7651905, 29.919887000000003, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (2, 'Aornos', 'Aornos was a mountain fortress and the site of Alexander the Great''s last siege during the winter of 327-6 BC. The ancient site likely corresponds to Ūṇa, a peak on the Pīr-Sar west of the Indus river.', 34.75257, 72.803461, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (3, 'The "Hochtor Sanctuary"', 'A Celto-Roman sanctuary situated at an ancient high-mountain pass in the eastern Alps near Grossglockner, excavated beginning in the 1990s. Its ancient name is unknown.', 47.081765, 12.842636, 'sanctuary');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (4, 'Lipara (settlement)', 'A Greek colony and long-time settlement on the island of the same name, located to the north of Sicily in the Tyrrhenian Sea. Modern Lipari.', 38.46740105, 14.953957299999999, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (5, 'Arch of Constantine', 'The Arch of Constantine at Rome, a triumphal arch dedicated in A.D. 315.', 41.889892, 12.4904941, 'arch');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (6, 'Taberna Pomaria di Felix', 'A fruit shop in Pompeii (I, 8, 1) with an entrance on to the Via dell''Abbondanza.', 40.75074883061887, 14.48995445324075, 'taberna-shop');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (7, 'S. Paulus', 'One of Rome''s four major papal basilicae, S. Paulus was founded by Constantine I in the early fourth century A.D. and expanded by Valentinian I in the 370s.', 41.858695, 12.476827, 'church');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (8, 'Calleva', 'Calleva Atrebatum (known as Silchester Roman Town) was an Iron Age oppidum and Roman town in  Britannia. It was the civitas capital of the Atrebates tribe.', 51.35546, -1.0915195, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (9, 'Colophon/Colophon ad Mare/Notion', 'A port city founded by Aeolian settlers at the mouth of the River Avci.', 37.9928, 27.1975, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (10, 'Bousiris', 'Bousiris was a city of Lower Egypt near the Phatnitic mouth of the Nile river and was considered one of the possible birthplaces of Osiris.', 30.913368, 31.238795500000002, 'settlement');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (11, 'Corinthia', 'Corinthia was a region of ancient Greece associated with the city-state Corinth.', 37.798572, 22.834379, 'region');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (12, 'Garumna (river)', 'The Garonne river is a river of southwestern Gaul and northern Iberia.', 44.810025550000006, -0.3184549, 'river');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (13, 'Caelius Mons', 'The Caelian Hill in Rome.', 41.88755097676503, 12.491300775912759, 'hill');
INSERT INTO `place` (`place_id`, `place_nom`, `place_description`, `place_longitude`, `place_latitude`, `place_type`) VALUES (14, 'Prinias (Patela)', 'An Iron Age settlement on the Patela plateau north of the modern village of Prinias; its ancient name is uncertain. The site is notable for its occupation from the end of the Bronze Age through to the Archaic period, as well as for the monumental architecture and Orientalizing sculpture of its Buildings (''Temples'') A and B. ', 35.168633, 25.000922, 'settlement');
INSERT INTO `user` (`user_id`, `user_nom`, `user_login`, `user_email`, `user_password`) VALUES (1, 'Administrator', 'admin', 'admin@supersite.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');
COMMIT;