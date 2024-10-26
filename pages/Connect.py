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
                "<h1><span style='color: #E8542A;'>CONNECT</span></h1>",
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <p>
                <a href="https://omegle.cc/" style="text-decoration: underline; color: #E8542A;">
                    SEE WHO IS ONLINE
                </a>
                <span style='color: #E8542A;'>:</span> 
                Speak to someone random or join a chatroom.
            </p>
            """,
            unsafe_allow_html=True
            )

        st.markdown(
            """
            <p>
                <a href="https://omegle.cc/" style="text-decoration: underline; color: #E8542A;">
                    CONNECT AND ENGAGED
                </a>
                <span style='color: #E8542A;'>:</span> 
                Connect with a believer who’s part of the unreached people group you want to serve.
            </p>
            """,
            unsafe_allow_html=True
            )
        
        st.markdown(
            """
            <p>
                <a href="https://omegle.cc/" style="text-decoration: underline; color: #E8542A;">
                    CONNECT TO ORGANIZATION
                </a>
                <span style='color: #E8542A;'>:</span> 
                 Find other organizations who are trying to reach the same people groups.
            </p>
            """,
            unsafe_allow_html=True
            )
       
        st.markdown(
            """
            <p>
                <a href="https://omegle.cc/" style="text-decoration: underline; color: #E8542A;">
                    HELP SOMONE BY SUBMITTING DATA
                </a>
                <span style='color: #E8542A;'>:</span> 
                 Help others gain social, political, and economic context by completing a form to share your knowledge about a people group to which you belong or with which you have extensive experience.
            </p>
            """,
            unsafe_allow_html=True
            )
        st.markdown(
            """
            <p>
                <a href="https://omegle.cc/" style="text-decoration: underline; color: #E8542A;">
                    CONTEXT LIBRARY
                </a>
                <span style='color: #E8542A;'>:</span> 
                 Explore our vetted, user-submitted data to gain more context about the people group you want to serve.
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
    
