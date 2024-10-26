import streamlit as st
import openai

addition_info='''
This visualization, titled "Reach Inhibitors," provides an analysis of the factors that make it difficult to reach specific affinity groups. It categorizes reach inhibitors by the intensity of their impact (large inhibitor in orange, minor inhibitor in gray) across various affinity groups. Here’s a breakdown of its elements:
Affinity Groups (Columns): The chart lists affinity groups across the top, including:
Asian Pacific Rim Peoples
Central Asian Peoples
South Asian Peoples
American Peoples
European Peoples
Northern African and Middle Eastern Peoples
Sub-Saharan African Peoples
Deaf Peoples
These groups represent different cultural or geographic regions, each facing unique challenges in reachability.
Reach Difficulty Factors (Rows): Down the left side, different factors are listed that affect reach difficulty, such as:
Dispersed: Likely indicates how spread out the population is, making engagement more logistically challenging.
Evangelical Engagement: Shows the level of current evangelical activity or its ease of establishment.
Freedom Index: Measures freedoms such as speech or religion, which can impact outreach efforts.
Government Restrictions Index: Indicates restrictions on religious or cultural activities.
Social Hostilities Index: Measures societal pressures or hostilities, which can deter engagement.
Color Coding: Each cell is color-coded based on the severity of each inhibitor:
Large Inhibitor (orange): Represents a major challenge for that affinity group.
Minor Inhibitor (gray): Represents a less significant challenge.
Reach Difficulty Score (Bottom Row): This row provides an overall difficulty score for each group based on the cumulative impact of the listed factors. For instance:
Sub-Saharan African Peoples (Score: 56) and Northern African and Middle Eastern Peoples (Score: 55) have the highest scores, indicating they face the greatest overall challenges across multiple factors.
Asian Pacific Rim Peoples and European Peoples have lower scores (34 and 35, respectively), suggesting fewer or less severe inhibitors.
Filter by Continent: The top section allows filtering by continent, potentially for a focused analysis on geographic areas of interest.
Observations
Social and Political Restrictions: Northern African and Middle Eastern Peoples, and Sub-Saharan African Peoples face large inhibitors in the form of government restrictions and social hostilities, making outreach particularly difficult.
Nomadic and Dispersed Populations: Certain affinity groups, like Central Asian and Sub-Saharan African Peoples, face additional challenges due to their nomadic or dispersed nature, complicating consistent engagement.
Overall Difficulty Distribution: While all groups have some level of reach difficulty, groups like Sub-Saharan African Peoples face a wider range of severe inhibitors across multiple categories.
This visualization effectively highlights the complexity of reaching different affinity groups, providing insights into which factors need to be prioritized and addressed in order to enhance reach efforts.

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
                "<h1>REACH <span style='color: #E8542A;'>INHIBITOR</span></h1>",
                unsafe_allow_html=True
            )
        
        tableau_embed_code = """
        <div class='tableauPlaceholder' id='viz1729967709950' style='position: relative; width: 40%; height: 700px;'>
    <noscript>
        <a href='#'>
            <img alt='REACH INHIBITORS' src='https://public.tableau.com/static/images/Un/UnreachedAnalysis1/REACHINHIBITORS/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='UnreachedAnalysis1/REACHINHIBITORS' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Un/UnreachedAnalysis1/REACHINHIBITORS/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1729967709950');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {
        vizElement.style.width = '1300px';
        vizElement.style.height = '827px';
    } else if (divElement.offsetWidth > 500) {
        vizElement.style.width = '1300px';
        vizElement.style.height = '827px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = '777px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

    """

    # Render the Tableau embed code in Streamlit
        st.components.v1.html(tableau_embed_code, height=900, scrolling=True)
        st.write("South Asian Peoples, North African and Middle Eastern Peoples, and Sub-Saharan African People are the three IBM Affinity Groups that are the most difficult to reach based on a set of Reach Difficulty factors. See the REACH DIFFICULTY SCALE page for more details on the different fields.")
        st.write("Additionally, we conducted a statistical analysis on the different factors to see which ones are significant predictors of IMB’s Strategic Priority Index (SPI), which determines if a people group is Unengaged and Unreached, Engaged yet Unreached, or No Longer Unreached.")
        st.write("Using a Random Tree Classifification, we found that location is extremely significant when it comes to a people group’s engagement status.")
        st.image("images/locationreach.png", width=800) 

        st.write("Next, we aimed to determine what demographic factors of a people group contribute towards success of expanding the Gospel movement in their area.")
        st.write("Using a Random Forest Classification we found that access to resources such as Written Scripture, Gospel Recording, and Audio Scripture plays a large role in engagement. Additionally, hostility factors such as the level of difficulty it takes to live in the area (Physical Exertion), the freedom to share the Gospel in the area (Freedom Index), government restrictions on practicing religions (Government Restrictions Index), social threats on religion (Social Hostilities Index), and US Department of State travel warning status (Threat Level) are significant predictors.")
        st.image("images/factorreach.png", width=800) 
        st.write("An important takeaway from this analysis is that recorded and audio versions of Scripture were more significant in determining reach and engagement than written Scripture. This could be due to the fact that less than 5% of languages have a writing system (World’s Writing System). Additionally, access to recorded and audio scripture typically imply that there is already access to written Scripture, leading to more options overall for Gospel engagement.")
    
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
    