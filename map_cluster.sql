-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Bulan Mei 2024 pada 06.08
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `map_cluster`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_cluster`
--

CREATE TABLE `data_cluster` (
  `kecamatan` varchar(255) DEFAULT NULL,
  `data_1` int(11) DEFAULT NULL,
  `data_2` int(11) DEFAULT NULL,
  `data_3` int(11) DEFAULT NULL,
  `Latitude` double NOT NULL,
  `Longtitude` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `data_cluster`
--

INSERT INTO `data_cluster` (`kecamatan`, `data_1`, `data_2`, `data_3`, `Latitude`, `Longtitude`) VALUES
('Samarinda Ulu', 26, 25, 24, -0.45194246196740445, 117.11298969051651),
('Samarinda Utara', 56, 48, 54, -0.39712395408742346, 117.21902756585209),
('Sungai Kunjang', 23, 23, 23, -0.5105627926447233, 117.08489800256115),
('Samarinda Kota', 41, 52, 36, -0.4992718369128387, 117.15066750852381),
('Samarinda Seberang', 9, 17, 29, -0.5166479182179353, 117.13172732014654),
('Samarinda Ilir', 56, 69, 61, -0.5072844564117136, 117.16048001560958),
('Sungai Pinang', 18, 20, 16, -0.4697835726695095, 117.19048835189065),
('Sambutan', 21, 33, 57, -0.5251918511640112, 117.21279861104325),
('Palaran', 4, 6, 8, -0.6048267226452794, 117.1833425119649),
('Loa Janan Ilir', 15, 6, 8, -0.5540814604812369, 117.11360385193743);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
