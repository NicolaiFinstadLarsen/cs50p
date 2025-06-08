from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("times", "B", 16)

pdf.cell(0, 15, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
# coursor_y = pdf.get_y()

# print(f"{coursor_y=}")
pdf.image("shirtificate.png", w=72, x=(210-72)/2)

pdf.set_y(50) # Jusst guessing.
pdf.set_font("times", "I", 10)
pdf.set_text_color(255,255,255)

user_name=input("Name: ")
pdf.cell(0, 10, user_name, new_x="LMARGIN", new_y="NEXT", align="C")

# For submit 50
# pdf.output("shirtificate.pdf") 

pdf.output(f"{user_name}.pdf")

# print(pdf.w)


