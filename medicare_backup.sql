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
  KEY `customer_id` (`customer_id`),
  KEY `medicine_id` (`medicine_id`),
  CONSTRAINT `carts_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `carts_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts`
--

LOCK TABLES `carts` WRITE;
/*!40000 ALTER TABLE `carts` DISABLE KEYS */;
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
INSERT INTO `categories` VALUES (1,'Vitamins and Supplements','Health supplements and multivitamins.'),(2,'Skin Care','Medicines and creams for skin care and treatments.'),(3,'Allergy Relief','Medicines to manage and treat allergies.'),(4,'Digestive Health','Medicines for digestive system care, such as antacids and laxatives.'),(5,'Heart Health','Medicines for cardiovascular health and blood pressure management.'),(6,'Diabetes Care','Medicines and supplies for managing diabetes.'),(7,'Eye Care','Drops and medicines for eye health and infections.'),(8,'Child Health','Medicines specifically formulated for children.'),(9,'Women\'s Health','Medicines for women-specific health conditions.'),(10,'Men\'s Health','Medicines for men-specific health conditions.'),(11,'Mental Health','Medicines for mental health and neurological disorders.'),(12,'First Aid','Medicines and items for immediate first aid care.'),(13,'Respiratory Health','Medicines for asthma and other respiratory conditions.'),(14,'Herbal Remedies','Natural and herbal medicine options.'),(15,'Weight Management','Medicines and supplements for weight loss or gain.'),(16,'Immunity Boosters','Supplements and medicines to enhance immunity.'),(17,'Dental Care','Medicines and products for oral health and dental care.'),(18,'Antibiotics','Medicines used to treat bacterial infections.'),(19,'Pain Relief','Medicines for reducing pain and inflammation.'),(20,'Cold and Cough Relief','Medicines for relieving cold, cough, and flu symptoms.'),(23,'aaaaaaaaaaa','aaaaaaaaaaaaaaa');
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chats`
--

