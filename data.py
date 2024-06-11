
import streamlit as st
import pandas as pd
# توابع
def load_excel_file(file_name):
    try:
        data = pd.read_excel(f"{file_name}.xlsx")
    except Exception as e:
        st.error(f"Error loading file: {e}")


# صفحه اصلی
def main():
    
    # فرم ورودی برای انتخاب نام فایل
    file_name = st.text_input("نام نماد را وارد کنید:") + '.xlsx'
    
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
