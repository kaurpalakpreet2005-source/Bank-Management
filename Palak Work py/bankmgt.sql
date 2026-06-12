-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2026 at 10:58 AM
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
-- Database: `bankmgt`
--

-- --------------------------------------------------------

--
-- Table structure for table `create_table`
--

CREATE TABLE `create_table` (
  `Name` varchar(20) NOT NULL,
  `Account_Type` varchar(15) NOT NULL,
  `Amount` int(10) NOT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Account_no` int(11) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `create_table`
--

INSERT INTO `create_table` (`Name`, `Account_Type`, `Amount`, `Phone_Number`, `Gender`, `DOB`, `Email`, `Account_no`, `Username`, `Password`) VALUES
('Simran Kaur', 'Savings account', 31500, '9872802289', 'Female', '2016-05-01', 'simran12@gmail.com', 12101, 'simrann', 'sim102'),
('Palak', 'Savings account', 6100, '9878280456', 'Female', '2015-05-05', 'palak@gmail.com', 12102, 'palak', '123'),
('Ishpreet Kaur', 'Current account', 26681, '6284028569', 'Female', '2005-02-12', 'ish258@gmail.com', 12103, 'ishkaur', 'ish'),
('Aryan Sharma', 'Savings account', 1000, '9873692678', 'Male', '2003-03-11', 'aryan231@gmail.com', 12104, 'aryansharma', 'aryan231'),
('Ritu', 'Savings account', 11900, '8520758249', 'Female', '1993-09-17', 'ritu1516@gmail.com', 12105, 'rituu', '987'),
('Ayaaz', 'Current account', 2000, '6875248367', 'Male', '2002-11-21', 'ayaaz12@gmail.com', 12106, 'ayaazz', 'ayaz123'),
('Sameer ', 'Current account', 19000, '9654726989', 'Male', '1991-06-04', 'sameerr@gmail.com', 12107, 'sameerrr', 'sam05'),
('Dhruv', 'Current account', 1000, '9823457896', 'Male', '2001-06-27', 'dhruv@gmail.com', 12108, 'dhruv', 'dhruviee'),
('Arzoi', 'Savings account', 1000, '6541583659', 'Female', '2026-01-27', 'arzoi@gmail.com', 12109, 'Arzoi27', 'Arzoii'),
('Ukshu', 'Current account', 2000, '8425367895', 'Male', '2004-07-22', 'ukshu12@gmail.com', 12110, 'Ukshu', 'ukshuuu'),
('Manmeet Kaur', 'Savings account', 5000, '9852368749', 'Female', '2005-05-11', 'man12@gmail.com', 12111, 'Manmeet', 'mann'),
('Keyansh', 'Current account', 1562, '9872568942', 'Male', '2013-05-22', 'keyansh10@gmail.com', 12112, 'Keyansh', 'keyansh'),
('Jasviraj', 'Current account', 5500, '6258745639', 'Male', '2019-06-06', 'jas22@gmail.com', 12113, 'Jasss', 'Jas'),
('Hargun Singh', 'Current account', 2000, '9587254698', 'Male', '2004-09-02', 'hargun14@gmail.com', 12114, 'hargun', 'har'),
('Harjot SIngh', 'Savings account', 18644, '6587425369', 'Male', '2016-06-02', 'harjot5@gmail.com', 12115, 'harjot', 'harjot124'),
('bibek', 'Current account', 44531, '8780973234', 'Male', '2026-06-03', 'bibeksinghgill13@gma', 12116, 'bibek', 'bibek_s13');

-- --------------------------------------------------------

--
-- Table structure for table `deposit`
--

CREATE TABLE `deposit` (
  `Current Balance` int(10) NOT NULL,
  `Amount` int(10) NOT NULL,
  `Updated Balance` int(10) NOT NULL,
  `Description` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Username` varchar(30) NOT NULL,
  `Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `statement`
--

CREATE TABLE `statement` (
  `date` int(10) NOT NULL,
  `withdrawal` int(10) NOT NULL,
  `deposit` int(10) NOT NULL,
  `balance` int(10) NOT NULL,
  `narration` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `S.no.` int(10) NOT NULL,
  `Date` date NOT NULL,
  `Transaction type` varchar(10) NOT NULL,
  `Amount` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `withdraw`
--

CREATE TABLE `withdraw` (
  `Current Balance` int(10) NOT NULL,
  `Amount` int(10) NOT NULL,
  `Updated Balance` int(10) NOT NULL,
  `Description` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `create_table`
--
ALTER TABLE `create_table`
  ADD PRIMARY KEY (`Account_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `create_table`
--
ALTER TABLE `create_table`
  MODIFY `Account_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12117;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
