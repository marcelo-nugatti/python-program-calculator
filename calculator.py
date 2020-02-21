#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

print("#-----------CALCULATOR--------#\n")
print("Spanish version | software v1.0.2")
print("")
print("Si quieres SUMAR coloca: 'suma'")
print("Si quieres RESTAR coloca: 'resta'")
print("Si quieres DIVIDIR coloca: 'divide'")
print("Si quieres MULTIPLICAR coloca: 'multiplica'")
print("Si quieres sacar la RAÍZ CUADRADA coloca: 'raiz cuadrada'")
print("Si quieres SALIR coloca: 'salir ó exit'")
print("Si necesitas AYUDA coloca: 'ayuda ó help'")
print("")

def sqrt(value_one):
    """Su funcion es encontrar la raíz cuadrada de un número"""
    return math.sqrt(value_one)

def sum(value_one, value_two):
    """Su función es sumar"""
    return value_one + value_two

def subtract(value_one, value_two):
    """Su función es restar"""
    return value_one - value_two

def divide(value_one, value_two):
    """Su función es dividir"""
    try:
        return value_one / value_two
    except ZeroDivisionError:
        print("Error #921: No se puede dividir entre 0")
        return "Operación errónea"

def multiply(valor_uno, valor_dos):
    """Su función es multiplicar"""
    return valor_uno * valor_dos

while True:
    data = str(input("¿Qué deseas hacer?: ")).lower()
    
    try:

        if data == 'raiz cuadrada':
            num_one = float(input("Raíz cuadrada de: "))
            print(sqrt(num_one))

        if data == 'suma':
            num_one = float(input("Valor uno: "))
            num_two = float(input("Valor dos: "))
            print(sum(num_one, num_two))

        if data == 'resta':
            num_one = float(input("Valor uno: "))
            num_two = float(input("Valor dos: "))
            print(subtract(num_one, num_two))

        if data == 'divide':
            num_one = float(input("Valor uno: "))
            num_two = float(input("Valor dos: "))
            print(divide(num_one, num_two))

        if data == 'multiplica':
            num_one = float(input("Valor uno: "))
            num_two = float(input("Valor dos: "))
            print(multiply(num_one, num_two))

        if (data == 'salir' or data == 'exit'):
            print("Esperamos haberte ayudade ;)")
            break
    
        if (
                data != 'raiz cuadrada' and
                data != 'suma'          and
                data != 'multiplica'    and
                data != 'resta'         and
                data != 'ayuda'         and
                data != 'help'          and
                data != 'exit'          and
                data != 'salir'         and
                data != 'divide'        ):
            print("Lo que ingresaste es incorrecto, intentalo de nuevo ;)")
        
        if (data == 'ayuda' or data == 'help'):
            print("")
            print("AYUDA EN CAMINO ;)")
            print("")
            print("Si quieres SUMAR coloca: 'suma'")
            print("Si quieres RESTAR coloca: 'resta'")
            print("Si quieres DIVIDIR coloca: 'divide'")
            print("Si quieres MULTIPLICAR coloca: 'multiplica'")
            print("Si quieres sacar la RAÍZ CUADRADA coloca: 'raiz cuadrada'")
            print("Si quieres SALIR coloca: 'salir ó exit'")
            print("Si necesitas AYUDA coloca: 'ayuda ó help'")
            print("")

    
    except ValueError:
        print("Error #904: Debes ingresar un número")


# End of the program.
