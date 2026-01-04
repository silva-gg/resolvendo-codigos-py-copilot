"""
Testes para validar todas as soluções dos desafios Python.
"""

import unittest
import sys
import os

# Adiciona o diretório resolucoes_code ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resolucoes_code'))

from concat_dados import concatenar_dados
from repet_txt import repetir_texto
from ope_mat import somar, subtrair, multiplicar, dividir
from par_impar import verificar_par_impar
from media_notas import calcular_media
from palindromo import verificar_palindromo


class TestDesafio1ConcatenarDados(unittest.TestCase):
    """Testes para o desafio 1: Concatenar Dados"""
    
    def test_concatenar_strings(self):
        """Testa concatenação de duas strings"""
        self.assertEqual(concatenar_dados("Olá", "Mundo"), "OláMundo")
    
    def test_concatenar_numeros(self):
        """Testa concatenação de números"""
        self.assertEqual(concatenar_dados(123, 456), "123456")
    
    def test_concatenar_string_numero(self):
        """Testa concatenação de string com número"""
        self.assertEqual(concatenar_dados("Python", 3), "Python3")
    
    def test_concatenar_vazio(self):
        """Testa concatenação com strings vazias"""
        self.assertEqual(concatenar_dados("", "teste"), "teste")
        self.assertEqual(concatenar_dados("teste", ""), "teste")


class TestDesafio2RepetirTexto(unittest.TestCase):
    """Testes para o desafio 2: Repetir Texto"""
    
    def test_repetir_texto_basico(self):
        """Testa repetição básica de texto"""
        self.assertEqual(repetir_texto("Python", 3), "PythonPythonPython")
    
    def test_repetir_uma_vez(self):
        """Testa repetição uma vez"""
        self.assertEqual(repetir_texto("Teste", 1), "Teste")
    
    def test_repetir_zero_vezes(self):
        """Testa repetição zero vezes"""
        self.assertEqual(repetir_texto("Texto", 0), "")
    
    def test_repetir_com_espacos(self):
        """Testa repetição de texto com espaços"""
        self.assertEqual(repetir_texto("Oi ", 3), "Oi Oi Oi ")


class TestDesafio3OperacoesMatematicas(unittest.TestCase):
    """Testes para o desafio 3: Operações Matemáticas"""
    
    def test_somar(self):
        """Testa operação de soma"""
        self.assertEqual(somar(5, 3), 8)
        self.assertEqual(somar(-2, 4), 2)
        self.assertEqual(somar(0, 0), 0)
    
    def test_subtrair(self):
        """Testa operação de subtração"""
        self.assertEqual(subtrair(10, 3), 7)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)
    
    def test_multiplicar(self):
        """Testa operação de multiplicação"""
        self.assertEqual(multiplicar(4, 5), 20)
        self.assertEqual(multiplicar(-3, 2), -6)
        self.assertEqual(multiplicar(0, 100), 0)
    
    def test_dividir(self):
        """Testa operação de divisão"""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertAlmostEqual(dividir(7, 2), 3.5)
    
    def test_dividir_por_zero(self):
        """Testa divisão por zero"""
        resultado = dividir(10, 0)
        self.assertIsInstance(resultado, str)
        self.assertIn("Erro", resultado)


class TestDesafio4ParImpar(unittest.TestCase):
    """Testes para o desafio 4: Verificar Par ou Ímpar"""
    
    def test_numeros_pares(self):
        """Testa verificação de números pares"""
        self.assertEqual(verificar_par_impar(2), "par")
        self.assertEqual(verificar_par_impar(0), "par")
        self.assertEqual(verificar_par_impar(-4), "par")
        self.assertEqual(verificar_par_impar(100), "par")
    
    def test_numeros_impares(self):
        """Testa verificação de números ímpares"""
        self.assertEqual(verificar_par_impar(1), "ímpar")
        self.assertEqual(verificar_par_impar(7), "ímpar")
        self.assertEqual(verificar_par_impar(-3), "ímpar")
        self.assertEqual(verificar_par_impar(99), "ímpar")


class TestDesafio5MediaNotas(unittest.TestCase):
    """Testes para o desafio 5: Calcular Média de Notas"""
    
    def test_media_notas_inteiras(self):
        """Testa cálculo de média com notas inteiras"""
        self.assertAlmostEqual(calcular_media(10, 8, 9), 9.0)
        self.assertAlmostEqual(calcular_media(7, 7, 7), 7.0)
    
    def test_media_notas_decimais(self):
        """Testa cálculo de média com notas decimais"""
        self.assertAlmostEqual(calcular_media(8.5, 9.0, 7.5), 8.333333, places=5)
    
    def test_media_notas_zero(self):
        """Testa cálculo de média com zeros"""
        self.assertAlmostEqual(calcular_media(0, 0, 0), 0.0)
    
    def test_media_notas_mistas(self):
        """Testa cálculo de média com notas mistas"""
        self.assertAlmostEqual(calcular_media(10, 5, 7), 7.333333, places=5)


class TestDesafio6Palindromo(unittest.TestCase):
    """Testes para o desafio 6: Verificar Palíndromos"""
    
    def test_palindromos_simples(self):
        """Testa palíndromos simples"""
        self.assertTrue(verificar_palindromo("arara"))
        self.assertTrue(verificar_palindromo("ovo"))
        self.assertTrue(verificar_palindromo("radar"))
    
    def test_nao_palindromos(self):
        """Testa palavras que não são palíndromos"""
        self.assertFalse(verificar_palindromo("python"))
        self.assertFalse(verificar_palindromo("teste"))
        self.assertFalse(verificar_palindromo("codigo"))
    
    def test_palindromos_maiusculas(self):
        """Testa palíndromos com letras maiúsculas"""
        self.assertTrue(verificar_palindromo("Arara"))
        self.assertTrue(verificar_palindromo("RADAR"))
    
    def test_palindromos_com_espacos(self):
        """Testa palíndromos com espaços"""
        self.assertTrue(verificar_palindromo("a nut for a jar of tuna"))
        self.assertTrue(verificar_palindromo("o lobo ama o bolo"))
    
    def test_palindromo_uma_letra(self):
        """Testa palíndromo de uma letra"""
        self.assertTrue(verificar_palindromo("a"))
        self.assertTrue(verificar_palindromo("z"))
    
    def test_string_vazia(self):
        """Testa string vazia (é considerada palíndromo)"""
        self.assertTrue(verificar_palindromo(""))


if __name__ == '__main__':
    unittest.main()
