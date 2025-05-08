from fpdf import FPDF
import os

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title font
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt='Nutrition for the Elderly: Key Dietary Needs and Tips for Healthy Aging', ln=True, align='C')

# Add space before starting content
pdf.ln(10)

# Set content font
pdf.set_font('Arial', '', 12)

# Define the content of the article
content = [
    "As we age, our bodies undergo significant changes, making nutrition more important than ever. Proper nutrition helps older adults maintain physical health, cognitive function, and overall vitality. Understanding the specific dietary needs of seniors can lead to healthier, more vibrant aging.",
    # Rest of the content lines...
]

# Add content to PDF line by line
for line in content:
    pdf.multi_cell(0, 10, line)

# Specify the desktop path where you want to save the PDF
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
pdf_output = os.path.join(desktop_path, "nutrition_for_the_elderly.pdf")

# Save the PDF to the desktop
pdf.output(pdf_output)

pdf_output