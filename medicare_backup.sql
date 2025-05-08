-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: medicare
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (10),(43);
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('54b48e0cbe88');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time_slot` varchar(50) NOT NULL,
  `message` varchar(255) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `requested_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts`
--

DROP TABLE IF EXISTS `carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `medicine_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_cart_item` (`customer_id`,`medicine_id`),
  KEY `medicine_id` (`medicine_id`),
  CONSTRAINT `carts_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`),
  CONSTRAINT `carts_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicines` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts`
--

LOCK TABLES `carts` WRITE;
/*!40000 ALTER TABLE `carts` DISABLE KEYS */;
INSERT INTO `carts` VALUES (81,1,3,77),(82,1,3,93);
/*!40000 ALTER TABLE `carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Vitamins and Supplements','Health supplements and multivitamins.'),(2,'Skin Care','Medicines and creams for skin care and treatments.'),(3,'Allergy Relief','Medicines to manage and treat allergies.'),(4,'Digestive Health','Medicines for digestive system care, such as antacids and laxatives.'),(5,'Heart Health','Medicines for cardiovascular health and blood pressure management.'),(6,'Diabetes Care','Medicines and supplies for managing diabetes.'),(7,'Eye Care','Drops and medicines for eye health and infections.'),(8,'Child Health','Medicines specifically formulated for children.'),(9,'Women\'s Health','Medicines for women-specific health conditions.'),(10,'Men\'s Health','Medicines for men-specific health conditions.'),(11,'Mental Health','Medicines for mental health and neurological disorders.'),(12,'First Aid','Medicines and items for immediate first aid care.'),(13,'Respiratory Health','Medicines for asthma and other respiratory conditions.'),(14,'Herbal Remedies','Natural and herbal medicine options.'),(15,'Weight Management','Medicines and supplements for weight loss or gain.'),(16,'Immunity Boosters','Supplements and medicines to enhance immunity.'),(17,'Dental Care','Medicines and products for oral health and dental care.'),(18,'Antibiotics','Medicines used to treat bacterial infections.'),(19,'Pain Relief','Medicines for reducing pain and inflammation.'),(20,'Cold and Cough Relief','Medicines for relieving cold, cough, and flu symptoms.');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chats`
--

DROP TABLE IF EXISTS `chats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `is_from_customer` tinyint(1) DEFAULT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `chats_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chats`
--