LOCK TABLES `chats` WRITE;
/*!40000 ALTER TABLE `chats` DISABLE KEYS */;
INSERT INTO `chats` VALUES (1,3,'Hello, I have a question about my recent order.',1,1,'2025-04-23 16:39:37'),(2,3,'What is your question? I\'m here to help.',0,1,'2025-04-23 17:39:37'),(3,3,'I ordered Paracetamol but received Aspirin instead. Can you help?',1,1,'2025-04-24 16:39:37'),(4,3,'I apologize for the mix-up. We\'ll send the correct medicine right away.',0,1,'2025-04-24 17:09:37'),(5,3,'Thank you! When can I expect the delivery?',1,1,'2025-04-25 11:39:41'),(11,3,'Hello, I need help with a prescription upload.',1,1,'2025-04-25 10:40:40'),(12,3,'The site says my file format is not supported. What formats can I use?',1,1,'2025-04-25 11:40:41'),(13,3,'you need to upload jpeg picture files',0,1,'2025-04-25 10:41:20'),(14,3,'okay',0,1,'2025-04-25 10:50:22'),(15,51,'Can I get a refill on my previous prescription?',1,1,'2025-04-24 10:15:00'),(16,52,'Your prescription has been refilled and is ready for delivery.',0,1,'2025-04-24 11:00:00'),(17,51,'yes sure',0,1,'2025-04-25 11:12:12'),(18,51,'hello, you there?',0,1,'2025-04-25 11:33:54'),(19,52,'ji',0,1,'2025-04-25 11:35:16'),(20,51,'kire bhai',0,1,'2025-04-25 11:41:58'),(21,51,'hey',0,1,'2025-04-26 19:26:21'),(22,3,'jpeg',0,1,'2025-04-26 19:26:39');
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
INSERT INTO `customers` VALUES (3),(8),(46),(48),(49),(50),(51),(52);
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
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicines`
--

LOCK TABLES `medicines` WRITE;
/*!40000 ALTER TABLE `medicines` DISABLE KEYS */;
INSERT INTO `medicines` VALUES (1,'Cefixime','Antibiotic for bacterial infections.',140,10,NULL,NULL,1),(2,'Azithromycin','Antibiotic for respiratory and skin infections.',180,0,NULL,NULL,1),(3,'Ciprofloxacin','Broad-spectrum antibiotic for various infections.',120,350,NULL,NULL,1),(4,'Napa Extra','Paracetamol for pain and fever relief.',30,500,NULL,NULL,2),(5,'Ace Plus','Pain reliever and fever reducer.',25,200,NULL,NULL,2),(6,'Synflex 550','Nonsteroidal anti-inflammatory drug for pain relief.',80,200,NULL,NULL,2),(7,'Histacin Syrup','Syrup for cough and cold symptoms.',50,200,NULL,NULL,3),(8,'Fexo 120','Tablet for cold and allergy symptoms.',80,150,NULL,NULL,3),(9,'Sinarest','Tablet for cold, runny nose, and headache.',70,180,NULL,NULL,3),(10,'Revital','Multivitamin and mineral supplement for overall health.',120,50,NULL,NULL,4),(11,'Cipcal 500','Calcium supplement for bone health.',80,100,NULL,NULL,4),(12,'Centrum','Multivitamin for adults.',150,40,NULL,NULL,4),(13,'Fusiderm Cream','Topical antibiotic for skin infections.',100,20,NULL,NULL,5),(14,'Betnovate-N','Cream for eczema and dermatitis.',90,30,NULL,NULL,5),(15,'Dermovate','Cream for psoriasis and other skin conditions.',120,25,NULL,NULL,5),(16,'Alatrol','Antihistamine for allergy relief.',50,200,NULL,NULL,6),(17,'Alergin','Tablet for managing allergies.',45,150,NULL,NULL,6),(18,'Histacin','Antihistamine for allergic reactions.',40,180,NULL,NULL,6),(19,'Seclo 20','Proton pump inhibitor for acidity and ulcers.',60,100,NULL,NULL,7),(20,'Neoceptin R','Antacid for indigestion and acid reflux.',40,120,NULL,NULL,7),(21,'Domperon','Tablet for nausea and vomiting.',50,150,NULL,NULL,7),(22,'Aspirin','Blood thinner to prevent heart attacks.',5,500,NULL,NULL,8),(23,'Clopidogrel','Medicine for heart disease and stroke prevention.',20,300,NULL,NULL,8),(24,'Atorvastatin','Cholesterol-lowering medication.',35,400,NULL,NULL,8),(25,'Metforal 500','Oral medicine for diabetes.',30,300,NULL,NULL,9),(26,'Gluformin','Metformin tablet for blood sugar control.',25,250,NULL,NULL,9),(27,'Insulatard','Insulin for diabetes management.',700,50,NULL,NULL,9),(28,'Tobradex','Eye drops for bacterial eye infections.',120,30,NULL,NULL,10),(29,'Refresh Tears','Eye drops for dry eyes.',200,20,NULL,NULL,10),(30,'Zaditen','Eye drops for allergy relief.',150,25,NULL,NULL,10),(31,'Paracil 120','Paracetamol syrup for fever and pain.',40,100,NULL,NULL,11),(32,'Histacin Syrup','Syrup for allergies in children.',50,90,NULL,NULL,11),(33,'Orsaline-N','Oral rehydration solution for dehydration.',10,300,NULL,NULL,11),(34,'Femisol','Tablet for menstrual pain relief.',80,100,NULL,NULL,12),(35,'Calcium D','Calcium and vitamin D supplement for women.',150,50,NULL,NULL,12),(36,'Primolut-N','Tablet for menstrual cycle management.',90,60,NULL,NULL,12),(37,'Menabol','Supplement for testosterone support.',120,40,NULL,NULL,13),(38,'Proviron','Medicine for male infertility.',500,20,NULL,NULL,13),(39,'Tadalafil','Medicine for erectile dysfunction.',600,15,NULL,NULL,13),(40,'Sertraline','Medicine for depression and anxiety.',250,30,NULL,NULL,14),(41,'Olanzapine','Tablet for bipolar disorder and schizophrenia.',300,20,NULL,NULL,14),(42,'Alprazolam','Medicine for anxiety and panic disorders.',200,25,NULL,NULL,14),(43,'Savlon Antiseptic Cream','Cream for minor wounds and cuts.',50,80,NULL,NULL,15),(44,'Betadine','Antiseptic solution for wound cleaning.',60,70,NULL,NULL,15),(45,'Hydrocortisone Cream','Cream for itch relief and inflammation.',100,30,NULL,NULL,15),(46,'Salbutamol','Inhaler for asthma relief.',250,60,NULL,NULL,16),(47,'Montelukast','Tablet for asthma and allergy management.',200,50,NULL,NULL,16),(48,'Ventolin','Nebulizer solution for respiratory conditions.',300,40,NULL,NULL,16),(49,'Arthralgia Oil','Herbal oil for joint pain relief.',150,40,NULL,NULL,17),(50,'Liveraid Capsule','Herbal liver support supplement.',100,30,NULL,NULL,17),(51,'Tulsi Tablet','Herbal tablet for immunity boosting.',90,50,NULL,NULL,17),(52,'Orlistat','Medicine for weight loss.',500,20,NULL,NULL,18),(53,'Slimfast','Weight loss supplement.',600,15,NULL,NULL,18),(54,'Fat Burner Plus','Herbal medicine for fat burning.',450,10,NULL,NULL,18),(55,'Zincovit','Zinc and multivitamin supplement.',80,100,NULL,NULL,19),(56,'Emergen-C','Vitamin C supplement for immune support.',120,50,NULL,NULL,19),(57,'Immunace','Supplement for enhancing immunity.',150,40,NULL,NULL,19),(58,'Sensodyne Toothpaste','Toothpaste for sensitive teeth.',200,60,NULL,NULL,20),(59,'Corsodyl Mouthwash','Mouthwash for gum care.',250,50,NULL,NULL,20),(60,'Colgate Herbal Toothpaste','Toothpaste with herbal extracts.',100,70,NULL,NULL,20),(61,'Monas 10','For asthma and allergic rhinitis',300,50,NULL,0,13),(63,'aaaab','aaab',300,5,NULL,0,19),(65,'Azmasol Inhaler','For asthma',240,100,NULL,0,13),(66,'aaaaaaaaaaaaaa','aaaaaaaaaaaaaaa',10,10,NULL,0,23),(67,'aaaaaa','aaaaaaab',300,10,NULL,0,23);
/*!40000 ALTER TABLE `medicines` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3,'Md. Rafiul Islam','rafit991@gmail.com','rafit991','Zigatola, Dhanmondi','01845904415','customer','customer'),(4,'Test User','test@example.com','testpassword',NULL,NULL,'customer','customer'),(8,'test111','test1@gmail.com','test1234',NULL,'12345678901','customer','customer'),(10,'Rafit','rafit@admin.com','rafit123',NULL,NULL,'admin','admin'),(43,'wasi','wasi@admin.com','wasi1234','Shantinagar','0168234342','admin','admin'),(44,'Rafu','rafu@staff.com','rafu1234','Eije Ekhaneiiiiiii','121313241','staff','staff'),(46,'Shutupp','shut@up.com','12345678','Eije','1234567890','customer','customer'),(47,'Hello Ji','hello@ji.com','hello123','None','12345678901','customer','customer'),(48,'Lmao','lmao@gg.com','lmao1234','None','12345678901','customer','customer'),(49,'Abcd','ab@cd.com','12345678',NULL,'01812345679','customer','customer'),(50,'Skibidi','skibidi@rizz.com','skibidi123','','12369696969','customer','customer'),(51,'Raihan','raihan@gmail.com','raihan123','','01889122334','customer','customer'),(52,'Rafi','rafi@gmail.com','rafi1234','','01912234567','customer','customer');
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

-- Dump completed on 2025-04-28 19:44:24
