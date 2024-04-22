def get_var_from_options(data_type, options, prompt, error_message) :
    if data_type == int :
        queried = get_int(prompt, error_message)
        while queried not in options :
            queried = get_int(prompt, error_message)
        return queried
    

def get_var(data_type, prompt, error_message) :
    if data_type == int :
        return get_int(prompt, error_message)
    

def get_int(prompt, error_message) :
    while True:
        try:
            entered = int(input(prompt))
            return entered
        except ValueError:
            print(error_message, prompt)