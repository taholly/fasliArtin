from pathlib import Path
import streamlit as st
import pandas as pd
# توابع
def load_excel_file(file_name):
    def load_excel_file(file_name):
    try:
        DATA_FILENAME = Path(__file__).parent/f'{file_name}.xlsx'
        data = pd.read_excel(DATA_FILENAME)
        return data  # اینجا اضافه شود
    except Exception as e:
        st.error(f"Error loading file: {e}")

# صفحه اصلی
def main():
    
    # فرم ورودی برای انتخاب نام فایل
    file_name = st.text_input("نام نماد را وارد کنید:")
    
    st.title(f"{file_name}")


    
    if st.button("View Excel"):
        if file_name:
            data = load_excel_file(file_name)
            if data is not None:
                st.write("### Data:")
                st.dataframe(data)
        else:
            st.warning("Please enter a file name.")

if __name__ == "__main__":
    main()
