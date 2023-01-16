-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: 192.168.0.20    Database: a_system
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `m_numbering`
--

DROP TABLE IF EXISTS `m_numbering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `m_numbering` (
  `id` varchar(45) NOT NULL,
  `no` int NOT NULL DEFAULT '1',
  `name` varchar(45) NOT NULL,
  `biko` varchar(200) DEFAULT NULL,
  `toroku` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `kosin` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `m_numbering`
--

LOCK TABLES `m_numbering` WRITE;
/*!40000 ALTER TABLE `m_numbering` DISABLE KEYS */;
INSERT INTO `m_numbering` VALUES ('1',1,'1','1','2022-12-19 08:21:34','2022-12-19 08:21:34'),('2021121230014',1,'ポテチ','1','2022-12-19 08:24:48','2022-12-19 08:24:48'),('21',1,'213','12','2022-12-18 22:53:56','2022-12-18 22:53:56'),('a',1,'bb','vvc','2022-12-18 22:30:24','2022-12-18 22:30:24'),('aaaa',1,'aaa','aa','2022-12-18 22:46:15','2022-12-18 22:46:15'),('aaad',1,'fdsa','','2022-12-18 23:17:18','2022-12-18 23:17:18'),('aadsa',1,'fds','s','2022-12-18 23:15:44','2022-12-18 23:15:44'),('ad',1,'fda','','2022-12-19 17:10:43','2022-12-19 17:10:43'),('asdfds',1,'adsffd','','2022-12-19 17:12:02','2022-12-19 17:12:02'),('asdfdsa',1,'fds','','2022-12-19 08:28:31','2022-12-19 08:28:31'),('asdffddsa',1,'asdfdsaf','asdf','2022-12-19 17:18:24','2022-12-19 17:18:24'),('asdg',1,'d','','2022-12-19 17:11:09','2022-12-19 17:11:09'),('dd',1,'sa','as','2022-12-18 23:00:43','2022-12-18 23:00:43'),('dfsa',1,'fasdfd','asdfdaf','2022-12-19 17:57:49','2022-12-19 17:57:49'),('dfsad',1,'fsdf','asd','2022-12-19 17:13:06','2022-12-19 17:13:06'),('ds',1,'df','','2022-12-18 23:17:44','2022-12-18 23:17:44'),('ee',1,'dd','','2022-12-18 22:57:19','2022-12-18 22:57:19'),('re',1,'ef','','2022-12-19 08:26:01','2022-12-19 08:26:01'),('sd',1,'fっds','','2022-12-20 14:44:14','2022-12-20 14:44:14'),('test',1,'aa','','2022-12-18 22:42:26','2022-12-18 22:42:26'),('tre',1,'qer','asd','2022-12-18 23:16:06','2022-12-18 23:16:06');
/*!40000 ALTER TABLE `m_numbering` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-16 22:28:56
