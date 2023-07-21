# DECORATORI

# @property
# @abstractmethod

def new_decorator(original_func):
    # original func = referinta catre functia care urmeaza a fi decorata

    def wrapper_func():
        # scriem cod care vrem sa se intample
        # inainte de apelarea functiei original_func
        print("Niste cod inaintea apelului original_func")

        # apelam functia original_func
        original_func()

        # scriem cod care vrem sa se intample
        # dupa apelarea functiei original_func
        print("Niste cod dupa apelul original_func")

    return wrapper_func


@new_decorator
def func_needs_decoration():
    print("Vreau sa fiu decorata")


func_needs_decoration()


@new_decorator
def hello():
    print("Hello Pythonistas!")


hello()

# Daca aplicam decoratorul pe functia de mai jos, va functiona?






def decorator_salut(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"Am intrat in functia {original_func.__name__}")

        original_func(*args, **kwargs)

        print(f"Am iesit din functia {original_func.__name__}")

    return wrapper_func

@decorator_salut
def salut(name):
    print(f"Salut, {name}")

salut("Ana")