# infinite loop
#while True:
#    print("Hello")

# project code but with a twist
todos = []
while True:
    # things that will be excuted in cycles belong in here
    user_prompt = "enter a todo" # not a good way run makes program heavier keep out of loop
    todo = input(user_prompt)
    print(todo.capitalize()) # caps first letter of sentence
    print(todo.title()) # caps first letter of each word in a sentence
    todos.append(todo)