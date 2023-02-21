-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2023 at 05:53 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banking`
--

-- --------------------------------------------------------

--
-- Table structure for table `car_loan`
--

CREATE TABLE `car_loan` (
  `id` int(11) NOT NULL,
  `loan_size` varchar(255) NOT NULL,
  `main_routing` varchar(50) NOT NULL,
  `main_account_number` varchar(50) NOT NULL,
  `apr_payment` varchar(50) NOT NULL,
  `monthly_payment` varchar(50) NOT NULL,
  `external_routing_payment` varchar(50) NOT NULL,
  `external_acc_num_payment` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `compound_investing`
--

CREATE TABLE `compound_investing` (
  `id` int(11) NOT NULL,
  `account_number` varchar(50) NOT NULL,
  `routing` varchar(50) NOT NULL,
  `compound_interest_percent` varchar(255) NOT NULL,
  `invest_num` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `house_loan`
--

CREATE TABLE `house_loan` (
  `id` int(11) NOT NULL,
  `loan_size` varchar(255) NOT NULL,
  `routing` varchar(50) NOT NULL,
  `account_number` varchar(50) NOT NULL,
  `external_routing_payment` varchar(50) NOT NULL,
  `external_acct_num_payment` varchar(50) NOT NULL,
  `apr` varchar(255) NOT NULL,
  `monthly_payment` varchar(255) NOT NULL,
  `payment_due` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `id` int(11) NOT NULL,
  `routing` varchar(50) NOT NULL,
  `account_number` varchar(50) NOT NULL,
  `external_routing_payment` varchar(50) NOT NULL,
  `external_acct_num_payment` varchar(50) NOT NULL,
  `loan_size` varchar(255) NOT NULL,
  `apr` varchar(50) NOT NULL,
  `monthly_payment` varchar(255) NOT NULL,
  `payment_due` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `main_account`
--

CREATE TABLE `main_account` (
  `id` int(11) NOT NULL,
  `checking` varchar(255) NOT NULL,
  `saving` varchar(255) NOT NULL,
  `routing` varchar(50) NOT NULL,
  `account_number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `routing` varchar(50) NOT NULL,
  `account_number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `car_loan`
--
ALTER TABLE `car_loan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `compound_investing`
--
ALTER TABLE `compound_investing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `house_loan`
--
ALTER TABLE `house_loan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_account`
--
ALTER TABLE `main_account`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `car_loan`
--
ALTER TABLE `car_loan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `compound_investing`
--
ALTER TABLE `compound_investing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `house_loan`
--
ALTER TABLE `house_loan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan`
--
ALTER TABLE `loan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_account`
--
ALTER TABLE `main_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
