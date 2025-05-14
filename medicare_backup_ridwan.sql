-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2025 at 07:42 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medicare`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `admins`:
--   `id`
--       `users` -> `id`
--

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`) VALUES
(10),
(43);

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--
-- Creation: May 12, 2025 at 05:07 PM
--

DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `alembic_version`:
--

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('54b48e0cbe88');

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--
-- Creation: May 12, 2025 at 05:07 PM
--

DROP TABLE IF EXISTS `appointments`;
CREATE TABLE `appointments` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time_slot` varchar(50) NOT NULL,
  `message` varchar(255) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `requested_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `appointments`:
--   `customer_id`
--       `customers` -> `id`
--   `doctor_id`
--       `doctors` -> `id`
--

-- --------------------------------------------------------

--
-- Table structure for table `carts`
--
-- Creation: May 06, 2025 at 05:26 AM
-- Last update: May 14, 2025 at 05:39 AM
--

DROP TABLE IF EXISTS `carts`;
CREATE TABLE `carts` (
  `id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `medicine_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `carts`:
--   `customer_id`
--       `users` -> `id`
--   `medicine_id`
--       `medicines` -> `id`
--

--
-- Dumping data for table `carts`
--

INSERT INTO `carts` (`id`, `quantity`, `customer_id`, `medicine_id`) VALUES
(81, 1, 3, 77),
(82, 1, 3, 93),
(129, 1, 54, 77);

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `categories`:
--

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `description`) VALUES
(1, 'Vitamins and Supplements', 'Health supplements and multivitamins.'),
(2, 'Skin Care', 'Medicines and creams for skin care and treatments.'),
(3, 'Allergy Relief', 'Medicines to manage and treat allergies.'),
(4, 'Digestive Health', 'Medicines for digestive system care, such as antacids and laxatives.'),
(5, 'Heart Health', 'Medicines for cardiovascular health and blood pressure management.'),
(6, 'Diabetes Care', 'Medicines and supplies for managing diabetes.'),
(7, 'Eye Care', 'Drops and medicines for eye health and infections.'),
(8, 'Child Health', 'Medicines specifically formulated for children.'),
(9, 'Women\'s Health', 'Medicines for women-specific health conditions.'),
(10, 'Men\'s Health', 'Medicines for men-specific health conditions.'),
(11, 'Mental Health', 'Medicines for mental health and neurological disorders.'),
(12, 'First Aid', 'Medicines and items for immediate first aid care.'),
(13, 'Respiratory Health', 'Medicines for asthma and other respiratory conditions.'),
(14, 'Herbal Remedies', 'Natural and herbal medicine options.'),
(15, 'Weight Management', 'Medicines and supplements for weight loss or gain.'),
(16, 'Immunity Boosters', 'Supplements and medicines to enhance immunity.'),
(17, 'Dental Care', 'Medicines and products for oral health and dental care.'),
(18, 'Antibiotics', 'Medicines used to treat bacterial infections.'),
(19, 'Pain Relief', 'Medicines for reducing pain and inflammation.'),
(20, 'Cold and Cough Relief', 'Medicines for relieving cold, cough, and flu symptoms.');

-- --------------------------------------------------------

--
-- Table structure for table `chats`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `chats`;
CREATE TABLE `chats` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `is_from_customer` tinyint(1) DEFAULT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `chats`:
--   `customer_id`
--       `users` -> `id`
--

--
-- Dumping data for table `chats`
--

