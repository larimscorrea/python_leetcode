class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    # Cria um nó de sentinela (dummy node) para facilitar a construção da nova lista
    dummy = ListNode()
    current = dummy

    # Percorre ambas as listas até que uma delas se esgote
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Anexa os nós restantes da lista que ainda não se esgotou
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Retorna a cabeça da nova lista, ignorando o nó de sentinela
    return dummy.next

# Função para imprimir a lista ligada (para fins de teste)
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Exemplo de uso
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_two_lists(list1, list2)
print_list(merged_list)  # Saída esperada: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
