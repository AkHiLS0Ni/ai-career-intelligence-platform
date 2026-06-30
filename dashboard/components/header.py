import streamlit as st


def page_header(title: str, subtitle: str = ""):
    """
    Display a professional page header.
    """

    st.title(title)

    if subtitle:
        st.markdown(
            f"<h4 style='color:gray'>{subtitle}</h4>",
            unsafe_allow_html=True,
        )

    st.divider()
