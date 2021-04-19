-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: localhost
-- Üretim Zamanı: 19 Nis 2021, 02:55:39
-- Sunucu sürümü: 8.0.17
-- PHP Sürümü: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `emreblog`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`) VALUES
(1, 'emre karadeniz', 'emrekrdenz@gmail.com', 'emrekrdenz', '$5$rounds=535000$/CaePR1v/aYCGlpe$8IkpzUbIbcQw9TBXG9Dtr77ZSaIWaMBkpwT711WY.Z7'),
(4, 'Emre Karadenizz', 'emredeneme@gmail.com', 'emrekrdenz1', '$5$rounds=535000$ung1qdOpq9sFVnvO$PYEJsQoebeT/958mEWQjXXxS2bMLmzMi4ZvOG0.HsO3'),
(5, 'emre karadeniz', 'emrekrdenz@gmail.com', 'emrekrdenzz', '$5$rounds=535000$2LRf9dnUrbfo3TPA$ea/jSj2fV.VzEZ25Ikm8L.Ele6LuJHdCS30mp0.Qau7'),
(7, 'Emre Karadeniz', 'emrekrdenz@gmail.com', 'emrekrdenzzz', '$5$rounds=535000$y67VALprhH5.x35L$XFPyXQeYUTXzFzERx0sNiNsPEAdFJeS0gW2eOaXl7x0'),
(8, 'Emre Karadeniz', 'emrekrdenz@gmail.com', 'emrek', '$5$rounds=535000$gGF4Uol1c09qANrG$x0rSTh66Zmoaq9Tniw8FNcuR8WWLIjuS6cwNBzk4b1B'),
(13, 'Ömer Faruk Karadeniz', 'omer@gmail.com', 'omerkrdenz', '$5$rounds=535000$NAtwJBb1MLHC5CUa$pYRe788xOnKvabLrrm0sXrLIN7.Sq9ocaBdNw8NIhn6');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
