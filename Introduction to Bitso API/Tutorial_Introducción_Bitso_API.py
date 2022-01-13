import bitso
api = bitso.Api('API_KEY', 'API_SECRET')

# Libros de pedidos disponibles en Bitso
libros = api.available_books()
print("Libros disponibles", libros)

# Extracción de listado
print("\nLista:", libros.books)

# Extracción de elemento de listado
print("\nElemento 0:", libros.books[0])
