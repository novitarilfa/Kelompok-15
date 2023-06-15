import csv

def register():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("Registrasi berhasil.\n")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login berhasil.\n")
                return

    print("Username atau password salah.\n")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        choice = input("Pilih opsi: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Opsi tidak valid.\n")

if __name__ == '__main__':
    main()
