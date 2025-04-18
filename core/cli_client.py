import requests

BASE_URL = "http://127.0.0.1:8000/api/"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0NTM3NzQyLCJpYXQiOjE3NDQ1Mzc0NDIsImp0aSI6ImQ0NTY1YzUyMmFlZTRlOTZiYjA2OGRmYjViZmU5MzM0IiwidXNlcl9pZCI6Mn0.-uSN3HHxIcTzCThah0bw5GrCbrYu0E7e2b-T5TdElKU"  # Замени с реалния JWT токен

def get_users():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(f"{BASE_URL}users/", headers=headers)
    if response.status_code == 200:
        print("Users:")
        for user in response.json():
            print(user)
    else:
        print(f"Error: {response.status_code}, {response.text}")

def create_user(username, email, password, is_customer=True, is_delivery=False, is_restaurant=False):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    data = {
        "username": username,
        "email": email,
        "password": password,
        "is_customer": is_customer,
        "is_delivery": is_delivery,
        "is_restaurant": is_restaurant,
    }
    response = requests.post(f"{BASE_URL}users/", json=data, headers=headers)
    if response.status_code == 201:
        print("User created successfully!")
    else:
        print(f"Error: {response.status_code}, {response.text}")

def main():
    print("Welcome to the Food Delivery CLI!")
    while True:
        print("\nOptions:")
        print("1. List users")
        print("2. Create a new user")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            get_users()
        elif choice == "2":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            is_customer = input("Is customer? (y/n): ").lower() == "y"
            is_delivery = input("Is delivery? (y/n): ").lower() == "y"
            is_restaurant = input("Is restaurant? (y/n): ").lower() == "y"
            create_user(username, email, password, is_customer, is_delivery, is_restaurant)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()