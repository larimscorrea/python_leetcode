# Primeira forma de fazer

def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

# Exemplo 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Saída: [0, 1]

# Exemplo 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Saída: [1, 2]

# Exemplo 3
nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Saída: [0, 1]

# Segunda forma de fazer.

def two_sum(nums, target):
    # Loop passa cada elemento no array usando o loop for. 
    for i in range(len(nums)):

        # Pega o elemento complementar do elemento atual.
        complement = target - nums[i]

        # Usa o loop while para pesquisar pelo complemento no elemento restante. 
        j = i + 1
        while j < len(nums):
            if nums[j] == complement:
                return [i, j]
            j += 1

# Exemplo 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Saída: [0, 1]

# Exemplo 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Saída: [1, 2]

# Exemplo 3
nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Saída: [0, 1]

# Terceira forma de fazer

def two_sum(nums, target):
    # Loop passa por cada elemento no array usando o loop for
    for i in range(len(nums)):
        # Pega o complemento do elemento atual
        complement = target - nums[i]
        # Use outro loop for para pesquisar pelo complemento no elemento restante
        # Use another `for` loop to search for the complement in the remaining elements
        for j in range(i + 1, len(nums)):
            if nums[j] == complement:
                return [i, j]

# Exemplo 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Saída: [0, 1]

# Exemplo 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Saída: [1, 2]

# Exemplo 3
nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Saída: [0, 1]
