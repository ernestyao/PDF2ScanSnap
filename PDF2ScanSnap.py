import argparse
from pypdf import PdfReader, PdfWriter

# 需要改写的创建者信息
ScanSnap = "ScanSnap Manager #iX500 (W)"

def printMeta(fileName):
    reader = PdfReader(fileName)
    meta = reader.metadata
    if not meta.creator is None:
        print("Original Creator："+meta.creator)
    else:
        print("Creator is null")


def writeMeta(fileName):
    reader = PdfReader(fileName)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(
        {
            "/Creator": ScanSnap,
        }
    )
    # 修改后的文件名加上new后另存
    newfileName = fileName.rsplit('.', 1)[0] + "_new.pdf"
    with open(newfileName, "wb") as f:
        writer.write(f)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help = 'specify PDF file name')
args = parser.parse_args()
fileName = args.filename
if fileName == None:
    print(parser.usage)
    exit(0)
else:
    printMeta(fileName)
    writeMeta(fileName)
