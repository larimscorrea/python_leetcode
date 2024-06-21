def is_valid(s):
    # Dicionário que mapeia parênteses de fechamento para abertura
    bracket_map = {')': '(', ']': '[', '}': '{'}
    # Pilha para armazenar os parênteses de abertura
    stack = []

    # Percorre cada caractere na string
    for char in s:
        # Se o caractere é um parêntese de fechamento
        if char in bracket_map:
            # Pop do topo da pilha se não estiver vazia, caso contrário, coloca um marcador inválido
            top_element = stack.pop() if stack else '#'
            # Verifica se o parêntese de abertura no topo da pilha corresponde ao de fechamento
            if bracket_map[char] != top_element:
                return False
        else:
            # Se o caractere é um parêntese de abertura, empilha-o
            stack.append(char)

    # Verifica se a pilha está vazia (todos os parênteses foram correspondidos)
    return not stack

# Exemplos de uso
print(is_valid("()"))        # Saída: true
print(is_valid("()[]{}"))    # Saída: true
print(is_valid("(]"))        # Saída: false
print(is_valid("([)]"))      # Saída: false
print(is_valid("{[]}"))      # Saída: true
