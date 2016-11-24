
-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Dim 06 Novembre 2016 à 22:32
-- Version du serveur: 10.0.22-MariaDB
-- Version de PHP: 5.2.17

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `u925639974_grdf`
--

-- --------------------------------------------------------

--
-- Structure de la table `camion`
--
CREATE DATABASE IF NOT EXISTS u925639974_grdf

CREATE TABLE IF NOT EXISTS `camion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plaque` varchar(60) NOT NULL,
  `centre` varchar(50) NOT NULL,
  `nomcamion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=30 ;

--
-- Contenu de la table `camion`
--

INSERT INTO `camion` (`id`, `plaque`, `centre`, `nomcamion`) VALUES
(28, '1246', 'Massy', 'Camion2'),
(26, '1234561234', 'Toulouse', 'Camion1'),
(29, 'plaque dim', 'Massy', 'Camionleon');

-- --------------------------------------------------------

--
-- Structure de la table `centres`
--

CREATE TABLE IF NOT EXISTS `centres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `centres`
--

INSERT INTO `centres` (`id`, `nom`) VALUES
(1, 'Massy'),
(2, 'Toulouse');

-- --------------------------------------------------------

--
-- Structure de la table `effectifs`
--

CREATE TABLE IF NOT EXISTS `effectifs` (
  `ideff` int(11) NOT NULL AUTO_INCREMENT,
  `idcamion` varchar(50) NOT NULL,
  `idoutil` varchar(50) NOT NULL,
  `quantite` varchar(50) NOT NULL,
  PRIMARY KEY (`ideff`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Contenu de la table `effectifs`
--

INSERT INTO `effectifs` (`ideff`, `idcamion`, `idoutil`, `quantite`) VALUES
(7, '26', '3', '30'),
(8, '26', '4', '50'),
(14, '28', '4', '49'),
(15, '28', '3', '21'),
(17, '29', '3', '29'),
(18, '29', '4', '51');

-- --------------------------------------------------------

--
-- Structure de la table `outils`
--

CREATE TABLE IF NOT EXISTS `outils` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `ref` varchar(50) NOT NULL,
  `nbrmin` varchar(11) NOT NULL,
  `photo` varchar(100) NOT NULL,
  KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Contenu de la table `outils`
--

INSERT INTO `outils` (`id`, `nom`, `ref`, `nbrmin`, `photo`) VALUES
(3, 'Tournevis', '65464-4azefa', '30', 'tournevis.jpg'),
(4, 'Cle a molette', '5486R-aa', '50', 'cle-a-molette-facom-serie-113ac-image-210663-grande.jpg');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `utilisateur` varchar(30) NOT NULL,
  `motdepasse` varchar(30) NOT NULL,
  `site` varchar(30) NOT NULL,
  `admin` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Contenu de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id`, `utilisateur`, `motdepasse`, `site`, `admin`) VALUES
(1, 'admin', 'mdpadmin', 'Massy', 1),
(12, 'utilisateurbasique', 'mdp', 'Massy', 0),
(10, 'UtilisateurBasique3', 'mdp', 'Toulouse', 0),
(11, 'azerazer', 'azerzer', 'Toulouse', 0),
(13, 'azeffz', 'motdepasse', 'Massy', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
