import os
import webbrowser

class PdfReport:

    """
    Generates a pdf file that contains the data about the
    flatmates, their period and their share in the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        from fpdf import FPDF

        flatmate1_pay = round(flatmate1.pays(bill=bill, flatmate2=flatmate2),4)
        flatmate2_pay = round(flatmate2.pays(bill=bill, flatmate2=flatmate1),4)

        # Make pdf
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)
        #Add Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        # Add Period
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=f'{bill.period}', border=0, ln=1)
        pdf.cell(w=0, h=40, ln=1)

        # Add column names
        pdf.cell(w=200, h=40, txt="Flatmate name", border=1)
        pdf.cell(w=170, h=40, txt="Amount to pay", border=1, ln=1)

        # Add Flatmates
        pdf.cell(w=200, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=170, h=40, txt=f'{flatmate1_pay}', border=1, ln=1)

        pdf.cell(w=200, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=170, h=40, txt=f'{flatmate2_pay}', border=1, ln=1)

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))