INSERT INTO `chats` (`id`, `customer_id`, `message`, `is_from_customer`, `is_read`, `timestamp`) VALUES
(1, 3, 'Hello, I have a question about my recent order.', 1, 1, '2025-04-23 16:39:37'),
(2, 3, 'What is your question? I\'m here to help.', 0, 1, '2025-04-23 17:39:37'),
(3, 3, 'I ordered Paracetamol but received Aspirin instead. Can you help?', 1, 1, '2025-04-24 16:39:37'),
(4, 3, 'I apologize for the mix-up. We\'ll send the correct medicine right away.', 0, 1, '2025-04-24 17:09:37'),
(5, 3, 'Thank you! When can I expect the delivery?', 1, 1, '2025-04-25 11:39:41'),
(11, 3, 'Hello, I need help with a prescription upload.', 1, 1, '2025-04-25 10:40:40'),
(12, 3, 'The site says my file format is not supported. What formats can I use?', 1, 1, '2025-04-25 11:40:41'),
(13, 3, 'you need to upload jpeg picture files', 0, 1, '2025-04-25 10:41:20'),
(14, 3, 'okay', 0, 1, '2025-04-25 10:50:22'),
(15, 51, 'Can I get a refill on my previous prescription?', 1, 1, '2025-04-24 10:15:00'),
(16, 52, 'Your prescription has been refilled and is ready for delivery.', 0, 1, '2025-04-24 11:00:00'),
(17, 51, 'yes sure', 0, 1, '2025-04-25 11:12:12'),
(18, 51, 'hello, you there?', 0, 1, '2025-04-25 11:33:54'),
(19, 52, 'ji', 0, 1, '2025-04-25 11:35:16'),
(20, 51, 'kire bhai', 0, 1, '2025-04-25 11:41:58'),
(21, 51, 'hey', 0, 1, '2025-04-26 19:26:21'),
(22, 3, 'jpeg', 0, 1, '2025-04-26 19:26:39'),
(23, 3, 'okay', 1, 1, '2025-04-30 17:21:35'),
(24, 3, 'did you get your delivery?', 0, 1, '2025-04-30 17:22:23'),
(25, 3, 'not yet', 1, 1, '2025-04-30 17:31:36'),
(26, 3, 'than you for you patience sir', 0, 1, '2025-04-30 17:32:31'),
(27, 3, '.', 1, 1, '2025-04-30 17:47:31'),
(28, 3, 'lesgoooooooooo', 1, 1, '2025-04-30 17:48:41'),
(29, 3, '.', 0, 1, '2025-04-30 18:16:28'),
(30, 3, 'gg', 0, 1, '2025-04-30 18:34:57'),
(31, 3, 'wp', 1, 1, '2025-04-30 18:35:17'),
(32, 3, 'ty', 0, 1, '2025-04-30 18:42:46'),
(33, 3, 'okay', 1, 1, '2025-04-30 18:49:36'),
(34, 3, 'okay', 1, 1, '2025-04-30 18:54:46'),
(35, 3, 'gg', 1, 1, '2025-04-30 18:54:52'),
(36, 3, 'gg', 1, 1, '2025-04-30 18:54:52'),
(37, 3, 'gg', 1, 1, '2025-04-30 18:54:52'),
(38, 3, 'gg', 1, 1, '2025-04-30 18:54:53'),
(39, 3, 'oye', 1, 1, '2025-04-30 18:56:03'),
(40, 3, 'eeeeeeeeeeee', 1, 1, '2025-04-30 19:00:00'),
(41, 3, 'oye', 1, 1, '2025-04-30 19:06:08'),
(42, 3, 'thank god', 1, 1, '2025-04-30 19:07:14'),
(43, 3, 'yes yes yes', 0, 1, '2025-04-30 19:11:48'),
(44, 3, '.', 0, 1, '2025-04-30 19:13:20'),
(45, 3, 'hmm', 0, 1, '2025-04-30 19:15:04'),
(46, 3, 'shei shei', 0, 1, '2025-04-30 19:15:09'),
(47, 50, 'hello i want to ask something', 1, 1, '2025-04-30 19:20:48'),
(48, 50, 'sure sir, how can i help?', 0, 1, '2025-04-30 19:21:22'),
(49, 50, 'hello, this is staff', 0, 1, '2025-05-01 10:36:44'),
(50, 50, 'damn', 1, 1, '2025-05-01 10:37:13'),
(51, 50, 'yessir', 0, 1, '2025-05-02 11:29:21'),
(52, 50, 'ji', 0, 1, '2025-05-02 11:31:30'),
(53, 50, 'yooooooooooooo', 1, 1, '2025-05-02 11:31:44'),
(54, 50, 'is it working?', 0, 1, '2025-05-02 11:38:12'),
(55, 50, 'i think so', 1, 1, '2025-05-02 11:38:36'),
(56, 50, 'ahem', 0, 1, '2025-05-02 11:45:43'),
(57, 50, 'hu', 0, 1, '2025-05-02 11:45:57'),
(58, 50, 'sure', 0, 1, '2025-05-02 11:47:14'),
(59, 50, 'okay', 1, 1, '2025-05-02 11:47:33'),
(60, 50, 'uf', 1, 1, '2025-05-02 11:58:54'),
(61, 50, 'o', 1, 1, '2025-05-02 11:58:57'),
(62, 50, 'siu', 1, 1, '2025-05-02 11:59:02'),
(63, 50, 'eeeeeeeeeeee', 1, 1, '2025-05-02 12:10:30'),
(64, 50, 'hehe', 1, 1, '2025-05-02 12:10:42'),
(65, 50, 'lesgooo', 1, 1, '2025-05-02 12:10:46'),
(66, 50, 'yeah it\'s fixed now', 0, 1, '2025-05-02 12:15:36'),
(67, 50, 'perfecto', 1, 1, '2025-05-02 12:18:52'),
(68, 46, 'hello?', 1, 0, '2025-05-13 20:57:59');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `customers`:
--   `id`
--       `users` -> `id`
--

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`) VALUES
(3),
(8),
(46),
(48),
(49),
(50),
(51),
(52),
(53),
(54);

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--
-- Creation: May 12, 2025 at 05:07 PM
--

DROP TABLE IF EXISTS `doctors`;
CREATE TABLE `doctors` (
  `id` int(11) NOT NULL,
  `specialization` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `doctors`:
--   `id`
--       `users` -> `id`
--

-- --------------------------------------------------------

--
-- Table structure for table `medicines`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `medicines`;
CREATE TABLE `medicines` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` float NOT NULL,
  `stock` int(11) NOT NULL,
  `expiry_date` date DEFAULT NULL,
  `low_stock_flag` tinyint(1) DEFAULT NULL,
  `category_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `medicines`:
--   `category_id`
--       `categories` -> `id`
--

--
-- Dumping data for table `medicines`
--

INSERT INTO `medicines` (`id`, `name`, `description`, `price`, `stock`, `expiry_date`, `low_stock_flag`, `category_id`) VALUES
(69, 'Vitamin C 500mg', 'Boosts immunity and overall health.', 8.99, 100, NULL, NULL, 1),
(70, 'Multivitamin Capsules', 'Daily nutritional supplement.', 12.49, 150, NULL, NULL, 1),
(71, 'Omega-3 Fish Oil', 'Supports heart and brain health.', 15, 80, NULL, NULL, 1),
(72, 'Hydrocortisone Cream', 'For skin irritations and rashes.', 5.25, 50, NULL, NULL, 2),
(73, 'Acne Control Gel', 'Treats acne and pimples.', 7.95, 5, NULL, NULL, 2),
(74, 'Moisturizing Lotion', 'Hydrates dry skin.', 6.75, 100, NULL, NULL, 2),
(75, 'Cetirizine Tablets', 'Relieves allergy symptoms.', 4.99, 200, NULL, NULL, 3),
(76, 'Loratadine 10mg', 'Non-drowsy allergy relief.', 5.5, 180, NULL, NULL, 3),
(77, 'Allergy Eye Drops', 'Reduces eye itchiness from allergies.', 6.3, 90, NULL, NULL, 3),
(78, 'Antacid Tablets', 'Neutralizes stomach acid.', 3.2, 100, NULL, NULL, 4),
(79, 'Laxative Syrup', 'Relieves constipation.', 4.75, 70, NULL, NULL, 4),
(80, 'Probiotic Capsules', 'Supports digestive balance.', 11.25, 60, NULL, NULL, 4),
(81, 'Aspirin 81mg', 'Supports heart health.', 2.99, 120, NULL, NULL, 5),
(82, 'Atorvastatin 20mg', 'Lowers cholesterol.', 10.45, 80, NULL, NULL, 5),
(83, 'Blood Pressure Monitor', 'Tracks blood pressure.', 25, 20, NULL, NULL, 5),
(84, 'Insulin Pen', 'Helps manage blood sugar.', 30, 40, NULL, NULL, 6),
(85, 'Glucose Test Strips', 'For blood sugar testing.', 18.5, 100, NULL, NULL, 6),
(86, 'Metformin 500mg', 'Controls blood sugar levels.', 7.99, 150, NULL, NULL, 6),
(87, 'Lubricant Eye Drops', 'Relieves dry eyes.', 4.5, 70, NULL, NULL, 7),
(88, 'Antibiotic Eye Drops', 'Treats eye infections.', 6.25, 60, NULL, NULL, 7),
(89, 'Eye Vitamin Supplement', 'Supports vision health.', 9.9, 50, NULL, NULL, 7),
(90, 'Paracetamol for Kids', 'Pain and fever relief for kids.', 3.4, 100, NULL, NULL, 8),
(91, 'Multivitamin Syrup', 'Nutritional supplement for kids.', 6.8, 80, NULL, NULL, 8),
(92, 'Cough Syrup for Kids', 'Soothes cough in children.', 5.1, 70, NULL, NULL, 8),
(93, 'Iron Tablets', 'Supports women health.', 4.95, 90, NULL, NULL, 9),
(94, 'Folic Acid 400mcg', 'Prenatal supplement.', 3.75, 120, NULL, NULL, 9),
(95, 'Menstrual Pain Relief', 'Relieves period cramps.', 6.6, 80, NULL, NULL, 9),
(96, 'Vitality Capsules', 'Supports male vitality.', 20, 30, NULL, NULL, 10),
(97, 'Hair Growth Supplement', 'Promotes hair health.', 12.5, 45, NULL, NULL, 10),
(98, 'Prostate Support', 'Supports prostate function.', 14.3, 50, NULL, NULL, 10),
(99, 'Sertraline 50mg', 'Treats depression and anxiety.', 9, 60, NULL, NULL, 11),
(100, 'Melatonin 3mg', 'Promotes better sleep.', 7.2, 80, NULL, NULL, 11),
(101, 'Brain Boost Omega-3', 'Supports cognitive health.', 13.75, 40, NULL, NULL, 11),
(102, 'Antiseptic Cream', 'Prevents infection in minor cuts.', 3.95, 100, NULL, NULL, 12),
(103, 'Bandage Roll', 'Sterile wound dressing.', 2.5, 150, NULL, NULL, 12),
(104, 'Burn Relief Spray', 'Cools and soothes burns.', 4.8, 60, NULL, NULL, 12),
(105, 'Inhaler Salbutamol', 'Relieves asthma symptoms.', 8, 70, NULL, NULL, 13),
(106, 'Cough Suppressant Syrup', 'Soothes persistent cough.', 5.3, 90, NULL, NULL, 13),
(107, 'Steam Inhaler', 'Clears nasal congestion.', 22, 25, NULL, NULL, 13),
(108, 'Tulsi Drops', 'Boosts immunity naturally.', 4.2, 60, NULL, NULL, 14),
(109, 'Ashwagandha Capsules', 'Reduces stress.', 10.25, 50, NULL, NULL, 14),
(110, 'Neem Tablets', 'Supports skin health.', 5.6, 70, NULL, NULL, 14),
(111, 'Green Tea Extract', 'Boosts metabolism.', 8.99, 80, NULL, NULL, 15),
(112, 'Meal Replacement Shake', 'Supports weight loss.', 14.99, 50, NULL, NULL, 15),
(113, 'Appetite Suppressant', 'Controls hunger cravings.', 11.75, 30, NULL, NULL, 15),
(114, 'Zinc Tablets', 'Supports immune function.', 3.9, 100, NULL, NULL, 16),
(115, 'Elderberry Syrup', 'Natural immune support.', 7.45, 60, NULL, NULL, 16),
(116, 'Vitamin D3 1000IU', 'Boosts immunity.', 6.3, 90, NULL, NULL, 16),
(117, 'Toothache Relief Gel', 'Numbs dental pain.', 4, 100, NULL, NULL, 17),
(118, 'Fluoride Mouthwash', 'Protects against cavities.', 5.75, 70, NULL, NULL, 17),
(119, 'Sensitive Toothpaste', 'Reduces tooth sensitivity.', 6.5, 80, NULL, NULL, 17),
(120, 'Amoxicillin 500mg', 'Treats bacterial infections.', 8, 100, NULL, NULL, 18),
(121, 'Azithromycin 250mg', 'Broad-spectrum antibiotic.', 9.5, 80, NULL, NULL, 18),
(122, 'Ciprofloxacin 500mg', 'Used for various infections.', 7.6, 90, NULL, NULL, 18),
(123, 'Ibuprofen 400mg', 'Reduces pain and inflammation.', 4.2, 150, NULL, NULL, 19),
(124, 'Paracetamol 500mg', 'Common pain reliever.', 3.8, 200, NULL, NULL, 19),
(125, 'Diclofenac Gel', 'Topical pain relief.', 6, 60, NULL, NULL, 19),
(126, 'Cold Relief Tablets', 'Relieves cold symptoms.', 4.95, 120, NULL, NULL, 20),
(127, 'Cough Drops', 'Soothes sore throat.', 2.99, 200, NULL, NULL, 20),
(128, 'Flu Care Syrup', 'Fights flu symptoms.', 6.25, 90, NULL, NULL, 20);

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--
-- Creation: May 12, 2025 at 05:03 PM
--

DROP TABLE IF EXISTS `notifications`;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `notification_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `notifications`:
--   `staff_id`
--       `users` -> `id`
--

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`id`, `staff_id`, `message`, `is_read`, `timestamp`, `notification_type`) VALUES
(1, 44, 'napa is about get stocked out', 1, '2025-05-01 10:50:38', 'stock_alert'),
(2, 44, 'the user id 50 did not receive the order', 1, '2025-05-01 10:51:01', 'order_issue'),
(3, 44, 'Since, eid is coming, we will stop accepting orders from tomorrow', 1, '2025-05-01 10:51:55', 'general'),
(4, 44, 'hmm', 1, '2025-05-01 10:56:01', 'general'),
(5, 44, 'siu', 1, '2025-05-02 14:37:55', 'stock_alert'),
(6, 44, 'cr7', 1, '2025-05-02 14:38:34', 'general'),
(7, 44, 'lesgooooooooooooooooooooo', 1, '2025-05-05 16:19:15', 'general'),
(8, 44, 'nokia', 1, '2025-05-05 16:29:01', 'general'),
(9, 44, 'dawdasd', 1, '2025-05-05 16:45:50', 'stock_alert'),
(10, 44, 'adsasdawd', 1, '2025-05-05 16:45:54', 'system_alert'),
(11, 44, 'adwadasgwe', 1, '2025-05-05 16:45:58', 'system_alert'),
(12, 44, 'siuuuuuuuuuuuuuuuu\r\n', 1, '2025-05-05 16:53:19', 'general'),
(13, 44, '1', 1, '2025-05-05 16:53:21', 'stock_alert'),
(14, 44, '2', 1, '2025-05-05 16:53:23', 'stock_alert'),
(15, 44, '3', 1, '2025-05-05 16:53:24', 'stock_alert'),
(16, 44, '4', 1, '2025-05-05 16:53:25', 'stock_alert'),
(17, 44, '5', 1, '2025-05-05 16:53:27', 'stock_alert'),
(18, 44, '6', 1, '2025-05-05 16:53:29', 'stock_alert'),
(19, 44, '7', 1, '2025-05-05 17:04:20', 'stock_alert'),
(20, 44, '8', 1, '2025-05-05 17:04:22', 'stock_alert'),
(21, 44, '9', 1, '2025-05-05 17:04:24', 'stock_alert'),
(22, 44, '10', 1, '2025-05-05 17:04:28', 'stock_alert'),
(23, 44, '11', 1, '2025-05-05 17:07:31', 'stock_alert'),
(24, 44, '12', 1, '2025-05-05 17:07:32', 'stock_alert'),
(25, 44, '13', 1, '2025-05-05 17:07:34', 'stock_alert'),
(26, 44, '14', 1, '2025-05-05 17:07:35', 'stock_alert'),
(27, 44, 'last test\r\n', 1, '2025-05-05 17:11:44', 'general');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--
-- Creation: May 14, 2025 at 02:33 AM
-- Last update: May 14, 2025 at 05:39 AM
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `total_price` float NOT NULL,
  `status` varchar(50) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `payment_status` varchar(50) NOT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  `bkash_number` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `orders`:
