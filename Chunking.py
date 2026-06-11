from Parsing import extract_plain_text
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunk(pdf_path):
    # Get Raw Text
    raw_text = extract_plain_text(pdf_path)
    
    # Text Spliting Rule Setup
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 150,
        separators=["\n\n", "\n", " ", ""]
    )
    
    
    # Generate Chunks
    chunks = text_splitter.split_text(raw_text)
    
    return chunks








BASE_DIR = Path.home()
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parent
ROOT_DIR = PROJECT_DIR.parent
FILE_DIR = ROOT_DIR / "Lawyer Assistant" / "lawyer_assistant" / "uploads" / "constitutions" / "Constitution.pdf"


#extract_from_pdf(FILE_DIR)


#doc = pymupdf.open(FILE_DIR)

#print (doc.load_page(0))

#print(f"Base Dir: {base_dir}")
#print(f"Current Dir: {CURRENT_DIR}")
#print("Success")
    
    
    
    
# Exicute The Code

if __name__ == "__main__":
    pdf_file = FILE_DIR
    
    my_chunks = create_chunk(pdf_file)
    
    print(f"Successfully created {len(my_chunks)} chunks.")
    print("______Sample Chunk_______")
    print(my_chunks[70])