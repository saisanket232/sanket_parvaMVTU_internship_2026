# Defining the Library class to represent a library system
class Library:
    # Class variables: These are shared across all instances (members) of the Library class
    library_name = "Kuvempu - Public Library"  # Name of the library
    location = "Bengaluru"                     # Location of the library
    number_of_members = 0                      # Total number of registered members
    number_of_books = 0                        # Total tracking count of all available books
    books_collection = []                      # A shared list storing details of all books in the library
    borrowed_books = []                        # A shared master list tracking all books borrowed by all members

    # Constructor method to initialize instance variables when a new Library member (object) is created
    def __init__(self, member, member_id):
        # Public instance variables (can be accessed freely from outside the class by anyone)
        self.member = member                   # string: Name of the member
        self.borrowed_books = []               # list: Stores books currently borrowed by this specific member safely
        self.total_borrowed = 0                # integer: Count of books currently borrowed by this member

        # Protected instance variables (indicated by a single underscore '_', meant for internal use and subclass use only)
        self._membership_type = "Regular"      # Type of membership (default is "Regular")
        self._member_id = member_id            # Unique ID allocated to the new member

        # Private instance variables (indicated by double underscore '__', hidden from direct outside access to enforce encapsulation)
        self.__fine_amount = 0                 # Total fines accumulated by the member for returning late
        self.__max_books_allowed = 3           # Limit: Maximum number of books a member can hold at the same time


    # @classmethod decorator tells Python this method applies to the class 'Library' itself, not a specific instance.
    @classmethod
    def add_book(cls, book, author, genre, publisher, copies=1):
        # Reassigning 'book' variable to a dictionary containing all the formal details of the new book
        book = {
            # Auto-generating a strict sequential unique ID based on the current collection size
            "book_id": len(cls.books_collection) + 1,
            "book": book,                              # Name of the book
            "author": author,                          # Author of the book
            "genre": genre,                            # Category of the book
            "publisher": publisher,                    # Publisher of the book
            "available_copies": copies,                # Quantity available to lend out
            "total_copies": copies                     # Total quantity owned by the library
        }
        # Appending the new book dictionary into the shared class level books_collection list
        cls.books_collection.append(book)
        # Tallying up the total number of physical books now inside the library
        cls.number_of_books += copies

        # Printing out a success confirmation along with the full dictionary details of the book
        print(f"Book Added Successfully! The Details are as follows: ")
        print(f"Book Name: {book}")
        print(f"Author: {author}")
        print(f"Genre: {genre}")
        print(f"Publisher: {publisher}")
        print(f"Available Copies: {copies}\n")


    # Another @classmethod specifically used to cleanly display all books currently registered in the database
    @classmethod
    def list_books(cls):
        # Safety Check: Verifying whether the library is entirely empty
        if not cls.books_collection:
            print("No books available in the library. Come after some time.")
            return  # Exits early if no books exist
       
        # Print a nice formatted header indicating where these books belong
        print(f"{cls.library_name} - {cls.location}")
        # Print table column headings defining alignments (<5 means left-aligned with a strict width of 5 characters, etc.)
        print(f"{'ID': <5} {'Book Name': <30} {'Author': <20} {'Available': <10}")
       
        # Loop exactly one time for each distinct book in our global collection
        for book in cls.books_collection:
            # Print each dictionary's details precisely formatting them into visually distinct columns
            print(f"{book['book_id']:<5} {book['book']:<30} {book['author']:<25} {book['available_copies']:<10}")

        # Print the total gross number of books currently recorded in the library databases
        print(f"Total Books in Library: {cls.number_of_books} \n")

    # Private method (has double underscore '__'). This math formula can only be utilized internally from within the class bounds.
    def __calculate_fine(self, days_late):
        return days_late * 5  # Financial policy: Returns a number charging 5 rupees for every late day
   
    # Protected method (has single underscore '_'). Should only be used by this class or its inheritances.
    def _get_current_date(self):
        # We import the datetime tool temporarily just to acquire the exact current timestamp
        from datetime import datetime
        # Instantly generate and return the current date and time cleanly structured as "YYYY-MM-DD HH:MM:SS"
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    # Public instance method allowing a specific member object to officially check out a book using its 'book_id'
    def lend_book(self, book_id):
        book_to_lend = None  # Temporary placeholder variable to hold the reference for the book requested
        
        # Validation 1: Check internally if the member has already reached their maximum borrowing limit (accessing private var)
        if self.total_borrowed >= self.__max_books_allowed:
            print("Maximum borrow limit reached!")
            return  # Cancel the checkout process
            
        # Validation 2: Linearly search for the explicitly requested book_id inside the library's master collection
        for book in Library.books_collection:
            if book['book_id'] == book_id:
                book_to_lend = book  # If a match is found, assign the reference to our placeholder
                break                # Escape the loop early since we found it
                
        # Validation 3: Ensure the book realistically exists inside the library logs
        if not book_to_lend:
            print(f"Book with ID {book_id} not found!")
            return False
            
        # Validation 4: Double check if all physical copies naturally ran out already
        if book_to_lend['available_copies'] <= 0:
            print(f"Sorry! {book_to_lend['book']} is currently not available.")
            return False
            
        # Validation 5: Loop to check if this specific member has strictly borrowed this exact exact book before without returning it
        for borrowed in self.borrowed_books:
            if borrowed['book_id'] == book_id and not borrowed['returned']:
                print(f"You have already borrowed '{book_to_lend['book']}'!")
                return False  # Cancels process to prevent infinite hoarding
           
        # Logic Start: If all validations pass, proceed to successfully grant the library book!
        # Step A: Decrement available physical copies specifically for that book by exactly 1
        book_to_lend['available_copies'] -= 1
        # Step B: Decrement the generalized total number of freely existing books by exactly 1
        Library.number_of_books -= 1
        
        # Step C: Generate a local dictionary log to hold granular details for this specific borrow transaction
        borrow_record = {
            "book_id": book_id,
            "book": book_to_lend['book'],
            "author": book_to_lend['author'],
            "borrowed_date": self._get_current_date(), # Triggering protected inner method for a timestamp
            "returned": False                          # Flag signifying the literal status (not returned yet)
        }
        
        # Step D: Insert the temporary log dictionary into the member's private tracked borrow list
        self.borrowed_books.append(borrow_record)
        # Step E: Increment their count integer variable signifying they hold one more book now
        self.total_borrowed += 1

        # Step F: Push a parallel generic copy to the Library's global historic list of all borrowed movements
        Library.borrowed_books.append({
            "member": self.member,
            "book": book_to_lend['book'],
            "book_id": book_id,
            "borrowed_date": self._get_current_date()
        })

        # Process Confirmation: Inform the console about the exact operation result
        print("Book borrowed successfully!")
        print(f"Member Name: {self.member}")
        print(f"Book: {book_to_lend['book']}")
        print(f"Author: {book_to_lend['author']}")
        print(f"Borrowed Date: {borrow_record['borrowed_date']}")
        print(f"Remaining Copies: {book_to_lend['available_copies']} \n")

    # Public instance method letting a member process returning a book. Includes an optional days_late parameter.
    def return_book(self, book_id, days_late=0):
        borrowed_record = None # Placeholer to find the log showing this person genuinely borrowed it
        
        # Step 1: Scan this member's active borrow logs to prove they took it and haven't given it back
        for record in self.borrowed_books:
            if record['book_id'] == book_id and not record['returned']:
                borrowed_record = record
                break

        # If we didn't populate the placeholder, they legally can't return it
        if not borrowed_record:
            print("You have not borrowed this book or it's already returned!")
            return False

        library_book = None # Placeholder to discover the global parent structure for the original book
        
        # Step 2: Look up the identical book object residing globally in the library databases
        for book in Library.books_collection:
            if book['book_id'] == book_id:
                library_book = book
                break

        # Step 3: Mutate the master values safely back to normality
        if library_book:
            library_book['available_copies'] += 1 # Freeing up exactly 1 stock
            Library.number_of_books += 1          # Replacing 1 global physical unit

        # Step 4: Toggle the member's private record signifying it is properly closed out
        borrowed_record['returned'] = True
        borrowed_record['returned_date'] = self._get_current_date() # Stamping the literal precise time
        self.total_borrowed -= 1 # Deflating their active borrow count

        # Step 5: Iteratively hunt down the matching log inside the global library logs and seal it via 'returned_date'
        for record in Library.borrowed_books:
            if (record['member'] == self.member and record['book_id'] == book_id and 'returned_date' not in record):
                record['returned_date'] = self._get_current_date()

        # Step 6: Confirmation prints reporting the success and statistics
        print("Book Returned Successfully!")
        print(f"Member: {self.member}")
        print(f"Book: {borrowed_record['book']}")
        print(f"Returned Date: {borrowed_record['returned_date']}")

        # Step 7: Evaluate fines if it was definitively late
        if days_late > 0:
                fine = self.__calculate_fine(days_late)     # Trigger internal restricted method for mathematics
                self.__fine_amount += fine                  # Pile up the charge privately behind the scenes
                print(f"Late return! Fine: Rs.{fine}/-")
       
        # Print the updated fresh availability info if it resolved smoothly
        if library_book:
            print(f"Available Copies: {library_book['available_copies']}\n")
        return True
   
    # Public accessor method providing a safe structured way strictly just to fetch and display the hidden private fine total
    def get_fine(self):
        print(f"Total fine: Rs.{self.__fine_amount}")

    # Public diagnostic method purely returning internal configurations about the profile
    def show_membership(self):
        print("Membereship Details:")
        # Displaying combinations of public keys and securely extracted protected fields.
        print(f"Member: {self.member}\nMember ID: {self._member_id}\nMembership Type: {self._membership_type}")
   

