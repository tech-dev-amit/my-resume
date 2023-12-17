import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from annotated_text import annotated_text
from streamlit_extras.colored_header import colored_header

# Define your personal information
name = "Amit :green[Lulla]"
email = "amitlulla9324@gmail.com"
linkedin = "https://www.linkedin.com/in/amit-lulla-techgenius"
github = "https://github.com/amitlulla5920"
about_me = f"""
Hello, I'm Amit Lulla, a Software Developer and AI Tools Developer with over 1 year of experience in the field. I am based in Nashik Road, Maharashtra, India. I'm passionate about technology and specialize in a variety of technical areas, making me a versatile and valuable asset to any team.

**Technical Skills:**
- :blue[Webscraping Expert:] I have a strong proficiency in web scraping techniques, using tools like Puppeteer, Playwright, and Langchain.
- :green[Data Processing Specialist:] I excel in data processing and analysis using Python libraries such as Pandas and NumPy.
- :red[AI Architect:] I have experience in designing and implementing AI systems, including natural language processing (NLP) with NLTK and PyTorch.
- :violet[Streamlit Developer:] I can create interactive web applications using Streamlit.
- :rainbow[Programming Languages:] I'm proficient in Python, JavaScript, and have a basic understanding of Java, C, and C++.
- :orange[Libraries:] My expertise includes Spacy for Python and various JavaScript libraries.
- :gray[JavaScript Frameworks:] I have experience with Vue.js and React.
- :blue[Front-end Technologies:] I'm skilled in HTML5 and CSS3.
- :green[Backend Technologies:] I have worked with Node.js and Express.js.
- :red[Database Management:] I'm proficient in MySQL.
- :violet[Version Control:] I'm experienced in using Git, Github, and Bitbucket.

**Projects:**
1. **Automate Browsing — AI Assistant for Browser [POC]** (Team Size: 2)
   - My Role: R&D, system design, AI configuration, and development.
   - Description: Developed an AI assistant capable of automating browser tasks based on user instructions.

2. **Automate Data Collection — AI Assistant for Data Collection [POC]** (Team Size: 2)
   - My Role: R&D, system design, AI configuration, and development.
   - Description: Created an AI assistant for data collection from various websites in a specific domain, including a chatbot for domain-related queries.

3. **Salesforce B2C — Salesforce Commerce Cloud** (Team Size: 5)
   - My Role: Team Lead, requirement analysis, time estimations, work allocation, and project management.
   - Description: Led a team in developing custom web pages, integrating payment gateways, and bulk product imports.

4. **Salesforce Integration — Integration** (Team Size: 1)
   - Description: Successfully integrated Salesforce Org with multiple external platforms, including Quickbooks and backup systems.

**Additional Skills:**
- **Creative PPT Making:** Proficient in creating visually engaging presentations using Microsoft PowerPoint and Google Slides.
- **Well Documentation:** Diligent in documenting project specifications, technical guides, and API references.
- **Research & Development:** Enthusiastic about exploring emerging technologies, participating in hackathons, and contributing to open-source projects.
- **Excellent Communication Skills:** Strong verbal and written communication abilities.
- **Problem-Solving:** Skilled in identifying challenges, developing creative solutions, and implementing effective problem-solving strategies.

**Professional Summary:**
I am a skilled Software Developer and AI Tools Developer with over 1 year of experience working at Dreamwares IT Solutions and Integrately Company. I have a strong background in Salesforce development and front-end development, with a focus on AI tools development and research. I am a quick learner and have a deep understanding of cutting-edge AI tools, technologies, and frameworks. I am dedicated to driving innovation and providing impactful business solutions through AI.

**Education:**
- Certified Salesforce Platform Developer [Lvl -1]
- Bachelor's in Computer Application, Pratap College Amalner - 2021

**Personal Attributes:**
- Quick Learner: I embrace challenges with a growth mindset and rapidly adapt to new technologies.
- High Focus: I maintain a detail-oriented approach even in demanding and fast-paced environments.
- Dedicated: I am committed to the success of projects and go the extra mile to deliver top-notch solutions.

I am excited to bring my expertise and passion for technology to contribute to your projects and help drive innovation. Let's connect and explore how we can work together to achieve remarkable results.
You can reach me at {email}, and you can find me on:

- LinkedIn: [Amit Lulla]({linkedin})
- GitHub: [amitlulla5920]({github})
"""
profile_img = "images\profile.png"

# Define your projects, skills, and social links 
projects = [
    # Define your projects here
]

skills = [
    # Define your skills here
]

social_links = {
    "LinkedIn": linkedin,
    "GitHub": github,
    # Add more social links if needed
}

