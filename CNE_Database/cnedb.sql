CREATE DATABASE  IF NOT EXISTS `cnedb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cnedb`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: cnedb
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Group Information',7,'add_groups'),(26,'Can change Group Information',7,'change_groups'),(27,'Can delete Group Information',7,'delete_groups'),(28,'Can view Group Information',7,'view_groups'),(29,'Can add questions',8,'add_question'),(30,'Can change questions',8,'change_question'),(31,'Can delete questions',8,'delete_question'),(32,'Can view questions',8,'view_question'),(33,'Can add User Information',9,'add_usersprofile'),(34,'Can change User Information',9,'change_usersprofile'),(35,'Can delete User Information',9,'delete_usersprofile'),(36,'Can view User Information',9,'view_usersprofile'),(37,'Can add PaperList',10,'add_paperlist'),(38,'Can change PaperList',10,'change_paperlist'),(39,'Can delete PaperList',10,'delete_paperlist'),(40,'Can view PaperList',10,'view_paperlist'),(41,'Can add Papers',11,'add_paper'),(42,'Can change Papers',11,'change_paper'),(43,'Can delete Papers',11,'delete_paper'),(44,'Can view Papers',11,'view_paper'),(45,'Can add CandidateResult',12,'add_candidateresult'),(46,'Can change CandidateResult',12,'change_candidateresult'),(47,'Can delete CandidateResult',12,'delete_candidateresult'),(48,'Can view CandidateResult',12,'view_candidateresult'),(49,'Can add QuestionDatabase',13,'add_questiondatabase'),(50,'Can change QuestionDatabase',13,'change_questiondatabase'),(51,'Can delete QuestionDatabase',13,'delete_questiondatabase'),(52,'Can view QuestionDatabase',13,'view_questiondatabase');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cnexplorer_candidateresult`
--

DROP TABLE IF EXISTS `cnexplorer_candidateresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cnexplorer_candidateresult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `answer` longtext NOT NULL,
  `paper_id` int NOT NULL,
  `question_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CNExplorer_candidate_paper_id_ccd1a737_fk_CNExplore` (`paper_id`),
  KEY `CNExplorer_candidate_question_id_24696a9d_fk_CNExplore` (`question_id`),
  KEY `CNExplorer_candidateresult_user_id_8aeec4b3_fk_Users_id` (`user_id`),
  CONSTRAINT `CNExplorer_candidate_paper_id_ccd1a737_fk_CNExplore` FOREIGN KEY (`paper_id`) REFERENCES `cnexplorer_paperlist` (`id`),
  CONSTRAINT `CNExplorer_candidate_question_id_24696a9d_fk_CNExplore` FOREIGN KEY (`question_id`) REFERENCES `cnexplorer_question` (`id`),
  CONSTRAINT `CNExplorer_candidateresult_user_id_8aeec4b3_fk_Users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cnexplorer_candidateresult`
--

LOCK TABLES `cnexplorer_candidateresult` WRITE;
/*!40000 ALTER TABLE `cnexplorer_candidateresult` DISABLE KEYS */;
INSERT INTO `cnexplorer_candidateresult` VALUES (1,'',1,1,1),(2,'-3.2+2.4j',1,2,1),(3,'',1,3,1),(4,'',1,4,1),(5,'',1,5,1),(16,'12',4,16,1),(17,'kfsud',4,17,1),(18,'safsdf',4,18,1),(19,'afds',4,19,1),(20,'fasdf',4,20,1),(21,'',5,21,1),(22,'',5,22,1),(23,'',5,23,1),(24,'',5,24,1),(25,'',5,25,1),(31,'-0.4-2.2j',7,31,1),(32,'',7,32,1),(33,'-3.2+2.4j',7,33,1),(34,'',7,34,1),(35,'',7,35,1);
/*!40000 ALTER TABLE `cnexplorer_candidateresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cnexplorer_paper`
--

DROP TABLE IF EXISTS `cnexplorer_paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cnexplorer_paper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `PaperListID_id` int NOT NULL,
  `question_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CNExplorer_paper_PaperListID_id_fb8b4e6c_fk_CNExplore` (`PaperListID_id`),
  KEY `CNExplorer_paper_question_id_f2d277d4_fk_CNExplorer_question_id` (`question_id`),
  CONSTRAINT `CNExplorer_paper_PaperListID_id_fb8b4e6c_fk_CNExplore` FOREIGN KEY (`PaperListID_id`) REFERENCES `cnexplorer_paperlist` (`id`),
  CONSTRAINT `CNExplorer_paper_question_id_f2d277d4_fk_CNExplorer_question_id` FOREIGN KEY (`question_id`) REFERENCES `cnexplorer_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cnexplorer_paper`
