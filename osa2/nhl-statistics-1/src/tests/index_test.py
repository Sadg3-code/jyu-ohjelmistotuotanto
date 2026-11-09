import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_loytaa_olemassaolevan_pelaajan(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
    
    def test_eniten_pisteita(self):
        top = self.stats.top(1)
        self.assertEqual(top[0].name, "Gretzky")

    def test_etsi_tiimin_pelaajat(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]
        self.assertEqual(len(players), 3)
        self.assertIn("Gretzky", names)
        self.assertNotIn("Yzerman", names)
    
    def test_etsi_pelaajaa_ei_loydy(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_etsitaan_pelaajan_statsit(self):
        f = self.stats.top(1)[0]
        self.assertEqual(str(f), "Gretzky EDM 35 + 89 = 124")