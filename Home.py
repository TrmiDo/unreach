import streamlit as st
import openai

addition_info='''
Use this if the user ask about the page
The image provides a visual analysis of the concept of "Unreached" populations around the world. Here’s a breakdown:

### 1. **Global Map (Left Side)**
   - **Map Visualization**: The world map is highlighted with several orange dots representing the "unreached" population in different regions. Areas with more intense clusters indicate a higher concentration of unreached people groups.
   - **Unreached Indicator**: The total number is shown as `4.8B Unreached`, signifying that 4.8 billion people fall into this category globally.

### 2. **Reach by Continent (Right Side)**
   - **Continents and Reach Percentage**:
     - **Asia**: Shows the highest percentage of unreached people, with **36%** of the total "high need" population. The remaining reach needed is **3.052M**.
     - **Africa**: Represents **33%** of the "high need" category, with **966M** remaining.
     - **Europe**: Stands at **10%** of the "high need" category, with a need to reach **667M** more people.
     - **Americas**: Indicates a high reach success with **93%** reached and only **72M** remaining to be reached.
     - **Oceania**: Also shows a high success rate with **86%** reached, leaving **6M** still unreached.

### 3. **Color Coding & Categories**
   - **Orange (High Need)**: Represents regions or groups with the highest need for outreach or connection. This color predominantly highlights the challenge in Asia and Africa.
   - **Gray (Low Need)**: Represents areas where significant progress has been made in reaching the targeted populations, with the Americas and Oceania being highlighted in this category.

### **General Insights**:
   - The visualization emphasizes that Asia and Africa are the regions with the highest unmet need.
   - Europe has a notable "high need" population, but the numbers are smaller compared to Asia and Africa.
   - The Americas and Oceania are leading in terms of successful reach efforts.

this is for the second picture:
The image showcases a bar chart that analyzes **Affinity Groups’ Access to Scripture** by different scripture resources. Here's a breakdown of the content:

### 1. **Categories of Affinity Groups** (Columns)
   - The data is segmented by several affinity groups, including:
     - **Asian Pacific Rim Peoples**
     - **Central Asian Peoples**
     - **South Asian Peoples**
     - **American Peoples**
     - **European Peoples**
     - **Northern African and Middle Eastern Peoples**
     - **Sub-Saharan African Peoples**
     - **Deaf Peoples**
   
### 2. **Scripture Resources** (Rows)
   - Access to scripture is measured across several resources:
     - **Written Scripture**
     - **Audio Scripture**
     - **Gospel Recording**
     - **Gospel Films**
     - **Jesus Film**
     - **Radio Broadcast**
     - **the HOPE**
     - **Grand Total** (Summary of access for all resources)

### 3. **Color Coding**
   - **Orange** indicates **No Access** to the particular type of scripture resource for the affinity group.
   - **Gray** indicates **Access** to the scripture resource.

### 4. **Insights by Resource**:
   - For many affinity groups, there are significant gaps in access, particularly for **Central Asian Peoples**, **Northern African and Middle Eastern Peoples**, and **Deaf Peoples**, where many bars are completely orange.
   - **Asian Pacific Rim Peoples** and **South Asian Peoples** have some access, indicated by gray segments, but the distribution shows they still have unmet needs in certain scripture resources.
   - Groups like **American Peoples** and **European Peoples** generally have better access across all categories, with more gray bars (indicating access).
   - **Sub-Saharan African Peoples** have partial access, with notable gaps in resources like **Written Scripture**, **Jesus Film**, and **Radio Broadcast**.

### **General Observations**:
   - Access to different forms of scripture is not evenly distributed across affinity groups.
   - There is a notable emphasis on the need to expand resources like **Audio Scripture** and **Gospel Films** for the more underserved groups.
   - Some groups, particularly **Deaf Peoples**, are highlighted as severely lacking access to all forms of scripture resources.


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
                "<h1>WHO ARE THE <span style='color: #E8542A;'>UNREACHED</span>?</h1>",
                unsafe_allow_html=True
            )
        st.write("The Unreached are members of people groups with less than 2% evangelical populations.")
        st.write("The largest groups of unreached peoples are found in Asia and Africa. Explore the interactive maps below to learn more about the individuals who need to be engaged with Scripture.")

    # Your Tableau embed code
        tableau_embed_code = """
        <div class='tableauPlaceholder' id='viz1729958193642' style='position: relative; width: 100%; height: 100%;'>
            <noscript>
                <a href='#'>
                    <img alt='WHO ARE THE UNREACHED?' src='https://public.tableau.com/static/images/Un/UnreachedAnalysisWhoAreTheUnreached/WHOARETHEUNREACHED2/1_rss.png' style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz' style='width: 100%; height: 85vh;'>  <!-- 85vh for 85% of the viewport height -->
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='path' value='views/UnreachedAnalysisWhoAreTheUnreached/WHOARETHEUNREACHED2?:language=en-US&:embed=true&publish=yes&:sid=&:redirect=auth' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/Un/UnreachedAnalysisWhoAreTheUnreached/WHOARETHEUNREACHED2/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
                <param name='filter' value='publish=yes' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1729958193642');
            var vizElement = divElement.getElementsByTagName('object')[0];
            vizElement.style.width = '100%';  // Full container width
            vizElement.style.height = '85vh';  // 85% of the viewport height
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """

    # Render the Tableau embed code in Streamlit
        st.components.v1.html(tableau_embed_code, height=600, scrolling=False)
    # next part
        st.write("The International Mission Board (IMB), a missions group focused on making disciples through church planting and missionary work, provides open-access data regarding a variety of evangelism, hostility, and reach factors for different people groups.")
        st.write("IMB Affinity Groups are categorizations for people groups who share similar cultural, linguistic, and ethnic qualities. These broad groupings allow for us to see where the greatest gaps are in reach efforts across a variety of Scripture Resources.")

        tableau_embed_code2 ='''
        <div class='tableauPlaceholder' id='viz1729958704081' style='position: relative'><noscript><a href='#'><img alt='WHO ARE THE UNREACHED? (3) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Un&#47;UnreachedAnalysisAffinityGroupsAccess&#47;WHOARETHEUNREACHED3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='UnreachedAnalysisAffinityGroupsAccess&#47;WHOARETHEUNREACHED3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Un&#47;UnreachedAnalysisAffinityGroupsAccess&#47;WHOARETHEUNREACHED3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1729958704081');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1300px';vizElement.style.height='349px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1300px';vizElement.style.height='349px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        '''
        st.components.v1.html(tableau_embed_code2, height=500, scrolling=False)
        
        
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
    