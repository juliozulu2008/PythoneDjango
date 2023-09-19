class CalculadoraWindows:
    """
    Esta classe representa uma calculadora simples semelhante à calculadora padrão do Windows.

    Uso:
    Para usar a calculadora, crie uma instância desta classe e use os métodos de operação disponíveis.

    Exemplo de uso:

    calc = CalculadoraWindows()
    resultado = calc.somar(5, 3)
    print(resultado)  # Saída: 8
    """

    def somar(self, a, b):
        """
        Soma dois números.

        Args:
            a (float ou int): O primeiro número.
            b (float ou int): O segundo número.

        Returns:
            float ou int: O resultado da soma de a e b.
        """
        return a + b

    def subtrair(self, a, b):
        """
        Subtrai dois números.

        Args:
            a (float ou int): O número do qual será subtraído.
            b (float ou int): O número que será subtraído de a.

        Returns:
            float ou int: O resultado da subtração de a por b.
        """
        return a - b

    def multiplicar(self, a, b):
        """
        Multiplica dois números.

        Args:
            a (float ou int): O primeiro número.
            b (float ou int): O segundo número.

        Returns:
            float ou int: O resultado da multiplicação de a e b.
        """
        return a * b

    def dividir(self, a, b):
        """
        Divide dois números.

        Args:
            a (float ou int): O número que será dividido.
            b (float ou int): O divisor.

        Returns:
            float ou int: O resultado da divisão de a por b.
        """
        if b == 0:
            raise ValueError("A divisão por zero não é permitida.")
        return a / b

# Exemplo de uso da calculadora
calc = CalculadoraWindows()
resultado_soma = calc.somar(5, 3)
resultado_subtracao = calc.subtrair(10, 4)
resultado_multiplicacao = calc.multiplicar(7, 2)
resultado_divisao = calc.dividir(8, 2)

print("Resultado da Soma:", resultado_soma)
print("Resultado da Subtração:", resultado_subtracao)
print("Resultado da Multiplicação:", resultado_multiplicacao)
print("Resultado da Divisão:", resultado_divisao)