# Set the Streamlit page layout to wide
st.set_page_config(layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


# # Create a sidebar for navigation

with st.sidebar:
    tabs = on_hover_tabs(tabName=["Home", "Projects", "Skills", "Social Links"], 
                         iconName=["home", "work", "star", "people"], 
                         styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'cyan',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'},},
                             key="1", default_choice=0)

# Main content based on the selected tab

if tabs == "Home":
    # st.title(f"{name}")
    # st.markdown(f"📧 Email: {email}")
    # st.markdown(f"🔗 LinkedIn: [{name}]({linkedin})") 👨‍💻
    # st.markdown(f"🐙 GitHub: [{name}]({github})")
    container = st.container()
    # Create a two-column layout
    col1, col2, col3 = container.columns(3)
    
    with col1:
        st.image(f"{profile_img}", use_column_width="never", caption="Amit Lulla")

    # Column 2: Display the text
    with col2:
        # new_title = f'''<p style="font-family:sans-serif; color:Cyan; font-size: 150px;">AMIT LULLA</p>'''
        # st.markdown(new_title, unsafe_allow_html=True)
        st.title(':blue[Amit Lulla] :sunglasses:')
        st.markdown(
        "👋 Howdy, Code Conjurer! 🚀✨\n\n"
        "I'm Amit Lulla, the tech wizard who turns \"404 Not Found\" into \"200 OK\" with a sprinkle of Python and a dash of JavaScript. 🐍🤖\n\n"
        "🧙‍♂️ When I'm not wrestling with code, I'm the maestro of Generative AI, the guru of Prompt Engineering, and the sheriff of staying up-to-date with more AI models than I have coffee cups. ☕🤯\n\n"
        "💻 Armed with my trusty keyboard and an endless supply of cat gifs, I navigate the GitHub jungle, swinging between repositories like Tarzan in the digital vines. 🌐🐒\n\n"
        "📚 Docs are my love language. I speak fluent README and can decipher research papers faster than you can say \"bug-free.\" 📖💬\n\n")
        st.markdown('<a href="https://github.com/tech-dev-amit"><img src="https://www.svgrepo.com/show/331724/github-code-source.svg" alt="GitHub" height="50"></a>'
        '&nbsp;&nbsp;&nbsp;'
        '<a href="mailto:tech.dev.amit@gmail.com"><img src="https://i.pinimg.com/originals/8f/c3/7b/8fc37b74b608a622588fbaa361485f32.png" alt="EMail" height="50"></a>'
        '&nbsp;&nbsp;&nbsp;'
        '<a href="https://www.linkedin.com/in/amit-lulla-techgenius/"><img src="https://icons.iconarchive.com/icons/martz90/circle/512/linkedin-icon.png" alt="LinkedIn" height="50"></a>', 
        unsafe_allow_html=True
        )
        with open("Amit Lulla - Resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="⬇️ Download Resume",
                    data=PDFbyte,
                    file_name="Amit Lulla - Resume.pdf",
                    mime='application/octet-stream')

    # container = st.container()
    with col3:
        st.image("https://i.gifer.com/embedded/download/QWsX.gif", use_column_width="never", caption="AI")


    
    colored_header(
    label="**Professional Summary:**",
    description="Here is my Professional Summary",
    color_name="blue-green-70",
    )
    annotated_text(
        "I am a skilled ", ("Software Developer and AI Tools Developer", "", "#ff6b6b"), "with over 1 year of experience working at Dreamwares IT Solutions and Integrately Company. I have a strong background in Salesforce development and front-end development, with a focus on AI tools development and research. I am a quick learner and have a deep understanding of cutting-edge AI tools, technologies, and frameworks. I am dedicated to driving innovation and providing impactful business solutions through AI."
    )

    colored_header(
    label="Technical Skills:",
    description="Here are List of My Technical Skills",
    color_name="light-blue-70",
    )
    """
    - :blue[Webscraping Expert:] I have a strong proficiency in web scraping techniques, using tools like Puppeteer, Playwright, and Langchain.
    - :green[Data Processing Specialist:] I excel in data processing and analysis using Python libraries such as Pandas and NumPy.
    - :red[AI Architect:] I have experience in designing and implementing AI systems, including natural language processing (NLP) with NLTK and PyTorch.
    - :violet[Streamlit Developer:] I can create interactive web applications using Streamlit.
    - :rainbow[Programming Languages:] I'm proficient in Python, JavaScript, and have a basic understanding of Java, C, and C++.
    - :orange[Libraries:] My expertise includes Spacy for Python and various JavaScript libraries.
    - :gray[JavaScript Frameworks:] I have experience with Vue.js and React.
    - :blue[Front-end Technologies:] I'm skilled in HTML5 and CSS3.
    - :green[Backend Technologies:] I have worked with Node.js and Express.js.
    - :red[Database Management:] I'm proficient in MySQL.
    - :violet[Version Control:] I'm experienced in using Git, Github, and Bitbucket."""
    # container.write("")
    # # Column 1: Display the image
    
    
    colored_header(
    label="**Education:**",
    description="Here is Education Background:",
    color_name="red-70",
    )
    annotated_text(
        ("Certified Salesforce Platform Developer [Lvl -1]", "", "#ff4b4b"),
        "\n\n",
        ("Bachelor's in Computer Application, Pratap College Amalner - 2021", "", "#4b72ff")
    )


    

    colored_header(
    label="**Personal Attributes:**",
    description="Here are my Personal Attributes",
    color_name="green-70",
    )
    annotated_text(
        ("Quick Learner", "", "#50c878"),  
        "- I embrace challenges with a growth mindset and rapidly adapt to new technologies.\n\n",
        ("High Focus", "", "#ff6b6b"),  
        "- I maintain a detail-oriented approach even in demanding and fast-paced environments.\n\n",
        ("Dedicated", "", "#ffcc00"),
        "- I am committed to the success of projects and go the extra mile to deliver top-notch solutions.\n\n"
    )
    
elif tabs == "Projects":
    st.title("👨‍💻My :blue[Projects]")

    colored_header(
    label="**Projects:**",
    description="Here are List of My Projects",
    color_name="violet-70",
    )
    annotated_text(
    ("1. **Automate Browsing - AI Assistant for Browser**", "(Team Size: 2)", "#50c8bd"),  # Green color for dark theme
    "\n- My Role: R&D, system design, AI configuration, and development."
    "\n- Description: Developed an AI assistant capable of automating browser tasks based on user instructions.\n\n",
    ("2. **Automate Data Collection — AI Assistant for Data Collection**", "(Team Size: 2)", "#ff6b6b"),  # Red color for dark theme
    "\n- My Role: R&D, system design, AI configuration, and development."
    "\n- Description: Created an AI assistant for data collection from various websites in a specific domain, including a chatbot for domain-related queries.\n\n",
    ("3. **Salesforce B2C — Salesforce Commerce Cloud**", "(Team Size: 5)", "#ffcc00c7"),  # Yellow color for dark theme
    "\n- My Role: Team Lead, requirement analysis, time estimations, work allocation, and project management."
    "\n- Description: Led a team in developing custom web pages, integrating payment gateways, and bulk product imports.\n\n",
    ("4. **Salesforce Integration — Integration**", "(Team Size: 1)", "#ff9900"),  # Orange color for dark theme
    "\n- Description: Successfully integrated Salesforce Org with multiple external platforms, including Quickbooks and backup systems.\n"
)

    # for project in projects:
    #     st.subheader(project["title"])
    #     st.image(project["image"], caption=project["description"], use_column_width=True)

elif tabs == "Skills":
    st.title("📚:orange[Skills]")
    # st.write(", ".join(skills))
    colored_header(
    label="Technical Skills:",
    description="Here are List of My Technical Skills",
    color_name="light-blue-70",
    )
    """
    - :blue[Webscraping Expert:] I have a strong proficiency in web scraping techniques, using tools like Puppeteer, Playwright, and Langchain.
    - :green[Data Processing Specialist:] I excel in data processing and analysis using Python libraries such as Pandas and NumPy.
    - :red[AI Architect:] I have experience in designing and implementing AI systems, including natural language processing (NLP) with NLTK and PyTorch.
    - :violet[Streamlit Developer:] I can create interactive web applications using Streamlit.
    - :rainbow[Programming Languages:] I'm proficient in Python, JavaScript, and have a basic understanding of Java, C, and C++.
    - :orange[Libraries:] My expertise includes Spacy for Python and various JavaScript libraries.
    - :gray[JavaScript Frameworks:] I have experience with Vue.js and React.
    - :blue[Front-end Technologies:] I'm skilled in HTML5 and CSS3.
    - :green[Backend Technologies:] I have worked with Node.js and Express.js.
    - :red[Database Management:] I'm proficient in MySQL.
    - :violet[Version Control:] I'm experienced in using Git, Github, and Bitbucket."""

    colored_header(
    label="**Additional Skills:**",
    description="Here are few Additional Skills",
    color_name="orange-70",
    )
    """
- :orange[**Creative PPT Making:**] Proficient in creating visually engaging presentations using Microsoft PowerPoint and Google Slides.
- :red[**Well Documentation:**] Diligent in documenting project specifications, technical guides, and API references.
- :blue[**Research & Development:**] Enthusiastic about exploring emerging technologies, participating in hackathons, and contributing to open-source projects.
- :violet[**Excellent Communication Skills:**] Strong verbal and written communication abilities.
- :rainbow[**Problem-Solving:**] Skilled in identifying challenges, developing creative solutions, and implementing effective problem-solving strategies.
"""

elif tabs == "Social Links":
    st.title("🔗Social :violet[Links]")
    # Add custom CSS and content
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Apply custom CSS styles
    local_css("socials.css")

    # Display additional content from "cards.txt"
    f = open("socials.txt")
    st.markdown(str(f.read()), unsafe_allow_html=True)
    f.close()


# Footer
st.markdown(
    """
    ---
    Amit Lulla :heart: 
    """,
    unsafe_allow_html=True,
)
