import pytest
from codigo.bytebank import Funcionario
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  #  GIVEN-CONTEXTO
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()   #  WHEN - ACAO

        assert resultado == esperado    #  THEN - DESFECHO

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' #GIVEN-CONTEXTO
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # WHEN=ACAO

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100mil_deve_retornar_90mil(self):
        entrada_salario = 100000 #GIVEN
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome,11/11/2000, entrada_salario)
        funcionario_teste.decrescimo_salario() #WHEN
        resultado = funcionario_teste.salario

        assert resultado == esperado #THEN

    @mark.calular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # GIVEN
        esperado = 100

        funcionario_teste = Funcionario('teste', '11 / 11 / 2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # WHEN

        assert resultado == esperado  # THEN

    @mark.calular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000  # GIVEN

            funcionario_teste = Funcionario('teste', '11 / 11 / 2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # WHEN

            assert resultado  # THEN

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000 # GIVEN
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__() # WHEN

        assert resultado == esperado  # THEN

