import random
# Preguntas para el juego
questions = [ 
             "¿Qué función se usa para obtener la longitud de una cadena en Python?",
            "¿Cuál de las siguientes opciones es un número entero en Python?",
            "¿Cómo se solicita entrada del usuario en Python?",
            "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
            "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
            ]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario", 
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="), ]

#Puntaje del jugador al finalizar
puntaje_user = 0
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#Evitamos acceder a las 3 listas utilizando indices
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for question, user_answer, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i in range(len(user_answer)):
        print(f"{i + 1}. {user_answer[i]}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = int(input("Respuesta: ")) - 1
        if not (0 <= user_answer <= 3):
            print ("Respuesta no valida") 
        if user_answer!= correct_index:
            puntaje_user = puntaje_user - 0.5 
            print ("Respuesta Incorrecta")   
        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            puntaje_user = puntaje_user + 1
            print("¡Correcto!")
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_index])
    # Se imprime un blanco al final de la pregunta
    print()
# Se imprime la cantidad de puntos que logro el usuario    
print("El puntaje final fue de ", puntaje_user,"puntos")
