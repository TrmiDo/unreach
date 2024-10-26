import streamlit as st


st.set_page_config(page_title="Languages and Countries Analysis", layout="wide")

logo_path = "images/unreachedLogo.png"  # Replace with your logo path
st.image(logo_path, width=200)  # You can adjust the width as needed

# Create a two-column layout
col1, col2 = st.columns([3, 1])  # Adjust column sizes as needed (e.g., 3:1 ratio)

# Main content in the left column
with col1:
    with st.container():
        st.markdown(
                "<h1><span style='color: #E8542A;'>RESOURCES</span></h1>",
                unsafe_allow_html=True
        )

        st.markdown(
            """
            <p>
                <a href="https://grd.imb.org/research-data/" style="text-decoration: underline; color: #E8542A;">
                    IMB DATABASE
                </a>
                <span style='color: #E8542A;'>:</span> 
                 We primarily used IMB’s 2024-05 GSEC Listing Of People Groups data set for our visuals and analysis.
            </p>
            """,
            unsafe_allow_html=True
            )

        st.markdown(
            """
            <p>
                <a href="https://grd.imb.org/research-data/" style="text-decoration: underline; color: #E8542A;">
                    JOSHUA PROJECT DATABASE
                </a>
                <span style='color: #E8542A;'>:</span> 
                 Take a look at similar datasets from the Joshua Project, which used IMB data. You’ll also find some audience-submitted data visualizations. Explore Stratus Earth for a deep dive into the different difficulties people across the globe.
            </p>
            """,
            unsafe_allow_html=True
            )
        
        st.image("images/earth.JPG", width=300)  # Optional: Add a profile image

        
        
        st.markdown(
            """
            <p>
                <a href="https://m.joshuaproject.net/resources/datasets" style="text-decoration: underline; color: #E8542A;">
                    THE AUDIENCE MAP
                </a>
                <span style='color: #E8542A;'>:</span> 
                 Learn about who you’re reaching and gain more context into the different struggles they face on a daily basis.
            </p>
            """,
            unsafe_allow_html=True
            )
        
# Profile section in the right column
with col2:
    st.markdown(
        """
        <div style="border: 2px solid #E8542A; border-radius: 5px; padding: 5px; background-color: #333333;">
            <h3 style='font-size: 20px; text-align: center; color: white;'>Connect with Missionaries</h3>
        </div>
        """,
        unsafe_allow_html=True)

    st.image("images/missionaryImage.png", width=150)  # Optional: Add a profile image
    st.write('''Meet Chun, a young woman from China who faced persecution firsthand. When her pastor was jailed for spreading the Gospel, she was thrust into uncertainty. Determined to nurture God’s kingdom, Chun courageously sought innovative ways to overcome the fears that persecution instilled in both believers and seekers alike.

Talk to Chun and others across the globe to hear their stories.''')
   
