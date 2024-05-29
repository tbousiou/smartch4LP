import streamlit as st
import pandas as pd
from solver import solve_lp

st.title('SmartCH4 Γραμμικός Προγραμματισμός')
"""
Εφαρμογή για τη βελτιστοποίηση κόστους παραγωγής μεθανίου με τη χρήση γραμμικού προγραμματισμού.
"""




st.header('Περιγραφή προβλήματος', divider='rainbow')

st.markdown("""
O γραμμικός προγραμματισμός είναι μια τεχνική για τον υπολογισμό της βέλτισης λύσης σε ένα πρόβλημα που μοντελοποιείται ως ένα σύνολο γραμμικών σχέσεων. 

Διαθέτουμε ένα σύνολο υποστρωμάτων **S<sub>i</sub>** (S1, S2, S3, ..) για την παραγωγή μεθανίου με τα παρακάτω χαρακτηριστικά:
- **B**: Δυναμικό παραγωγής μεθανίου (L<sub>CH4</sub>/KgVS)
- **W**: Διαθέσιμο βάρος (Kg)
- **C**: Κόστος ανά Kg (Euro/Kg)
- **D**: Απόσταση από τη μονάδα (Km). Η απόσταση επηρεάζει το κόστος μεταφοράς και 

Το ζητούμενο είναι να βρεθεί η βέλτιστη σύνθεση σε βάρος των υποστρωμάτων **X<sub>i</sub>** (X1, X2, X3, ...) που θα ελαχιστοποιεί το συνολικό κόστος υποστρωμάτων **Κ** και θα πετυχαίνει τον στόχο παραγωγής μεθανίου **T** με απόκλιση +/- **e** %.

**Συνάρτηση κόστους K (objective function):**

Ελαχιστοποίησε το κόστος Κ. Το συνολικό κόστος ισούται με το κόστος αγοράς Kb συν το κόστος μεταφοράς Kt:

Kb = Σ(Ci * Xi)

Kt = Σ(Di * Xi) ???

=> Κ = Σ(Ci * Xi + Di * Xi)

**Υπό τους περιορισμούς (constraints):**

Το δυναμικό παραγωγής μεθανού πρέπει να είναι στο εύρος του στόχου:
            
- T*(1-e) <= Σ(Bi * Xi) <= T*(1+e)

Το συνολικό βάρος των υποστρωμάτων πρέπει να είναι μικρότερο ή ίσο του διαθέσιμου:

- 0 <= Xi <= Wi (Το διαθέσιμο βάρος κάθε υποστρώματος)

""", unsafe_allow_html=True,)



substrate_names = ['S1', 'S2', 'S3']


df = pd.DataFrame({
    'B': [10.2, 9.8, 7.6],
    'W': [300, 450, 220],
    'C': [3, 4, 2],
    'D': [30, 40, 20],
}, index=substrate_names)

st.header('Υπολογισμός βέλτισης λύσης', divider='rainbow')
st.subheader('Δεδομένα υποσρτωμάτων')

df

col1, col2 = st.columns(2)
with col1:
    st.number_input('Στόχος παραγωγής μεθανίου (T)',
                value=100, min_value=50, max_value=200)
with col2:
    st.number_input('Απόκλιση στόχου (%)', value=0.1,
                min_value=0.01, max_value=0.3)


# Add a button to solve the linear programming problem
if st.button('Solve LP'):
    solution = solve_lp()
    if solution:
        st.write('Βρέθηκε βέλτιση λύση:')
        st.table(solution)
    else:
        st.write('Δε βρέθηκε βέλτιση λύση. Ελέγξτε τους περιορισμούς.')
