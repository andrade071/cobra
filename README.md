Este projeto contém testes automatizados para diversas funções desenvolvidas em Python. O objetivo é validar o comportamento esperado de funções simples, como soma, login, divisão, entre outras. O framework utilizado para os testes é o **pytest**.

As seguintes funções são testadas neste repositório:

1. **Função soma(a, b, c)**:
   Descrição: Retorna a soma de três números inteiros.
   - **Testes**: Verifica se a soma de valores variados (positivos, negativos e zeros) está correta.
   
2. **Função `reverter_string(s)`**:
   - **Descrição**: Recebe uma string e retorna sua versão invertida.
   - **Testes**: Verifica se a inversão de strings simples, com um único caractere e vazias, ocorre corretamente.

3. **Função `login(usuario, senha)`**:
   - **Descrição**: Verifica se o usuário e senha fornecidos são válidos, retornando `True` se forem, ou `False` caso contrário.
   - **Testes**: Verifica credenciais válidas e inválidas.

4. **Função `dividir(a, b)`**:
   - **Descrição**: Realiza a divisão de `a` por `b`, levantando uma exceção `ZeroDivisionError` se `b` for zero.
   - **Testes**: Verifica a divisão de números e lida com a exceção de divisão por zero.

5. **Função `buscar_elemento(lista, elemento)`**:
   - **Descrição**: Retorna o índice do elemento na lista ou -1 se o elemento não for encontrado.
   - **Testes**: Verifica a busca de elementos dentro de uma lista e a resposta quando o elemento não é encontrado.

6. **Função `calcular_area_quadrado(lado)`**:
   - **Descrição**: Calcula a área de um quadrado dado o comprimento do lado.
   - **Testes**: Verifica a área com diferentes tamanhos de lado, incluindo valores negativos e zero.

7. **Função `cadastrar_usuario(dados)`**:
   - **Descrição**: Adiciona um novo usuário à lista de usuários cadastrados.
   - **Testes**: Verifica se o usuário foi corretamente adicionado à lista de usuários.

8. **Função `ordenar(lista)`**:
   - **Descrição**: Ordena uma lista de números em ordem crescente.
   - **Testes**: Verifica a ordenação de listas com diferentes elementos.

9. **Função `gerar_numero_aleatorio(inicio, fim)`**:
   - **Descrição**: Gera um número aleatório dentro de um intervalo especificado.
   - **Testes**: Verifica se o número gerado está dentro do intervalo correto.

10. **Função `calcular_imposto(renda)`**:
    - **Descrição**: Calcula o imposto de acordo com a renda, aplicando uma taxa fixa de 15%.
    - **Testes**: Verifica o cálculo do imposto para diferentes valores de renda.
