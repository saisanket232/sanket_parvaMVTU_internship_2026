#list propoerties

book=["single","double","triple"]
print("Book :",book)

print(book,type(book))

print("length :",len(book))

Count=book.count("single")
print("Count of Single:",Count)

print(book[0],book[2])

book.append("fourth")
print("Append :",book)

book.insert(2,"fifth")
print("Insert :",book)
#pop(index)
book.pop(3)
print("Pop :",book)
#remove(value)
book.remove("single")
print("Remove :",book)

book.reverse()
print("Reverse :",book)

books=book.copy()
print("Copy :",books)

group=["sixth","seventh"]
book.extend(group)
print("Extend :",book)

#sort

print("before sort :",book)
print("after sort :",sorted(book))
# book.sort(reverse=True)==used to sort in reverse order
print("Reverse sort :",sorted(book,reverse=True))
print("Original list :",book)
h4=book.index("double")
print("Index of double :",h4)
#del 
del book[2]
print("Del :",book)

book.clear()
print("Clear :",book)