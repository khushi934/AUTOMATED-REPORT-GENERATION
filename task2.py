import pandas as pd
from fpdf import FPDF

# Function to read and analyze data
def analyze_data(file_path):
    data = pd.read_csv(file_path)
    summary = data.describe()
    return summary

# Function to generate PDF report
def generate_pdf_report(summary, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    for column in summary.columns:
        pdf.cell(200, 10, txt=f"Summary for {column}", ln=True, align='L')
        for stat in summary.index:
            value = summary.at[stat, column]
            pdf.cell(200, 10, txt=f"{stat}: {value}", ln=True, align='L')
        pdf.ln(5)
    
    pdf.output(output_path)

# Main function
def main():
    file_path = input("Enter the path to the CSV file: ")
    output_path = "data_analysis_report.pdf"
    summary = analyze_data(file_path)
    generate_pdf_report(summary, output_path)
    print(f"PDF report generated: {output_path}")

if __name__ == "__main__":
    main()
