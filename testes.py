import pytest
import random


def soma(a, b, c):
    return a + b + c


def reverter_string(s):
    return s[::-1]


def login(usuario, senha):
    usuario_valido = "admin"
    senha_valida = "1234"
    return usuario == usuario_valido and senha == senha_valida


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def buscar_elemento(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return -1


def calcular_area_quadrado(lado):
    return lado ** 2


usuarios_cadastrados = []


def cadastrar_usuario(dados):
    usuarios_cadastrados.append(dados)


def ordenar(lista):
    return sorted(lista)


def gerar_numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)


def calcular_imposto(renda):
    taxa_imposto = 0.15
    return renda * taxa_imposto


def test_soma():
    assert soma(1, 2, 3) == 6
    assert soma(0, 0, 0) == 0
    assert soma(-1, 1, 0) == 0


def test_reverter_string():
    assert reverter_string("abc") == "cba"
    assert reverter_string("a") == "a"
    assert reverter_string("") == ""


def test_login():
    assert login("admin", "1234") is True
    assert login("admin", "wrongpassword") is False
    assert login("user", "1234") is False


def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)


def test_buscar_elemento():
    assert buscar_elemento([1, 2, 3], 2) == 1
    assert buscar_elemento([1, 2, 3], 4) == -1
    assert buscar_elemento([], 1) == -1


def test_calcular_area_quadrado():
    assert calcular_area_quadrado(4) == 16
    assert calcular_area_quadrado(0) == 0
    assert calcular_area_quadrado(-3) == 9


def test_cadastrar_usuario():
    cadastrar_usuario({"usuario": "joao", "senha": "123"})
    assert len(usuarios_cadastrados) == 1
    assert usuarios_cadastrados[0]["usuario"] == "joao"


def test_ordenar():
    assert ordenar([3, 1, 2]) == [1, 2, 3]
    assert ordenar([10, 5, 3, 7]) == [3, 5, 7, 10]
    assert ordenar([1, 2, 3]) == [1, 2, 3]


def test_gerar_numero_aleatorio():
    for _ in range(100):
        numero = gerar_numero_aleatorio(1, 10)
        assert 1 <= numero <= 10


def test_calcular_imposto():
    assert calcular_imposto(1000) == 150
    assert calcular_imposto(5000) == 750
    assert calcular_imposto(0) == 0
