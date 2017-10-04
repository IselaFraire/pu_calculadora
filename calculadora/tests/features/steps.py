# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que sumo los números "([^"]*)" y "([^"]*)"')
def dado_que_sumo_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))

@step(u'Dado que resto dos números "([^"]*)" y "([^"]*)"')
def dado_que_resto_dos_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

@step(u'Dado que multiplico dos números "([^"]*)" y "([^"]*)"')
def dado_que_multiplico_dos_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicacion(int(num1), int(num2))

@step(u'Dado que divido dos números "([^"]*)" y "([^"]*)"')
def dado_que_divido_dos_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))

@step(u'Dado que potencio dos números "([^"]*)" y "([^"]*)"')
def dado_que_potencio_dos_numeros_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))

@step(u'Dado que saco la raiz del número "([^"]*)"')
def dado_que_saco_la_raiz_del_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz(int(num1))

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == world.cal.obtener_resultado(),\
     'El resultado esperado de '+esperado+" y el obtenido es"+str(obtenido)


