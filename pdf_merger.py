"""
Merging PDFs into one big PDF has never been so easy and free thanks to creators of pyPDF2
"""
from PyPDF2 import PdfFileMerger, PdfFileReader
from PyPDF2.utils import PdfReadError
from argparse import ArgumentParser


def is_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            PdfFileReader(pdf_file)
        return True
    except (PdfReadError, OSError, FileNotFoundError):
        """
        Possible exceptions:
        PdfReadError - When problem opening a PDF file.
        OSError - When a non-pdf file such as txt is attempted to be opened.
        PyPDF2 throws OSError: [Errno 22] Invalid argument
        FileNotFoundError - When the filename is not found in the argument list.
        """
        return False


def merge_pdfs(list_of_pdf, merged_filename="merged.pdf"):
    merger = PdfFileMerger()
    for pdf in list_of_pdf:
        if is_pdf(pdf):
            merger.append(pdf)
    try:
        merger.write(merged_filename)
    except (PdfReadError, AttributeError) as e:
        print(e)


if __name__ == '__main__':
    parser = ArgumentParser()
    # -f / --file accepts a list of arguments, the nargs=+ means it accepts 1 or more
    parser.add_argument('-f', '--file', nargs='+', dest="user_inputs", help='pdf files to merge', required=True)
    parser.add_argument('-o', '--outfile', dest='output_filename', help="filename after merged pdf, default is "
                                                                        "merged.pdf if not specified", required=False)
    args = parser.parse_args()
    if args.output_filename:
        merge_pdfs(args.user_inputs, args.output_filename)
    else:
        merge_pdfs(args.user_inputs)
