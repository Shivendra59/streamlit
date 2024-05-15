import streamlit as st
from session_manager import save_leave_data, session_state


def apply_leave():
    st.markdown(
        """
    <style>
    .inline-block {
        display: inline-block;
        margin-right: 10px;
        font-weight: bold;
        font-size: 18px;
    }
    .inline-block a {
        text-decoration: none;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
       <div class="inline-block">
            <a href="/" class="back-btn">&#8592;</a>
        </div>
        <div class="inline-block">
            Apply Leaves
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("Details")
    col1, col2 = st.columns([1, 1])
    col3, col4 = st.columns([1, 1])

    with col1:
        applied_to = st.selectbox("Applied To *", ["Select","Vyshnavi K"])
    with col2:
        cc = st.selectbox("CC *", ["Select", "CC1", "CC2"])
    with col3:
        from_date = st.date_input("From Date *")
    with col4:
        to_date = st.date_input("To Date *")

    col5, col6 = st.columns([1, 1])
    with col5:
        leave_type = st.selectbox("Leave Type *", ["Select", "Sick", "Privilege Leave", "Loss of Pay"])
    with col6:
        duration = st.selectbox("Leave Duration *", ["Select Duration", "Full Day", "Half Day", "Short Day"])
   
    reason = st.text_area("Reason *", placeholder="Write here...")

    document = st.file_uploader("Attach Document (Optional)", type=["pdf", "jpg", "png"])

    col7, col8 = st.columns([0.2, 1])
    with col7:
        if st.button("Submit"):
            if (applied_to == "Select" or cc == "Select" or from_date is None or to_date is None or leave_type == "Select" or duration == "Select Duration" or reason == ""):
                st.error("Please fill out all the mandatory fields.")
            else:
                if session_state.current_user:
                    save_leave_data(applied_to,cc,from_date,to_date,leave_type, duration,reason,document, session_state.current_user.id,)
                    st.success("Leave application submitted successfully!")
    with col8:
        if st.button("Cancel"):
            st.warning("Leave application cancelled.")
        