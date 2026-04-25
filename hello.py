import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    # Проверяем флаг формального приветствия
    if formal:
        # Выводим формальное приветствие с фамилией
        print(f"Добрый день, {name} {lastname}!")
    else:
        # Выводим неформальное приветствие
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