--   `customer_id`
--       `users` -> `id`
--

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `customer_id`, `order_date`, `total_price`, `status`, `payment_method`, `payment_status`, `transaction_id`, `bkash_number`) VALUES
(55, 46, '2025-05-14 03:40:25', 34.5, 'Delivered', 'Cash on Delivery', 'Paid', NULL, NULL),
(56, 46, '2025-05-14 03:40:58', 56.75, 'Pending', 'bKash', 'Pending', 'abdcdassadasdsdasda', '01728345647'),
(57, 46, '2025-05-14 03:49:47', 7.95, 'Dispatched for Delivery', 'Cash on Delivery', 'Pending', NULL, NULL),
(58, 46, '2025-05-14 04:03:19', 16.5, 'Pending', 'Cash on Delivery', 'Pending', NULL, NULL),
(64, 54, '2025-05-14 04:58:16', 14.25, 'Pending', 'Cash on Delivery', 'Pending', NULL, NULL),
(65, 46, '2025-05-14 05:28:17', 14.3, 'Pending', 'Cash on Delivery', 'Pending', NULL, NULL),
(66, 46, '2025-05-14 05:39:19', 8, 'Pending', 'Cash on Delivery', 'Pending', NULL, NULL),
(67, 46, '2025-05-14 05:39:48', 14.25, 'Pending', 'Cash on Delivery', 'Pending', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `order_details`;
CREATE TABLE `order_details` (
  `id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` float NOT NULL,
  `order_id` int(11) NOT NULL,
  `medicine_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `order_details`:
--   `order_id`
--       `orders` -> `id`
--   `medicine_id`
--       `medicines` -> `id`
--

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--
-- Creation: May 13, 2025 at 03:46 PM
--

DROP TABLE IF EXISTS `order_items`;
CREATE TABLE `order_items` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `medicine_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `order_items`:
--   `order_id`
--       `orders` -> `id`
--   `medicine_id`
--       `medicines` -> `id`
--

-- --------------------------------------------------------

--
-- Table structure for table `prescriptions`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `prescriptions`;
CREATE TABLE `prescriptions` (
  `id` int(11) NOT NULL,
  `file_path` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `prescriptions`:
--   `customer_id`
--       `users` -> `id`
--

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `staff`:
--   `id`
--       `users` -> `id`
--

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`) VALUES
(44);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--
-- Creation: May 06, 2025 at 05:26 AM
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `role` varchar(20) NOT NULL,
  `type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELATIONSHIPS FOR TABLE `users`:
--

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `address`, `phone`, `role`, `type`) VALUES
(3, 'Md. Rafiul Islam', 'rafit991@gmail.com', 'rafit991', 'Zigatola, Dhanmondi', '01845904415', 'customer', 'customer'),
(4, 'Test User', 'test@example.com', 'testpassword', NULL, NULL, 'customer', 'customer'),
(8, 'test111', 'test1@gmail.com', 'test1234', NULL, '12345678901', 'customer', 'customer'),
(10, 'rafitboo', 'rafit@admin.com', 'rafit123', 'romjan bus', '2345678910', 'admin', 'admin'),
(43, 'wasi', 'wasi@admin.com', 'wasi1234', 'Shantinagar', '0168234342', 'admin', 'admin'),
(44, 'Rafu', 'rafu@staff.com', 'rafu1234', 'Eije Ekhaneiiiiiii', '121313241', 'staff', 'staff'),
(46, 'Shutupp', 'shut@up.com', '12345678', 'Eije', '1234567890', 'customer', 'customer'),
(47, 'Hello Ji', 'hello@ji.com', 'hello123', 'None', '12345678901', 'customer', 'customer'),
(48, 'Lmao', 'lmao@gg.com', 'lmao1234', 'None', '12345678901', 'customer', 'customer'),
(49, 'Abcd', 'ab@cd.com', '12345678', NULL, '01812345679', 'customer', 'customer'),
(50, 'Skibidi', 'skibidi@rizz.com', 'skibidi123', '', '12369696969', 'customer', 'customer'),
(51, 'Raihan', 'raihan@gmail.com', 'raihan123', '', '01889122334', 'customer', 'customer'),
(52, 'Rafi', 'rafi@gmail.com', 'rafi1234', '', '01912234567', 'customer', 'customer'),
(53, 'Lesgooooooooo', 'lsg@oo.com', 'lesgo123', NULL, '271378162197', 'customer', 'customer'),
(54, 'Ridu06', 'arifridwanshadid@gmail.com', '87654321', NULL, '01728345446', 'customer', 'customer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `doctor_id` (`doctor_id`);

--
-- Indexes for table `carts`
--
ALTER TABLE `carts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_cart_item` (`customer_id`,`medicine_id`),
  ADD KEY `medicine_id` (`medicine_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicines`
--
ALTER TABLE `medicines`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `staff_id` (`staff_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `medicine_id` (`medicine_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `medicine_id` (`medicine_id`);

--
-- Indexes for table `prescriptions`
--
ALTER TABLE `prescriptions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointments`
--
ALTER TABLE `appointments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `carts`
--
ALTER TABLE `carts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `chats`
--
ALTER TABLE `chats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `medicines`
--
ALTER TABLE `medicines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;

--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `prescriptions`
--
ALTER TABLE `prescriptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admins`
--
ALTER TABLE `admins`
  ADD CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`);

--
-- Constraints for table `appointments`
--
ALTER TABLE `appointments`
  ADD CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`);

--
-- Constraints for table `carts`
--
ALTER TABLE `carts`
  ADD CONSTRAINT `carts_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `carts_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicines` (`id`);

--
-- Constraints for table `chats`
--
ALTER TABLE `chats`
  ADD CONSTRAINT `chats_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `doctors`
--
ALTER TABLE `doctors`
  ADD CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`);

--
-- Constraints for table `medicines`
--
ALTER TABLE `medicines`
  ADD CONSTRAINT `medicines_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);

--
-- Constraints for table `notifications`
--
ALTER TABLE `notifications`
  ADD CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  ADD CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicines` (`id`);

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicines` (`id`);

--
-- Constraints for table `prescriptions`
--
ALTER TABLE `prescriptions`
  ADD CONSTRAINT `prescriptions_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
