import abc


class Pessoa:
    def __init__(self, nome, cpf, dt_nasc):
        self._nome = nome
        self._cpf = cpf
        self._dt_nasc = dt_nasc

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, p_nome):
        self._nome = p_nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, p_cpf):
        self._cpf = p_cpf

    @property
    def datanascimento(self):
        return self._dt_nasc

    @datanascimento.setter
    def datanascimento(self, p_dtnasc):
        self._dt_nasc = p_dtnasc


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, dt_nasc, salario, cargo):
        super().__init__(nome, cpf, dt_nasc)
        self._salario = salario
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if (self._salario < 0):
            print('salario não pode ser negativo')
        else:
            self._salario = valor

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, crg):
        self._cargo = crg


class Cliente(Pessoa):
    def __init__(self, nome, cpf, dt_nasc):
        super().__init__(nome, cpf, dt_nasc)


class Pedido:
    def __init__(self, preco, desconto, preco_desconto, cliente):
        self._preco = preco
        self._desconto = desconto
        self._preco_desconto = preco_desconto
        self._cliente = cliente


    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, prc):
        self._preco = prc

    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, dsc):
        self._desconto = dsc

    @property
    def preco_desconto(self):
        return self._preco_desconto

    @preco_desconto.setter
    def preco_desconto(self, prc_des):
        self._preco_desconto = prc_des

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, clie):
        self._cliente = clie

    def calcular_preco(self, preco_tot):
        val = sum(preco_tot)
        self._preco = val
        return self._preco

    def calcular_desconto(self, des):
        self._desconto = self._preco * des
        return self._desconto

    def calcular_preco_com_desconto(self):
        self._preco_desconto = self._preco - self._desconto
        return self._preco_desconto


class Desconto(abc.ABC):
    @abc.abstractmethod
    def calcular_desconto(self):
        pass
