#!/usr/bin/env python
# coding: utf-8
# %%
import streamlit as st
import pandas as pd
import os


# %%

# توابع
def load_excel_file(file_path, file_name):
    try:
        full_path = os.path.join(file_path, file_name)
        data = pd.read_excel(full_path)
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")


# صفحه اصلی
def main():
    
    # فرم ورودی برای انتخاب نام فایل
    file_name = st.text_input("نام نماد را وارد کنید:") + '.xlsx'
    
    st.title(f"{file_name}")

    file_path = "D:\\codal\\fasli\\"
    
    if st.button("View Excel"):
        if file_name:
            data = load_excel_file(file_path=file_path,file_name=file_name)
            if data is not None:
                st.write("### Data:")
                st.dataframe(data)
        else:
            st.warning("Please enter a file name.")

if __name__ == "__main__":
    main()



# %%
