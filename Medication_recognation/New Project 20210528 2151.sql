-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.19


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema db_medicine
--

CREATE DATABASE IF NOT EXISTS db_medicine;
USE db_medicine;

--
-- Definition of table `tbl_medicine`
--

DROP TABLE IF EXISTS `tbl_medicine`;
CREATE TABLE `tbl_medicine` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `brand_name` varchar(45) NOT NULL,
  `type_` varchar(45) NOT NULL,
  `text_` varchar(45) NOT NULL,
  `use_` varchar(450) NOT NULL,
  `mfg` varchar(45) NOT NULL,
  `expiry` varchar(45) NOT NULL,
  `dosage` varchar(450) NOT NULL,
  `colour` varchar(45) NOT NULL,
  `l_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_medicine`
--

/*!40000 ALTER TABLE `tbl_medicine` DISABLE KEYS */;
INSERT INTO `tbl_medicine` (`id`,`name`,`brand_name`,`type_`,`text_`,`use_`,`mfg`,`expiry`,`dosage`,`colour`,`l_name`) VALUES 
 (2,'Pilogo','leeford','capsule','',' it is used in piles, doses are as follow:','25-Mar-20','06-Sep-22','3 times a day','blue','1.jpg'),
 (3,'Dailyglim','leeford','tablet','','Medicine name is dailyglim, it is used in sugar, doses are as follow: thrice a day .\'','16-Oct-19','15-Feb-23','3 times a day','while blue','2.jpg'),
 (4,'Geomax D3','leeford','capsule','','Medicine name is geomax, it is used to boost calcium, doses are as follow: thrice a day .\'','24-Jan-20','04-Apr-21','3 times a day','red','3.jpg'),
 (5,'Ural','Vasu','capsule','vasu','Medicine name is ural, it is used for urine infections, doses are as follow: thrice a day .\'','12-Mar-20','27-May-22','3 times a day','blue yellow','4.jpg'),
 (6,'Okacet','cipla','tablet','','Medicine name is okacet, it is used in cold, doses are as follow: thrice a day .\'','17-Jul-20','19-Aug-22','3 times a day','while','5.jpg'),
 (7,'Telmigen','troikka pharma','tablet','','Medicine name is telmigen, it is used in sugar, doses are as follow: thrice a day .\'','19-Jan-19','11-Mar-22','3 times a day','pink white','6.jpg'),
 (8,'Spasmonil','cipla','tablet','','Medicine name is spasmonil, it is used in stomach pain, doses are as follow: thrice a day .\'','17-Nov-20','25-Mar-23','3 times a day','white','7.jpg'),
 (9,'Lynx 500','Lynx','capsule','lynx','Medicine name is lynx 500, it is used as antibiotic, doses are as follow: thrice a day .\'','26-Jan-20','16-Sep-23','3 times a day','red green','8.jpg'),
 (10,'Cipcoz','leeford','tablet','','Medicine name is cipcoz, it is used as antibiotic, doses are as follow: thrice a day .\'','26-Mar-20','11-Feb-21','3 times a day','white','9.jpg'),
 (11,'Zandu Vigorax','emami','capsule','zandu ','Medicine name is zandu vigorax, it is used for stamina, doses are as follow: thrice a day .\'','11-Jan-19','30-Sep-20','3 times a day','golden','10.jpg'),
 (12,'Aclomate','ajnata pharma','tablet','','Medicine name is aclomate , it is used for controlling blood pressure, doses are as follow: thrice a day .\'','13-May-19','17-Jun-21','3 times a day','white yellow','11.jpg'),
 (13,'Febutax','leeford','tablet','','Medicine name is febutax , it is used for gout , doses are as follow: thrice a day .\'','11-Jul-19','21-Apr-22','3 times a day','orange ','12.jpg'),
 (14,'CetJoint','leeford','capsule','','Medicine name is cetjoint, it is used for bone recovery , doses are as follow: thrice a day .\'','21-May-20','09-Feb-22','3 times a day','red white','13.jpg'),
 (15,'Becosules','pfizer limited','capsule','becosules','Medicine name is becosules , it is used for vitamin b , doses are as follow: thrice a day .\'','20-Dec-20','20-May-22','3 times a day','orange black','14.jpg'),
 (16,'Femozar','leeford','capsule','','Medicine name is femozar, it is used as pain killer , doses are as follow: thrice a day .\'','11-Sep-19','31-Jan-22','3 times a day','red','15.jpg'),
 (17,'zosert','sunpharma','tablet','','Medicine name is zosert, it is used as anti depressants , doses are as follow: thrice a day .\'','21-May-18','08-Mar-21','3 times a day','blue','16.jpg'),
 (18,'Sugar Away','international herbal','tablet','','Medicine name is sugaraway , it is used for controlling sugar .\'','20-03-2020','09-Jan-21','3 times a day','wooden brown','17.jpg'),
 (19,'Roko','cipla','capsule','','Medicine name is roko, it is used for cough\'','23-Mar-20','25-Dec-23','3 times a day','yellow','18.jpg'),
 (20,'Escipil','leeford','tablet','','Medicine name is escipil, it is used for sleep , doses are as follow: thrice a day .\'','11-Jan-19','21-Feb-21','3 times a day','yellow','19.jpg'),
 (21,'Mucolite','Dr Reddy','tablet','','Medicine name is mucolite, it is used for cough and cold, doses are as follow: thrice a day .\'','17-Feb-19','13-Dec-21','3 times a day','white','20.jpg'),
 (22,'Pamonext','Cadila','tablet','','Medicine name is pamonext, it is used for controlling multi vitamin, doses are as follow: thrice a day .\'','21-Mar-20','13-Sep-22','3 times a day','light brown','21.jpg'),
 (23,'Crocin','gsk group','tablet','crocin','Medicine name is crocin , it is used for headache, doses are as follow: thrice a day .\'','19-May-18','21-Feb-22','3 times a day','white','22.jpg'),
 (24,'Plaros','ajnata pharma','tablet','','Medicine name is plaros , it is used for blood thinning , doses are as follow: thrice a day .\'','21-May-19','25-Mar-22','3 times a day','light brown','23.jpg'),
 (26,'vitamine_c','pfizer','pill','capsules','immunity','2021-03-03','2021-03-24','1-1-1','white','vitamine_c.jpg');
/*!40000 ALTER TABLE `tbl_medicine` ENABLE KEYS */;


--
-- Definition of table `tbl_patient`
--

DROP TABLE IF EXISTS `tbl_patient`;
CREATE TABLE `tbl_patient` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `r_mobile` varchar(45) NOT NULL,
  `disease` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_patient`
--

/*!40000 ALTER TABLE `tbl_patient` DISABLE KEYS */;
INSERT INTO `tbl_patient` (`id`,`name`,`password`,`email`,`mobile`,`address`,`r_mobile`,`disease`) VALUES 
 (1,'pramod','pramod','thephoenixzone@gmail.com','9890430022','pune','9890430022','covid'),
 (2,'dinesh','dinesh','dinesh@gmail.com','7350706868','sangamner','7350706868','diabetic'),
 (3,'vivek','vivek123@','vivek@gmail.com','9890430022','pune','7350706868','diabetic');
/*!40000 ALTER TABLE `tbl_patient` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
