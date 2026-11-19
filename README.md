# 1_lib
 
 
 (Library managment app)
 |
 |__cli.py   (main app and functions)
 |
 |__app
    |__models.py
    |       |__Book
    |       |__User(metacalss)
    |       |__Guest(User)
    |       |__Member(User)
    |       |__Librarian(User)
    |       |__Library
    |
    |__session.py
    |       |__LibSession
    |
    |__meta.py
    |       |__UserMeta(type)
    |
    |__descriptors.py
    |       |__Descriptor_int
    |
    |__exception.py
    |       |__LibraryError(Exception)
    |       |__BookNotFound(LibraryError)
    |       |__UserNotFound(LibraryError)
    |       |__PermissionDenied(LibraryError)
    |       |__BookNotAvailable(LibraryError)
    |       

==>> run cli.py to run a library with default values.
(can be add another users and books)

+library have three permission for three position(guest,member,librarian)
  with their own access.

+password for define new librarian user is (1234).