from fpdf import FPDF

def convert_text_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=9)

    with open(input_file, 'r', encoding='utf-8') as file:
        text_content = file.readlines()

    line_height = 8
    top_margin = 10

    pdf.set_top_margin(top_margin)

    for line in text_content:

        if "Username:" in line and "Hashed Password:" in line:
            pdf.multi_cell(0, line_height, line.strip())
        else:
            pdf.ln(line_height)
            pdf.multi_cell(0, line_height, line.strip())

    pdf.output(output_file)

if __name__ == "__main__":
    input_text_file = "input.txt"
    output_pdf_file = "output.pdf"

    convert_text_to_pdf(input_text_file, output_pdf_file)
