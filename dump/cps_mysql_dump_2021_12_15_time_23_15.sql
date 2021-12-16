-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cpsab
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cps_orders`
--

DROP TABLE IF EXISTS `cps_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cps_orders` (
  `internal_order_no` int NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `required_date` date DEFAULT NULL,
  `shipping_date` date DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `comments` text,
  `order_no_comments` text,
  PRIMARY KEY (`internal_order_no`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cps_orders`
--

LOCK TABLES `cps_orders` WRITE;
/*!40000 ALTER TABLE `cps_orders` DISABLE KEYS */;
INSERT INTO `cps_orders` VALUES (1,'2021-12-12','2021-12-15','2021-12-13','Ok, blev postad som den skulle.','Detta var den sista jag hade på mitt lager.','Inget att rapportera.'),(2,'2021-12-12','2021-12-15','2021-12-13','Ok, blev postad som den skulle.','Detta var den sista jag hade på mitt lager.','Inget att rapportera.'),(3,'2021-12-12','2021-12-15','2021-12-13','Ok, blev postad som den skulle.','Detta var den sista jag hade på mitt lager.','Inget att rapportera.'),(4,'2016-06-20','1957-07-17','2012-09-15','Ok','',''),(5,'1950-09-25','1975-10-10','1902-09-26','Ok','',''),(6,'1906-10-23','2013-12-12','2019-12-22','Nok','',''),(7,'2018-08-26','2016-05-12','2016-06-20','Ok','',''),(8,'2012-05-07','2014-01-27','2016-12-02','Ok','',''),(9,'2016-06-12','1991-05-04','2015-08-27','Nok','',''),(10,'2006-05-04','2016-12-01','1992-08-21','Ok','',''),(11,'2017-08-13','2019-04-22','1991-05-04','Ok','',''),(12,'1976-04-01','2011-05-13','1985-03-17','Nok','',''),(13,'2006-05-04','2014-11-04','2018-08-26','Nok','',''),(14,'2010-06-21','2015-06-24','1950-09-25','Nok','',''),(15,'2014-08-21','2012-09-22','1973-09-02','Ok','',''),(16,'2018-06-15','2017-03-12','1978-07-02','Nok','',''),(17,'2017-07-27','2015-10-08','2012-09-22','Nok','',''),(18,'2012-09-29','2021-04-11','2017-07-27','Ok','',''),(19,'2010-06-21','2013-11-10','2021-04-11','Ok','',''),(20,'1992-02-19','1990-05-08','1996-04-09','Ok','',''),(21,'2018-06-15','1978-07-02','2015-10-08','Ok','',''),(22,'1982-05-15','1978-07-02','2012-10-31','Ok','',''),(23,'1987-12-22','2019-01-27','2014-10-25','Nok','',''),(24,'2013-11-10','2015-08-28','1906-10-23','Nok','',''),(25,'2020-11-20','1982-10-12','1982-05-15','Nok','',''),(26,'1960-06-26','2012-05-17','2017-11-23','Nok','',''),(27,'2012-09-29','1978-09-04','2017-06-03','Ok','',''),(28,'2021-02-08','2013-11-10','1906-10-23','Ok','',''),(29,'1972-06-23','2019-12-22','1957-06-05','Nok','',''),(30,'2016-09-26','2010-02-11','2016-05-12','Ok','',''),(31,'2019-01-27','1992-02-19','2010-02-11','Nok','',''),(32,'1982-10-12','2021-04-11','2019-04-22','Ok','',''),(33,'2009-05-04','1980-03-18','2000-12-28','Nok','',''),(34,'1957-06-05','2016-06-20','2099-02-25','Ok','',''),(35,'2014-08-21','1955-01-31','1960-06-26','Ok','',''),(36,'2014-04-29','1966-02-24','2013-10-29','Ok','',''),(37,'2007-08-17','2013-11-28','2021-03-12','Ok','',''),(38,'2021-08-02','2019-12-22','2011-12-17','Nok','',''),(39,'2018-06-15','1964-10-29','1986-04-09','Ok','',''),(40,'2018-06-15','2012-09-15','1990-05-08','Nok','',''),(41,'2018-08-26','1990-05-08','2014-08-21','Nok','',''),(42,'1992-08-21','2013-07-03','2012-09-29','Nok','',''),(43,'1959-04-08','2012-10-31','2014-10-25','Nok','',''),(44,'2017-06-07','2021-03-12','2001-05-27','Ok','',''),(45,'2015-10-08','2001-05-27','1959-04-08','Ok','',''),(46,'2019-12-22','2012-05-05','1957-07-17','Ok','',''),(47,'2018-06-09','1990-05-08','2017-07-27','Nok','',''),(48,'2016-06-12','2014-08-09','1957-06-05','Nok','',''),(49,'2019-01-27','2016-06-12','2012-05-07','Ok','',''),(50,'2017-07-27','2012-09-15','2021-02-08','Nok','',''),(51,'2012-09-15','1996-04-09','1982-05-15','Ok','',''),(52,'2016-06-14','1996-04-09','1985-03-17','Ok','',''),(53,'2020-11-20','2019-04-22','2016-06-20','Ok','',''),(54,'2016-12-01','2019-12-22','2015-08-28','Nok','',''),(55,'2013-12-12','2014-08-21','2014-04-29','Ok','',''),(56,'2000-12-28','1957-06-05','1957-06-05','Ok','',''),(57,'1966-09-16','2014-10-25','2021-01-05','Nok','',''),(58,'2007-08-17','2016-09-26','2010-02-11','Nok','',''),(59,'2015-10-08','2016-12-01','1957-06-05','Nok','',''),(60,'1972-04-02','1982-05-15','1957-07-17','Ok','',''),(61,'2016-06-14','1953-02-06','1972-04-02','Nok','',''),(62,'2016-05-12','2014-08-09','2012-05-17','Ok','',''),(63,'2014-08-21','1966-02-24','2012-09-15','Ok','',''),(64,'2017-03-12','1985-03-17','2021-04-11','Ok','',''),(65,'2018-06-09','2016-09-26','1959-04-08','Ok','',''),(66,'1972-04-02','2001-05-27','2020-11-20','Nok','',''),(67,'2014-10-25','2012-03-28','1973-09-02','Ok','',''),(68,'1959-04-08','2014-08-21','2012-09-29','Nok','',''),(69,'2021-03-12','2017-06-07','2013-03-12','Ok','',''),(70,'2019-12-22','2007-08-17','2016-06-14','Nok','',''),(71,'1966-02-24','1964-10-29','1902-09-26','Ok','',''),(72,'2015-08-27','2013-11-10','2013-03-12','Nok','',''),(73,'1902-09-26','2017-01-12','2009-05-04','Nok','',''),(74,'2009-05-04','1978-12-12','2019-12-22','Nok','',''),(75,'2015-08-28','2016-12-02','2016-06-12','Ok','',''),(76,'2009-04-06','2013-07-03','2014-04-29','Nok','',''),(77,'1985-03-17','2021-08-02','2015-06-08','Nok','',''),(78,'1902-09-26','2014-11-04','2015-10-02','Nok','','');
/*!40000 ALTER TABLE `cps_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_cars`
--

DROP TABLE IF EXISTS `customer_cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_cars` (
  `reg_no` varchar(20) NOT NULL,
  `manufacturer` varchar(100) NOT NULL,
  `color` varchar(45) NOT NULL,
  `model` varchar(45) NOT NULL,
  `year_model` varchar(45) NOT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`reg_no`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `customer_cars_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `customers` (`id_customers`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_cars`
--

LOCK TABLES `customer_cars` WRITE;
/*!40000 ALTER TABLE `customer_cars` DISABLE KEYS */;
INSERT INTO `customer_cars` VALUES ('AAC 755','Toyota Motor Corporation','orange','Somerset Monte Carlo','1958',3),('ABC 123','Saab','Blå','V70','1997',1),('ACH 306','Fiat Chrysler Automobiles','zink','Turbo m2','1997',53),('ACT 064','General Motors','purple','Crown Victoria 45','1986',23),('AKD 693','General Motors Company (GM)','yellow','V70','2007',18),('Akk 124','Saab','Blå','V70','1997',3),('AMF 077','The Mazda Motor Corporation','black','Testarossa Dakota','1994',12),('AQJ 414','General Motors','hazel','Testarossa Dakota','1961',6),('AVC 123','Saab','Blå','V70','1997',2),('BEK 810','Groupe Renault','hazel','Nassan Del Sol','1993',9),('BFR 058','British Motor Corporation','silver','Econoline 84 Series','2008',8),('BIE 409','Fiat Chrysler Automobiles','red','Monza Deloris','2017',45),('BWZ 088','General Motors Company (GM)','rainbow','Cooper Tempo','1974',11),('CKW 793','McLaren Automotive','hazel','Turbo m2','2012',42),('CUV 573','Fiat S.p.A','gold','Sapporo','1966',67),('DQT 041','BMW Group','rost red','ElCamino Wreck S-66','2018',21),('EET 229','General Motors (GM)','light green','De Tamato Sundance','1970',2),('EUV 523','Toyota Motor Corporation','gold','Scamp','1958',43),('FBM 117','Groupe Renault','green','The Topaz L6','2013',39),('FDU 690','The Mazda Motor Corporation','silver','Galant Forester','1957',43),('GCS 069','Toyota Motor Corporation','black','Safari 3000','2019',2),('GJC 577','Volkswagen AG','grey','Starion Blackwood','1983',22),('HUV 865','Toyota Motor Corporation','hazel','Scorpio White SoarDe','1981',28),('ISJ 083','Toyota Motor Corporation','green','Starion Blackwood','2018',20),('IUO 361','General Motors (GM)','white','Elantra Vantage 77-I','2003',2),('IUR 864','Renault–Nissan–Mitsubishi Alliance','gold','S60','1979',5),('JJZ 491','Fiat Chrysler Automobiles','pink','Brooklands Rival XI','1969',7),('JWC 598','Fiat Chrysler Automobiles','purple','The Topaz L6','1969',12),('JYA 729','Enhanced Ford Vehicles','blue','ElCamino Wreck S-66','1963',37),('KJG 001','General Motors (GM)','rainbow','Red Preach','2018',10),('KMY 966','Fiat Chrysler Automobiles Stellantis','light green','Javelin','1979',52),('LDZ 499','Renault–Nissan–Mitsubishi Alliance','hazel','Elantra Dino','1978',8),('LSH 967','Toyota Motor Corporation','red','Topaz Road L6','2002',18),('MLR 208','Stellantis','orange','Red Preach','1972',12),('MMC 041','Volkswagen AG','grey','De Tamato Sundance','2014',26),('MUS 634','The Honda Motor Company Ltd.','silver','Supra Somerset VI','1951',8),('MVV 392','Renault–Nissan–Mitsubishi Alliance','black','Somerset Monte Carlo','1953',12),('NDE 326','Volkswagen AG','zink','Turbo m2','2005',28),('NEY 486','Groupe Renault','orange','S 9000','1960',5),('NWF 591','KIA MOTORS CORPORATION','yellow','Pacifica Avenger IV','1965',36),('OAK 499','Groupe Renault','rainbow','Gran Fury Blue Tribute','1974',42),('ONK 942','General Motors (GM)','white','Galant Forester','2014',13),('OPB 767','Fuji Heavy Industries','rost red','Elantra Dino','1980',4),('PBD 287','Toyota Motor Corporation','green','Starion Blackwood','1962',18),('PFY 333','Toyota Motor Corporation','light green','Crown Victoria 45','1992',15),('POX 454','Volkswagen AG','grey','V 700','2006',23),('QHG 931','Toyota Motor Corporation','orange','Monza Deloris','1970',52),('QLA 888','Pagani Automobili S.p.A.','silver','Elantra Dino','2007',31),('QVE 255','Volkswagen AG','dark green','Aveo Super Foot','1977',19),('QWP 705','Fiat Chrysler Automobiles','yellow','Brooklands Rival XI','1956',4),('RFC 558','General Motors','orange','Scamp','2005',6),('RFQ 827','Fuji Heavy Industries','purple','Javelin','2014',1),('RVA 775','Fiat Chrysler Automobiles','green','Galant Forester','1977',24),('RXI 534','Volkswagen AG','yellow','Testarossa Dakota','2013',17),('SFP 767','Lagonda Global Holdings plc','dark green','Pacifica Avenger IV','2005',3),('SNH 824','Renault–Nissan–Mitsubishi Alliance','black','De Tamato Sundance','1987',16),('SSJ 728','Volkswagen AG','black','Nassan Del Sol','1960',31),('SSX 700','Volvo Cars','gold','Bend G-78','1979',7),('SZX 931','Toyota Motor Corporation','dark green','ElCamino Wreck S-66','1970',31),('TJJ 176','Hyundai Motor Group','grey','De Tamato Sundance','1982',16),('TNP 843','Royce Motor Cars Limited','green','S 9000','1973',33),('TUC 150','Renault–Nissan–Mitsubishi Alliance','red','Brooklands Rival XI','1983',60),('UVY 479','Stellantis','purple','ElCamino Wreck S-66','1999',36),('VVY 772','Fiat Chrysler Automobiles','silver','Scamp','1981',18),('WOO 024','Ford Motor Company','blue','Galant Forester','1966',56),('XAE 825','Fiat Chrysler Automobiles','dark green','V 700','1963',3),('XBJ 807','Fiat Chrysler Automobiles','blue','Javelin','1961',63),('XDK 211','Chrysler Cooperation','pink','Montana Sidekick V','1968',1),('XDN 150','Fiat Chrysler Automobiles','black','Brooklands Rival XI','1985',1),('XJS 013','The Honda Motor Company Ltd.','hazel','Econoline 84 Series','1975',14),('XQY 120','General Motors Company (GM)','green','Topaz Road L6','2003',27),('XXF 389','Royce Motor Cars Limited','grey','Montana Sidekick V','1973',13),('YGJ 345','Mercedes-Benz','white','S60','1989',22),('YQP 956','Volkswagen','black','S60','1991',15),('YUJ 919','General Motors Company (GM)','blue','V 700','1978',9),('YUO 382','Volkswagen AG','red','ElCamino Wreck S-66','1971',32);
/*!40000 ALTER TABLE `customer_cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id_customers` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `phone` varchar(45) NOT NULL,
  `adress1` varchar(150) NOT NULL,
  `adress2` varchar(150) DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `zip_code` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  `sales_representant` varchar(150) NOT NULL,
  `states` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_customers`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Bertil','Karlsson','','+4676048484848','Snövägen 5A','','Göteborg','44979','Sweden','Gustaf Andersson','Västra Götaland'),(2,'Anders','Larsson','','+46760848','Snipeväge 50A','','Göteborg','44979','Sweden','Gustaf Andersson','Västra Götaland'),(3,'Jonas','Larsson','','+46760848','Snipeväge 50A','','Göteborg','44979','Sweden','Gustaf Andersson','Västra Götaland'),(4,'Bob','Larsson','','+46760848','Snipeväge 50A','','Göteborg','44979','Sweden','Gustaf Andersson','Västra Götaland'),(5,'Orvar','Larsson','','+46760848','Snipeväge 50A','','Göteborg','44979','Sweden','Gustaf Andersson','Västra Götaland'),(6,'Martin','Eklund','K-Rauta AB','+46-715-553-0','Oskarsvägen 60','','Åstorp','88122','Sweden','Anders Hedlund ','Region Västerbotten'),(7,'Anna','Ivarsson','Nibe','+46-745-553-8','Trädgårdsgatan 12','','Trelleborg','88039','Sweden','Kerstin Sundberg ','Region Gotland'),(8,'Inger','Åkesson','Jerns','+46-775-555-9','Pärlgräsgatan 60','','Hillared','66321','Sweden','Bo Holmberg ','Region Jönköpings län'),(9,'Robert','Ek','Meca','+46-775-550-3','Wesslunds Gränd 5','','Täby','02177','Sweden','Madeleine Abrahamsson ','Region Kronoberg'),(10,'Camilla','Blomqvist','Bad & Värme','+46-785-559-8','Oskarsvägen 60','','Högsby','06651','Sweden','Leila Sundberg ','Region Örebro län'),(11,'Eric','Arvidsson','Swedish Match','+46-765-556-1','Korsträskvägen 5','','Askersund','56683','Sweden','Linda Åberg ','Region Värmland'),(12,'Frida','Hansen','Hallbergs Guld','+46-785-559-8','Oskarsgatan 67','','Upplands Väsby','29208','Sweden','Peter Ek ','Region Stockholm'),(13,'Signe','Sandström','Matrebellerna','+46-755-550-9','Loftaheden 65','','Söderköping','44700','Sweden','Felicia Holm ','Region Norrbotten'),(14,'Ingegerd','Bengtsson','Blomsterlandet','+46-735-558-8','Eriksbo Västergärde 81','','Floby','55312','Sweden','Lennart Olofsson ','Region Jönköpings län'),(15,'Anette','Lundberg','Apotea','+46-725-556-5','Orrspelsvägen 51','','Hillared','08043','Sweden','Caroline Wikström ','Västra Götalandsregionen'),(16,'Sten','Svensson','Happy Homes','+46-725-558-0','Sandhällagatan 21','','Göteborg','45088','Sweden','Gösta Persson ','Region Dalarna'),(17,'William','Blomqvist','Gina Tricot','+46-785-559-8','Dalhemsgatan 51','','Limmared','70303','Sweden','Khalil Persson ','Region Värmland'),(18,'Anneli','Ekström','Bygma','+46-795-557-3','Sandhällagatan 77','','Strömsund','01183','Sweden','Anton Norberg ','Region Östergötland'),(19,'Elisabeth','Hermansson','Nokia','+46-715-559-2','Lundby 80','','Aneby','89490','Sweden','Birgitta Mohamed ','Region Örebro län'),(20,'Signe','Holmqvist','Team Sportia','+46-765-551-0','Trumvägen 15','','Skurup','23508','Sweden','Ove Olsson ','Region Sörmland'),(21,'Gunnar','Berggren','Pågens bröd AB','+46-745-558-2','Klörupsgatan 62','','Partille','70303','Sweden','Helena Pettersson ','Region Jämtland Härjedalen'),(22,'Eva','Johansson','Dustin','+46-775-558-3','Nöjesgatan 61','','Bjuv','92174','Sweden','Malin Bergqvist ','Region Kronoberg'),(23,'Andreas','Fransson','Apoteket AB','+46-785-550-0','Alvägen 4','','Hyssna','40272','Sweden','Salim Gunnarsson ','Region Blekinge'),(24,'Sofie','Lindholm','Audio Video','+46-755-552-9','Loftaheden 62','','Borgholm','05682','Sweden','Åsa Bergman ','Region Stockholm'),(25,'Helen','Söderberg','Jysk','+46-755-555-6','Klörupsgatan 23','','Dorotea','51258','Sweden','Filip Karlsson ','Region Kalmar län'),(26,'Cecilia','Fredriksson','Nordsjö Idé & Design','+46-765-556-1','Snårvägen 82','','Nacka','24009','Sweden','Arne Öberg ','Region Dalarna'),(27,'Tommy','Samuelsson','Skanska','+46-725-556-6','Ryttargatan 2','','Mullsjö','09100','Sweden','Annika Svensson ','Region Jämtland Härjedalen'),(28,'Caroline','Åkesson','Comfort','+46-725-556-4','Ryttarvägen 4','','Ystad','85635','Sweden','Arvid Sandström ','Region Uppsala'),(29,'Christina','Nordström','Biltema','+46-775-555-3','Hönefossvägen 32','','Ystad','58900','Sweden','Erik Strömberg ','Region Sörmland'),(30,'Inga','Blomqvist','Elgiganten','+46-775-550-3','Eriksbo Västergärde 34','','Falkenberg','15034','Sweden','Fredrik Jönsson ','Region Jämtland Härjedalen'),(31,'Mathias','Gustafsson','Alfa Laval','+46-715-553-0','Päronvägen 28','','Degerfors','32653','Sweden','Olov Falk ','Region Västernorrland'),(32,'Katarina','Arvidsson','XL-Bygg','+46-725-559-7','Höneforsgatan 4','','Gällivare','70168','Sweden','William Mattsson ','Region Norrbotten'),(33,'Sten','Mohamed','Happy Homes','+46-715-559-2','Pål Skräddares Väg 38','','Mariestad','37776','Sweden','Dan Lundström ','Region Norrbotten'),(34,'Kurt','Holm','Trademax, Furniturebox','+46-775-558-9','Framlyckevägen 31','','Överlida','34833','Sweden','Thomas Mårtensson ','Region Jönköpings län'),(35,'Yussuf','Viklund','Jysk','+46-705-555-6','Storegårdsvägen 10','','Åre','22876','Sweden','Wilhelm Hassan ','Region Gotland'),(36,'Hugo','Ahmed','Nordsjö Idé & Design','+46-715-556-2','Trumgatan 40','','Kil','36676','Sweden','Jonanna Johansson ','Region Halland'),(37,'Camilla','Gustafsson','Synoptik','+46-785-558-4','Hedehusgatan 74','','Östadkulle','02907','Sweden','Anette Hellström ','Region Jämtland Härjedalen'),(38,'Jörgen','Bergqvist','Office Depot','+46-745-558-7','Snårgatan 50','','Ängelholm','37267','Sweden','Lovisa Larsson ','Region Värmland'),(39,'Karin','Månsson','Stadium Outlet','+46-765-551-8','Pål Skräddares Väg 20','','Jakobsberg','14986','Sweden','Eva Lundström ','Region Gävleborg'),(40,'Jan','Åberg','Hexagon','+46-715-556-2','Apelsingatan 49','','Åmål','24540','Sweden','Kenneth Lundgren ','Region Östergötland'),(41,'Wilhelm','Lindholm','Coop Mitt','+46-785-559-6','Storegårdsgatan 98','','Piteå','41883','Sweden','Oliver Nilsson ','Region Gotland'),(42,'Claes','Falk','Blomsterlandet','+46-755-557-4','Snårvägen 5','','Borås','41883','Sweden','Kerstin Holmberg ','Region Dalarna'),(43,'Eva','Andreasson','Nibe','+46-755-556-6','Åsavägen 91','','Kalix','41534','Sweden','Viktoria Ali ','Region Västernorrland'),(45,'Kent','Fransson','Latour','+46-715-556-9','Höneforsgatan 77','','Nordmaling','22876','Sweden','Ingeborg Norberg ','Region Stockholm'),(46,'Tomas','Berglund','Team Sportia','+46-755-555-6','Lundby 77','','Degerfors','87982','Sweden','Gun Pålsson ','Region Halland'),(47,'Marcus','Lundberg','Media Markt','+46-725-554-2','Vansövägen 98','','Solna','39227','Sweden','Marie Engström ','Region Gävleborg'),(48,'Eva','Engström','Granngården','+46-745-554-1','Grötvägen 62','','Gnosjö','34833','Sweden','Lisa Abrahamsson ','Region Blekinge'),(49,'Åke','Berglund','Komplett.se','+46-755-555-6','Tulpangatan 15','','Gustavsberg','81133','Sweden','Anette Lundgren ','Region Sörmland'),(51,'Fredrik','Hedlund','Guldfynd','+46-775-555-3','Apelsinvägen 88','','Gnesta','03739','Sweden','Arne Viklund ','Region Västmanland'),(52,'Joakim','Lindström','Kicks','+46-765-559-1','Skärpingegatan 18','','Haparanda','00366','Sweden','Kerstin Jönsson ','Region Jönköpings län'),(53,'Fatima','Berglund','Jula','+46-795-554-4','Grötgatan 15','','Arentorp','05682','Sweden','Peter Hansson ','Region Västmanland'),(54,'Per','Falk','Swedbank','+46-705-551-5','Västerhansjön 74','','Sollefteå','26294','Sweden','Simon Mårtensson ','Region Gotland'),(55,'Simon','Björklund','Audio Video','+46-705-556-7','Storegårdsvägen 60','','Hässleholm','08043','Sweden','Marianne Falk ','Region Gotland'),(56,'Linnéa','Falk','XXL Sport och vildmark','+46-755-556-6','Pikogatan 82','','Upplands Väsby','01068','Sweden','John Lindström ','Region Kronoberg'),(57,'Ingvar','Arvidsson','Cervera','+46-725-558-3','Hindås Stationsväg 65','','Ardala','36676','Sweden','Marianne Hansson ','Region Stockholm'),(58,'Anton','Nordin','Rusta','+46-715-558-3','Tistelgatan 15','','Timmele','70303','Sweden','Bengt Öberg ','Region Skåne'),(59,'Thomas','Berggren','Maximat','+46-795-552-9','Tulpanvägen 80','','Länghem','97894','Sweden','Rikard Magnusson ','Region Kronoberg'),(60,'Göran','Hassan','Elgiganten','+46-765-551-8','Aspvägen 86','','Överkalix','01068','Sweden','Anna Strömberg ','Region Uppsala'),(61,'Kurt','Danielsson','Autoexperten','+46-745-553-8','Apelsinvägen 80','','Kiruna','03110','Sweden','Louise Hansen ','Region Norrbotten'),(62,'Michel','Åberg','Bygghemma.se','+46-735-550-8','Äppelvägen 70','','Limmared','04557','Sweden','Kia Holmgren ','Region Stockholm'),(63,'Kent','Ahmed','Specsavers','+46-745-558-7','Oskarsgatan 12','','Hudiksvall','32653','Sweden','Miakel Sjöberg ','Region Uppsala'),(64,'Emma','Falk','Chilli, Wegot','+46-795-553-1','Äppelgatan 72','','Torsås','03739','Sweden','Elsa Bergqvist ','Region Dalarna'),(65,'Berit','Isaksson','Din Sko','+46-775-557-6','Apelsingatan 65','','Filsbäck','44700','Sweden','Anita Mårtensson ','Region Blekinge'),(66,'Henrik','Larsson','Coop Nord','+46-765-554-6','Västerhansjön 66','','Halmstad','36676','Sweden','Leif Löfgren ','Region Gotland'),(67,'Anton','Ek','Coop Sverige','+46-725-558-0','Hindås Stationsväg 12','','Nora','44700','Sweden','Alexandra Hermansson ','Region Uppsala'),(68,'Helena','Dahl','Autoexperten','+46-795-552-0','Ångpannevägen 82','','Skurup','24540','Sweden','Rune Lindholm ','Region Gävleborg'),(69,'Lars','Jansson','Intersport','+46-715-556-2','Apelsingatan 91','','Storfors','50403','Sweden','Emanuel Samuelsson ','Region Kalmar län'),(70,'Britt','Blomqvist','Atlascopco','+46-705-556-7','Brunnevägen 82','','Piteå','22876','Sweden','Adnan Jansson ','Region Gävleborg'),(71,'Monica','Jansson','Biltema','+46-725-554-2','Åbyhöjden 23','','Valdemarsvik','37267','Sweden','Therese Eliasson ','Region Västerbotten'),(72,'Stefan','Åkesson','SEB','+46-705-551-5','Nöjesgatan 29','','Mölndal','34971','Sweden','Per Lundin ','Region Sörmland'),(73,'Gustav','Jakobsson','Byggmax','+46-765-551-0','Håstads Bygata 41','','Nedre Gärdsjö','36965','Sweden','Kjell Wikström ','Region Halland'),(74,'Roland','Håkansson','Elon','+46-755-556-6','Jordgubbsvägen 77','','Åmål','39227','Sweden','Kenneth Holmqvist ','Region Gotland'),(75,'Bo','Ek','Gina Tricot','+46-735-558-8','Päronvägen 62','','Vilhelmina','08043','Sweden','Ebba Sjöberg ','Region Sörmland'),(76,'Caroline','Nyström','Kappahl','+46-765-559-2','Dyvik 46','','Tumba','15034','Sweden','Kent Åkesson ','Region Örebro län'),(77,'Ulla','Magnusson','Maximat','+46-755-552-9','Ångpannegatan 98','','Hortlax','41883','Sweden','Elias Ek ','Region Västernorrland'),(78,'Carina','Öberg','Swedbank AB','+46-715-559-5','Sandhällagatan 25','','Enköping','99211','Sweden','Göran Henriksson ','Västra Götalandsregionen'),(80,'Gösta','Forsberg','Volvo AB','+46-715-550-8','Loftaheden 48','','Borgholm','01183','Sweden','Anna Abrahamsson ','Region Uppsala'),(81,'Laban','Andersson','Bofinken','08-56565656','Smultronvägen','','Göteborg','44978','Sweden','Inger Bertilsson','Västra Götaland');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `manufacturer_id` int NOT NULL AUTO_INCREMENT,
  `name_manufacturer` varchar(45) NOT NULL,
  `main_office_adress1` varchar(100) NOT NULL,
  `main_office_adress2` varchar(100) DEFAULT NULL,
  `main_office_name` varchar(100) NOT NULL,
  `contact_person_name` varchar(200) NOT NULL,
  `contact_person_phone` varchar(45) NOT NULL,
  `contact_person_email` varchar(45) NOT NULL,
  PRIMARY KEY (`manufacturer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
INSERT INTO `manufacturers` VALUES (1,'Saab','Snårskogen 11','','Saab Trollhättan AB','Ove Jansson','+46758785841','ove.jansson123@saab.se'),(2,'Saab','Snårskogen 11','','Saab Trollhättan AB','Ove Jansson','+46758785841','ove.jansson123@saab.se'),(3,'Saab','Snårskogen 11','','Saab Trollhättan AB','Ove Jansson','+46758785841','ove.jansson123@saab.se'),(4,'Volkswagen AG','Eriksbo Västergärde','','Varbers kontoret','Kerstin_Abrahamsson','+46-745-554-1','Kerstin_Abrahamsson@hotmail.com'),(5,'Fiat Chrysler Automobiles','Trädgårdsgatan','','Falkenberg kontoret','John_Jansson','+46-765-556-1','John_Jansson@outlook.com'),(6,'Renault–Nissan–Mitsubishi Alliance','Handslagarevägen','','Stockholms kontoret','Oliver_Forsberg','+46-755-555-6','Oliver_Forsberg@hotmail.com'),(7,'Toyota Motor Corporation','Esplanadgatan','','Göteborgs kontoret','Britt_Jansson','+46-745-559-9','Britt_Jansson@yahoo.com'),(8,'Fiat Chrysler Automobiles','Lergatan','','Varbers kontoret','Leif_Hansen','+46-745-554-1','Leif_Hansen@yahoo.com'),(9,'Chrysler Cooperation','Enestigen','','Stockholms kontoret','Camilla_Svensson','+46-705-556-2','Camilla_Svensson@gmail.com'),(10,'General Motors','Molngatan','','Varbers kontoret','Alexandra_Engström','+46-785-551-9','Alexandra_Engström@yahoo.com'),(11,'Enhanced Ford Vehicles','Klövervägen','','Falkenberg kontoret','Wilhelm_Hermansson','+46-735-558-8','Wilhelm_Hermansson@gmail.com'),(12,'Tata Motors','Billsbro Karlslund','','Falkenberg kontoret','Kenneth_Bengtsson','+46-775-558-9','Kenneth_Bengtsson@outlook.com'),(13,'Renault–Nissan–Mitsubishi Alliance','Aspvägen','','Göteborgs kontoret','Birgitta_Mohamed','+46-745-555-3','Birgitta_Mohamed@live.se'),(14,'British Motor Corporation','Hantverkargatan','','Stockholms kontoret','Julia_Nordin','+46-755-552-9','Julia_Nordin@live.se'),(15,'Fiat Chrysler Automobiles','Klörupsgatan','','Varbers kontoret','Magdalena_Lindström','+46-775-558-3','Magdalena_Lindström@outlook.com'),(16,'Toyota Motor Corporation','Sandhällagatan','','Falkenberg kontoret','Christina_Olofsson','+46-785-554-3','Christina_Olofsson@yahoo.com'),(17,'Stellantis','Bagarbovägen','','Göteborgs kontoret','Björn_Martinsson','+46-755-550-2','Björn_Martinsson@gmail.com'),(18,'General Motors','Algatan','','Varbers kontoret','Emanuel_Gunnarsson','+46-795-553-1','Emanuel_Gunnarsson@hotmail.com'),(19,'McLaren Automotive','Algatan','','Falkenberg kontoret','Amanda_Lind','+46-705-555-2','Amanda_Lind@gmail.com'),(20,'Fiat Chrysler Automobiles','Äppelvägen','','Varbers kontoret','Ella_Hermansson','+46-715-554-7','Ella_Hermansson@live.se'),(21,'Renault–Nissan–Mitsubishi Alliance','Aspvägen','','Göteborgs kontoret','Louise_Öberg','+46-735-550-8','Louise_Öberg@live.se'),(22,'Fiat S.p.A','Jordgubbsgatan','','Varbers kontoret','Eva_Berg','+46-725-558-3','Eva_Berg@gmail.com'),(23,'Volkswagen AG','Knektvägen','','Falkenberg kontoret','Miakel_Magnusson','+46-785-553-2','Miakel_Magnusson@hotmail.com'),(24,'Fiat S.p.A','Aspö Lilla Östergården','','Falkenberg kontoret','Alexandra_Håkansson','+46-755-552-9','Alexandra_Håkansson@hotmail.com'),(25,'Toyota Motor Corporation','Mållångsbogatan','','Falkenberg kontoret','Martin_Lundin','+46-785-559-5','Martin_Lundin@hotmail.com'),(26,'Chrysler Cooperation','Eriksbo Västergärde','','Varbers kontoret','Elias_Lind','+46-775-553-5','Elias_Lind@gmail.com'),(27,'Ford Motor Company','Trädgårdsgatan','','Göteborgs kontoret','Simon_Eliasson','+46-715-550-8','Simon_Eliasson@outlook.com'),(28,'Renault–Nissan–Mitsubishi Alliance','Enestigen','','Varbers kontoret','Maria_Ek','+46-785-554-8','Maria_Ek@live.se'),(29,'Tata Motors','Knektvägen','','Stockholms kontoret','Rolf_Nilsson','+46-705-556-2','Rolf_Nilsson@gmail.com'),(30,'Pagani Automobili S.p.A.','Päronvägen','','Falkenberg kontoret','Ebba_Arvidsson','+46-715-550-8','Ebba_Arvidsson@outlook.com'),(31,'Toyota Motor Corporation','Grötgatan','','Göteborgs kontoret','Sofie_Jönsson','+46-725-556-6','Sofie_Jönsson@outlook.com'),(32,'Enhanced Ford Vehicles','Storegårdsvägen','','Stockholms kontoret','Linnea_Ahmed','+46-795-555-1','Linnea_Ahmed@hotmail.com'),(33,'Pagani Automobili S.p.A.','Aprilvägen','','Göteborgs kontoret','Gunnar_Ahmed','+46-775-553-5','Gunnar_Ahmed@yahoo.com'),(34,'Lagonda Global Holdings plc','Höneforsgatan','','Varbers kontoret','Miakel_Nordin','+46-785-558-9','Miakel_Nordin@yahoo.com'),(35,'Tata Motors','Loftaheden','','Varbers kontoret','John_Berg','+46-775-559-8','John_Berg@outlook.com'),(36,'General Motors (GM)','Skärpingegatan','','Falkenberg kontoret','Ingegerd_Dahlberg','+46-785-559-6','Ingegerd_Dahlberg@live.se'),(37,'Groupe Renault','Oskarsgatan','','Varbers kontoret','Vidhelm_Sandberg','+46-795-557-3','Vidhelm_Sandberg@outlook.com'),(38,'Renault–Nissan–Mitsubishi Alliance','Pikogatan','','Stockholms kontoret','Berit_Jönsson','+46-765-555-1','Berit_Jönsson@gmail.com'),(39,'Mercedes-Benz','Hantverkargatan','','Göteborgs kontoret','Anton_Forsberg','+46-765-559-1','Anton_Forsberg@hotmail.com'),(40,'Chrysler Cooperation','Lundby','','Falkenberg kontoret','William_Bergqvist','+46-715-559-5','William_Bergqvist@gmail.com'),(41,'Fiat Chrysler Automobiles','Orrspelsvägen','','Falkenberg kontoret','Gunnar_Löfgren','+46-725-556-4','Gunnar_Löfgren@gmail.com'),(42,'Chrysler Cooperation','Aspgatan','','Stockholms kontoret','Barbro_Fredriksson','+46-755-550-4','Barbro_Fredriksson@yahoo.com'),(43,'Volkswagen AG','Wesslunds Gränd','','Varbers kontoret','Carina_Hermansson','+46-775-550-3','Carina_Hermansson@live.se'),(44,'McLaren Automotive','Hedehusgatan','','Stockholms kontoret','Lina_Mohamed','+46-795-551-3','Lina_Mohamed@live.se'),(45,'The Mazda Motor Corporation','Gärdesgatan','','Göteborgs kontoret','Linnea_Jansson','+46-705-554-8','Linnea_Jansson@yahoo.com'),(46,'Volvo Cars','Pärlgräsvägen','','Falkenberg kontoret','Robert_Karlsson','+46-775-553-5','Robert_Karlsson@hotmail.com'),(47,'Volkswagen AG','Billsbro Karlslund','','Falkenberg kontoret','Ida_Danielsson','+46-765-551-8','Ida_Danielsson@yahoo.com'),(48,'General Motors Company (GM)','Ryttarvägen','','Varbers kontoret','Anna_Viklund','+46-705-556-7','Anna_Viklund@live.se'),(49,'Chrysler Cooperation','Grötvägen','','Falkenberg kontoret','Annika_Löfgren','+46-785-558-4','Annika_Löfgren@gmail.com'),(50,'General Motors','Åbyhöjden','','Falkenberg kontoret','Åsa_Lindholm','+46-745-559-9','Åsa_Lindholm@yahoo.com'),(51,'Fiat Chrysler Automobiles','Dalhemsvägen','','Stockholms kontoret','Kurt_Sjögren','+46-715-554-7','Kurt_Sjögren@outlook.com'),(52,'Fiat Chrysler Automobiles','Pärlgräsvägen','','Varbers kontoret','Lena_Bergström','+46-745-557-3','Lena_Bergström@live.se'),(53,'The Mazda Motor Corporation','Pikovägen','','Varbers kontoret','Ingeborg_Hellström','+46-755-553-9','Ingeborg_Hellström@gmail.com'),(54,'Volkswagen AG','Hönefossvägen','','Stockholms kontoret','Emanuel_Gunnarsson','+46-755-553-9','Emanuel_Gunnarsson@hotmail.com'),(55,'The Mazda Motor Corporation','Nöjesgatan','','Falkenberg kontoret','Anders_Lundström','+46-725-558-3','Anders_Lundström@outlook.com'),(56,'Fiat Chrysler Automobiles Stellantis','Marbäck Ekhult','','Göteborgs kontoret','Roland_Dahl','+46-755-550-4','Roland_Dahl@hotmail.com'),(57,'Pagani Automobili S.p.A.','Billsbro Karlslund','','Varbers kontoret','Jonas_Viklund','+46-715-550-8','Jonas_Viklund@yahoo.com'),(58,'General Motors Company (GM)','Simpnäs','','Varbers kontoret','Björn_Johansson','+46-725-558-3','Björn_Johansson@hotmail.com'),(59,'Toyota Motor Corporation','Åbyhöjden','','Stockholms kontoret','Kent_Åkesson','+46-775-555-0','Kent_Åkesson@gmail.com'),(60,'Stellantis','Tuvvägen','','Göteborgs kontoret','Siv_Bergström','+46-765-551-8','Siv_Bergström@live.se'),(61,'Fiat Chrysler Automobiles','Äppelvägen','','Varbers kontoret','Kurt_Lund','+46-795-558-3','Kurt_Lund@hotmail.com'),(62,'Tata Motors','Stackekärrsgatan','','Göteborgs kontoret','Astrid_Blom','+46-795-558-5','Astrid_Blom@gmail.com'),(63,'Renault–Nissan–Mitsubishi Alliance','Västerhansjön','','Göteborgs kontoret','Magdalena_Öberg','+46-765-559-1','Magdalena_Öberg@yahoo.com'),(64,'British Motor Corporation','Oskarsvägen','','Stockholms kontoret','Märta_Magnusson','+46-725-556-6','Märta_Magnusson@outlook.com'),(65,'Lagonda Global Holdings plc','Orrspelsvägen','','Stockholms kontoret','Sofia_Henriksson','+46-795-557-1','Sofia_Henriksson@outlook.com'),(66,'Ford Motor Company','Nöjesgatan','','Stockholms kontoret','Adnan_Ek','+46-725-558-3','Adnan_Ek@live.se'),(67,'Hyundai Motor Group','Mållångsbogatan','','Varbers kontoret','Alf_Ek','+46-725-554-7','Alf_Ek@outlook.com'),(68,'Pagani Automobili S.p.A.','Apelsingatan','','Stockholms kontoret','Victoria_Forsberg','+46-745-552-7','Victoria_Forsberg@hotmail.com'),(69,'Ford Motor Company','Pärlgräsgatan','','Varbers kontoret','Robin_Henriksson','+46-775-550-3','Robin_Henriksson@yahoo.com'),(70,'General Motors Company (GM)','Pärlgräsvägen','','Stockholms kontoret','Kristina_Lindholm','+46-775-559-8','Kristina_Lindholm@yahoo.com'),(71,'Renault–Nissan–Mitsubishi Alliance','Bonnorp','','Göteborgs kontoret','Jonas_Månsson','+46-795-558-5','Jonas_Månsson@yahoo.com'),(72,'Royce Motor Cars Limited','Idvägen','','Varbers kontoret','Ulf_Lindqvist','+46-765-559-2','Ulf_Lindqvist@yahoo.com'),(73,'Ford Motor Company','Hedehusvägen','','Varbers kontoret','Frida_Hellström','+46-725-556-6','Frida_Hellström@live.se'),(74,'Volvo Cars','Aprilvägen','','Falkenberg kontoret','Gösta_Olsson','+46-755-553-9','Gösta_Olsson@yahoo.com'),(75,'British Motor Corporation','Orrspelsvägen','','Stockholms kontoret','Andreas_Ström','+46-775-556-2','Andreas_Ström@gmail.com'),(76,'Volvo Cars','Pärlgräsgatan','','Göteborgs kontoret','Gustav_Hedlund','+46-775-550-3','Gustav_Hedlund@outlook.com'),(77,'Ford Motor Company','Ramsviken','','Göteborgs kontoret','Gunnel_Claesson','+46-715-554-2','Gunnel_Claesson@hotmail.com'),(78,'Fiat Chrysler Automobiles','Aspgatan','','Varbers kontoret','Fredrik_Holmqvist','+46-795-551-7','Fredrik_Holmqvist@gmail.com');
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers_has_cps_orders`
--

DROP TABLE IF EXISTS `manufacturers_has_cps_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers_has_cps_orders` (
  `manufacturers_manufacturer_id` int NOT NULL,
  `cps_orders_internal_order_no` int NOT NULL,
  PRIMARY KEY (`manufacturers_manufacturer_id`,`cps_orders_internal_order_no`),
  KEY `fk_manufacturers_has_cps_orders_cps_orders1_idx` (`cps_orders_internal_order_no`),
  KEY `fk_manufacturers_has_cps_orders_manufacturers1_idx` (`manufacturers_manufacturer_id`),
  CONSTRAINT `fk_manufacturers_has_cps_orders_cps_orders1` FOREIGN KEY (`cps_orders_internal_order_no`) REFERENCES `cps_orders` (`internal_order_no`) ON UPDATE CASCADE,
  CONSTRAINT `fk_manufacturers_has_cps_orders_manufacturers1` FOREIGN KEY (`manufacturers_manufacturer_id`) REFERENCES `manufacturers` (`manufacturer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers_has_cps_orders`
--

LOCK TABLES `manufacturers_has_cps_orders` WRITE;
/*!40000 ALTER TABLE `manufacturers_has_cps_orders` DISABLE KEYS */;
INSERT INTO `manufacturers_has_cps_orders` VALUES (1,1),(60,1),(2,2),(4,2),(10,2),(3,3),(15,3),(2,4),(9,4),(1,5),(4,5),(7,5),(11,5),(7,6),(13,6),(22,6),(47,6),(5,7),(8,7),(11,7),(13,7),(24,7),(15,8),(6,9),(10,9),(11,9),(13,10),(17,10),(12,11),(16,11),(33,12),(3,13),(13,13),(20,14),(26,15),(4,16),(6,16),(12,16),(26,17),(45,17),(4,18),(9,18),(24,18),(29,18),(6,19),(30,19),(36,19),(9,21),(31,22),(40,22),(26,24),(21,27),(33,27),(12,28),(35,28),(4,29),(22,30),(31,30),(44,30),(60,30),(23,31),(32,31),(23,32),(6,33),(9,35),(27,35),(4,39),(3,40),(27,41),(69,42),(9,44),(16,45),(35,47),(30,51),(14,53),(9,54),(21,57),(59,57);
/*!40000 ALTER TABLE `manufacturers_has_cps_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_no` int NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `required_date` date NOT NULL,
  `shipping_date` date DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `comments` text,
  `customers_id_customers` int NOT NULL,
  PRIMARY KEY (`order_no`),
  KEY `fk_orders_customers1_idx` (`customers_id_customers`),
  CONSTRAINT `fk_orders_customers1` FOREIGN KEY (`customers_id_customers`) REFERENCES `customers` (`id_customers`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2021-10-10','2021-10-15','2021-10-12','Ok','Denna kommer gå i tid.',1),(2,'2021-10-10','2021-10-15','2021-10-12','Ok','Denna kommer gå i tid.',2),(3,'2021-10-10','2021-10-15','2021-10-12','Ok','Denna kommer gå i tid.',1),(4,'2016-12-01','2006-05-04','2015-06-08','Nok','',3),(5,'2021-01-05','2016-12-02','2017-08-13','Nok','',2),(6,'1950-09-25','2014-04-29','2008-12-06','Ok','',2),(7,'2016-05-12','2012-05-07','2012-05-07','Ok','',5),(8,'1982-10-12','2006-05-04','2012-10-31','Ok','',6),(9,'1957-07-17','1966-02-24','2013-07-03','Nok','',4),(10,'2015-06-08','2016-05-12','1992-02-19','Nok','',3),(11,'2014-08-21','1978-07-02','1950-09-25','Ok','',1),(12,'1972-06-23','2009-04-06','1982-05-15','Ok','',11),(13,'2000-12-28','1973-09-02','2009-04-06','Nok','',5),(14,'2012-05-07','1966-09-16','2013-03-12','Ok','',12),(15,'2018-08-26','1972-06-23','2013-11-10','Ok','',5),(16,'2013-09-05','2015-08-28','1996-04-09','Ok','',2),(17,'2021-04-11','1953-02-06','2009-05-04','Ok','',4),(18,'2017-06-03','2010-06-21','2017-06-07','Nok','',9),(19,'1986-04-09','2018-08-26','1976-04-01','Ok','',11),(20,'2017-08-13','1960-06-26','1981-03-16','Ok','',8),(21,'2000-12-28','2016-06-20','1978-12-12','Nok','',15),(22,'2021-02-08','1972-06-23','2018-06-15','Ok','',22),(23,'2021-03-12','1959-04-08','2020-11-20','Ok','',7),(24,'2015-10-02','2009-05-04','2012-10-31','Nok','',7),(25,'1960-06-26','1955-01-31','2013-09-05','Nok','',3),(26,'2018-08-26','1978-07-02','2013-07-03','Ok','',25),(27,'2021-02-08','2006-05-04','1960-06-26','Ok','',17),(28,'2010-02-11','2012-10-31','2015-10-02','Nok','',16),(29,'1953-02-06','2014-10-25','2012-09-29','Nok','',10),(30,'2006-05-04','1972-04-02','1991-05-04','Nok','',4),(31,'2013-11-10','1902-09-26','2014-04-29','Ok','',7),(32,'1978-07-02','1966-02-24','2021-08-02','Nok','',27),(33,'2009-05-04','2013-10-29','2021-02-08','Nok','',20),(34,'2021-04-11','2015-08-28','2016-09-26','Ok','',23),(35,'1957-07-17','2018-06-09','2018-06-15','Nok','',33),(36,'1950-09-25','1950-09-25','2010-06-21','Nok','',21),(37,'2014-04-29','2017-08-13','2016-12-02','Ok','',19),(38,'1953-02-06','1996-04-09','1982-05-15','Ok','',30),(39,'1950-09-25','2014-10-25','2017-08-13','Nok','',10),(40,'1976-04-01','1972-04-02','2014-08-09','Ok','',19),(41,'2018-06-09','1966-09-16','2016-06-20','Nok','',29),(42,'2013-03-12','2012-03-28','2012-05-07','Nok','',28),(43,'1978-12-12','2015-08-28','2016-05-12','Nok','',29),(44,'1957-06-05','1975-10-10','2016-06-12','Nok','',41),(45,'2017-06-03','2099-02-25','2021-01-05','Ok','',26),(46,'2010-02-11','2019-12-22','2019-01-27','Nok','',29),(47,'2015-10-02','2015-08-27','2015-10-02','Nok','',6),(48,'2014-04-29','2013-11-28','2014-11-04','Ok','',11),(49,'2015-06-08','2021-04-11','1982-10-12','Nok','',34),(50,'2020-11-20','2017-08-13','2012-05-05','Ok','',22),(51,'2014-10-25','1981-03-16','2013-10-29','Ok','',49),(52,'2009-05-04','2012-05-07','1957-07-17','Ok','',18),(53,'2013-11-28','1986-04-09','1957-07-17','Ok','',1),(54,'2012-05-05','1966-09-16','2014-10-25','Nok','',13),(55,'2012-03-28','2016-06-14','2015-10-02','Nok','',22),(56,'1978-12-12','2016-06-14','1986-04-09','Ok','',10),(57,'2016-12-02','1980-03-18','2014-11-04','Nok','',47),(58,'1972-04-02','1972-06-23','2021-04-11','Nok','',54),(59,'2018-08-26','2015-10-02','1982-05-15','Ok','',4),(60,'2012-10-31','1981-03-16','2017-08-24','Nok','',60),(61,'1986-04-09','1964-10-29','2010-06-21','Nok','',29),(62,'1976-04-01','2014-01-27','1976-04-01','Ok','',12),(63,'2014-01-27','2015-10-02','1978-09-04','Ok','',14),(64,'2014-11-04','2011-12-17','2011-12-17','Nok','',41),(65,'2016-05-12','2017-06-07','2014-01-27','Ok','',43),(66,'2014-08-21','2016-05-12','2019-01-27','Nok','',22),(67,'2013-03-12','2017-08-13','1980-03-18','Nok','',45),(68,'2012-10-31','2021-03-12','2019-01-27','Ok','',11),(69,'2016-12-01','2016-06-14','1950-09-25','Nok','',63),(70,'1950-09-25','2006-05-04','2013-09-05','Nok','',70),(71,'2015-06-08','2012-09-29','1957-06-05','Nok','',36),(72,'2021-03-12','1960-06-26','2016-12-01','Ok','',71),(73,'2012-09-15','2017-08-24','1966-09-16','Ok','',18),(74,'2009-04-06','2012-05-07','1978-09-04','Nok','',31),(75,'2017-08-24','2012-05-07','2015-08-28','Ok','',19),(76,'2012-05-05','1987-12-22','1960-06-26','Ok','',26),(77,'2001-05-27','1985-03-17','1981-03-16','Ok','',32),(78,'2013-03-12','2013-10-29','1973-09-02','Ok','',9);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordersdetails`
--

DROP TABLE IF EXISTS `ordersdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordersdetails` (
  `orders_order_no` int NOT NULL,
  `products_product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `price_each` decimal(10,2) NOT NULL,
  PRIMARY KEY (`orders_order_no`,`products_product_id`),
  KEY `fk_orders_has_products_products1_idx` (`products_product_id`),
  KEY `fk_orders_has_products_orders1_idx` (`orders_order_no`),
  CONSTRAINT `fk_orders_has_products_orders1` FOREIGN KEY (`orders_order_no`) REFERENCES `orders` (`order_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_has_products_products1` FOREIGN KEY (`products_product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordersdetails`
--

LOCK TABLES `ordersdetails` WRITE;
/*!40000 ALTER TABLE `ordersdetails` DISABLE KEYS */;
INSERT INTO `ordersdetails` VALUES (1,1,12,200.00),(1,27,58,3348.64),(2,2,12,200.00),(2,5,92,890.32),(2,7,24,21690.27),(2,18,59,13253.05),(2,19,1,13897.59),(3,3,12,200.00),(3,6,39,15953.02),(4,1,77,28522.22),(4,2,36,483.42),(4,4,54,2459.69),(5,6,66,10619.45),(5,7,30,6595.01),(5,8,36,16522.95),(5,12,30,29341.74),(5,19,98,12306.72),(5,29,71,24095.51),(6,1,57,21860.29),(6,31,88,25436.18),(7,1,39,17611.94),(7,2,40,9318.08),(7,4,29,23903.81),(7,8,88,27525.23),(7,9,10,12642.51),(7,10,37,25649.02),(7,55,33,2691.18),(8,2,70,25905.21),(8,9,77,27789.66),(8,56,64,10404.73),(9,14,52,910.12),(10,12,3,23094.15),(10,39,75,13878.63),(11,13,85,4651.01),(11,24,68,2786.64),(13,18,84,4101.42),(13,21,43,1061.69),(13,22,91,21049.87),(14,2,89,21943.84),(14,3,49,12192.20),(14,64,83,6490.73),(17,8,23,24291.66),(17,10,45,5729.88),(18,16,51,10656.33),(20,7,18,4544.42),(21,11,16,26675.00),(21,38,96,24151.60),(22,4,14,21595.87),(22,24,48,6394.86),(23,3,69,19115.61),(23,20,89,14426.55),(23,33,52,16070.24),(24,58,14,25317.15),(27,21,51,26005.62),(27,26,85,29159.52),(28,11,87,14657.06),(30,6,34,25796.13),(31,9,76,29703.58),(31,11,61,5607.72),(32,25,30,16119.16),(33,19,94,23256.84),(33,29,73,11689.67),(34,32,56,9695.16),(38,39,59,25033.05),(41,7,34,17426.31),(42,7,37,1608.78),(44,12,28,28830.57),(45,9,40,5968.62),(48,12,98,756.97),(49,9,31,381.15),(54,21,14,26130.99),(55,17,50,24459.64),(59,32,31,25710.95),(63,30,56,17393.30),(65,27,68,7848.84),(67,15,5,23437.87),(68,31,80,20567.43),(69,54,79,1664.09);
/*!40000 ALTER TABLE `ordersdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payments_no` int NOT NULL AUTO_INCREMENT,
  `payment_date` date DEFAULT NULL,
  `payment_amount` decimal(10,2) NOT NULL,
  `customer_paid_bill_id` int DEFAULT NULL,
  PRIMARY KEY (`payments_no`),
  KEY `customer_paid_bill_id` (`customer_paid_bill_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`customer_paid_bill_id`) REFERENCES `customers` (`id_customers`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,'2021-10-12',1300.00,1),(2,'2021-10-12',1300.00,2),(3,'2021-10-12',1300.00,1),(4,'2012-03-28',25094.79,5),(5,'1975-10-10',11627.84,6),(6,'1986-04-09',4563.10,1),(7,'1981-03-16',20769.58,3),(8,'2020-11-20',29470.11,3),(9,'2013-12-12',2265.01,4),(10,'2012-05-05',17938.88,8),(11,'1972-04-02',20633.30,5),(12,'1966-09-16',29425.16,1),(13,'1960-06-26',3626.39,9),(14,'2017-08-24',18354.96,4),(15,'1972-06-23',14483.90,5),(16,'1986-04-09',28486.36,5),(17,'2009-05-04',22614.87,8),(18,'2016-09-26',10246.88,4),(19,'2012-09-29',13593.54,1),(20,'2019-12-22',28384.60,2),(21,'2014-10-25',21868.42,15),(22,'2017-03-12',20844.03,12),(23,'2015-06-24',27622.73,20),(24,'1906-10-23',27489.66,12),(25,'1972-04-02',27248.85,11),(26,'2013-09-05',13251.55,4),(27,'2015-08-27',29765.10,22),(28,'1902-09-26',24147.04,15),(29,'2013-11-10',11179.02,12),(30,'2019-12-22',25623.59,5),(31,'2008-12-06',14676.81,20),(32,'2014-08-21',28557.50,1),(33,'2019-12-22',7469.52,31),(34,'2018-06-09',1200.09,31),(35,'2007-08-17',28584.47,1),(36,'2015-10-02',737.88,26),(37,'2013-07-03',5763.29,37),(38,'2012-09-29',3501.73,10),(39,'2014-04-29',26456.10,9),(40,'2013-11-10',9375.97,14),(41,'2019-12-22',18190.30,42),(42,'2018-06-15',10854.23,30),(43,'1978-07-02',11215.84,22),(44,'2017-03-12',13441.73,17),(45,'2012-09-29',5029.56,13),(46,'2014-10-25',26529.74,31),(47,'2017-11-23',1448.00,9),(48,'2014-08-21',28050.51,30),(49,'2015-06-08',27745.35,15),(50,'2017-03-12',24143.93,36),(52,'2021-03-12',7826.31,14),(53,'2017-08-24',16684.28,12),(54,'2021-04-11',3119.21,42),(55,'2011-05-13',23489.76,37),(56,'2014-08-21',18164.10,57),(57,'2018-08-26',15563.90,3),(58,'2011-05-13',26442.86,19),(59,'1957-07-17',2892.19,38),(60,'2014-11-04',24902.17,3),(61,'2012-09-29',17250.26,53),(62,'1959-04-08',2486.43,56),(63,'1987-12-22',21470.42,24),(64,'2015-08-27',10938.87,55),(65,'2018-08-26',23640.52,16),(66,'2013-11-28',21562.82,40),(67,'2011-12-17',5758.60,17),(68,'1996-04-09',25246.07,68),(69,'2021-01-05',4017.92,47),(70,'2012-05-07',9033.90,37),(71,'2017-06-07',23561.51,59),(72,'2020-11-20',10801.92,43),(73,'1960-06-26',3295.51,53),(74,'2012-05-05',1099.72,46),(75,'1953-02-06',29386.08,30),(76,'2012-09-15',14148.52,59),(77,'1986-04-09',7691.06,10),(78,'2014-04-29',12050.44,66);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_description_table`
--

DROP TABLE IF EXISTS `product_description_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_description_table` (
  `product_description` varchar(50) DEFAULT NULL,
  `text_description` varchar(5000) DEFAULT NULL,
  `html_description` mediumtext,
  `image` mediumblob,
  `products_description_id` int DEFAULT NULL,
  `desc_count` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`desc_count`),
  KEY `fk_product_description_table_products1_idx` (`products_description_id`),
  CONSTRAINT `fk_product_description_table_products1` FOREIGN KEY (`products_description_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_description_table`
--

LOCK TABLES `product_description_table` WRITE;
/*!40000 ALTER TABLE `product_description_table` DISABLE KEYS */;
INSERT INTO `product_description_table` VALUES ('Saab Trollhättan','Saab vi flyger fram.','<h1>Saab</h1>',_binary 'saab.png',NULL,1),('Saab Trollhättan','Saab vi flyger fram.','<h1>Saab</h1>',_binary 'saab.png',NULL,2),('Saab Trollhättan','Saab vi flyger fram.','<h1>Saab</h1>',_binary 'saab.png',NULL,3),('ll','En liten groda','mjeow',_binary 'saab.jpg',4,4),('ee','En stor groda','lilla molntuss',_binary 'saab.jpg',5,5),('hh','En stor groda','mjau',_binary 'saab.jpg',6,6),('ii','En mycket fin katt','tralala',_binary 'saab.jpg',7,7),('kk','En stor groda','mjau',_binary 'saab.jpg',8,8),('mm','En liten uggla','mjau',_binary 'saab.jpg',9,9),('kk','En stor groda','lilla molntuss',_binary 'saab.jpg',10,10),('bb','Bla blaa blaaa blblablablaaa','mjau',_binary 'saab.jpg',11,11),('mm','En mycket fin katt','mjeow',_binary 'saab.jpg',12,12),('gg','En liten uggla','tralala',_binary 'saab.jpg',13,13),('dd','Bla blaa blaaa blblablablaaa','mjeow',_binary 'saab.jpg',14,14),('bb','En liten uggla','mjau',_binary 'saab.jpg',15,15),('gg','En liten groda','tralala',_binary 'saab.jpg',16,16),('ll','En liten uggla','mjeow',_binary 'saab.jpg',17,17),('aa','En mycket fin katt','lilla molntuss',_binary 'saab.jpg',18,18),('nn','En liten groda','mjau',_binary 'saab.jpg',19,19),('ii','En liten uggla','tralala',_binary 'saab.jpg',20,20),('aa','En stor groda','mjeow',_binary 'saab.jpg',21,21),('dd','Bla blaa blaaa blblablablaaa','lilla molntuss',_binary 'saab.jpg',22,22),('ii','En stor groda','lilla molntuss',_binary 'saab.jpg',23,23),('kk','En liten uggla','meow',_binary 'saab.jpg',24,24),('oo','Bla blaa blaaa blblablablaaa','meow',_binary 'saab.jpg',25,25),('ff','En stor groda','lilla molntuss',_binary 'saab.jpg',26,26),('nn','En stor groda','lilla molntuss',_binary 'saab.jpg',27,27),('mm','Bla blaa blaaa blblablablaaa','tralala',_binary 'saab.jpg',28,28),('cc','En liten uggla','lilla molntuss',_binary 'saab.jpg',29,29),('oo','En mycket fin katt','tralala',_binary 'saab.jpg',30,30),('aa','En stor groda','mjau',_binary 'saab.jpg',31,31),('gg','En liten groda','mjau',_binary 'saab.jpg',32,32),('hh','En stor groda','mjeow',_binary 'saab.jpg',33,33),('ff','En mycket fin katt','meow',_binary 'saab.jpg',34,34),('oo','Bla blaa blaaa blblablablaaa','mjeow',_binary 'saab.jpg',35,35),('ii','En mycket fin katt','lilla molntuss',_binary 'saab.jpg',36,36),('hh','En liten uggla','tralala',_binary 'saab.jpg',37,37),('gg','En stor groda','meow',_binary 'saab.jpg',38,38),('gg','En mycket fin katt','lilla molntuss',_binary 'saab.jpg',39,39),('mm','En mycket fin katt','lilla molntuss',_binary 'saab.jpg',40,40),('jj','En stor groda','tralala',_binary 'saab.jpg',41,41),('dd','En liten uggla','mjeow',_binary 'saab.jpg',42,42),('dd','En liten uggla','meow',_binary 'saab.jpg',43,43),('aa','En liten groda','lilla molntuss',_binary 'saab.jpg',44,44),('dd','En mycket fin katt','lilla molntuss',_binary 'saab.jpg',45,45),('cc','En liten uggla','meow',_binary 'saab.jpg',46,46),('jj','En liten uggla','meow',_binary 'saab.jpg',47,47),('ff','En liten groda','mjeow',_binary 'saab.jpg',48,48),('gg','En liten groda','tralala',_binary 'saab.jpg',49,49),('nn','En liten groda','meow',_binary 'saab.jpg',50,50),('ll','En stor groda','meow',_binary 'saab.jpg',51,51),('ii','En liten uggla','mjau',_binary 'saab.jpg',52,52),('bb','En stor groda','meow',_binary 'saab.jpg',53,53),('nn','En mycket fin katt','mjeow',_binary 'saab.jpg',54,54),('ff','En mycket fin katt','mjau',_binary 'saab.jpg',55,55),('ii','En stor groda','meow',_binary 'saab.jpg',56,56),('ii','Bla blaa blaaa blblablablaaa','mjeow',_binary 'saab.jpg',57,57),('bb','En liten groda','lilla molntuss',_binary 'saab.jpg',58,58),('kk','En stor groda','mjeow',_binary 'saab.jpg',59,59),('ee','Bla blaa blaaa blblablablaaa','mjeow',_binary 'saab.jpg',60,60),('oo','En mycket fin katt','meow',_binary 'saab.jpg',61,61),('dd','Bla blaa blaaa blblablablaaa','meow',_binary 'saab.jpg',62,62),('nn','Bla blaa blaaa blblablablaaa','mjeow',_binary 'saab.jpg',63,63),('aa','En liten uggla','meow',_binary 'saab.jpg',64,64),('dd','Bla blaa blaaa blblablablaaa','mjau',_binary 'saab.jpg',65,65),('ee','En liten uggla','meow',_binary 'saab.jpg',66,66),('mm','En mycket fin katt','lilla molntuss',_binary 'saab.jpg',67,67),('gg','En liten groda','lilla molntuss',_binary 'saab.jpg',68,68),('gg','En mycket fin katt','meow',_binary 'saab.jpg',69,69),('ii','Bla blaa blaaa blblablablaaa','mjeow',_binary 'saab.jpg',70,70),('mm','En stor groda','lilla molntuss',_binary 'saab.jpg',71,71),('cc','En liten groda','mjeow',_binary 'saab.jpg',72,72),('jj','En liten groda','mjeow',_binary 'saab.jpg',73,73),('ii','En liten uggla','meow',_binary 'saab.jpg',74,74),('oo','En liten uggla','lilla molntuss',_binary 'saab.jpg',75,75),('ee','En mycket fin katt','tralala',_binary 'saab.jpg',76,76),('nn','En liten groda','mjau',_binary 'saab.jpg',77,77),('mm','En stor groda','lilla molntuss',_binary 'saab.jpg',78,78);
/*!40000 ALTER TABLE `product_description_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(45) NOT NULL,
  `product_description` text NOT NULL,
  `inprice` decimal(10,2) NOT NULL,
  `outprice` decimal(10,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Sportratt till Saab 9000','En sportig ratt till Saab 9000',2700.99,3700.99),(2,'Sportratt till Saab 9000','En sportig ratt till Saab 9000',2700.99,3700.99),(3,'Sportratt till Saab 9000','En sportig ratt till Saab 9000',2700.99,3700.99),(4,'oljetråg','map sensor',7990.84,14849.21),(5,'belysning baklyckta','tändfördelare',201.54,28872.51),(6,'bromssköld','bromsskivor',25305.73,9633.14),(7,'växellåda','relä kylfläkt',24396.74,20795.28),(8,'smörjmedel','tätmassa för kylare',12620.81,20752.57),(9,'generator','oljeplugg',11435.69,17436.87),(10,'glasrengörning','vevlager',23224.18,7525.58),(11,'tätmassa för kylare','smörjmedel',24526.39,26857.42),(12,'filtersats','centrallås',29908.12,19527.87),(13,'färg och lacker','bromssköld',19556.61,11252.64),(14,'fläkt klimatanläggning','styrväxeldamask',10776.61,18068.17),(15,'slitagevarnare bromsbelägg','fjäderverktyg',8272.18,19122.85),(16,'färg och lacker','stötdämpare',23138.39,17527.88),(17,'blandningsklaff','hjullager',17859.20,4780.80),(18,'tätningsmedel','gasspjällsgivare',27175.27,24272.01),(19,'tätningsmedel','skarvtätning',28820.92,25504.98),(20,'abs krans','oljepump',655.58,4200.31),(21,'belysning baklyckta','kopplingsvajer',25200.76,13397.74),(22,'Bränslepump','hållare luftfilterhus',15311.50,16269.16),(23,'oljetråg','stabilisatorstag',24323.93,19506.90),(24,'vindrute lim','knackningssensor',8943.53,4228.74),(25,'startmotor','belysning baklyckta',8316.25,19410.95),(26,'elhiss','oljetrycksgivare',29166.14,7520.96),(27,'oljefilter','mutter axeltapp',6410.05,11465.30),(28,'drivaxel','mellanlager drivaxel',20221.06,7592.39),(29,'vevlager','tätmassa för kylare',29474.73,2714.35),(30,'oljeplugg','torkarmekanism',11028.75,11421.99),(31,'förångare','styrpackning',6680.21,1571.64),(32,'avgassystem','relä kylfläkt',16228.27,15333.12),(33,'torkarmekanism','filtersats',4556.56,15077.14),(34,'relä kylfläkt','kopplingsvajer',25206.68,10919.78),(35,'bilshampoo','avgassystem',23382.84,26860.22),(36,'oljetråg','baggageutrymme',12059.40,4797.66),(37,'bromsskivor','vevlager',19454.59,11671.33),(38,'fjädrar till dämpare','fläkt klimatanläggning',22648.88,7832.88),(39,'tändsystemsverktyg','mutter axeltapp',7655.65,22054.72),(40,'krängningshämmare','mellanlager drivaxel',18209.57,12406.41),(41,'vvt-ventil','kupefilter',5434.34,8734.80),(42,'gänglåsning','oljetrycksgivare',576.35,13274.57),(43,'styrstag','elhiss',16057.37,19265.48),(44,'limtape','bränslematning Filter',9628.26,29307.98),(45,'värmefläkt','ac slang',29947.00,24535.34),(46,'fjädrar till dämpare','upphängningssats spiralfjädrar',23053.55,6465.02),(47,'Bränslepump','batteri',9993.41,22158.89),(48,'slitagevarnare bromsbelägg','växellåda',4997.71,17402.16),(49,'sekundärluftfilter','drivaxel',7011.35,21119.99),(50,'filtersats','magnetkoppling',339.10,8483.13),(51,'däcktryck kontrollsystem','termokontakt',21122.32,8120.81),(52,'värmefläkt','halvljus led lampa',8892.82,17308.65),(53,'kardanaxelbult','ac slang',3299.18,8256.48),(54,'fönsterhiss','reparationssats styrled',20927.25,19064.25),(55,'belysning baklyckta','fläkt klimatanläggning',18578.32,3918.89),(56,'oljetråg','bromsljus',19761.37,11397.33),(57,'tätmassa för kylare','spraylim',23978.80,25722.90),(58,'bromsskivor','vindrute lim',2887.01,7960.74),(59,'karosserlim','bromsljus',20318.93,3723.60),(60,'halvljus led lampa','kamaxel givare',2710.87,10625.82),(61,'expansionsventil','frihjulsväxel startmotor',15395.52,24558.93),(62,'tätmassa för flänsar','oljefilter',21042.33,847.32),(63,'sensor pedalrörelse','styrstag',501.53,27900.36),(64,'skivbromsbelägg','oljefilter',10989.83,9105.37),(65,'centrallås','vindrute lim',77.08,28439.51),(66,'tändfördelare','styrpackning',3787.37,20424.70),(67,'urtrampningslager','dimmljus',5700.40,4030.29),(68,'batteri','fjädrar till dämpare',9933.24,29914.07),(69,'skivbromsbelägg','reglerventil kompressor',28291.32,11409.05),(70,'förångare','krängningshämmare',26054.99,14288.74),(71,'bilshampoo','fläkt klimatanläggning',2124.75,19172.24),(72,'termokontakt','reparationssats styrled',10032.60,5682.60),(73,'styrväxeldamask','inställning säte',19693.46,21481.86),(74,'ställmotor','rostlösare',15061.77,1238.49),(75,'plastlim','krängningshämmarbussning',28642.96,16984.18),(76,'tempgivare','drivaxel',15111.09,9554.55),(77,'hjullager','sekundärluftfilter',28273.62,15456.54),(78,'kardanaxelbult','avgassystem',16950.26,4704.00);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs`
--

DROP TABLE IF EXISTS `staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staffs` (
  `id_staff` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `job_title` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `store` varchar(45) NOT NULL,
  `reports_to` int NOT NULL,
  PRIMARY KEY (`id_staff`),
  KEY `fk_staffs_staffs1_idx` (`reports_to`),
  CONSTRAINT `fk_staffs_staffs1` FOREIGN KEY (`reports_to`) REFERENCES `staffs` (`id_staff`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs`
--

LOCK TABLES `staffs` WRITE;
/*!40000 ALTER TABLE `staffs` DISABLE KEYS */;
INSERT INTO `staffs` VALUES (1,'Kalle','Viberg','Motor Salesman','+4676885210','Göteborg',1),(2,'Challe','Berg','Motor Salesman','+4676885210','Göteborg',1),(3,'Anneli','Bergsson','Motor Salesman','+4676885210','Göteborg',1),(4,'Elisabeth','Eriksson','salesperson','+46-715-554-1','CPS Stockholm',2),(5,'Robin','Ek','sales manager','+46-775-555-3','CPS Linköping',4),(6,'Rune','Strömberg','customer manager relations','+46-705-554-8','CPS Örebro',5),(7,'Oscar','Jansson','orderhandler','+46-755-550-4','CPS Örebro',3),(8,'Margareta','Bergström','ceo','+46-765-555-1','CPS Malmö',4),(9,'Kurt','Bergman','account manager','+46-725-554-0','CPS Malmö',2),(10,'Ali','Sandberg','orderhandler','+46-725-553-1','CPS Skövde',1),(11,'Arne','Mårtensson','account manager','+46-765-554-6','CPS Örebro',4),(12,'Irene','Berg','sales manager','+46-725-554-7','CPS Stockholm',6),(13,'Kristina','Lundström','salesperson','+46-715-550-8','CPS Örebro',2),(14,'Karolina','Jonsson','account manager','+46-775-550-3','CPS Linköping',13),(15,'Lars','Isaksson','account manager','+46-705-555-2','CPS Linköping',14),(16,'Rune','Claesson','orderhandler','+46-795-552-9','CPS Örebro',11),(17,'Maria','Jansson','orderhandler','+46-735-558-8','CPS Göteborg',11),(18,'Karin','Svensson','sales manager','+46-705-556-2','CPS Norrköping',4),(19,'Fredrik','Lundgren','account manager','+46-735-559-4','CPS Norrköping',8),(20,'Kent','Mohamed','ceo','+46-745-552-7','CPS Stockholm',1),(21,'Rolf','Lindström','customer manager relations','+46-745-558-2','CPS Göteborg',7),(22,'Alexander','Gunnarsson','ceo','+46-795-555-1','CPS Linköping',21),(23,'Erika','Engström','ceo','+46-775-551-0','CPS Göteborg',2),(24,'Sofia','Hassan','sales manager','+46-785-552-4','CPS Skövde',3),(25,'Bo','Lund','salesperson','+46-705-556-2','CPS Malmö',12),(26,'Axel','Wallin','account manager','+46-745-552-7','CPS Örebro',8),(27,'Jonathan','Forsberg','salesperson','+46-775-555-9','CPS Norrköping',23),(28,'Maria','Johansson','account manager','+46-785-551-9','CPS Stockholm',18),(29,'Adam','Ahmed','ceo','+46-705-556-2','CPS Stockholm',26),(30,'Karl','Fransson','sales manager','+46-795-558-5','CPS Göteborg',4),(31,'Alexandra','Mohamed','sales manager','+46-755-558-1','CPS Skövde',30),(32,'Ingrid','Bergström','salesperson','+46-795-557-1','CPS Linköping',7),(33,'Ulla','Larsson','customer manager relations','+46-775-553-5','CPS Göteborg',22),(34,'Ulf','Björklund','customer manager relations','+46-745-557-3','CPS Göteborg',27),(35,'Susanne','Sandberg','account manager','+46-775-555-3','CPS Linköping',11),(36,'Lisa','Hedlund','salesperson','+46-755-550-9','CPS Örebro',27),(37,'Muhammed','Dahl','orderhandler','+46-715-559-2','CPS Stockholm',30),(38,'Amanda','Ström','customer manager relations','+46-715-556-2','CPS Skövde',24),(39,'Viola','Andersson','ceo','+46-725-554-2','CPS Linköping',15),(40,'Muhammed','Hansson','salesperson','+46-785-553-2','CPS Skövde',18),(41,'John','Bengtsson','customer manager relations','+46-785-557-2','CPS Skövde',19),(42,'Susanne','Jakobsson','salesperson','+46-755-553-9','CPS Stockholm',8),(43,'Alexander','Håkansson','orderhandler','+46-765-551-6','CPS Örebro',30),(44,'Filip','Blomqvist','salesperson','+46-745-557-3','CPS Stockholm',10),(45,'Kjell','Nilsson','sales manager','+46-795-555-1','CPS Göteborg',40),(46,'Magnus','Johansson','account manager','+46-785-559-5','CPS Linköping',14),(47,'Shariar','Larsson','customer manager relations','+46-775-555-9','CPS Skövde',25),(48,'Leila','Löfgren','orderhandler','+46-765-551-6','CPS Linköping',26),(49,'Gunnar','Wallin','ceo','+46-755-551-0','CPS Örebro',7),(50,'Josefin','Bergman','ceo','+46-755-550-4','CPS Örebro',11),(51,'Rolf','Fransson','orderhandler','+46-775-555-3','CPS Stockholm',46),(52,'Anton','Lundgren','customer manager relations','+46-715-552-2','CPS Göteborg',4),(53,'Lisa','Eklund','ceo','+46-725-554-0','CPS Norrköping',18),(54,'Therese','Nordin','orderhandler','+46-755-551-0','CPS Skövde',52),(55,'Agnes','Holmgren','ceo','+46-795-552-0','CPS Stockholm',2),(56,'Signe','Hassan','sales manager','+46-725-559-7','CPS Örebro',14),(57,'Adnan','Gunnarsson','customer manager relations','+46-705-551-5','CPS Linköping',5),(58,'Linus','Nordin','customer manager relations','+46-715-552-2','CPS Örebro',29),(59,'Arne','Persson','account manager','+46-715-556-9','CPS Göteborg',32),(60,'Therese','Arvidsson','account manager','+46-795-551-7','CPS Linköping',30),(61,'Salim','Blomqvist','orderhandler','+46-795-552-9','CPS Skövde',47),(62,'Åsa','Dahl','ceo','+46-715-556-2','CPS Malmö',40),(63,'Olle','Hansson','sales manager','+46-715-550-8','CPS Stockholm',28),(64,'Yasmin','Lindberg','sales manager','+46-725-558-0','CPS Örebro',31),(65,'Matilda','Lindqvist','customer manager relations','+46-755-555-6','CPS Stockholm',33),(66,'Charlotta','Persson','sales manager','+46-785-558-4','CPS Norrköping',28),(67,'Frida','Andreasson','customer manager relations','+46-715-554-7','CPS Skövde',54),(68,'Shariar','Jonsson','salesperson','+46-775-559-8','CPS Linköping',23),(69,'Olivia','Åberg','sales manager','+46-795-552-9','CPS Linköping',63),(70,'Sebastian','Holmqvist','sales manager','+46-745-553-8','CPS Örebro',5),(71,'Tommy','Olsson','sales manager','+46-785-550-0','CPS Göteborg',53),(72,'Gunnel','Blomqvist','ceo','+46-795-552-9','CPS Linköping',44),(73,'Ebba','Jönsson','ceo','+46-745-554-1','CPS Göteborg',12),(74,'Erik','Åberg','ceo','+46-795-551-3','CPS Stockholm',68),(75,'Emil','Wallin','sales manager','+46-775-555-9','CPS Stockholm',29),(76,'Tommy','Mohamed','salesperson','+46-745-552-7','CPS Skövde',48),(77,'Gunnar','Blom','customer manager relations','+46-725-559-7','CPS Linköping',51),(78,'Jan','Sjögren','orderhandler','+46-775-559-8','CPS Stockholm',48);
/*!40000 ALTER TABLE `staffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs_has_cpsorders`
--

DROP TABLE IF EXISTS `staffs_has_cpsorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staffs_has_cpsorders` (
  `staffs_id_staff` int NOT NULL,
  `cps_orders_internal_order_no` int NOT NULL,
  PRIMARY KEY (`staffs_id_staff`,`cps_orders_internal_order_no`),
  KEY `fk_staffs_has_cps_orders_cps_orders1_idx` (`cps_orders_internal_order_no`),
  KEY `fk_staffs_has_cps_orders_staffs1_idx` (`staffs_id_staff`),
  CONSTRAINT `fk_staffs_has_cps_orders_cps_orders1` FOREIGN KEY (`cps_orders_internal_order_no`) REFERENCES `cps_orders` (`internal_order_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_staffs_has_cps_orders_staffs1` FOREIGN KEY (`staffs_id_staff`) REFERENCES `staffs` (`id_staff`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs_has_cpsorders`
--

LOCK TABLES `staffs_has_cpsorders` WRITE;
/*!40000 ALTER TABLE `staffs_has_cpsorders` DISABLE KEYS */;
INSERT INTO `staffs_has_cpsorders` VALUES (1,1),(3,1),(4,1),(5,1),(1,2),(2,2),(3,2),(5,2),(1,3),(3,3),(4,3),(5,3),(2,4),(4,4),(2,5),(5,5),(2,6),(2,7),(3,7),(4,8),(5,8),(2,9),(3,9),(4,9),(5,9),(6,9),(5,10),(1,11),(6,12),(3,14),(4,14),(1,15),(2,15),(4,15),(2,16),(3,16),(2,17),(3,17),(5,17),(2,18),(3,18),(5,18),(1,19),(4,19),(6,19),(4,22),(2,24),(3,24),(1,25),(4,25),(1,27),(1,29),(3,29),(5,29),(3,30),(1,33),(4,33),(3,34),(2,36),(1,37),(2,37),(4,37),(1,38),(4,38),(1,39),(4,41),(4,43),(2,44),(2,47),(1,54),(1,56),(1,59),(5,60),(2,61),(3,62),(1,63),(3,71);
/*!40000 ALTER TABLE `staffs_has_cpsorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs_has_customers`
--

DROP TABLE IF EXISTS `staffs_has_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staffs_has_customers` (
  `staffs_id_staff` int NOT NULL,
  `customers_id_customers` int NOT NULL,
  PRIMARY KEY (`staffs_id_staff`,`customers_id_customers`),
  KEY `fk_staffs_has_customers_customers1_idx` (`customers_id_customers`),
  KEY `fk_staffs_has_customers_staffs1_idx` (`staffs_id_staff`),
  CONSTRAINT `fk_staffs_has_customers_customers1` FOREIGN KEY (`customers_id_customers`) REFERENCES `customers` (`id_customers`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_staffs_has_customers_staffs1` FOREIGN KEY (`staffs_id_staff`) REFERENCES `staffs` (`id_staff`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs_has_customers`
--

LOCK TABLES `staffs_has_customers` WRITE;
/*!40000 ALTER TABLE `staffs_has_customers` DISABLE KEYS */;
INSERT INTO `staffs_has_customers` VALUES (1,1),(2,1),(3,1),(4,1),(2,2),(6,2),(3,3),(6,3),(4,4),(5,4),(6,4),(1,5),(2,5),(6,5),(1,6),(2,6),(3,6),(4,6),(6,6),(1,7),(3,7),(1,8),(3,8),(2,9),(5,9),(5,10),(6,10),(1,11),(1,12),(3,12),(4,12),(6,13),(4,14),(5,14),(6,14),(1,15),(4,15),(1,16),(2,17),(4,18),(5,18),(3,19),(4,19),(5,19),(6,19),(6,21),(6,22),(5,23),(6,23),(6,25),(3,26),(4,26),(5,27),(3,29),(2,30),(5,30),(6,32),(3,33),(6,35),(1,37),(5,37),(5,38),(5,40),(1,42),(3,42),(6,43),(6,45),(6,48),(4,53),(6,53),(4,55),(5,57),(3,61),(2,62),(4,62),(6,63);
/*!40000 ALTER TABLE `staffs_has_customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage` (
  `storage_id` int NOT NULL AUTO_INCREMENT,
  `storage_name` varchar(150) NOT NULL,
  `storage_quantity` int NOT NULL,
  `storage_city` varchar(100) NOT NULL,
  PRIMARY KEY (`storage_id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (1,'CPS Main Storage',2000,'Göteborg'),(2,'CPS Main Storage',2000,'Göteborg'),(3,'CPS Main Storage',2000,'Göteborg'),(4,'lager malmö',5,'Kungsängen'),(5,'lager malmö',5,'Mullsjö'),(6,'lager stockholm',12,'Forsvik'),(7,'lager stockholm',64,'Filipstad'),(8,'lager malmö',64,'Floby'),(9,'lager stockholm',43,'Villie'),(10,'lager malmö',2,'Kalmar'),(11,'lager malmö',2,'Bjuv'),(12,'lager göteborg',5,'Borlänge'),(13,'lager malmö',5,'Oxelösund'),(14,'lager malmö',12,'Kiruna'),(15,'lager stockholm',64,'Vilhelmina'),(16,'lager göteborg',64,'Vimmerby'),(17,'lager stockholm',12,'Katrineholm'),(18,'lager malmö',43,'Nykvarn'),(19,'lager malmö',2,'Furusjö'),(20,'lager göteborg',12,'Nykvarn'),(21,'lager stockholm',43,'Kungsbacka'),(22,'lager göteborg',5,'Falun'),(23,'lager stockholm',12,'Hillared'),(24,'lager stockholm',64,'Dalstorp'),(25,'lager stockholm',5,'Västerhaninge'),(26,'lager stockholm',12,'Mölnlycke'),(27,'lager malmö',64,'Fagersanna'),(28,'lager malmö',43,'Norrtälje'),(29,'lager stockholm',12,'Kil'),(30,'lager göteborg',12,'Skinnskatteberg'),(31,'lager malmö',2,'Furusjö'),(32,'lager stockholm',64,'Tumba'),(33,'lager malmö',43,'Arboga'),(34,'lager malmö',12,'Fagersanna'),(35,'lager göteborg',43,'Åtvidaberg'),(36,'lager stockholm',64,'Lysekil'),(37,'lager malmö',12,'Linköping'),(38,'lager malmö',2,'Karlskoga'),(39,'lager malmö',2,'Åsarp'),(40,'lager göteborg',2,'Säffle'),(41,'lager malmö',2,'Älmhult'),(42,'lager göteborg',64,'Skara'),(43,'lager göteborg',43,'Filsbäck'),(44,'lager stockholm',2,'Enköping'),(45,'lager malmö',2,'Tidaholm'),(46,'lager malmö',64,'Märsta'),(47,'lager stockholm',12,'Åstorp'),(48,'lager göteborg',12,'Nedre Gärdsjö'),(49,'lager malmö',43,'Norrtälje'),(50,'lager göteborg',64,'Landskrona'),(51,'lager göteborg',12,'Norrköping'),(52,'lager stockholm',12,'Gävle'),(53,'lager malmö',12,'Varberg'),(54,'lager stockholm',12,'Tibro'),(55,'lager stockholm',43,'Skövde'),(56,'lager stockholm',64,'Strömsund'),(57,'lager stockholm',12,'Landskrona'),(58,'lager malmö',5,'Gudhem'),(59,'lager malmö',5,'Tierp'),(60,'lager stockholm',43,'Åstorp'),(61,'lager göteborg',5,'Herrljunga'),(62,'lager göteborg',64,'Mariestad'),(63,'lager malmö',64,'Luleå'),(64,'lager malmö',43,'Kebal'),(65,'lager stockholm',12,'Gullspång'),(66,'lager göteborg',5,'Laxå'),(67,'lager göteborg',43,'Strömstad'),(68,'lager göteborg',43,'Osby'),(69,'lager göteborg',5,'Sandhem'),(70,'lager göteborg',2,'Dalstorp'),(71,'lager malmö',12,'Oxelösund'),(72,'lager göteborg',64,'Mullsjö'),(73,'lager stockholm',2,'Ulricehamn'),(74,'lager stockholm',43,'Norrtälje'),(75,'lager göteborg',5,'Helsingborg'),(76,'lager stockholm',12,'Krokom'),(77,'lager göteborg',5,'Mellerud'),(78,'lager göteborg',43,'Sandhult');
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage_has_products`
--

DROP TABLE IF EXISTS `storage_has_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage_has_products` (
  `storage_storage_id` int NOT NULL,
  `products_product_id` int NOT NULL,
  PRIMARY KEY (`storage_storage_id`,`products_product_id`),
  KEY `fk_storage_has_products_products1_idx` (`products_product_id`),
  KEY `fk_storage_has_products_storage1_idx` (`storage_storage_id`),
  CONSTRAINT `fk_storage_has_products_products1` FOREIGN KEY (`products_product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_storage_has_products_storage1` FOREIGN KEY (`storage_storage_id`) REFERENCES `storage` (`storage_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage_has_products`
--

LOCK TABLES `storage_has_products` WRITE;
/*!40000 ALTER TABLE `storage_has_products` DISABLE KEYS */;
INSERT INTO `storage_has_products` VALUES (1,1),(10,1),(12,1),(14,1),(15,1),(36,1),(2,2),(4,2),(5,2),(11,2),(18,2),(23,2),(3,3),(10,3),(13,3),(19,3),(21,3),(1,4),(4,4),(3,5),(8,5),(17,6),(35,6),(7,7),(2,8),(19,8),(22,8),(54,8),(8,9),(29,10),(34,10),(4,11),(27,11),(46,11),(2,12),(10,12),(34,12),(10,13),(22,13),(11,14),(22,14),(3,15),(10,15),(24,15),(40,15),(23,16),(13,18),(17,19),(15,20),(36,20),(28,21),(1,22),(5,23),(36,23),(24,24),(52,24),(55,25),(8,29),(3,31),(34,31),(35,31),(44,32),(14,33),(50,33),(34,35),(31,37),(45,42),(6,47),(15,48),(49,51),(44,53),(65,53),(71,53),(14,57),(45,58),(59,59),(29,68),(68,69);
/*!40000 ALTER TABLE `storage_has_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplier_id` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(45) NOT NULL,
  `supplier_adress1` varchar(45) NOT NULL,
  `supplier_adress2` varchar(45) DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `zip_code` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  `contact_person` varchar(100) DEFAULT NULL,
  `phone_number` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Egons Bilfirma AB','Bergsvägen 17A','','Ubbhult','18380','Sweden','Egon Johnsson','+4607528125','egon.gmail.com'),(2,'Erlands Bilar AB','Skogsvägen 54 B','','Ubbhult','18380','Sweden','Erland Johnsson','+4607528125','erland.gmail.com'),(3,'Erlands Bilar AB','Skogsvägen 54 B','','Ubbhult','18380','Sweden','Erland Johnsson','+4607528125','erland.gmail.com'),(4,'johans verkstad','Handslagarevägen','','Örebro','96931','Sweden','Gunilla_Lundqvist','+46-755-557-4','Gunilla_Lundqvist@live.se'),(5,'jula','Ryttargatan','','Vansbro','62209','Sweden','Katarina_Nordström','+46-715-558-3','Katarina_Nordström@hotmail.com'),(6,'biltema','Molngatan','','Emmaboda','62010','Sweden','Oskar_Andreasson','+46-755-555-6','Oskar_Andreasson@gmail.com'),(7,'jula','Västerhansjön','','Tingsryd','94796','Sweden','Alexander_Mattsson','+46-715-553-1','Alexander_Mattsson@outlook.com'),(8,'johans verkstad','Billsbro Karlslund','','Strömsund','05644','Sweden','Johannes_Olofsson','+46-775-557-6','Johannes_Olofsson@live.se'),(9,'jula','Nöjesgatan','','Sandhult','34966','Sweden','Emelie_Eklund','+46-755-557-4','Emelie_Eklund@live.se'),(10,'jula','Algatan','','Älgarås','94796','Sweden','Julia_Axelsson','+46-795-557-3','Julia_Axelsson@yahoo.com'),(11,'biltema','Åbyhöjden','','Kävlinge','01447','Sweden','Jonas_Lundgren','+46-735-550-8','Jonas_Lundgren@hotmail.com'),(12,'johans verkstad','Snårvägen','','Pajala','87982','Sweden','Camilla_Hansson','+46-705-551-5','Camilla_Hansson@live.se'),(13,'jula','Pärongatan','','Stockholm','00315','Sweden','Agnes_Berg','+46-705-556-7','Agnes_Berg@gmail.com'),(14,'jula','Hönefossvägen','','Sätila','09100','Sweden','Fatima_Månsson','+46-785-558-4','Fatima_Månsson@live.se'),(15,'biltema','Skogsstigen','','Huddinge','88039','Sweden','Mats_Arvidsson','+46-775-553-5','Mats_Arvidsson@hotmail.com'),(16,'biltema','Skogsstigen','','Mörbylånga','07609','Sweden','Peter_Mårtensson','+46-755-557-4','Peter_Mårtensson@yahoo.com'),(17,'jula','Håstads Bygata','','Skurup','34966','Sweden','Göran_Holmgren','+46-725-558-3','Göran_Holmgren@gmail.com'),(18,'jula','Idvägen','','Vartofta','55312','Sweden','Magnus_Mohamed','+46-785-559-6','Magnus_Mohamed@live.se'),(19,'biltema','Handslagarevägen','','Frändefors','61281','Sweden','Fredrik_Engström','+46-705-556-2','Fredrik_Engström@gmail.com'),(20,'jula','Barkgatan','','Sandhult','70303','Sweden','Agneta_Nordström','+46-775-558-3','Agneta_Nordström@hotmail.com'),(21,'jula','Backsippestigen','','Bålsta','00315','Sweden','Marianne_Månsson','+46-705-554-8','Marianne_Månsson@yahoo.com'),(22,'jula','Backsippestigen','','Bålsta','26294','Sweden','Michel_Sjöberg','+46-745-558-2','Michel_Sjöberg@hotmail.com'),(23,'jula','Korsträskvägen','','Stockholm','26294','Sweden','Eric_Lindgren','+46-795-557-1','Eric_Lindgren@outlook.com'),(24,'johans verkstad','Bergsgatan','','Visby','90201','Sweden','Ingegerd_Lund','+46-785-558-4','Ingegerd_Lund@gmail.com'),(25,'biltema','Snårgatan','','Götene','50403','Sweden','Anette_Sundberg','+46-705-555-2','Anette_Sundberg@yahoo.com'),(26,'biltema','Hedehusvägen','','Västerås','16975','Sweden','Ella_Holmberg','+46-725-558-3','Ella_Holmberg@gmail.com'),(27,'jula','Grötvägen','','Trosa','10302','Sweden','Peter_Andersson','+46-765-551-6','Peter_Andersson@gmail.com'),(28,'jula','Pärlgräsgatan','','Pajala','34966','Sweden','John_Karlsson','+46-785-554-3','John_Karlsson@outlook.com'),(29,'jula','Apelsinvägen','','Nynäshamn','06651','Sweden','Rolf_Jansson','+46-735-551-1','Rolf_Jansson@yahoo.com'),(30,'jula','Algatan','','Örnsköldsvik','39227','Sweden','Gun_Ali','+46-725-554-7','Gun_Ali@yahoo.com'),(31,'jula','Apelsingatan','','Anderslöv','68883','Sweden','Marcus_Pettersson','+46-725-553-1','Marcus_Pettersson@outlook.com'),(32,'johans verkstad','Ångpannevägen','','Övertorneå','10336','Sweden','Hans_Magnusson','+46-785-550-0','Hans_Magnusson@outlook.com'),(33,'jula','Grötvägen','','Hedemora','72774','Sweden','Annika_Wikström','+46-715-552-2','Annika_Wikström@gmail.com'),(34,'jula','Åsavägen','','Enköping','57319','Sweden','Olov_Lundberg','+46-785-559-6','Olov_Lundberg@outlook.com'),(35,'johans verkstad','Apelsinvägen','','Storfors','04557','Sweden','Rikard_Björklund','+46-775-555-0','Rikard_Björklund@live.se'),(36,'johans verkstad','Pärongatan','','Bräcke','64799','Sweden','Lena_Holmgren','+46-755-555-6','Lena_Holmgren@hotmail.com'),(37,'jula','Sandhällavägen','','Hässleholm','89490','Sweden','Henry_Pettersson','+46-725-556-5','Henry_Pettersson@live.se'),(38,'johans verkstad','Pål Skräddares Väg','','Åsele','88369','Sweden','Anneli_Abrahamsson','+46-775-553-5','Anneli_Abrahamsson@outlook.com'),(39,'jula','Ryttarvägen','','Klagstorp','34833','Sweden','Kenneth_Hansen','+46-795-552-9','Kenneth_Hansen@hotmail.com'),(40,'biltema','Pål Skräddares Väg','','Arvika','62209','Sweden','Åsa_Olsson','+46-745-557-3','Åsa_Olsson@outlook.com'),(41,'jula','Pärlgräsvägen','','Emmaboda','41534','Sweden','Carl_Jansson','+46-745-555-3','Carl_Jansson@outlook.com'),(42,'johans verkstad','Stackekärrsgatan','','Kiruna','04821','Sweden','Lina_Jakobsson','+46-775-555-0','Lina_Jakobsson@live.se'),(43,'biltema','Åbyhöjden','','Lerdala','16975','Sweden','Oliver_Nilsson','+46-785-554-8','Oliver_Nilsson@hotmail.com'),(44,'johans verkstad','Brunnevägen','','Göteborg','10302','Sweden','John_Lundgren','+46-715-556-2','John_Lundgren@outlook.com'),(45,'johans verkstad','Wesslunds Gränd','','Berghem','14565','Sweden','Astrid_Wikström','+46-745-555-3','Astrid_Wikström@yahoo.com'),(46,'biltema','Oskarsvägen','','Älvdalen','24540','Sweden','Charlotta_Wikström','+46-795-551-3','Charlotta_Wikström@outlook.com'),(47,'johans verkstad','Gitarrvägen','','Åsele','05682','Sweden','Pia_Mohamed','+46-775-558-3','Pia_Mohamed@outlook.com'),(48,'jula','Mellangården','','Svenstavik','36965','Sweden','Ulla_Claesson','+46-785-559-6','Ulla_Claesson@hotmail.com'),(49,'johans verkstad','Nöjesgatan','','Valdemarsvik','84232','Sweden','Gunnel_Nordin','+46-795-558-3','Gunnel_Nordin@yahoo.com'),(50,'johans verkstad','Mållångsbogatan','','Emmaboda','02177','Sweden','Andreas_Öberg','+46-775-557-6','Andreas_Öberg@live.se'),(51,'biltema','Vansövägen','','Hallstahammar','14565','Sweden','Adam_Isaksson','+46-705-556-2','Adam_Isaksson@yahoo.com'),(52,'biltema','Trumgatan','','Uddevalla','36676','Sweden','Camilla_Lindqvist','+46-705-556-2','Camilla_Lindqvist@outlook.com'),(53,'johans verkstad','Trädgårdsgatan','','Ulricehamn','80577','Sweden','Michel_Axelsson','+46-745-555-3','Michel_Axelsson@outlook.com'),(54,'biltema','Mållångsbogatan','','Huddinge','28863','Sweden','Lisa_Öberg','+46-765-555-1','Lisa_Öberg@hotmail.com'),(55,'jula','Korsträskvägen','','Ludvika','15635','Sweden','Agneta_Abrahamsson','+46-785-558-9','Agneta_Abrahamsson@outlook.com'),(56,'johans verkstad','Esplanadgatan','','Gävle','30789','Sweden','Stig_Månsson','+46-795-554-4','Stig_Månsson@live.se'),(57,'johans verkstad','Jordgubbsgatan','','Gnesta','01068','Sweden','Ali_Björk','+46-725-553-1','Ali_Björk@gmail.com'),(58,'johans verkstad','Klövervägen','','Skutskär','08595','Sweden','Elias_Söderberg','+46-775-553-5','Elias_Söderberg@live.se'),(59,'johans verkstad','Ångpannegatan','','Huddinge','50814','Sweden','Christian_Lundström','+46-795-554-4','Christian_Lundström@outlook.com'),(60,'jula','Mellangården','','Linköping','50814','Sweden','Jonas_Axelsson','+46-735-558-8','Jonas_Axelsson@gmail.com'),(61,'johans verkstad','Ångpannevägen','','Laholm','80577','Sweden','Malin_Ahmed','+46-725-558-0','Malin_Ahmed@live.se'),(62,'johans verkstad','Ellenösvägen','','Växjö','36903','Sweden','Rikard_Karlsson','+46-775-556-2','Rikard_Karlsson@hotmail.com'),(63,'biltema','Snårgatan','','Svenljunga','00366','Sweden','Inga_Gunnarsson','+46-745-558-2','Inga_Gunnarsson@gmail.com'),(64,'jula','Apelsingatan','','Gudhem','30566','Sweden','Rikard_Håkansson','+46-775-556-2','Rikard_Håkansson@gmail.com'),(65,'johans verkstad','Jordgubbsvägen','','Staffanstorp','30789','Sweden','Hans_Åberg','+46-795-552-9','Hans_Åberg@yahoo.com'),(66,'johans verkstad','Snårvägen','','Sunne','56683','Sweden','Eric_Ek','+46-755-556-6','Eric_Ek@gmail.com'),(67,'johans verkstad','Pikogatan','','Gällivare','16975','Sweden','Carina_Nilsson','+46-725-556-5','Carina_Nilsson@live.se'),(68,'biltema','Dalhemsvägen','','Järpen','36676','Sweden','Julia_Sandberg','+46-715-550-8','Julia_Sandberg@gmail.com'),(69,'johans verkstad','Äppelgatan','','Smedjebacken','40272','Sweden','Cecilia_Nordström','+46-705-551-5','Cecilia_Nordström@outlook.com'),(70,'biltema','Bergsgatan','','Surahammar','34833','Sweden','Charlotta_Andersson','+46-725-556-4','Charlotta_Andersson@gmail.com'),(71,'johans verkstad','Storegårdsgatan','','Knivsta','44502','Sweden','Shariar_Jakobsson','+46-715-553-1','Shariar_Jakobsson@gmail.com'),(72,'johans verkstad','Tistelgatan','','Forshaga','02907','Sweden','Kent_Lundin','+46-725-556-6','Kent_Lundin@hotmail.com'),(73,'biltema','Nöjesgatan','','Trollhättan','56683','Sweden','Camilla_Eriksson','+46-735-559-4','Camilla_Eriksson@yahoo.com'),(74,'biltema','Esplanadgatan','','Djursholm','39227','Sweden','Hanna_Sandström','+46-795-557-1','Hanna_Sandström@gmail.com'),(75,'biltema','Jordgubbsgatan','','Ystad','51258','Sweden','Cecilia_Sundberg','+46-715-556-9','Cecilia_Sundberg@gmail.com'),(76,'biltema','Äppelvägen','','Frändefors','22876','Sweden','Leif_Lindgren','+46-755-550-9','Leif_Lindgren@yahoo.com'),(77,'johans verkstad','Mellangården','','Lycksele','01183','Sweden','Fatima_Mårtensson','+46-795-558-3','Fatima_Mårtensson@yahoo.com'),(78,'jula','Tistelgatan','','Värnamo','34966','Sweden','Emilia_Ali','+46-795-557-1','Emilia_Ali@live.se');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers_has_cps_orders`
--

DROP TABLE IF EXISTS `suppliers_has_cps_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers_has_cps_orders` (
  `suppliers_supplier_id` int NOT NULL,
  `cps_orders_internal_order_no` int NOT NULL,
  PRIMARY KEY (`suppliers_supplier_id`,`cps_orders_internal_order_no`),
  KEY `fk_suppliers_has_cps_orders_cps_orders1_idx` (`cps_orders_internal_order_no`),
  KEY `fk_suppliers_has_cps_orders_suppliers1_idx` (`suppliers_supplier_id`),
  CONSTRAINT `fk_suppliers_has_cps_orders_cps_orders1` FOREIGN KEY (`cps_orders_internal_order_no`) REFERENCES `cps_orders` (`internal_order_no`) ON UPDATE CASCADE,
  CONSTRAINT `fk_suppliers_has_cps_orders_suppliers1` FOREIGN KEY (`suppliers_supplier_id`) REFERENCES `suppliers` (`supplier_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers_has_cps_orders`
--

LOCK TABLES `suppliers_has_cps_orders` WRITE;
/*!40000 ALTER TABLE `suppliers_has_cps_orders` DISABLE KEYS */;
INSERT INTO `suppliers_has_cps_orders` VALUES (1,1),(2,1),(4,1),(9,1),(11,1),(19,1),(2,2),(4,2),(3,3),(5,3),(48,3),(5,4),(8,4),(15,4),(23,4),(2,5),(3,5),(5,5),(8,5),(38,5),(3,6),(7,6),(9,7),(18,7),(53,7),(6,8),(3,9),(6,9),(15,9),(12,11),(28,13),(32,13),(9,14),(26,14),(52,14),(1,15),(6,15),(28,15),(12,16),(13,17),(17,17),(30,17),(34,17),(2,19),(13,20),(20,20),(22,20),(28,20),(29,20),(31,20),(2,21),(6,21),(8,23),(23,23),(42,24),(19,25),(1,26),(5,28),(43,32),(36,34),(30,37),(16,38),(7,39),(15,41),(23,41),(58,41),(1,42),(60,43),(40,44),(69,45),(13,46),(1,48),(49,50),(25,55),(62,56),(41,58),(49,61),(12,63);
/*!40000 ALTER TABLE `suppliers_has_cps_orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-15 23:18:08
