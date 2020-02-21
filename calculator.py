#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

print("#-----------CALCULATOR--------#\n")
print("Spanish version | software v1.0.1")
print("")
print("Si quieres sumar coloca: 'suma'")
print("Si quieres restar coloca: 'resta'")
print("Si quieres dividir coloca: 'divide'")
print("Si quieres multiplicar coloca: 'multiplica'")
print("Si quieres sacar la raíz cuadrada coloca: 'raiz cuadrada'")
print("Si quieres salir coloca: 'salir ó exit'")
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
        print("No se puede dividir entre 0")
        return "Operación errónea"

def multiply(valor_uno, valor_dos):
    """Su función es multiplicar"""
    return valor_uno * valor_dos

while True:
    date = str(input("¿Qué deseas hacer?: ")).lower()

    if date == 'raiz cuadrada':
        num_one = float(input("Raíz cuadrada de: "))
        print(sqrt(num_one))

    if date == 'suma':
        num_one = float(input("Valor uno: "))
        num_two = float(input("Valor dos: "))
        print(sum(num_one, num_two))

    if date == 'resta':
        num_one = float(input("Valor uno: "))
        num_two = float(input("Valor dos: "))
        print(subtract(num_one, num_two))

    if date == 'divide':
        num_one = float(input("Valor uno: "))
        num_two = float(input("Valor dos: "))
        print(divide(num_one, num_two))

    if date == 'multiplica':
        num_one = float(input("Valor uno: "))
        num_two = float(input("Valor dos: "))
        print(multiply(num_one, num_two))

    if date == 'salir' or date == 'exit':
        print("Esperamos haberte ayudade ;)")
        break

# End of the program.
