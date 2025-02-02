import pandas as pd

def generate_csv(df, filename="report.csv"):
    """
    Generates a CSV report from the dataframe.
    """
    df.to_csv(filename, index=False)
    
def generate_excel(df, filename="report.xlsx"):
    """
    Generates an Excel report from the dataframe.
    """
    df.to_excel(filename, index=False)
    
def generate_pdf(df, filename="report.pdf"):
    """
    Generates a PDF report from the dataframe.
    (Implementation depends on the library, e.g., ReportLab, WeasyPrint)
    """
    # PDF generation code here
    pass
