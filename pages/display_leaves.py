import streamlit as st
from database import session
from database import MyLeave, BalanceLeave
from pages.apply_leave import apply_leave
from session_manager import session_state
from streamlit_extras.switch_page_button import switch_page


def display_leaves():
    def display_key_value_pairs(key_value_pairs):
        key_color = "#fefbf3" 
        value_color = "#faedc4"

        html_output = "<div style='display: flex;'>"
        for i, (key, value) in enumerate(key_value_pairs.items()):
            html_output += (
                f"<div style='background-color:{key_color}; padding: 7px; border-radius: 1px;'>"
                f"<span style='color:black;'><b>{key}</b>: </span>"
                "</div>"
                f"<div style='background-color:{value_color}; padding: 7px; border-radius: 1px; margin-left: 0px;'>"
                f"<span style='color:black;'>{value}</span>"
                "</div>"
                "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            )
        html_output += "</div>"
        st.write(html_output, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.write("# Leaves")
    with col2:
        search_input = st.text_input("Search")
    with col3:
        st.link_button("+ Apply Leave", "http://localhost:8501/apply_leave")

 
    balance_leave_records = session.query(BalanceLeave).all()
    fetched_leave_types = {}
    for record in balance_leave_records:
        fetched_leave_types[record.leave_type] = record.balance
    display_key_value_pairs(fetched_leave_types)
    st.write("")

    current_user_id = session_state.current_user.id
    summary_data = session.query(MyLeave).filter(MyLeave.user_id == current_user_id).all()
    summary_data = session.query(MyLeave).all()
    if search_input:
      summary_data = [leave for leave in summary_data if search_input.lower() in leave.reason.lower()]

    if summary_data:
        summary_table = []
        for index, leave in enumerate(summary_data, start=1):
            leave_info = {
                "S.No": index,
                "Reason": leave.reason,
                "Date Applied": leave.applied_date.strftime("%Y-%m-%d"),
                "Leave Type": leave.leaveType,
                "From Date": leave.from_date.strftime("%Y-%m-%d"),
                "To Date": leave.to_date.strftime("%Y-%m-%d"),
                "Status": leave.status,
                "Action": leave.action,
            }
            summary_table.append(leave_info)
        st.table(summary_table)
    else:
        st.write("No leave data available")
