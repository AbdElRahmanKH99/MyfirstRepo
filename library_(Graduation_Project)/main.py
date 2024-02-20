#Book you own

library = []
books_own = input("Enter the name of a book you own: ")
library.append(books_own)

#Another book or skip

books_own = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if books_own:
    library.append(books_own)
    print(f"Your Library: {library}")
else:
    print(f"Your Library: {library}")

#Print library and ask about future book

wishlist = []
books_own = input("Enter the name of a book you wish to have in the future: ")
wishlist.append(books_own)

#Another book or skip

books_own = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")

#Print whishlist and ask about acquired book or skip

if books_own:
    wishlist.append(books_own)
print(f"Your Wishlist: {wishlist}")
acquired_book = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")

#Print updated library and wishlist and ask about book to donate or skip

if acquired_book in wishlist:
    wishlist.remove(acquired_book)
    library.append(acquired_book)
    print(f"Updated Library: {library}")
    print(f"Updated Wishlist: {wishlist}")
print(f"Updated Library: {library}")
print(f"Updated Wishlist: {wishlist}")
donate_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donate_book in library:
    library.remove(donate_book)    
    print(f"Final Library after Donations: {library}")
print(f"Final Library: {library}")

#Print final library after donation
