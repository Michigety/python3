from pypdf import PdfWriter

def merge_pdf(files, name):
    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

    merger.write(f"{name}.pdf")
    merger.close()

if __name__ == "__main__":
    tmp = ["1.pdf", "2.pdf"]
    merge_pdf(tmp, "output")

