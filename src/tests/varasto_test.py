import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-10)
        self.varasto3 = Varasto(10,-20)
        self.varasto4 = Varasto(10,20)
        kukka = "sammakko"
        peruna = "porkkana"

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        #self.assertLessEqual(self.varasto.saldo, self.varasto.tilavuus)
    def test_varaston_tilavuus_nolla_tai_negatiivinen(self):
        self.assertEqual(self.varasto2.tilavuus,0)
        #self.assertGreater(self.varasto.tilavuus, 0)
    
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        #lisätty
    # def saldon_arvo_on_nollan_ja_tilavuuden_valilta(self):
    #     self.assertLessEqual(self.varasto.saldo, self.varasto.tilavuus)
    #     self.assertGreaterEqual(self.varasto.saldo,0)
    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    def test_alku_saldo_negatiivinen(self):
        varasto = Varasto(10,-20)
        self.assertAlmostEqual(varasto.saldo, 0)
    def test_alku_saldo_suurempi_kuin_varaston_tilavuus(self):
        varasto = Varasto(10,20)
        self.assertAlmostEqual(varasto.saldo,10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    def test_lisataan_negatiivinen_maara(self):
        maara = -10
        self.varasto.lisaa_varastoon(maara)
        
        jej = self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(jej,None)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    def test_lisataan_sopiva_maara(self):
        self.varasto.lisaa_varastoon(2)

        self.assertAlmostEqual(self.varasto.saldo,2)
    def test_lisataan_suuri_maara(self):
        self.varasto.lisaa_varastoon(120)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    def test_otetaan_negatiivinen_maara(self):
        matti = self.varasto.ota_varastosta(-20)
        self.assertAlmostEqual(matti,0)
    def test_otetaan_suuri_maara(self):
        self.varasto.ota_varastosta(200)
        self.assertAlmostEqual(self.varasto.saldo,0)
    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_strfunktio_palauttaa_oikean_tuloksen(self):
        testi = self.varasto.__str__()
        self.assertEqual(testi,"saldo = 0, vielä tilaa 10")