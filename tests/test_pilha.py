from unittest import TestCase
from ed.pilha import Pilha


class PilaTestCase(TestCase):

    def setUp(self):
        # super().setUp()
        self.pilha = Pilha()

    def test_pilha_vazia(self):
        self.assertTrue(self.pilha.vazia())

    def test_push_length(self):
        self.pilha.push(2)
        self.assertEqual(1, len(self.pilha))

    def test_pilha_nao_vazia(self):
        self.pilha.push(9)
        self.assertFalse(self.pilha.vazia())
    
    def test_push_pop_vazia(self):
        self.pilha.push(9)
        self.assertEqual(9, self.pilha.pop())
        self.assertTrue(self.pilha.vazia())
