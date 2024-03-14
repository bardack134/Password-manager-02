# Definir una función llamada 'decrypt' que toma el 'text' y el 'shift' como parámetros.
def decrypt(text, shift):
    
    # Crear una lista con las letras del alfabeto
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

   
  

    # Crear una lista vacía para guardar el nuevo alfabeto desplazado
    new_alphabet_list=[]
    
    # Recorrer cada letra del alfabeto original desde la posición indicada por el 'shift' hasta el final
    for i in range(shift, len(alphabet)):
        
        #evaluamos si el caracter esta o no en nuestra lista alfabeto
        if alphabet[i] in alphabet:
            # Añadir cada letra a la lista del nuevo alfabeto
            new_alphabet_list.append(alphabet[i])
            
            # Comprobar si la letra es la última del alfabeto original
            if i == alphabet.index('Z'):
                # Si es así, recorrer cada letra del alfabeto original desde el principio hasta la posición indicada por el 'shift'
                for j in range(0, shift):
                    # Añadir cada letra a la lista del nuevo alfabeto
                    new_alphabet_list.append(alphabet[j])
        
        else:
            # Añadir cada letra a la lista del nuevo alfabeto
            new_alphabet_list.append(i)
    
    # Crear una lista vacía para guardar el mensaje desencriptado
    secret_code_list=[]
    
    # Recorrer cada letra del mensaje encriptado
    for i in text:
        
        if i in alphabet:
            # Obtener la posición de la letra de acuerdo a la lista del nuevo alfabeto y asignarla a una variable llamada position_letter
            position_letter=new_alphabet_list.index(i)
            
            # Añadir la letra de acuerdo al alfabeto original a la lista del mensaje desencriptado
            secret_code_list.append(alphabet[position_letter])
        
        else:
            secret_code_list.append(i)
        
    # Convertir la lista del mensaje desencriptado en una cadena y asignarla a una variable llamada secret_code_string
    secret_code_string="".join(secret_code_list)
    
        
    return secret_code_string