import streamlit as st
from database import MyLeave, session, User

class SessionState:
    def __init__(self):
        self.current_user = None

def authenticate_user(email, password):
    try:
        user = session.query(User).filter(User.email==email, User.password==password).first()
        if user:
            return user
    except Exception as e:
        st.error("An error occurred during login:", e)

def create_new_user(email, password, role):
    try:
        new_user = User(password=password, email=email, role=role)
        session.add(new_user)
        session.commit()
        return new_user
    except Exception as e:
        st.error("An error occurred during user creation:", e)


def save_leave_data(applied_to, cc, from_date, to_date, leave_type, duration, reason, document, id):
    document_data = None
    if document is not None:
        document_data = document.read() 
    leave = MyLeave(
        appiled_to = applied_to,
        cc=cc,
        from_date=from_date,
        to_date=to_date,
        leaveType=leave_type,
        leaveDuration=duration,
        reason =reason,
        document=document_data,
        status="Pending",
        action="",
        user_id=id
    )
    session.add(leave)
    session.commit()        

session_state = SessionState()
