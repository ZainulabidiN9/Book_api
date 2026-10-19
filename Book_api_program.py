

# ---------------------------------------------BOOK API PRoGRAM---------------------------------------------------------------

import requests
import webbrowser

BASE_URL = "https://openlibrary.org"

HEADERS = {
    "User-Agent": "PythonBookSearch/1.0 (student-project)"
}


def get_description(book_key):
    """Fetch a book's description using its Open Library work ID."""

    if not book_key or not book_key.startswith("/works/"):
        return "Description is not available."

    try:
        url = f"{BASE_URL}{book_key}.json"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        description = response.json().get("description")

        if isinstance(description, dict):
            description = description.get("value", "")

        if isinstance(description, str) and description.strip():
            return description.strip()

        return "Description is not available."

    except requests.exceptions.Timeout:
        return "Request timed out while fetching description."

    except requests.exceptions.RequestException:
        return "Could not fetch the description."

    except ValueError:
        return "Invalid response received from the API."


def show_all_books():


    url = f"{BASE_URL}/subjects/fiction.json"

    params = {
        "limit": 100
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        books = response.json().get("works", [])

        if not books:
            print("No books found.")
            return

        print("\n===== BOOKS FROM OPEN LIBRARY =====")
        print("=" * 60)

        for index, book in enumerate(books, start=1):

            title = book.get("title", "Unknown title")

            authors = book.get("authors", [])

            author_names = [
                author.get("name", "Unknown author")
                for author in authors
            ]

            author_text = ", ".join(author_names)

            if not author_text:
                author_text = "Unknown author"

            print(f"\nBook {index}")
            print(f"Title:  {title}")
            print(f"Author: {author_text}")
            print("-" * 60)

        print(f"\nTotal books displayed: {len(books)}")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.HTTPError as error:
        print(f"Open Library server error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")

    except ValueError:
        print("Could not process the API response.")


def search_books():
    """Search books by author or title."""

    print("\n===== BOOK SEARCH SYSTEM =====")
    print("1. Search by author")
    print("2. Search by book title")
    print("3. Show All Books")

    choice = input("Choose an option (1, 2 or 3): ").strip()

    # Option 3: Display books from the fiction subject API.
    if choice == "3":
        show_all_books()
        return

    # Option 1: Search by author.
    elif choice == "1":
        search_type = "author"
        search_value = input("Enter author name: ").strip()

    # Option 2: Search by title.
    elif choice == "2":
        search_type = "title"
        search_value = input("Enter book title: ").strip()

    else:
        print("Invalid choice. Please select 1, 2 or 3.")
        return

    if not search_value:
        print("Please enter a search value.")
        return

    url = f"{BASE_URL}/search.json"

    params = {
        search_type: search_value,
        "fields": "key,title,author_name,first_publish_year,cover_i",
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        books = response.json().get("docs", [])

        if not books:
            print("No books found.")
            return

        print(f"\nSearch results for: {search_value}")
        print("=" * 60)

        for index, book in enumerate(books, start=1):

            title = book.get("title", "Unknown title")

            authors = book.get("author_name") or ["Unknown author"]

            year = book.get("first_publish_year", "Unknown")

            print(f"\nBook {index}: {title}")
            print(f"Author: {', '.join(authors)}")
            print(f"First published: {year}")

            print("-" * 60)

        # Ask the user to select a book.
        selection = input(
            "\nEnter a book number for details "
            "(or press Enter to return): "
        ).strip()

        if not selection:
            return

        try:
            index = int(selection) - 1

        except ValueError:
            print("Please enter a valid number.")
            return

        if index < 0 or index >= len(books):
            print("Invalid book number.")
            return

        selected_book = books[index]

        book_key = selected_book.get("key", "")
        cover_id = selected_book.get("cover_i")

        title = selected_book.get("title", "Unknown title")

        print(f"\n===== DETAILS: {title} =====")

        # Fetch description only for the selected book.
        description = get_description(book_key)

        print(f"Description: {description}")

        if cover_id:
            cover_url = (
                f"https://covers.openlibrary.org/b/id/"
                f"{cover_id}-L.jpg"
            )

            print(f"Cover image: {cover_url}")

        else:
            cover_url = None
            print("Cover image: Not available.")

        if book_key:
            details_url = f"{BASE_URL}{book_key}"
            print(f"Book details: {details_url}")

        # Open the cover and book details in the browser.
        if cover_url:
            webbrowser.open(cover_url)

        if book_key:
            webbrowser.open(f"{BASE_URL}{book_key}")

    except requests.exceptions.Timeout:
        print("Request timed out. Please check your internet.")

    except requests.exceptions.HTTPError as error:
        print(f"Open Library server error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")

    except ValueError:
        print("Could not process the API response.")


def main():
    """Run the book search system repeatedly."""

    while True:
        search_books()

        again = input(
            "\nWould you like to search again? (y/n): "
        ).strip().lower()

        if again != "y":
            print("\nThank you for using Book Search System!")
            break


if __name__ == "__main__":
    main()