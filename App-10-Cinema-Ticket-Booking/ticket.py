import fpdf
class Ticket:

    def __init__(self, ticket_id, username, price, seat):
        self.seat = seat
        self.price = price
        self.username = username
        self.ticket_id = ticket_id

    def to_pdf(self):
        pdf = fpdf.FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()


        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Ticket Booking", border=0, align="C", ln=1)
        pdf.cell(w=0, h=40, ln=1)

        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=150, h=40, txt="Name: ", border=1)
        pdf.cell(w=150, h=40, txt=f'{self.username}', border=1, ln=1)

        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=150, h=40, txt="Seat Number: ", border=1)
        pdf.cell(w=150, h=40, txt=f'{self.seat}', border=1, ln=1)

        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=150, h=40, txt="Ticket Id: ", border=1)
        pdf.cell(w=150, h=40, txt=f'{self.ticket_id}', border=1, ln=1)

        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=150, h=40, txt="Price: ", border=1)
        pdf.cell(w=150, h=40, txt=f'{self.price}', border=1, ln=1)

        pdf.output('Ticket.pdf')

