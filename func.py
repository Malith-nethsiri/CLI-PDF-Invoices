from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Arial", "", 12)

    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "INVOICE", ln=True, align='C')
        self.ln(10)

    def add_invoice_info(self, invoice_no, issued_date, due_date):
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Invoice No: {invoice_no}", ln=True)
        self.cell(0, 10, f"Issued Date: {issued_date}", ln=True)
        self.cell(0, 10, f"Due Date: {due_date}", ln=True)
        self.ln(5)

    def add_company_info(self, name, address, phone, email):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Company Details:", ln=True)
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Name: {name}", ln=True)
        self.multi_cell(0, 10, f"Address: {address}")
        self.cell(0, 10, f"Phone: {phone}", ln=True)
        self.cell(0, 10, f"Email: {email}", ln=True)
        self.ln(5)

    def add_customer_info(self, name, address, phone, email):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Customer Details:", ln=True)
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Name: {name}", ln=True)
        self.multi_cell(0, 10, f"Address: {address}")
        self.cell(0, 10, f"Phone: {phone}", ln=True)
        self.cell(0, 10, f"Email: {email}", ln=True)
        self.ln(5)

    def add_items_table(self, items, quantities, prices):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(70, 10, "Item", border=1, fill=True)
        self.cell(30, 10, "Qty", border=1, fill=True)
        self.cell(40, 10, "Price", border=1, fill=True)
        self.cell(40, 10, "Total", border=1, ln=True, fill=True)

        self.set_font("Arial", "", 12)
        total = 0
        for item, qty, price in zip(items, quantities, prices):
            subtotal = qty * price
            total += subtotal
            self.cell(70, 10, item, border=1)
            self.cell(30, 10, str(qty), border=1)
            self.cell(40, 10, f"${price:.2f}", border=1)
            self.cell(40, 10, f"${subtotal:.2f}", border=1, ln=True)

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(140, 10, "Total Amount", border=0)
        self.cell(40, 10, f"${total:.2f}", border=1, ln=True)

    def add_notes(self, notes):
        self.ln(10)
        self.set_font("Arial", "I", 11)
        self.multi_cell(0, 10, f"Notes: {notes}")

    def save(self, filename):
        if not filename.endswith(".pdf"):
            filename += ".pdf"
        self.output(filename)
        print(f"Invoice saved as {filename}")
        try:
            os.startfile(filename)  # Windows only
        except Exception:
            pass

