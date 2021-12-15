from app.view.cli.cli_app_mongo import mongo_db_menu
from app.view.cli.customer_menu import customer_menu
from app.view.cli.main_menu import menu
from app.view.cli.cli_app import main
from app.view.cli.order_menu import order_menu


def main_app():
    print("Choose your database to use: (1) mysql or (2) Mongodb")
    choice = str(input("> "))
    if choice == "1":
        # Calling the cli_app.py menu
        main()
    else:
        pass
        mongo_db_menu()


main_app()