--

LOCK TABLES `cnexplorer_paper` WRITE;
/*!40000 ALTER TABLE `cnexplorer_paper` DISABLE KEYS */;
/*!40000 ALTER TABLE `cnexplorer_paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cnexplorer_paperlist`
--

DROP TABLE IF EXISTS `cnexplorer_paperlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cnexplorer_paperlist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `is_allow` tinyint(1) NOT NULL,
  `groupNum_id` int NOT NULL,
  `is_attempted` varchar(32) NOT NULL,
  `startQuestionID` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CNExplorer_paperlist_groupNum_id_a0947164_fk_Groups_id` (`groupNum_id`),
  CONSTRAINT `CNExplorer_paperlist_groupNum_id_a0947164_fk_Groups_id` FOREIGN KEY (`groupNum_id`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cnexplorer_paperlist`
--

LOCK TABLES `cnexplorer_paperlist` WRITE;
/*!40000 ALTER TABLE `cnexplorer_paperlist` DISABLE KEYS */;
INSERT INTO `cnexplorer_paperlist` VALUES (1,'',0,1,'Not Answered','1'),(2,'',0,1,'Not Answered','6'),(3,'',0,1,'Not Answered','11'),(4,'',1,1,'Answered','16'),(5,'',1,1,'Answered','21'),(6,'',0,1,'Not Answered','26'),(7,'',1,1,'Answered','31');
/*!40000 ALTER TABLE `cnexplorer_paperlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cnexplorer_question`
--

DROP TABLE IF EXISTS `cnexplorer_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cnexplorer_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `equation` longtext NOT NULL,
  `answer` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cnexplorer_question`
--

LOCK TABLES `cnexplorer_question` WRITE;
/*!40000 ALTER TABLE `cnexplorer_question` DISABLE KEYS */;
INSERT INTO `cnexplorer_question` VALUES (1,'Divide and express in the form of a complex number a + b i',' (-1-2j)/(-4+3j)',' -2 / 25 + (11 / 25)j'),(2,'calculate',' -(-1+2j)*(3+4j)','11-2j'),(3,'calculate',' (1+2j)*z-(3+4j)=(3+6j)','5.2-0.4j'),(4,'Divide and express in the form of a complex number a + b i',' (-1-2j)/(-4+3j)',' -2 / 25 + (11 / 25)j'),(5,'calculate',' (1+2j)*z-(3+4j)=(3+6j)','5.2-0.4j'),(6,'Find the complex conjugate to',' 1+8j','1 - 8 j'),(7,'Express in the form of a complex number a + b i',' (-5-j)(-7+8j)/(2-4j)','109 / 10 + (53 / 10) i'),(8,'Find the complex conjugate to',' 1+8j','1 - 8 j'),(9,'calculate',' -(-1+2j)*(3+4j)','11-2j'),(10,'calculate',' -(1+2j)*z-(3+2j)=(5+2j)','-3.2+2.4j'),(11,'calculate',' (1+2j)*z-(3+4j)=(3+6j)','5.2-0.4j'),(12,'Multiply and express in the form of a complex number a + b i',' (-5+3j)(-4+8j)','-4 - 52 j'),(13,'Divide and express in the form of a complex number a + b i',' (-1-2j)/(-4+3j)',' -2 / 25 + (11 / 25)j'),(14,'Add and express in the form of a complex number a + b i',' (2+3j)+(-4+5j)-(9-3j)/3','-5 + 9 j'),(15,'calculate ',' (1+j)+(3+2j)','4+3j'),(16,'Divide and express in the form of a complex number a + b i',' (-1-2j)/(-4+3j)',' -2 / 25 + (11 / 25)j'),(17,'calculate',' (21-7j)/(-2e^3j)','0.09000000000000001+0.015714285714285715j'),(18,'Express in the form of a complex number a + b i',' -(7-j)(-4-2j)(2-j)','70 - 10 i'),(19,'calculate',' (21-7j)/(-2e^3j)','0.09000000000000001+0.015714285714285715j'),(20,'calculate ',' (1+j)+(4+2j)','5+3j'),(21,'Add and express in the form of a complex number a + b i',' (2+3j)+(-4+5j)-(9-3j)/3','-11+11j'),(22,'solve the equation',' - (9-2j) *z-(3+4j)=(3e^0.2pij)','-3.2+2.4j'),(23,'Express in the form of a complex number a + b i',' (9+23j)*(-5+8j)','-229-43j'),(24,'Express in the form of a complex number a + b i',' (-5+13j)*(-5+8j)','-79-105j'),(25,'Add and express in the form of a complex number a + b i',' (2+3j)+(-4+5j)-(9-3j)/3','-11+11j'),(26,'Divide and express in the form of a complex number a + b i',' (-1-2j)/(-4+3j)','-0.4-2.2j'),(27,'Multiply and express in the form of a complex number a + b i',' (-5+3j)*(-4+8j)','-4 - 52 j'),(28,'solve the equation',' - (1+2j) *z-(3+4j)=(3e^0.2pij)','-3.4+j'),(29,'calculate',' -(1+2j)*z-(3+2j)=(5+2j)','-3.2+2.4j'),(30,'Add and express in the form of a complex number a + b i',' (2+3j)+(-4+5j)-(9-3j)/3','-11+11j'),(31,'Divide and express in the form of a complex number a + b i',' (-1-2j)/(-4+3j)','-0.4-2.2j'),(32,'Express in the form of a complex number a + b i',' (9+23j)*(-5+8j)','-229-43j'),(33,'calculate',' -(1+2j)*z-(3+2j)=(5+2j)','-3.2+2.4j'),(34,'calculate',' (1+2j)*z-(3+4j)=(3+6j)','5.2-0.4j'),(35,'calculate ',' (-5+13j)*(-5+8j)','-79-105j');
/*!40000 ALTER TABLE `cnexplorer_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cnexplorer_questiondatabase`
--

DROP TABLE IF EXISTS `cnexplorer_questiondatabase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cnexplorer_questiondatabase` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `equation` longtext NOT NULL,
  `answer` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cnexplorer_questiondatabase`
--

LOCK TABLES `cnexplorer_questiondatabase` WRITE;
/*!40000 ALTER TABLE `cnexplorer_questiondatabase` DISABLE KEYS */;
INSERT INTO `cnexplorer_questiondatabase` VALUES (1,'calculate','(1+2j)*z-(3+4j)=(3+6j)','5.2-0.4j'),(2,'calculate','-(1+2j)*z-(3+2j)=(5+2j)','-3.2+2.4j'),(3,'Add and express in the form of a complex number a + b i','(2+3j)+(-4+5j)-(9-3j)/3','-11+11j'),(4,'Multiply and express in the form of a complex number a + b i','(-5+3j)*(-4+8j)','-4 - 52 j'),(5,'Divide and express in the form of a complex number a + b i','(-1-2j)/(-4+3j)','-0.4-2.2j'),(6,'Find the complex conjugate to','(1+8j)','1 - 8 j'),(7,'Find the complex conjugate to','(1-9j)','1+9j'),(8,'Express in the form of a complex number a + b i','(-5+13j)*(-5+8j)','-79-105j'),(9,'Express in the form of a complex number a + b i','(9+23j)*(-5+8j)','-229-43j'),(10,'solve the equation','- (9-2j) *z-(3+4j)=(3e^0.2pij)','-3.2+2.4j'),(11,'solve the equation','- (9-2j)*z+(5+4j)=(3e^0.2pij)','0.22+0.29j'),(12,'solve the equation','- (1+2j) *z-(3+4j)=(3e^0.2pij)','-3.4+j'),(13,'solve the equation','- (1+2j) *z-(3+4j)=(3e^0.6pij)','-3.18-0.54j');
/*!40000 ALTER TABLE `cnexplorer_questiondatabase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(12,'CNExplorer','candidateresult'),(7,'CNExplorer','groups'),(11,'CNExplorer','paper'),(10,'CNExplorer','paperlist'),(8,'CNExplorer','question'),(13,'CNExplorer','questiondatabase'),(9,'CNExplorer','usersprofile'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'CNExplorer','0001_initial','2022-03-23 20:06:35.648684'),(2,'CNExplorer','0002_questiondatabase','2022-03-23 20:06:35.670712'),(3,'CNExplorer','0003_paperlist_is_attempted','2022-03-23 20:06:35.708517'),(4,'CNExplorer','0004_paperlist_startquestionid','2022-03-23 20:06:35.772578'),(5,'contenttypes','0001_initial','2022-03-23 20:06:35.804149'),(6,'auth','0001_initial','2022-03-23 20:06:36.878294'),(7,'admin','0001_initial','2022-03-23 20:06:37.088659'),(8,'admin','0002_logentry_remove_auto_add','2022-03-23 20:06:37.119236'),(9,'admin','0003_logentry_add_action_flag_choices','2022-03-23 20:06:37.148297'),(10,'contenttypes','0002_remove_content_type_name','2022-03-23 20:06:37.479381'),(11,'auth','0002_alter_permission_name_max_length','2022-03-23 20:06:37.645954'),(12,'auth','0003_alter_user_email_max_length','2022-03-23 20:06:37.840458'),(13,'auth','0004_alter_user_username_opts','2022-03-23 20:06:37.869167'),(14,'auth','0005_alter_user_last_login_null','2022-03-23 20:06:38.021141'),(15,'auth','0006_require_contenttypes_0002','2022-03-23 20:06:38.024519'),(16,'auth','0007_alter_validators_add_error_messages','2022-03-23 20:06:38.031797'),(17,'auth','0008_alter_user_username_max_length','2022-03-23 20:06:38.112493'),(18,'auth','0009_alter_user_last_name_max_length','2022-03-23 20:06:38.185186'),(19,'auth','0010_alter_group_name_max_length','2022-03-23 20:06:38.309238'),(20,'auth','0011_update_proxy_permissions','2022-03-23 20:06:38.320317'),(21,'auth','0012_alter_user_first_name_max_length','2022-03-23 20:06:38.417399'),(22,'sessions','0001_initial','2022-03-23 20:06:38.498231');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `groupName` varchar(32) NOT NULL,
  `groupCode` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES (1,'CN1','1');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `usertype` varchar(32) NOT NULL,
  `emailAddress` varchar(32) NOT NULL,
  `groupNum_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Users_groupNum_id_5fead0da_fk_Groups_id` (`groupNum_id`),
  CONSTRAINT `Users_groupNum_id_5fead0da_fk_Groups_id` FOREIGN KEY (`groupNum_id`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'StudentAdmin','123','Student','123456@qq.com',1),(3,'zyh','020214','Student','123456@qq.com',1),(4,'Dylan','123456','Teacher','dylan@outlook.com',1),(5,'Lebron','123456','Teacher','lebron@outlook.com',1),(6,'wade','123456','Teacher','wade@outlook.com',1),(7,'james','123456','Teacher','james@outlok.com',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-24  8:54:44
