# Facultad de Ingenieria Universidad de Buenos Aires

# Script Name		: factorial.py
# Author				: Rolon Leonel
# Created				: 20th Dic 2016
# Last Modified		:
# Version				: python 2.7

# FACTORIAL
def factorial(n):
        if n == 0:
                return 1
        else:
                r = 1
                i = 1
                while i <= n:
                        r = r*i
                        i = i + 1
                return r