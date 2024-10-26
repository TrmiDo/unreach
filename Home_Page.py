import streamlit as st

# Set up page config
st.set_page_config(page_title="Languages and Countries Analysis", layout="wide")

st.write("Use the sidebar to navigate to different pages.")

# Sidebar for user selection (if you have multiple dashboards)
st.sidebar.title("Dashboard Selection")
dashboard = st.sidebar.selectbox(
    "Choose a Tableau Dashboard",
    ("Unreached Analysis", "Dashboard 2", "Dashboard 3")
)

# HTML code for the Tableau embed
unreached_analysis_html = """
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

# Display the selected dashboard
if dashboard == "Unreached Analysis":
    st.write("### WHO ARE THE UNREACHED?")
    st.components.v1.html(unreached_analysis_html, height=827, scrolling=True)
else:
    st.write("### Select a different dashboard for display")
