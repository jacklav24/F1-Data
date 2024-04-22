import numpy as np


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

def get_string_list_from_options(options, kill_switch, prompt, error_message) :
    result = []
    queried = get_string(prompt, error_message)
    while queried not in kill_switch :
        while not np.any(queried == options):
            queried = get_string(prompt, error_message)
        result.append(queried)
        queried = get_string(prompt, error_message)
    return result

def get_string(prompt, error_message) :
    while True:
        try:
            entered = str(input(prompt))
            return entered
        except ValueError:
            print(error_message, prompt)
