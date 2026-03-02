from faker import Faker

fk = Faker()

print("Name: ", fk.name_female())
print("Email: ", fk.email())
print("City: ", fk.city())
print("Mobile: ", fk.phone_number())
print("Country: ", fk.country())
print("Job: ", fk.job())

for i in range(1,10):
    print("----------------------------------")
    print("Count:", i)
    print("Name: ", fk.name_female())
    print("Email: ", fk.email())
    print("City: ", fk.city())
    print("Mobile: ", fk.phone_number())
    print("Country: ", fk.country())
    print("Job: ", fk.job())
    user_data = f"{fk.name_female()}, {fk.email()}, {fk.city()}\n"
    with open("user_details.txt", "a") as file:
        file.write(user_data)
