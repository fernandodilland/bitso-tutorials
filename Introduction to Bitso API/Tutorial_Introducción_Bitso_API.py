import bitso
api = bitso.Api('API_KEY', 'API_SECRET')

# Libros de pedidos disponibles en Bitso
libros = api.available_books()
print("Libros disponibles:", libros)

# Extracción de lista
print("Lista:", libros.books)

# Extracción de elemento de lista
print("Elemento 0:", libros.books[0])
