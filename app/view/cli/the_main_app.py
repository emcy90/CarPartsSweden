
from app.view.cli.customer_menu import customer_menu
from app.view.cli.main_menu import menu
from app.view.cli.cli_app import main
from app.view.cli.cli_app_mongo import main1


def main_app():
    print("Choose your database to use: (1) mysql or (2) Mongodb")
    choice = str(input("> "))
    if choice == "1":
        # Calling the cli_app.py menu
        main()
    else:
        main1()


main_app()
