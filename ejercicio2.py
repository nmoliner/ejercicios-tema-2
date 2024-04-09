def modificar(lista):
    # Remove duplicates
    lista = list(set(lista))
    
    # Sort in descending order
    lista.sort(reverse=True)
    
    # Remove odd numbers
    lista = [num for num in lista if num % 2 == 0]
    
    # Calculate the sum
    suma = sum(lista)
    
    # Add the sum as the first element
    lista.insert(0, suma)
    
    return lista

# Test the function with the following list
lista = [4, 7, 2, 9, 10, 21, 12, 7, 4]
print(modificar(lista))
