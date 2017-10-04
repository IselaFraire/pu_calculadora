#Implementando calculador con Travis

class Calculadora():

    def suma(self, num1, num2):
        resultado = (int, long, float, complex)

        if isinstance(num1, resultado) and isinstance(num2, resultado):
            return num1 + num2
        else:
            raise ValueError

    def resta(self, num1, num2):
        resultado = (int, long, float, complex)

        if isinstance(num1, resultado) and isinstance(num2, resultado):
            return num1 - num2
        else:
            raise ValueError

    def multiplicacion(self, num1, num2):
        resultado = (int, long, float, complex)

        if isinstance(num1, resultado) and isinstance(num2, resultado):
            return num1 * num2
        else:
            raise ValueError

    def division(self, num1, num2):
        if num1 == 0 or num2 <= 0:
            raise ValueError
        else:
            return num1 / num2

    def raiz(self, num1):
        if num1 >= 0:
            return num1 ** 0.5
        else:
            raise ValueError

    def potencia(self, num1, num2):

        if num1 == '/' or num1 == '%' or num1 == '^' and num2 == '/' or num2 == '%' or num2 == '^':
                raise ValueError
        else:
            return num1 ** num2


"""
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
	try:
	    self.resultado = num1 + num2
	except:
	    return 'Datos incorrectos'

"""
