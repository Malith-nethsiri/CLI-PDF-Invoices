from func import PDF
from datetime import date
import typer

app = typer.Typer()

@app.command()
def create_invoice():

    pdf = PDF()

    # Invoice Info
    invoice_no = input("Invoice Number: ")
    issued_date = input("Issued Date (YYYY-MM-DD): ") or date.today().strftime("%Y-%m-%d")
    due_date = input("Due Date (YYYY-MM-DD): ")
    pdf.add_invoice_info(invoice_no, issued_date, due_date)

    # Company Info
    typer.echo("\n--- Company Info ---")
    c_name = input("Company Name: ")
    c_address = input("Company Address: ")
    c_phone = input("Company Phone: ")
    c_email = input("Company Email: ")
    pdf.add_company_info(c_name, c_address, c_phone, c_email)

    # Customer Info
    typer.echo("\n--- Customer Info ---")
    cu_name = input("Customer Name: ")
    cu_address = input("Customer Address: ")
    cu_phone = input("Customer Phone: ")
    cu_email = input("Customer Email: ")
    pdf.add_customer_info(cu_name, cu_address, cu_phone, cu_email)

    # Items
    typer.echo("\n--- Item Details ---")
    items = input("Enter items (comma-separated): ").split(",")
    quantities = list(map(int, input("Enter quantities (comma-separated): ").split(",")))
    prices = list(map(float, input("Enter prices (comma-separated): ").split(",")))
    pdf.add_items_table(items, quantities, prices)

    # Notes
    notes = input("Any additional notes? ")
    pdf.add_notes(notes)

    # Save
    filename = input("Enter filename for PDF: ")
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    pdf.save(filename)

if __name__ == "__main__":
    app()

