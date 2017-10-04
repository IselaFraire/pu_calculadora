import unittest

from Calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):


    def setUp(self):
	self.calc = Calculadora()

    def test_valor_inicio_igual_cero(self):
	result = 0
        self.assertEquals(0, result)

    def test_sumar_2_mas_2_igual_4(self):
	result = self.calc.suma(2,2)
	self.assertEquals(4, result)

    def test_sumar_3_mas_3_igual_6(self):
	result = self.calc.suma(3,3)
	self.assertEquals(6, result)

    def test_sumar_menos_1_mas_3_igual_1(self):
	result = self.calc.suma(-1,2)
	self.assertEquals(1, result)

    def test_sumar_t_mas_dos_igual_error(self):
    	self.assertRaises(ValueError, self.calc.suma, 't', 4)
 
    def test_restar_4_menos_3_1(self):
	result = self.calc.resta(-4,-3)
	self.assertEquals(-1, result)

    def test_restar_1_menos_3_4(self):
	result = self.calc.resta(-1,3)
	self.assertEquals(-4, result)

    def test_restar_10_menos_9_1(self):
	result = self.calc.resta(10,9)
	self.assertEquals(1, result)

    def test_restar_h_menos_2(self):
	self.assertRaises(ValueError, self.calc.resta,'h',2)
  
    def test_multiplicar_5_por_5_25(self):
	result = self.calc.multiplicacion(5,5)
	self.assertEquals(25, result)

    def test_multiplicar_5_por_porciento_error(self):
	self.assertRaises(ValueError, self.calc.multiplicacion, 5,'%')

    def test_multiplicar_meno_5_por_5_menos_25(self):
	result = self.calc.multiplicacion(-5,5)
	self.assertEquals(-25, result)

    def test_dividir_0_entre_0_error(self):
	self.assertRaises(ValueError, self.calc.division, 0,0)

    def test_dividir_h_entre_h_error(self):
	self.assertRaises(ValueError, self.calc.division,0,'h')

    def test_dividir_50_entre_0_error(self):
	self.assertRaises(ValueError, self.calc.division,50,0)

    def test_dividir_menos_05_entre_menos_05_1(self):
	result = self.calc.division(10,5)
	self.assertEquals(2, result)

    def test_raiz_meno_100_error(self):
	self.assertRaises(ValueError, self.calc.raiz,-100)
    
    def test_raiz_100_10(self):
	result = self.calc.raiz(100)
	self.assertEquals(10.0,result)

    def test_potencia_2_a_la_3_8(self):
        result = self.calc.potencia(2,3)
	self.assertEquals(8,result)

    def test_potencia_meno_5_a_la_5_menos_3125(self):
	result = self.calc.potencia(-5,5)
	self.assertEquals(-3125,result)

    def test_potencia_operador_error(self):
	self.assertRaises(ValueError, self.calc.potencia,'%',9)

    def tearDown(self):
	pass

if __name__ == '__main__':#pragma: no cover
    unittest.main()


