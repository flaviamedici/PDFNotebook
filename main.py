from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # adding main pages
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 25, 200, 25)

    # set the footer
    pdf.ln(265)
    pdf.set_font('Arial', 'B', size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

#adding additional pages based on the topic
    for i in range(row['Pages']-1):
        pdf.add_page()
        for x in range(20, 280, 10):
            pdf.line(10, x, 200, x)
        # set the footer
        pdf.ln(265)
        pdf.set_font('Arial', 'B', size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

pdf.output("output.pdf")