from fpdf import FPDF

def generar_ticket_pdf():
    productos = [
        {"nombre": "Manzana", "cantidad": 2, "precio_unitario": 3.5},
        {"nombre": "Leche", "cantidad": 1, "precio_unitario": 15.0},
        {"nombre": "Pan", "cantidad": 3, "precio_unitario": 5.0},
    ]

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Encabezado
    pdf.cell(200, 10, txt="TICKET DE COMPRA", ln=True, align='C')
    pdf.cell(200, 10, txt="---------------------", ln=True, align='C')

    # Cuerpo
    total = 0
    pdf.cell(50, 10, txt="Producto", border=1)
    pdf.cell(30, 10, txt="Cantidad", border=1)
    pdf.cell(40, 10, txt="Precio Unit.", border=1)
    pdf.cell(30, 10, txt="Subtotal", border=1, ln=True)

    for producto in productos:
        subtotal = producto["cantidad"] * producto["precio_unitario"]
        total += subtotal
        pdf.cell(50, 10, txt=producto["nombre"], border=1)
        pdf.cell(30, 10, txt=str(producto["cantidad"]), border=1)
        pdf.cell(40, 10, txt=f"${producto['precio_unitario']:.2f}", border=1)
        pdf.cell(30, 10, txt=f"${subtotal:.2f}", border=1, ln=True)

    # Total
    pdf.cell(150, 10, txt="TOTAL", border=1)
    pdf.cell(30, 10, txt=f"${total:.2f}", border=1, ln=True)

    # Guardar el archivo
    pdf.output("ticket.pdf")
    print("Ticket generado como 'ticket.pdf'.")

generar_ticket_pdf()
