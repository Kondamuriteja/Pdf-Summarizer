import streamlit as st
from Extraction import extract_text_from_pdf, read_text_from_file
from summary import search_in_text, summarize_text

def handle_query(query, text):
    query_lower = query.lower()
    if "summary" in query_lower or "summarize" in query_lower:
        return summarize_text(text)
    else:
        results = search_in_text(text, query)
        if results:
            return '\n'.join(results)
        else:
            return "No matches found."

def main():
    st.title("PDF Question Answering Chatbot")

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None:
        pdf_path = 'uploaded_file.pdf'
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.read())
        
        output_file = 'extracted_text.txt'
        extract_text_from_pdf(pdf_path, output_file)
        
        pdf_text = read_text_from_file(output_file)
        
        user_query = st.text_input("Ask a question about the PDF:")

        if st.button("Submit"):
            if user_query:
                response = handle_query(user_query, pdf_text)
                st.write(response)

if __name__ == "__main__":
    main()
