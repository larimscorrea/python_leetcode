def is_palindrome(x):
    # Se o número for negativo, ele não pode ser um palíndromo
    if x < 0:
        return False
    
    # Converte o número para string
    x_str = str(x)
    
    # Inverte a string
    x_str_reversed = x_str[::-1]
    
    # Compara a string original com a string invertida
    if x_str == x_str_reversed:
        return True
    else:
        return False

# Exemplos de uso
print(is_palindrome(121))   # Saída: True
print(is_palindrome(-121))  # Saída: False
print(is_palindrome(10))    # Saída: False
print(is_palindrome(12321)) # Saída: True