# --- Setup Phase: Adding Books ---
# Instead of instancing, we call the class methods directly via Library to cleanly dump data inward
Library.add_book("Sri Ramayana Darshanam", "Kuvempu", "Mythology", "Sapna Book House", 5)
Library.add_book("Srimadh Bhagavatham", "Madhwa", "Mythology", "Geetha Book House", 8)
Library.add_book("Panchatantra", "Ram", "Fiction", "Kids Stories", 12)
Library.add_book("Amar Chitra Katha", "Keshav", "Fiction", "Kids Stories", 15)

# Generating an overarching snapshot visualization checking the inventory after our inserts
Library.list_books()


# --- Member Registration Phase ---
# Booting up 3 disparate user Member instances by creating objects out of the Library archetype
member1 = Library("Akshay Rao", "M-001")
member2 = Library("Ajay Rao", "M-002")
member3 = Library("Vikas", "M-003")


# --- Active Execution Phase ---
# member1 explicitly demands checking out book with ID 1
member1.lend_book(1)
# member2 intentionally borrows the exact same book with ID 1 (copies of book #1 will deplete furthermore)
member2.lend_book(1)

# member3 decides to aggressively hoard books quickly
member3.lend_book(3)
member3.lend_book(4)
member3.lend_book(1)
# ⚠️ This next instruction line correctly triggers a failure mechanism since member3 struck the __max_books_allowed boundary (3 books)!
member3.lend_book(2)


# Taking another snapshot visualization. Observe closely how available copies naturally fell dynamically.
Library.list_books()


# --- Restoring Phase ---
# member1 fulfills returning book with ID 1 securely
member1.return_book(1)

# Third observation visualization confirming copies logically bounced correctly upward!
Library.list_books()

# Triggering member1's formal system to display hidden fine records cleanly outward
member1.get_fine()