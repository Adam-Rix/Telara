from Telara.Extraction.Extractor import \
    parse_site,\
    download_table


def Extract():
    # inputs
    url = input("Enter the required URL: ")
    filename = input("Enter the desired name for table: ")
    # calls
    tables = parse_site(url)
    download_table(tables, filename)

def Format():
    print("Reformat extracted tables")

def Exit():
    print("Exiting...")

def Tmenu():
    while True:
        print("What do u need from me, Boss?")
        print("1. Extract tables from the site")
        print("2. Reformat extracted tables")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Extract()
        elif choice == '2':
            Format()
        elif choice == '3':
            Exit()
            break
        else:
            print("Invalid option! Please enter a valid option.")

Tmenu()