LOCK TABLES `chats` WRITE;
/*!40000 ALTER TABLE `chats` DISABLE KEYS */;
INSERT INTO `chats` VALUES (1,3,'Hello, I have a question about my recent order.',1,1,'2025-04-23 16:39:37'),(2,3,'What is your question? I\'m here to help.',0,1,'2025-04-23 17:39:37'),(3,3,'I ordered Paracetamol but received Aspirin instead. Can you help?',1,1,'2025-04-24 16:39:37'),(4,3,'I apologize for the mix-up. We\'ll send the correct medicine right away.',0,1,'2025-04-24 17:09:37'),(5,3,'Thank you! When can I expect the delivery?',1,1,'2025-04-25 11:39:41'),(11,3,'Hello, I need help with a prescription upload.',1,1,'2025-04-25 10:40:40'),(12,3,'The site says my file format is not supported. What formats can I use?',1,1,'2025-04-25 11:40:41'),(13,3,'you need to upload jpeg picture files',0,1,'2025-04-25 10:41:20'),(14,3,'okay',0,1,'2025-04-25 10:50:22'),(15,51,'Can I get a refill on my previous prescription?',1,1,'2025-04-24 10:15:00'),(16,52,'Your prescription has been refilled and is ready for delivery.',0,1,'2025-04-24 11:00:00'),(17,51,'yes sure',0,1,'2025-04-25 11:12:12'),(18,51,'hello, you there?',0,1,'2025-04-25 11:33:54'),(19,52,'ji',0,1,'2025-04-25 11:35:16'),(20,51,'kire bhai',0,1,'2025-04-25 11:41:58'),(21,51,'hey',0,1,'2025-04-26 19:26:21'),(22,3,'jpeg',0,1,'2025-04-26 19:26:39'),(23,3,'okay',1,1,'2025-04-30 17:21:35'),(24,3,'did you get your delivery?',0,1,'2025-04-30 17:22:23'),(25,3,'not yet',1,1,'2025-04-30 17:31:36'),(26,3,'than you for you patience sir',0,1,'2025-04-30 17:32:31'),(27,3,'.',1,1,'2025-04-30 17:47:31'),(28,3,'lesgoooooooooo',1,1,'2025-04-30 17:48:41'),(29,3,'.',0,1,'2025-04-30 18:16:28'),(30,3,'gg',0,1,'2025-04-30 18:34:57'),(31,3,'wp',1,1,'2025-04-30 18:35:17'),(32,3,'ty',0,1,'2025-04-30 18:42:46'),(33,3,'okay',1,1,'2025-04-30 18:49:36'),(34,3,'okay',1,1,'2025-04-30 18:54:46'),(35,3,'gg',1,1,'2025-04-30 18:54:52'),(36,3,'gg',1,1,'2025-04-30 18:54:52'),(37,3,'gg',1,1,'2025-04-30 18:54:52'),(38,3,'gg',1,1,'2025-04-30 18:54:53'),(39,3,'oye',1,1,'2025-04-30 18:56:03'),(40,3,'eeeeeeeeeeee',1,1,'2025-04-30 19:00:00'),(41,3,'oye',1,1,'2025-04-30 19:06:08'),(42,3,'thank god',1,1,'2025-04-30 19:07:14'),(43,3,'yes yes yes',0,1,'2025-04-30 19:11:48'),(44,3,'.',0,1,'2025-04-30 19:13:20'),(45,3,'hmm',0,1,'2025-04-30 19:15:04'),(46,3,'shei shei',0,1,'2025-04-30 19:15:09'),(47,50,'hello i want to ask something',1,1,'2025-04-30 19:20:48'),(48,50,'sure sir, how can i help?',0,1,'2025-04-30 19:21:22'),(49,50,'hello, this is staff',0,1,'2025-05-01 10:36:44'),(50,50,'damn',1,1,'2025-05-01 10:37:13'),(51,50,'yessir',0,1,'2025-05-02 11:29:21'),(52,50,'ji',0,1,'2025-05-02 11:31:30'),(53,50,'yooooooooooooo',1,1,'2025-05-02 11:31:44'),(54,50,'is it working?',0,1,'2025-05-02 11:38:12'),(55,50,'i think so',1,1,'2025-05-02 11:38:36'),(56,50,'ahem',0,1,'2025-05-02 11:45:43'),(57,50,'hu',0,1,'2025-05-02 11:45:57'),(58,50,'sure',0,1,'2025-05-02 11:47:14'),(59,50,'okay',1,1,'2025-05-02 11:47:33'),(60,50,'uf',1,1,'2025-05-02 11:58:54'),(61,50,'o',1,1,'2025-05-02 11:58:57'),(62,50,'siu',1,1,'2025-05-02 11:59:02'),(63,50,'eeeeeeeeeeee',1,1,'2025-05-02 12:10:30'),(64,50,'hehe',1,1,'2025-05-02 12:10:42'),(65,50,'lesgooo',1,1,'2025-05-02 12:10:46'),(66,50,'yeah it\'s fixed now',0,1,'2025-05-02 12:15:36'),(67,50,'perfecto',1,1,'2025-05-02 12:18:52');
/*!40000 ALTER TABLE `chats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (3),(8),(46),(48),(49),(50),(51),(52),(53);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctors` (
  `id` int(11) NOT NULL,
  `specialization` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicines`
--

DROP TABLE IF EXISTS `medicines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` float NOT NULL,
  `stock` int(11) NOT NULL,
  `expiry_date` date DEFAULT NULL,
  `low_stock_flag` tinyint(1) DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `medicines_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicines`
--

LOCK TABLES `medicines` WRITE;
/*!40000 ALTER TABLE `medicines` DISABLE KEYS */;
INSERT INTO `medicines` VALUES (69,'Vitamin C 500mg','Boosts immunity and overall health.',8.99,100,NULL,NULL,1),(70,'Multivitamin Capsules','Daily nutritional supplement.',12.49,150,NULL,NULL,1),(71,'Omega-3 Fish Oil','Supports heart and brain health.',15,80,NULL,NULL,1),(72,'Hydrocortisone Cream','For skin irritations and rashes.',5.25,50,NULL,NULL,2),(73,'Acne Control Gel','Treats acne and pimples.',7.95,5,NULL,NULL,2),(74,'Moisturizing Lotion','Hydrates dry skin.',6.75,100,NULL,NULL,2),(75,'Cetirizine Tablets','Relieves allergy symptoms.',4.99,200,NULL,NULL,3),(76,'Loratadine 10mg','Non-drowsy allergy relief.',5.5,180,NULL,NULL,3),(77,'Allergy Eye Drops','Reduces eye itchiness from allergies.',6.3,90,NULL,NULL,3),(78,'Antacid Tablets','Neutralizes stomach acid.',3.2,100,NULL,NULL,4),(79,'Laxative Syrup','Relieves constipation.',4.75,70,NULL,NULL,4),(80,'Probiotic Capsules','Supports digestive balance.',11.25,60,NULL,NULL,4),(81,'Aspirin 81mg','Supports heart health.',2.99,120,NULL,NULL,5),(82,'Atorvastatin 20mg','Lowers cholesterol.',10.45,80,NULL,NULL,5),(83,'Blood Pressure Monitor','Tracks blood pressure.',25,20,NULL,NULL,5),(84,'Insulin Pen','Helps manage blood sugar.',30,40,NULL,NULL,6),(85,'Glucose Test Strips','For blood sugar testing.',18.5,100,NULL,NULL,6),(86,'Metformin 500mg','Controls blood sugar levels.',7.99,150,NULL,NULL,6),(87,'Lubricant Eye Drops','Relieves dry eyes.',4.5,70,NULL,NULL,7),(88,'Antibiotic Eye Drops','Treats eye infections.',6.25,60,NULL,NULL,7),(89,'Eye Vitamin Supplement','Supports vision health.',9.9,50,NULL,NULL,7),(90,'Paracetamol for Kids','Pain and fever relief for kids.',3.4,100,NULL,NULL,8),(91,'Multivitamin Syrup','Nutritional supplement for kids.',6.8,80,NULL,NULL,8),(92,'Cough Syrup for Kids','Soothes cough in children.',5.1,70,NULL,NULL,8),(93,'Iron Tablets','Supports women health.',4.95,90,NULL,NULL,9),(94,'Folic Acid 400mcg','Prenatal supplement.',3.75,120,NULL,NULL,9),(95,'Menstrual Pain Relief','Relieves period cramps.',6.6,80,NULL,NULL,9),(96,'Vitality Capsules','Supports male vitality.',20,30,NULL,NULL,10),(97,'Hair Growth Supplement','Promotes hair health.',12.5,45,NULL,NULL,10),(98,'Prostate Support','Supports prostate function.',14.3,50,NULL,NULL,10),(99,'Sertraline 50mg','Treats depression and anxiety.',9,60,NULL,NULL,11),(100,'Melatonin 3mg','Promotes better sleep.',7.2,80,NULL,NULL,11),(101,'Brain Boost Omega-3','Supports cognitive health.',13.75,40,NULL,NULL,11),(102,'Antiseptic Cream','Prevents infection in minor cuts.',3.95,100,NULL,NULL,12),(103,'Bandage Roll','Sterile wound dressing.',2.5,150,NULL,NULL,12),(104,'Burn Relief Spray','Cools and soothes burns.',4.8,60,NULL,NULL,12),(105,'Inhaler Salbutamol','Relieves asthma symptoms.',8,70,NULL,NULL,13),(106,'Cough Suppressant Syrup','Soothes persistent cough.',5.3,90,NULL,NULL,13),(107,'Steam Inhaler','Clears nasal congestion.',22,25,NULL,NULL,13),(108,'Tulsi Drops','Boosts immunity naturally.',4.2,60,NULL,NULL,14),(109,'Ashwagandha Capsules','Reduces stress.',10.25,50,NULL,NULL,14),(110,'Neem Tablets','Supports skin health.',5.6,70,NULL,NULL,14),(111,'Green Tea Extract','Boosts metabolism.',8.99,80,NULL,NULL,15),(112,'Meal Replacement Shake','Supports weight loss.',14.99,50,NULL,NULL,15),(113,'Appetite Suppressant','Controls hunger cravings.',11.75,30,NULL,NULL,15),(114,'Zinc Tablets','Supports immune function.',3.9,100,NULL,NULL,16),(115,'Elderberry Syrup','Natural immune support.',7.45,60,NULL,NULL,16),(116,'Vitamin D3 1000IU','Boosts immunity.',6.3,90,NULL,NULL,16),(117,'Toothache Relief Gel','Numbs dental pain.',4,100,NULL,NULL,17),(118,'Fluoride Mouthwash','Protects against cavities.',5.75,70,NULL,NULL,17),(119,'Sensitive Toothpaste','Reduces tooth sensitivity.',6.5,80,NULL,NULL,17),(120,'Amoxicillin 500mg','Treats bacterial infections.',8,100,NULL,NULL,18),(121,'Azithromycin 250mg','Broad-spectrum antibiotic.',9.5,80,NULL,NULL,18),(122,'Ciprofloxacin 500mg','Used for various infections.',7.6,90,NULL,NULL,18),(123,'Ibuprofen 400mg','Reduces pain and inflammation.',4.2,150,NULL,NULL,19),(124,'Paracetamol 500mg','Common pain reliever.',3.8,200,NULL,NULL,19),(125,'Diclofenac Gel','Topical pain relief.',6,60,NULL,NULL,19),(126,'Cold Relief Tablets','Relieves cold symptoms.',4.95,120,NULL,NULL,20),(127,'Cough Drops','Soothes sore throat.',2.99,200,NULL,NULL,20),(128,'Flu Care Syrup','Fights flu symptoms.',6.25,90,NULL,NULL,20);
/*!40000 ALTER TABLE `medicines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `notification_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_id` (`staff_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,44,'napa is about get stocked out',1,'2025-05-01 10:50:38','stock_alert'),(2,44,'the user id 50 did not receive the order',1,'2025-05-01 10:51:01','order_issue'),(3,44,'Since, eid is coming, we will stop accepting orders from tomorrow',1,'2025-05-01 10:51:55','general'),(4,44,'hmm',1,'2025-05-01 10:56:01','general'),(5,44,'siu',1,'2025-05-02 14:37:55','stock_alert'),(6,44,'cr7',1,'2025-05-02 14:38:34','general'),(7,44,'lesgooooooooooooooooooooo',1,'2025-05-05 16:19:15','general'),(8,44,'nokia',1,'2025-05-05 16:29:01','general'),(9,44,'dawdasd',1,'2025-05-05 16:45:50','stock_alert'),(10,44,'adsasdawd',1,'2025-05-05 16:45:54','system_alert'),(11,44,'adwadasgwe',1,'2025-05-05 16:45:58','system_alert'),(12,44,'siuuuuuuuuuuuuuuuu\r\n',1,'2025-05-05 16:53:19','general'),(13,44,'1',1,'2025-05-05 16:53:21','stock_alert'),(14,44,'2',1,'2025-05-05 16:53:23','stock_alert'),(15,44,'3',1,'2025-05-05 16:53:24','stock_alert'),(16,44,'4',1,'2025-05-05 16:53:25','stock_alert'),(17,44,'5',1,'2025-05-05 16:53:27','stock_alert'),(18,44,'6',1,'2025-05-05 16:53:29','stock_alert'),(19,44,'7',1,'2025-05-05 17:04:20','stock_alert'),(20,44,'8',1,'2025-05-05 17:04:22','stock_alert'),(21,44,'9',1,'2025-05-05 17:04:24','stock_alert'),(22,44,'10',1,'2025-05-05 17:04:28','stock_alert'),(23,44,'11',1,'2025-05-05 17:07:31','stock_alert'),(24,44,'12',1,'2025-05-05 17:07:32','stock_alert'),(25,44,'13',1,'2025-05-05 17:07:34','stock_alert'),(26,44,'14',1,'2025-05-05 17:07:35','stock_alert'),(27,44,'last test\r\n',1,'2025-05-05 17:11:44','general');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `price` float NOT NULL,
  `order_id` int(11) NOT NULL,
  `medicine_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `medicine_id` (`medicine_id`),
  CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `total_price` float NOT NULL,
  `status` varchar(50) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `payment_status` varchar(50) NOT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescriptions`
--

DROP TABLE IF EXISTS `prescriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prescriptions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_path` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `prescriptions_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescriptions`
--

LOCK TABLES `prescriptions` WRITE;
/*!40000 ALTER TABLE `prescriptions` DISABLE KEYS */;
/*!40000 ALTER TABLE `prescriptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (44);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `role` varchar(20) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3,'Md. Rafiul Islam','rafit991@gmail.com','rafit991','Zigatola, Dhanmondi','01845904415','customer','customer'),(4,'Test User','test@example.com','testpassword',NULL,NULL,'customer','customer'),(8,'test111','test1@gmail.com','test1234',NULL,'12345678901','customer','customer'),(10,'rafitboo','rafit@admin.com','rafit123','romjan bus','2345678910','admin','admin'),(43,'wasi','wasi@admin.com','wasi1234','Shantinagar','0168234342','admin','admin'),(44,'Rafu','rafu@staff.com','rafu1234','Eije Ekhaneiiiiiii','121313241','staff','staff'),(46,'Shutupp','shut@up.com','12345678','Eije','1234567890','customer','customer'),(47,'Hello Ji','hello@ji.com','hello123','None','12345678901','customer','customer'),(48,'Lmao','lmao@gg.com','lmao1234','None','12345678901','customer','customer'),(49,'Abcd','ab@cd.com','12345678',NULL,'01812345679','customer','customer'),(50,'Skibidi','skibidi@rizz.com','skibidi123','','12369696969','customer','customer'),(51,'Raihan','raihan@gmail.com','raihan123','','01889122334','customer','customer'),(52,'Rafi','rafi@gmail.com','rafi1234','','01912234567','customer','customer'),(53,'Lesgooooooooo','lsg@oo.com','lesgo123',NULL,'271378162197','customer','customer');
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

-- Dump completed on 2025-05-08 19:54:45
