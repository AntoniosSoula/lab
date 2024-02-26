import requests

def get_server_info(url):
    try:
        response = requests.head(url)
        server_info = response.headers.get('Server', 'Server information not available')
        print(f"(α) Λογισμικό εξυπηρετητή: {server_info}")

        cookies = response.cookies
        if cookies:
            print("(β) Η σελίδα χρησιμοποιεί cookies.")
            print("(γ) Πληροφορίες για τα cookies:")
            for cookie in cookies:
                cookie_name = cookie.name
                cookie_expires = "Δεν καθορίζεται" if cookie.expires is None else str(cookie.expires)
                print(f"  - Όνομα: {cookie_name}, Διάρκεια Εγκυρότητας: {cookie_expires}")
        else:
            print("(β) Η σελίδα δεν χρησιμοποιεί cookies.")
    except requests.exceptions.RequestException as e:
        print(f"Σφάλμα κατά την επικοινωνία με το URL: {e}")

def main():
    user_url = input("Εισάγετε το URL: ")
    get_server_info(user_url)

if __name__ == "__main__":
    main()
