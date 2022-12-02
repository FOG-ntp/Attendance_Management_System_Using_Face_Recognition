-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: face_recognition
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
-- Table structure for table `regteach`
--

DROP TABLE IF EXISTS `regteach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regteach` (
  `fname` varchar(150) DEFAULT NULL,
  `lname` varchar(150) DEFAULT NULL,
  `cnum` varchar(45) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `ssq` varchar(150) DEFAULT NULL,
  `sa` varchar(150) DEFAULT NULL,
  `pwd` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regteach`
--

LOCK TABLES `regteach` WRITE;
/*!40000 ALTER TABLE `regteach` DISABLE KEYS */;
INSERT INTO `regteach` VALUES ('nguyen','phong','123456723','admin@gmail.com','Ngày tháng sinh','2901','admin');
/*!40000 ALTER TABLE `regteach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stdattendance`
--

DROP TABLE IF EXISTS `stdattendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stdattendance` (
  `std_id` int NOT NULL,
  `std_roll_no` varchar(45) DEFAULT NULL,
  `std_name` varchar(45) DEFAULT NULL,
  `std_time` varchar(45) DEFAULT NULL,
  `std_date` varchar(45) DEFAULT NULL,
  `std_attendance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stdattendance`
--

LOCK TABLES `stdattendance` WRITE;
/*!40000 ALTER TABLE `stdattendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `stdattendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Student_ID` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Department` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `Mobile_No` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Roll_No` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Teacher_Name` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('1','phong','Kỹ thuật phần mềm','Chính quy','2022','Học kì-1','Sáng','Nam','29/01/2002','123123123','QB','1234','phong@gmail.com','Lê Tân','Có Ảnh'),('2','quynh','Thiết kế mĩ thuật số','Chính quy','2020','Học kì-1','Sáng','Nữ','26/10/2002','123123123','QT','20IT868','quynh@gmail.com','Lee Tan','Có Ảnh');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-02 22:38:14
