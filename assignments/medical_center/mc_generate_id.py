def generate_id():
    path = 'new.txt'
    with open(path, 'r') as file:
        generated_id = file.read().strip()
        file.close()
    counter = int(generated_id) + 1
    with open(path, 'w') as file:
        file.write(str(counter))
    return generated_id