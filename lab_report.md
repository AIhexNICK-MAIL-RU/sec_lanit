# Отчет по лабораторной работе

## История коммитов в локальном репозитории
* 0b6f3e5 Initial commit
* 66a411b chore: update comments in master branch to create conflict
* b7a3771 style: change to camelCase coding style
* 1761f7c docs: add comprehensive comments and docstrings
* 7f9c947 style: change to camelCase coding style
| * e5ef0e0 style: change to camelCase coding style
|/  
* 2b835da Add interactive name input
* f9f7f04 Add dirty hello.py with security issues
* 87a6f78 first commit with gitleaks config
* 2f35261 first commit
* 378b2d7 feat: signed commit


## История коммитов в удаленном репозитории

* 0b6f3e5 Initial commit
* 66a411b chore: update comments in master branch to create conflict
* b7a3771 style: change to camelCase coding style
* 1761f7c docs: add comprehensive comments and docstrings
* 7f9c947 style: change to camelCase coding style
| * e5ef0e0 style: change to camelCase coding style
|/  
* 2b835da Add interactive name input
* f9f7f04 Add dirty hello.py with security issues
* 87a6f78 first commit with gitleaks config
* 2f35261 first commit
* 378b2d7 feat: signed commit


## Ветки в удаленном репозитории

  origin/HEAD -> origin/main
  origin/main
  origin/master
  origin/patch2


## Итоговый код hello.py

```python
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
```
