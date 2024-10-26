import streamlit as st


# Add the logo at the top left
logo_path = "images/unreachedLogo.png"  # Replace with your logo path
st.image(logo_path, width=200)  # You can adjust the width as needed

# Create a two-column layout
col1, col2 = st.columns([3, 1])  # Adjust column sizes as needed (e.g., 3:1 ratio)

# Main content in the left column
with col1:

    st.title("Home Page")
    st.write("We could have a verse here like:  \" 19 Therefore go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, 20 and teaching them to obey everything I have commanded you. And surely I am with you always, to the very end of the age.\" ")
    st.write("Matthew 28:19-20")

    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Reach Difficulty Scale", "Reach Inhibitors", "Resources", "Connect"])

    # Content for Home Tab
    with tab1:
        st.header("Home")
        st.write("Welcome to the Home page!")

    # Content for Language Analysis Tab
    with tab2:
        st.header("Reach Difficulty Scale")
        st.write("This section contains language analysis data.")
        # Your Tableau embed code
        tableau_embed_code = """
        <div class='tableauPlaceholder' id='viz1729904265033' style='position: relative'>
        <noscript><a href='#'><img alt='WHO ARE THE UNREACHED?' src='https://public.tableau.com/static/images/Un/UnreachedAnalysis/WHOARETHEUNREACHED/1_rss.png' style='border: none' /></a></noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='UnreachedAnalysis/WHOARETHEUNREACHED' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Un/UnreachedAnalysis/WHOARETHEUNREACHED/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1729904265033');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1300px';vizElement.style.height='827px';}
        else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1300px';vizElement.style.height='827px';}
        else { vizElement.style.width='100%';vizElement.style.height='1177px';}
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
        """
        
        # Render the Tableau embed code in Streamlit
        st.components.v1.html(tableau_embed_code, height=600, scrolling=True)


    # Content for Country Statistics Tab
    with tab3:
        st.header("Reach Inhibitors")
        st.write("Here you will find various country statistics.")

    # Content for Country Statistics Tab
    with tab4:
        st.header("Resources")
        st.write("Here you will find various country statistics.")

    # Content for Country Statistics Tab
    with tab5:
        st.header("Connect")
        st.write('''Meet ___, a ___ from China who witnessed persecution firsthand. After getting thrown 
                into uncertainty when her pastor was jailed for spreading the Gospel, she was motivated 
                to find ways to continue growing God’s kingdom, but she had to find innovative ways to get past the fears persecution brought into the hearts and minds of both existing believers and unbelievers.
                Talk to ____ and others across the globe to hear their stories.''')

# Profile section in the right column
with col2:
        st.markdown(
        """
        <div style="border: 2px solid #E8542A; border-radius: 5px; padding: 5px; background-color: #333333;">
            <h3 style='font-size: 20px; text-align: center;'>Connect with Missionaries</h3>
        </div>
        """,
        unsafe_allow_html=True)

        st.image("images/missionaryImage.png", width=150)  # Optional: Add a profile image
        st.write('''Meet ___, a ___ from China who witnessed persecution firsthand. After getting thrown 
                into uncertainty when her pastor was jailed for spreading the Gospel, she was motivated 
                to find ways to continue growing God’s kingdom, but she had to find innovative ways to get past the fears persecution brought into the hearts and minds of both existing believers and unbelievers.
                Talk to ____ and others across the globe to hear their stories.''')