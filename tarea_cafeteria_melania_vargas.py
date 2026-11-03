# Tarea 3 - Sistema de Pedidos para Cafetería


def mostrar_menu(menu):
    print("\n--- MENÚ DE LA CAFETERÍA ---")
    # Muestra los productos numerados con su precio usando formato monetario
    for i, (prod, precio) in enumerate(menu.items(), 1):
        print(f"{i}. {prod.capitalize()} - ${precio:.2f}")

def agregar_producto(menu, pedido):
    print("\n--- AGREGAR AL PEDIDO ---")
    mostrar_menu(menu)
    
    # Pedir el producto que se desea agregar
    nombre = input("¿Qué producto deseas agregar?: ").strip().lower()
    
    # Validación de existencia del producto en el menú usando un bucle con for/else (requisito técnico)
    for item in menu:
        if item == nombre:
            break
    else:
        # Se ejecuta si el bucle termina sin encontrar el producto
        print(f"❌ El producto '{nombre}' no está disponible en el menú.")
        return

    # Pedir cantidad y validar que sea un número entero positivo
    while True:
        try:
            cantidad = int(input(f"¿Cuántas unidades de '{nombre}' deseas?: "))
            if cantidad > 0:
                break
            else:
                print("❌ La cantidad debe ser mayor a cero.")
        except ValueError:
            print("❌ Por favor, ingresa un número entero válido.")

    # Agregar a la lista del pedido o sumar si ya estaba registrado
    encontrado = False
    for item in pedido:
        if item["producto"] == nombre:
            item["cantidad"] += cantidad
            encontrado = True
            break
            
    if not encontrado:
        pedido.append({
            "producto": nombre,
            "precio": menu[nombre],
            "cantidad": cantidad
        })
        
    print(f"¡Listo! Se agregó {cantidad} de '{nombre}' a tu pedido.")

def ver_pedido(pedido):
    print("\n--- TU PEDIDO ACTUAL ---")
    if not pedido:
        print("Aún no tienes productos en tu pedido.")
        return 0.0

    subtotal_total = 0.0
    for item in pedido:
        subtotal = item["precio"] * item["cantidad"]
        subtotal_total += subtotal
        print(f"- {item['cantidad']}x {item['producto'].capitalize()} | Precio unitario: ${item['precio']:.2f} | Subtotal: ${subtotal:.2f}")
    
    print(f"\nSubtotal a pagar: ${subtotal_total:.2f}")
    return subtotal_total

def finalizar_pedido(nombre, pedido):
    subtotal = ver_pedido(pedido)
    if subtotal == 0.0:
        print("Tu carrito está vacío, no se puede finalizar.")
        return False

    print("\n--- FINALIZAR COMPRA ---")
    # Pedir y validar la propina (entre 0 y 100)
    while True:
        try:
            propina_porcentaje = float(input("¿Qué porcentaje de propina deseas dejar (0 al 100)?: "))
            if 0 <= propina_porcentaje <= 100:
                break
            else:
                print("❌ El porcentaje debe estar entre 0 y 100.")
        except ValueError:
            print("❌ Entrada inválida. Ingresa un número.")

    # Cálculos finales con formato de dos decimales
    monto_propina = subtotal * (propina_porcentaje / 100)
    total = subtotal + monto_propina

    # Resumen detallado con f-strings
    print("\n" + "="*35)
    print("      RESUMEN DE SU PEDIDO      ")
    print("="*35)
    print(f"Cliente: {nombre.title()}")
    print("Detalle:")
    for item in pedido:
        sub = item["precio"] * item["cantidad"]
        print(f"  • {item['cantidad']}x {item['producto'].capitalize()} -> ${sub:.2f}")
    
    print("-" * 35)
    print(f"Subtotal:       ${subtotal:.2f}")
    print(f"Propina ({propina_porcentaje:.0f}%):  ${monto_propina:.2f}")
    print(f"TOTAL A PAGAR:  ${total:.2f}")
    print("="*35)
    print("¡Muchas gracias por tu visita a nuestra cafetería!")
    return True

def main():
    # Menú con al menos 6 productos almacenados en un diccionario
    menu_cafeteria = {
        "espresso": 1.50,
        "capuchino": 2.50,
        "latte": 2.75,
        "americano": 1.75,
        "mocha": 3.00,
        "croissant": 2.25
    }

    pedido = []

    print("☕ ¡Bienvenido a nuestra cafetería! ☕")
    nombre_cliente = input("Por favor, dinos tu nombre: ").strip()
    print(f"\nHola {nombre_cliente.title()}, ¡qué gusto saludarte!")

    # Bucle principal del menú repetitivo
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("a. Ver menú de productos")
        print("b. Agregar producto al pedido")
        print("c. Ver mi pedido actual")
        print("d. Finalizar pedido y salir")
        
        opcion = input("Elige una opción (a, b, c, d): ").strip().lower()

        if opcion == 'a':
            mostrar_menu(menu_cafeteria)
        elif opcion == 'b':
            agregar_producto(menu_cafeteria, pedido)
        elif opcion == 'c':
            ver_pedido(pedido)
        elif opcion == 'd':
            completado = finalizar_pedido(nombre_cliente, pedido)
            if completado:
                break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()