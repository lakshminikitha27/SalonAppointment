-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: django
-- ------------------------------------------------------
-- Server version	8.0.40

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add salon',1,'add_salon'),(2,'Can change salon',1,'change_salon'),(3,'Can delete salon',1,'delete_salon'),(4,'Can view salon',1,'view_salon'),(5,'Can add service',2,'add_service'),(6,'Can change service',2,'change_service'),(7,'Can delete service',2,'delete_service'),(8,'Can view service',2,'view_service'),(9,'Can add user',3,'add_userdetails'),(10,'Can change user',3,'change_userdetails'),(11,'Can delete user',3,'delete_userdetails'),(12,'Can view user',3,'view_userdetails'),(13,'Can add booked slot',4,'add_bookedslot'),(14,'Can change booked slot',4,'change_bookedslot'),(15,'Can delete booked slot',4,'delete_bookedslot'),(16,'Can view booked slot',4,'view_bookedslot'),(17,'Can add appointment',5,'add_appointment'),(18,'Can change appointment',5,'change_appointment'),(19,'Can delete appointment',5,'delete_appointment'),(20,'Can view appointment',5,'view_appointment'),(21,'Can add log entry',6,'add_logentry'),(22,'Can change log entry',6,'change_logentry'),(23,'Can delete log entry',6,'delete_logentry'),(24,'Can view log entry',6,'view_logentry'),(25,'Can add permission',7,'add_permission'),(26,'Can change permission',7,'change_permission'),(27,'Can delete permission',7,'delete_permission'),(28,'Can view permission',7,'view_permission'),(29,'Can add group',8,'add_group'),(30,'Can change group',8,'change_group'),(31,'Can delete group',8,'delete_group'),(32,'Can view group',8,'view_group'),(33,'Can add content type',9,'add_contenttype'),(34,'Can change content type',9,'change_contenttype'),(35,'Can delete content type',9,'delete_contenttype'),(36,'Can view content type',9,'view_contenttype'),(37,'Can add session',10,'add_session'),(38,'Can change session',10,'change_session'),(39,'Can delete session',10,'delete_session'),(40,'Can view session',10,'view_session'),(41,'Can add service feedback',11,'add_servicefeedback'),(42,'Can change service feedback',11,'change_servicefeedback'),(43,'Can delete service feedback',11,'delete_servicefeedback'),(44,'Can view service feedback',11,'view_servicefeedback');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_myApp_userdetails_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_myApp_userdetails_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_userdetails` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'admin','logentry'),(8,'auth','group'),(7,'auth','permission'),(9,'contenttypes','contenttype'),(5,'myApp','appointment'),(4,'myApp','bookedslot'),(1,'myApp','salon'),(2,'myApp','service'),(11,'myApp','servicefeedback'),(3,'myApp','userdetails'),(10,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-29 06:05:01.424758'),(2,'contenttypes','0002_remove_content_type_name','2024-11-29 06:05:01.502043'),(3,'auth','0001_initial','2024-11-29 06:05:01.853039'),(4,'auth','0002_alter_permission_name_max_length','2024-11-29 06:05:01.935754'),(5,'auth','0003_alter_user_email_max_length','2024-11-29 06:05:01.942363'),(6,'auth','0004_alter_user_username_opts','2024-11-29 06:05:01.949138'),(7,'auth','0005_alter_user_last_login_null','2024-11-29 06:05:01.956013'),(8,'auth','0006_require_contenttypes_0002','2024-11-29 06:05:01.959072'),(9,'auth','0007_alter_validators_add_error_messages','2024-11-29 06:05:01.965595'),(10,'auth','0008_alter_user_username_max_length','2024-11-29 06:05:01.972170'),(11,'auth','0009_alter_user_last_name_max_length','2024-11-29 06:05:01.981208'),(12,'auth','0010_alter_group_name_max_length','2024-11-29 06:05:02.001932'),(13,'auth','0011_update_proxy_permissions','2024-11-29 06:05:02.009241'),(14,'auth','0012_alter_user_first_name_max_length','2024-11-29 06:05:02.017734'),(15,'myApp','0001_initial','2024-11-29 06:05:03.291582'),(16,'admin','0001_initial','2024-11-29 06:05:03.507959'),(17,'admin','0002_logentry_remove_auto_add','2024-11-29 06:05:03.523169'),(18,'admin','0003_logentry_add_action_flag_choices','2024-11-29 06:05:03.544248'),(19,'sessions','0001_initial','2024-11-29 06:05:03.597604'),(20,'myApp','0002_servicefeedback','2024-11-29 07:58:53.353733');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6gwioutglrkq14r3eyvjelwdrgeryefc','.eJxVjMEOwiAQBf-FsyFlgaV49N5vILCAVA1NSnsy_rs06UGvb2bemzm_b8XtLa1ujuzKBLv8bsHTM9UDxIev94XTUrd1DvxQ-Ekbn5aYXrfT_TsovpVeKzEqKwMNGTGbgN5rgUQWRCZJWhoDwRJGBSBs6r8WbJLUo2EEjYF9vtk4N30:1tfhZC:FHooLBWMbOJCYM9VPuRhrPOahTIjy9-wB3AdjB0v47Y','2025-02-19 15:43:54.973453'),('pijuotbth4awt30wbp4yyn0u56onkcak','.eJxVjMEOwiAQBf-FsyFlgaV49N5vILCAVA1NSnsy_rs06UGvb2bemzm_b8XtLa1ujuzKBLv8bsHTM9UDxIev94XTUrd1DvxQ-Ekbn5aYXrfT_TsovpVeKzEqKwMNGTGbgN5rgUQWRCZJWhoDwRJGBSBs6r8WbJLUo2EEjYF9vtk4N30:1tfDAu:mUHNwk_WlVt8wJ3MMgfMOr2E3Eh9WPOg_JzM41S17rk','2025-02-18 07:16:48.250980');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_appointment`
--

