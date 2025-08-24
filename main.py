import streamlit as st
import pandas as pd



def main():
    st.title("Hello from render-app!")
    st.write("This is a simple Streamlit app.")

    sample_df = pd.DataFrame({
        "Column 1": [1, 2, 3],
        "Column 2": ["A", "B", "C"]
    })
    st.write("Here is a sample DataFrame:")
    st.dataframe(sample_df, hide_index=True)

if __name__ == "__main__":
    main()
