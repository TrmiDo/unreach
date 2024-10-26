import streamlit as st

addition_info ='''
now use this:
This visualization titled "Reach Difficulty Scale" appears to represent a dataset analyzing languages or people groups in terms of the difficulty of reaching them. The chart measures "Reach Difficulty Score" and "Population" for various languages, with options to filter by continent and affinity group. Here’s a breakdown of the elements:
Reach Difficulty Score (X-axis, left): This scale ranges from 0 to 100, with a higher score indicating a greater difficulty in reaching the respective language or group. The chart includes several languages, with scores predominantly in the 79-87 range, suggesting these groups are challenging to reach.
Population (X-axis, right): The second measure indicates the population size for each language group, ranging up to 1 billion. This information provides context for the impact of reaching each group. Larger bars here represent larger populations for each group, though most groups here have moderate populations.
Color Coding (High Risk vs. Low Risk):
High Risk (orange): This designation highlights certain groups or regions as more at risk, possibly due to sociopolitical factors, geographic isolation, or cultural sensitivities.
Low Risk (gray): These groups are comparatively less risky to engage, though they may still have high reach difficulty scores.
Filter by Continent and Affinity Group: The left side of the visualization offers filters by continents (Africa, North America, Asia, and Oceania) and affinity groups (likely groups with shared cultural or linguistic characteristics). These filters allow for a refined view based on specific geographic or cultural criteria.
Observations on Specific Languages: Languages like Danau and Tunni have the highest reach difficulty scores (87 and 86, respectively). This suggests that efforts to reach these groups would require significant resources, possibly due to language barriers, remoteness, or other socio-cultural factors.
Overall, this visualization is a strategic tool for prioritizing outreach based on difficulty and risk, helping decision-makers identify where resources are most needed and assess potential risks for each group.


'''

st.set_page_config(page_title="Languages and Countries Analysis", layout="wide")

logo_path = "images/unreachedLogo.png"  # Replace with your logo path
st.image(logo_path, width=200)  # You can adjust the width as needed

# Create a two-column layout
col1, col2 = st.columns([3, 1])  # Adjust column sizes as needed (e.g., 3:1 ratio)

# Main content in the left column
with col1:
    with st.container():
        st.markdown(
                "<h1>REACH <span style='color: #E8542A;'>DIFFICULTY</span> SCALE</h1>",
                unsafe_allow_html=True
            )
        st.write("We utilized 12 fields provided by IMB to create a scale that ranks the difficulty to reach individuals on a scale of 0-10.")
        
        tableau_embed_code = """
        <div class='tableauPlaceholder' id='viz1729959617412' style='position: relative; max-width: 100%;'>
        <noscript>
            <a href='#'>
                <img alt='REACH DIFFICULTY SCALE' 
                     src='https://public.tableau.com/static/images/Un/UnreachedAnalysisReachDifficultyScale/REACHDIFFICULTYSCALE/1_rss.png' 
                     style='border: none; max-width: 100%;' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none; max-width: 100%;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='UnreachedAnalysisReachDifficultyScale/REACHDIFFICULTYSCALE' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Un/UnreachedAnalysisReachDifficultyScale/REACHDIFFICULTYSCALE/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1729959617412');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if (divElement.offsetWidth > 800) {
            vizElement.style.width = '100%';
            vizElement.style.height = '800px';
        } else if (divElement.offsetWidth > 500) {
            vizElement.style.width = '100%';
            vizElement.style.height = '700px';
        } else {
            vizElement.style.width = '100%';
            vizElement.style.height = '1000px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """

    # Render the Tableau embed code in Streamlit
        st.components.v1.html(tableau_embed_code, height=800, scrolling=False)
    

    
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
    
