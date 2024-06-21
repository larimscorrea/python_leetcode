def remove_duplicates(nums):
    # Verifica se o array está vazio
    if not nums:
        return 0
    
    # Inicializa o ponteiro de gravação
    i = 1
    
    # Percorre o array a partir do segundo elemento
    for j in range(1, len(nums)):
        # Se o elemento atual é diferente do anterior, é um elemento único
        if nums[j] != nums[j - 1]:
            # Coloca o elemento único na posição marcada pelo ponteiro de gravação
            nums[i] = nums[j]
            # Incrementa o ponteiro de gravação
            i += 1
    
    # Retorna o número de elementos únicos
    return i

# Exemplos de uso
nums = [1, 1, 2]
k = remove_duplicates(nums)
print(k)  # Saída: 2
print(nums[:k])  # Saída: [1, 2]

nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(nums)
print(k)  # Saída: 5
print(nums[:k])  # Saída: [0, 1, 2, 3, 4]
