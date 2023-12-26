from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
name = input("Name: ")

pdf.image("shirtificate.png", 1, 25, 150)
pdf.set_font("helvetica", "B", 25)
pdf.cell(0, 60, 'CS50 Shirtificate.', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.set_text_color(255, 255, 255)
pdf.text(x=62, y=150, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")