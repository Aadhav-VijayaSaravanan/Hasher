from faker import Faker
from hashe import generate_password, hash_password
from file import create_file, append_to_file
from pdf import convert_text_to_pdf  # Import the function from pdf_converter.py

def generate_user_info(faker, num_users):
    usernames_passwords = [f"{faker.user_name()} {generate_password()}" for _ in range(num_users)]
    return "\n".join(usernames_passwords)

def main():
    faker = Faker()

    random_user_info_filename = "info.txt"
    hashed_user_info_filename = "hashed.txt"
    hashed_user_info_pdf_filename = "hashed.pdf"  # New PDF file name

    create_file(random_user_info_filename)
    create_file(hashed_user_info_filename)

    with open(random_user_info_filename, "w") as random_user_info_file, open(hashed_user_info_filename, "w") as hashed_user_info_file:
        for iteration in range(1, 101):
            user_info = generate_user_info(faker, 10)
            random_user_info_file.write(user_info + "\n")
            append_to_file(hashed_user_info_filename, f"\nHashed User Information - Run {iteration}\n")
            for line in user_info.splitlines():
                username, password = line.strip().split()
                hashed_password = hash_password(password)
                append_to_file(hashed_user_info_filename, f"Username: {username}, Hashed Password: {hashed_password}\n")

        # Convert hashed.txt to PDF
        convert_text_to_pdf(hashed_user_info_filename, hashed_user_info_pdf_filename)

if __name__ == "__main__":
    main()