DROP TABLE IF EXISTS `myapp_appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_appointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `slot_id` bigint DEFAULT NULL,
  `salon_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myApp_appointment_user_id_2ff41bd6_fk_myApp_userdetails_id` (`user_id`),
  KEY `myApp_appointment_slot_id_90f89984_fk_myApp_bookedslot_id` (`slot_id`),
  KEY `myApp_appointment_salon_id_eb4b1b9b_fk_myApp_salon_id` (`salon_id`),
  KEY `myApp_appointment_service_id_3175ba23_fk_myApp_service_id` (`service_id`),
  CONSTRAINT `myApp_appointment_salon_id_eb4b1b9b_fk_myApp_salon_id` FOREIGN KEY (`salon_id`) REFERENCES `myapp_salon` (`id`),
  CONSTRAINT `myApp_appointment_service_id_3175ba23_fk_myApp_service_id` FOREIGN KEY (`service_id`) REFERENCES `myapp_service` (`id`),
  CONSTRAINT `myApp_appointment_slot_id_90f89984_fk_myApp_bookedslot_id` FOREIGN KEY (`slot_id`) REFERENCES `myapp_bookedslot` (`id`),
  CONSTRAINT `myApp_appointment_user_id_2ff41bd6_fk_myApp_userdetails_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_userdetails` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_appointment`
--

