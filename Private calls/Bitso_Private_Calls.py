import bitso
api = bitso.Api('API_KEY', 'API_SECRET')

# Estado de la cuenta
estado = api.account_status() # Clase
print("\nEstado:", estado.status)

# Saldo de la cuenta
saldo = api.balances() # Clase
print("\nMonedas:", saldo.currencies) # Lista
print("Disponible en BTC:", saldo.btc.available) # Decimal

# Operaciones
operaciones = api.ledger() # Lista
print("\nOperacion:", operaciones[0].balance_updates) # Lista
print("Detalle:", operaciones[0].balance_updates[0].amount) # Decimal

# Retiros
retiros = api.withdrawals() # Lista
print("\nRetiro:", retiros[0]) # Clase

# Fondeos
fondeos = api.fundings() # Lista
print("\nFondeo:", fondeos[0]) # Clase

# Operaciones de trading del usuario
op_trading = api.user_trades()
print("\nOperacion:", op_trading[0]) # Clase # .side, .book, .type, .btc

# Órdenes abiertas
ordenes_abiertas = api.open_orders('btc_mxn')
print("\nOrden abierta:", ordenes_abiertas[0]) # Clase # .price .oid

# Cancelar orden
cancelar = api.cancel_order(ORDER_ID)
print("Cancelación:", cancelar)

# Poner ordenes_abiertas
orden = api.place_order(book='btc_mxn', side='sell', order_type='limit', major='.01', price='600000.00')
print("Orden puesta:", orden)
