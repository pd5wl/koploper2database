--
-- Databank: `koploper2database`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `output`
--

CREATE TABLE IF NOT EXISTS `output` (
  `loc` int(11) NOT NULL,
  `blok` int(11) NOT NULL,
  `mod_time` text NOT NULL,
  `real_time` text NOT NULL,
  `route` text NOT NULL,
  PRIMARY KEY (`loc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
