# AUTOMATED-REPORT-GENERATION
**COMPANY**: CODETECH IT SOLUTIONS

**NAME**: KHUSHI CHAUDHARY

**INTERN ID**:CT08IHY

**DOMAIN**: PYTHON

**BATCH DURATION**: DECEMBER 30TH,2024 TO JANUARY 30TH,2025

**MENTOR NAME**: NEELA SANTOSH

**DESCRIPTION**:
This Python script combines data analysis and report generation functionalities to create a PDF report summarizing key statistics of a dataset provided in a CSV file. It uses the pandas library for data manipulation and analysis, and the FPDF library to create and format the PDF report. The script is structured into three primary components: data analysis, PDF generation, and a main function to drive the execution.

Detailed Explanation
1. Data Analysis Using pandas
The function analyze_data(file_path) is responsible for reading and analyzing the CSV file:

Input: The user provides the path to the CSV file containing tabular data.
Processing: The pandas library reads the CSV data using pd.read_csv(file_path). The .describe() method of pandas is then applied to compute key statistical summaries (e.g., count, mean, standard deviation, min, max, and quartiles) for each column in the dataset.
Output: The function returns a DataFrame object (summary) containing these statistical summaries, which is later used for report generation.
2. Generating the PDF Report
The function generate_pdf_report(summary, output_path) takes the statistical summary and creates a well-structured PDF report:

A new PDF object is created using FPDF(). The report starts with a title "Data Analysis Report," aligned at the center.
For each column in the dataset, the function iterates through its statistical summary and adds formatted lines to the PDF. Each line contains a descriptive statistic (e.g., mean or standard deviation) and its corresponding value.
The report is saved to the specified output_path (default is "data_analysis_report.pdf").
Key Features of PDF Generation:
Readable Formatting: Each column's name and its statistical summaries are grouped, making it easier for users to interpret the results.
Structure and Layout: Appropriate line breaks and padding are used for clarity.
3. Main Function Execution
The main() function orchestrates the entire script:

It prompts the user to input the file path of the dataset.
The file is analyzed by invoking analyze_data(file_path).
The statistical summary is passed to generate_pdf_report() to create the PDF file.
After successful generation, the path of the PDF is displayed to the user.
Practical Use Case
This script is particularly useful for individuals or organizations who need to analyze datasets quickly and present insights in a report format. Examples include:

Business Analysts: Automatically generate reports for sales or customer data.
Researchers: Summarize experimental data for further analysis.
Educators: Teach data analysis concepts and reporting techniques.
How It Works in VS Code
Using VS Code makes executing this script seamless:

Setup:

Install the required libraries (pandas and fpdf) via pip install pandas fpdf.
Save the script in a .py file (e.g., data_analysis.py).
Execution:

Open a terminal in VS Code and run the script using python data_analysis.py.
Provide the path to a valid CSV file when prompted.
Result:

A PDF report (data_analysis_report.pdf) will be generated in the script's directory, summarizing the dataset's key statistics.
Summary
This script streamlines the process of analyzing numerical data and generating a professional PDF report. It combines the simplicity of pandas for analysis and the flexibility of FPDF for document generation. By automating this process, the script saves time and reduces manual errors in creating structured reports, making it a valuable tool for data-driven decision-making.







