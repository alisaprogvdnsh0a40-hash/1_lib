# 1_lib
 |
 |__cli.py   (main app and functions)
 |
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
 |__exceprion.py
 |       |__LibraryError(Exception)
 |       |__BookNotFound(LibraryError)
 |       |__UserNotFound(LibraryError)
 |       |__PermissionDenied(LibraryError)
 |       |__BookNotAvailable(LibraryError)
 |       
    