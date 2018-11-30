-- MySQL dump 10.13  Distrib 8.0.12, for osx10.13 (x86_64)
--
-- Host: localhost    Database: DeviceTracker
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Device`
--
DROP TABLE IF EXISTS `Device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Device` (
  `device_id` int(11) NOT NULL AUTO_INCREMENT,
  `device_type` varchar(30) DEFAULT NULL,
  `make` varchar(30) DEFAULT NULL,
  `model` varchar(30) DEFAULT NULL,
  `serial_no` varchar(30) DEFAULT NULL,
  `warranty_exp` date DEFAULT NULL,
  PRIMARY KEY (`device_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Device`
--

LOCK TABLES `Device` WRITE;
/*!40000 ALTER TABLE `Device` DISABLE KEYS */;
INSERT INTO `Device` VALUES (1,'Laptop','Apple','Macbook','10010','2018-12-31'),(2,'Mouse','Apple','MacMouse','10020','2018-12-31'),(3,'Earpods','Apple','Airpods','10030','2018-12-31'),(4,'Laptop','Apple','Macbook','10040','2020-01-01'), (5,'Printer','HP','LaserJet','1111','2020-02-02');
/*!40000 ALTER TABLE `Device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Employee` (
  `employ_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`employ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (123,'Abc','1970-01-01','2018-12-31');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issued_to`
--

DROP TABLE IF EXISTS `issued_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `issued_to` (
  `employ_id` int(11) DEFAULT NULL,
  `device_id` int(11) DEFAULT NULL,
  `issued_date` date DEFAULT NULL,
  `returned_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issued_to`
--

LOCK TABLES `issued_to` WRITE;
/*!40000 ALTER TABLE `issued_to` DISABLE KEYS */;
INSERT INTO `issued_to` VALUES (123,1,'1970-01-01','2018-12-31'),(123,2,'1970-01-01',NULL),(123,3,'1990-01-01',NULL);
/*!40000 ALTER TABLE `issued_to` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-24  2:14:34
