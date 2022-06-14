def print_hello(name=""):
    if name:
        print(f"Hello {name} from {{ cookiecutter.project_name }}!")
    else:
        print("Hello from {{ cookiecutter.project_name }}!")
