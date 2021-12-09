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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `customer_cars_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `customers` (`id_customers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_manufacturers_has_cps_orders_cps_orders1` FOREIGN KEY (`cps_orders_internal_order_no`) REFERENCES `cps_orders` (`internal_order_no`),
  CONSTRAINT `fk_manufacturers_has_cps_orders_manufacturers1` FOREIGN KEY (`manufacturers_manufacturer_id`) REFERENCES `manufacturers` (`manufacturer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_orders_customers1` FOREIGN KEY (`customers_id_customers`) REFERENCES `customers` (`id_customers`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_orders_has_products_orders1` FOREIGN KEY (`orders_order_no`) REFERENCES `orders` (`order_no`),
  CONSTRAINT `fk_orders_has_products_products1` FOREIGN KEY (`products_product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`customer_paid_bill_id`) REFERENCES `customers` (`id_customers`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_product_description_table_products1` FOREIGN KEY (`products_description_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_staffs_staffs1` FOREIGN KEY (`reports_to`) REFERENCES `staffs` (`id_staff`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_staffs_has_cps_orders_cps_orders1` FOREIGN KEY (`cps_orders_internal_order_no`) REFERENCES `cps_orders` (`internal_order_no`),
  CONSTRAINT `fk_staffs_has_cps_orders_staffs1` FOREIGN KEY (`staffs_id_staff`) REFERENCES `staffs` (`id_staff`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_staffs_has_customers_customers1` FOREIGN KEY (`customers_id_customers`) REFERENCES `customers` (`id_customers`),
  CONSTRAINT `fk_staffs_has_customers_staffs1` FOREIGN KEY (`staffs_id_staff`) REFERENCES `staffs` (`id_staff`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_storage_has_products_products1` FOREIGN KEY (`products_product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `fk_storage_has_products_storage1` FOREIGN KEY (`storage_storage_id`) REFERENCES `storage` (`storage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk_suppliers_has_cps_orders_cps_orders1` FOREIGN KEY (`cps_orders_internal_order_no`) REFERENCES `cps_orders` (`internal_order_no`),
  CONSTRAINT `fk_suppliers_has_cps_orders_suppliers1` FOREIGN KEY (`suppliers_supplier_id`) REFERENCES `suppliers` (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-06 11:30:28