LOCK TABLES `myapp_appointment` WRITE;
/*!40000 ALTER TABLE `myapp_appointment` DISABLE KEYS */;
INSERT INTO `myapp_appointment` VALUES (1,'2024-11-29','2024-11-29 07:48:51.804941',1,3,1,3),(2,'2024-11-30','2024-11-30 04:31:41.389897',1,4,3,1),(3,'2024-11-30','2024-11-30 04:37:12.194846',1,5,2,2),(4,'2024-11-30','2024-11-30 06:08:07.800054',3,6,1,3),(5,'2024-11-30','2024-11-30 06:24:33.770354',3,7,1,3),(6,'2024-12-02','2024-12-02 07:10:46.588244',3,8,2,1),(7,'2025-01-08','2025-01-07 14:59:41.487609',1,9,1,1),(8,'2025-02-05','2025-02-04 05:11:08.972157',1,18,3,3),(9,'2025-02-05','2025-02-04 05:20:26.390677',1,19,1,3);
/*!40000 ALTER TABLE `myapp_appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_bookedslot`
--

DROP TABLE IF EXISTS `myapp_bookedslot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_bookedslot` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `salon_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myApp_bookedslot_time_date_salon_id_242c5832_uniq` (`time`,`date`,`salon_id`),
  KEY `myApp_bookedslot_salon_id_4cd0d503_fk_myApp_salon_id` (`salon_id`),
  KEY `myApp_bookedslot_service_id_6ce40808_fk_myApp_service_id` (`service_id`),
  CONSTRAINT `myApp_bookedslot_salon_id_4cd0d503_fk_myApp_salon_id` FOREIGN KEY (`salon_id`) REFERENCES `myapp_salon` (`id`),
  CONSTRAINT `myApp_bookedslot_service_id_6ce40808_fk_myApp_service_id` FOREIGN KEY (`service_id`) REFERENCES `myapp_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_bookedslot`
--

LOCK TABLES `myapp_bookedslot` WRITE;
/*!40000 ALTER TABLE `myapp_bookedslot` DISABLE KEYS */;
INSERT INTO `myapp_bookedslot` VALUES (2,'14:30:00.000000','2024-11-29','MADDI LAKSHMI NIKITHA','2024-11-29 07:45:12.522889',1,1),(3,'15:30:00.000000','2024-11-29','Likhitha Sree','2024-11-29 07:48:51.798409',1,3),(4,'15:30:00.000000','2024-11-30','likki','2024-11-30 04:31:41.384391',3,1),(5,'15:30:00.000000','2024-11-30','Likhitha Sree','2024-11-30 04:37:12.187318',2,2),(6,'12:30:00.000000','2024-11-30','Neha Sarva','2024-11-30 06:08:07.791141',1,3),(7,'16:00:00.000000','2024-11-30','MADDI LAKSHMI NIKITHA','2024-11-30 06:24:33.766714',1,3),(8,'16:00:00.000000','2024-12-02','Nikitha','2024-12-02 07:10:46.580076',2,1),(9,'10:00:00.000000','2025-01-08','Lakshmi Nikitha','2025-01-07 14:59:41.482483',1,1),(12,'10:30:00.000000','2025-02-04','','2025-02-03 12:23:24.870256',1,1),(14,'10:30:00.000000','2025-02-05','Nikitha27','2025-02-03 12:25:05.992542',1,1),(18,'10:30:00.000000','2025-02-05','Nikitha27','2025-02-04 05:11:08.939329',3,3),(19,'12:30:00.000000','2025-02-05','Nikitha27','2025-02-04 05:20:26.384354',1,3);
/*!40000 ALTER TABLE `myapp_bookedslot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_salon`
--

DROP TABLE IF EXISTS `myapp_salon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_salon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` longtext NOT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `image_name` varchar(100) NOT NULL,
  `rating` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_salon`
--

LOCK TABLES `myapp_salon` WRITE;
/*!40000 ALTER TABLE `myapp_salon` DISABLE KEYS */;
INSERT INTO `myapp_salon` VALUES (1,'VOX-The Luxury Salon','Suchitra, 4th Floor, Merix Square, above Bajaj Electronics, opposite Decathlon, Petbasheerabad, Kompally, Hyderabad, Telangana 500067',17.510131318298146,78.47974739815258,'salon1.jpg',0),(2,'Toni and Guy Salon','First Floor, 6/105/7/A, Suchitra, Godavari Homes, Quthbullapur, Hyderabad, Telangana 500055',17.50384840018909,78.46875585229792,'toni.jpg',0),(3,'Kuts and Kolors mens Salon','37-458, Maisamh no 37, 458, Somaiah Nagar, Jagathgiri Gutta, Hyderabad, Telangana 500037',17.5042882843715,78.42623110996864,'kuts.jpg',0);
/*!40000 ALTER TABLE `myapp_salon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_salon_services`
--

DROP TABLE IF EXISTS `myapp_salon_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_salon_services` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `salon_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myApp_salon_services_salon_id_service_id_5b46e7f4_uniq` (`salon_id`,`service_id`),
  KEY `myApp_salon_services_service_id_3b7e812b_fk_myApp_service_id` (`service_id`),
  CONSTRAINT `myApp_salon_services_salon_id_7dde57a9_fk_myApp_salon_id` FOREIGN KEY (`salon_id`) REFERENCES `myapp_salon` (`id`),
  CONSTRAINT `myApp_salon_services_service_id_3b7e812b_fk_myApp_service_id` FOREIGN KEY (`service_id`) REFERENCES `myapp_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_salon_services`
--

LOCK TABLES `myapp_salon_services` WRITE;
/*!40000 ALTER TABLE `myapp_salon_services` DISABLE KEYS */;
INSERT INTO `myapp_salon_services` VALUES (1,1,1),(2,1,3),(3,2,1),(4,2,2),(5,3,1),(6,3,3);
/*!40000 ALTER TABLE `myapp_salon_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_service`
--

DROP TABLE IF EXISTS `myapp_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_service` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_name` varchar(100) NOT NULL,
  `duration` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `myapp_service_chk_1` CHECK ((`duration` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_service`
--

LOCK TABLES `myapp_service` WRITE;
/*!40000 ALTER TABLE `myapp_service` DISABLE KEYS */;
INSERT INTO `myapp_service` VALUES (1,'Hair Cut',500.00,'hair.jpg',30),(2,'Manicure',1000.00,'manic.jpg',45),(3,'Facial Treatment',2000.00,'facial.jpg',60);
/*!40000 ALTER TABLE `myapp_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_servicefeedback`
--

DROP TABLE IF EXISTS `myapp_servicefeedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_servicefeedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int DEFAULT NULL,
  `comments` longtext,
  `created_at` datetime(6) NOT NULL,
  `appointment_id` bigint DEFAULT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myApp_servicefeedbac_appointment_id_e883171a_fk_myApp_app` (`appointment_id`),
  KEY `myApp_servicefeedback_service_id_25cebddc_fk_myApp_service_id` (`service_id`),
  CONSTRAINT `myApp_servicefeedbac_appointment_id_e883171a_fk_myApp_app` FOREIGN KEY (`appointment_id`) REFERENCES `myapp_appointment` (`id`),
  CONSTRAINT `myApp_servicefeedback_service_id_25cebddc_fk_myApp_service_id` FOREIGN KEY (`service_id`) REFERENCES `myapp_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_servicefeedback`
--

LOCK TABLES `myapp_servicefeedback` WRITE;
/*!40000 ALTER TABLE `myapp_servicefeedback` DISABLE KEYS */;
INSERT INTO `myapp_servicefeedback` VALUES (1,5,'It was nice','2024-11-29 08:01:48.431110',1,3),(2,1,'worst','2024-11-30 06:08:58.556358',4,3);
/*!40000 ALTER TABLE `myapp_servicefeedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_userdetails`
--

DROP TABLE IF EXISTS `myapp_userdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_userdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `city` varchar(100) NOT NULL,
  `address_line` varchar(255) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` varchar(10) NOT NULL,
  `country` varchar(100) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_userdetails`
--

LOCK TABLES `myapp_userdetails` WRITE;
/*!40000 ALTER TABLE `myapp_userdetails` DISABLE KEYS */;
INSERT INTO `myapp_userdetails` VALUES (1,'pbkdf2_sha256$870000$ZTFm0tgbPNfSGWqlM9HUIw$zj40VQqVQDuYJktjcoNo/e8S+CiFnZ9ttB4h8UKFzhc=','2025-02-05 15:43:54.967872',0,'Nikitha27','21r21a05g9@mlrinstitutions.ac.in',0,1,'2024-11-29 07:15:27.937146','08008177355','Nikitha27','Maddi','Female','Hyderabad','Gokul\'s Nandanam,Simhapuri Colony','Telangana','500043','India','2004-07-27'),(2,'pbkdf2_sha256$870000$9Qfme4lXh62iVTt8dK5ZGh$U5qLWbOTRGUib8JeYUy+4oLwnEbfPBGIewl0AkxbXRY=',NULL,0,'likhitha','2004likhithasree@gmail.com',0,1,'2024-11-29 07:18:53.955167','07416434654','Likhitha','Kagitapalli','Female','Hyderabad','Gokul\'s Nandanam,Simhapuri Colony','Telangana','500043','India','2004-01-02'),(3,'pbkdf2_sha256$870000$Uq2N9rxIbzTFPMGsiYsAVV$BKEwLoIlBPms9HKJTPnW9xWlD2CJbSycAtUret4L8ng=','2024-12-02 07:27:43.342235',0,'Neha','sarvaneha123@gmail.com',0,1,'2024-11-30 06:06:50.184898','6309858561','Neha','Sarva','Female','Hyderabad','Gokul\'s Nandanam,Simhapuri Colony','Telangana','500043','India','2003-08-12');
/*!40000 ALTER TABLE `myapp_userdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_userdetails_groups`
--

DROP TABLE IF EXISTS `myapp_userdetails_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_userdetails_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userdetails_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myApp_userdetails_groups_userdetails_id_group_id_c4edd4a0_uniq` (`userdetails_id`,`group_id`),
  KEY `myApp_userdetails_groups_group_id_97efccca_fk_auth_group_id` (`group_id`),
  CONSTRAINT `myApp_userdetails_gr_userdetails_id_a5dcf1c4_fk_myApp_use` FOREIGN KEY (`userdetails_id`) REFERENCES `myapp_userdetails` (`id`),
  CONSTRAINT `myApp_userdetails_groups_group_id_97efccca_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_userdetails_groups`
--

LOCK TABLES `myapp_userdetails_groups` WRITE;
/*!40000 ALTER TABLE `myapp_userdetails_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_userdetails_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_userdetails_user_permissions`
--

DROP TABLE IF EXISTS `myapp_userdetails_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_userdetails_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userdetails_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myApp_userdetails_user_p_userdetails_id_permissio_4a7edffb_uniq` (`userdetails_id`,`permission_id`),
  KEY `myApp_userdetails_us_permission_id_0474e9c9_fk_auth_perm` (`permission_id`),
  CONSTRAINT `myApp_userdetails_us_permission_id_0474e9c9_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `myApp_userdetails_us_userdetails_id_447d86e3_fk_myApp_use` FOREIGN KEY (`userdetails_id`) REFERENCES `myapp_userdetails` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_userdetails_user_permissions`
--

LOCK TABLES `myapp_userdetails_user_permissions` WRITE;
/*!40000 ALTER TABLE `myapp_userdetails_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_userdetails_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-08 11:28:01
