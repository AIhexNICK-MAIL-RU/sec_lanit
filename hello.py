import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="User's last name"),
    formal: bool = typer.Option(False, "--formal", "-f", help="Use formal greeting"),
):
    """
    COMBINED: Измененный комментарий из master + camelCase стиль из patch2.
    """
    userLastname = lastname
    isFormal = formal

    if isFormal == True:
        greeting = f"Добрый день, {name} {userLastname}!"
    else:
        greeting = f"Привет, {name}!"

    print(greeting)

if __name__ == "__main__":
    typer.run(main)
