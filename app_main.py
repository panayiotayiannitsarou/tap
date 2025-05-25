import streamlit as st
import pandas as pd
import openpyxl
import io
import base64

st.set_page_config(page_title="Κατανομή Μαθητών", layout="wide")

# --- Κωδικός Πρόσβασης ---
def password_gate():
    if "access_granted" not in st.session_state:
        st.session_state.access_granted = False

    if not st.session_state.access_granted:
        code = st.text_input("\U0001f510 Εισάγετε τον κωδικό πρόσβασης", type="password")
        if code == "katanomi2025":
            st.session_state.access_granted = True
        else:
            st.stop()

password_gate()

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 Εισαγωγή", "🧮 Κατανομή Μαθητών", "📚 Συχνές Ερωτήσεις", "📥 Εξαγωγή Excel", "📬 Επικοινωνία"])

# --- Tab 1: Εισαγωγή ---
with tab1:
    st.title("📘 Κατανομή Μαθητών με Παιδαγωγικά Κριτήρια")
    st.markdown("## Κανένας Άνθρωπος δεν είναι Νησί – John Donne")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Κανένας άνθρωπος δεν είναι νησί**,  
        ολοκληρωμένος από μόνος του.  
        κάθε άνθρωπος είναι κομμάτι της ηπείρου,  
        μέρος του όλου.  
        [...]  
        Ο θάνατος κάθε ανθρώπου με μειώνει,  
        γιατί εγώ είμαι μέρος της ανθρωπότητας.
        """)
    with col2:
        st.markdown("""
        *No man is an island*,  
        entire of itself;  
        every man is a piece of the continent,  
        a part of the main.  
        [...]  
        Any man's death diminishes me,  
        because I am involved in mankind.
        """)

    st.markdown("---")
    st.markdown("## Η Κοινωνική Δικαιοσύνη στα Σχολεία – Ζήτημα Ύψιστης Σημασίας")
    st.markdown("""
    Η κοινωνική δικαιοσύνη δεν είναι πολυτέλεια, αλλά ευθύνη κάθε σχολείου. Ο εκπαιδευτικός οφείλει να διασφαλίζει ισότητα και ενσυναίσθηση στην πράξη. 
    Η πλήρης και ακριβής καταγραφή των χαρακτηριστικών κάθε παιδιού – όπως η γλωσσική επάρκεια, οι ιδιαίτερες ανάγκες ή η κοινωνική δυναμική – είναι βασική για μια δίκαιη κατανομή στα τμήματα.
    """)
    st.markdown(
        '''
        <div style="padding: 1rem; background-color: #f0f8ff; border-left: 5px solid #1f77b4; font-style: italic;">
        ✨ «Κάποιες φορές αισθανόμαστε ότι αυτό που κάνουμε είναι μόνο μια σταγόνα στον ωκεανό.<br>
        Αλλά ο ωκεανός θα ήταν μικρότερος αν έλειπε αυτή η σταγόνα.»<br>
        — <strong>Μητέρα Τερέζα</strong>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.image("final_logo_bottom_right.png", width=120)
    st.markdown(
        "<div style='text-align: center; font-style: italic; font-size: 14px;'>"
        "Για μια παιδεία που βλέπει το φως στα παιδιά,<br>"
        "ακόμη και εκεί που άλλοι βλέπουν σκιές"
        "</div>",
        unsafe_allow_html=True
    )

# Οι υπόλοιπες καρτέλες συμπληρώνονται αναλόγως

