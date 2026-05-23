import streamlit as st
import joblib
import PyPDF2
import requests
import plotly.express as px
import pandas as pd

from streamlit_lottie import st_lottie

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Career Predictor",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# -----------------------------
# LOTTIE FUNCTION
# -----------------------------
def load_lottieurl(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

# -----------------------------
# LOAD ANIMATION
# -----------------------------
lottie_ai = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json"
)

# -----------------------------
# PDF GENERATOR
# -----------------------------
def generate_pdf(top_career, score, roadmap):

    doc = SimpleDocTemplate("career_report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "<b>AI Career Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    career = Paragraph(
        f"<b>Recommended Career:</b> {top_career}",
        styles['BodyText']
    )

    elements.append(career)

    score_text = Paragraph(
        f"<b>Resume Score:</b> {score}/100",
        styles['BodyText']
    )

    elements.append(score_text)

    elements.append(Spacer(1, 20))

    roadmap_title = Paragraph(
        "<b>Career Roadmap</b>",
        styles['Heading2']
    )

    elements.append(roadmap_title)

    for step in roadmap:

        elements.append(
            Paragraph(f"• {step}", styles['BodyText'])
        )

    doc.build(elements)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #020617, #0F172A);
    color: white;
}

/* Main container */
.block-container {
    padding-top: 2rem;
}

/* Main Title */
.main-title {
    font-size: 60px;
    font-weight: 800;
    color: #38BDF8;
}

/* Subtitle */
.subtitle {
    font-size: 22px;
    color: #CBD5E1;
}

/* Section Headings */
.section-title {
    color: #38BDF8;
    font-size: 32px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
}

/* Text Area */
textarea {
    font-size: 20px !important;
    background-color: #1E293B !important;
    color: white !important;
    border-radius: 15px !important;
}

/* File uploader */
section[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.04);
    padding: 15px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Buttons */
.stButton button {
    width: 100%;
    height: 60px;
    border-radius: 14px;
    background: linear-gradient(90deg, #0EA5E9, #38BDF8);
    color: white;
    font-size: 24px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background: linear-gradient(90deg, #38BDF8, #0EA5E9);
    transform: scale(1.01);
}

/* Result Cards */
.result-card {
    background: linear-gradient(135deg, #111827, #1E293B);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
    border-left: 6px solid #38BDF8;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background-color: #38BDF8;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    margin-top: 60px;
}

/* Mobile Responsive */
@media (max-width: 768px) {

    .main-title {
        font-size: 38px !important;
    }

    .subtitle {
        font-size: 18px !important;
    }

    textarea {
        font-size: 16px !important;
    }

    .stButton button {
        height: 50px !important;
        font-size: 18px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
hero1, hero2 = st.columns([1.2, 1])

with hero1:

    st.markdown("""
    <div class='main-title'>
    🚀 AI Career Path Predictor
    </div>

    <div class='subtitle'>
    Discover your future career using AI-powered resume analysis and smart skill prediction.
    </div>
    """, unsafe_allow_html=True)

with hero2:

    st_lottie(
        lottie_ai,
        height=300,
        key="ai_animation"
    )

# -----------------------------
# SKILL DATABASE
# -----------------------------
skill_database = {
    "Python", "Machine Learning", "Deep Learning",
    "HTML", "CSS", "JavaScript", "React",
    "Node.js", "SQL", "Java", "C++",
    "TensorFlow", "PyTorch", "Data Science",
    "AWS", "Cloud", "Cybersecurity",
    "Linux", "Git", "Figma", "UI/UX",
    "Networking", "Communication",
    "Leadership", "Problem Solving",
    "Docker", "Kubernetes", "Flask",
    "Django", "MongoDB", "Power BI",
    "Medicine", "Surgery", "Healthcare",
    "Hospital", "Patient Care",
    "Acting", "Music", "Dance",
    "Photography", "Animation"
}

# -----------------------------
# DOMAIN KEYWORDS
# -----------------------------
domains = {

    "Tech": [
        "python", "machine learning",
        "ai", "sql", "javascript",
        "react", "html", "css",
        "cloud", "aws", "docker",
        "kubernetes", "coding"
    ],

    "Medical": [
        "hospital", "surgery",
        "medicine", "patient",
        "healthcare", "nursing",
        "diagnosis", "treatment",
        "injections"
    ],

    "Creative": [
        "dance", "acting",
        "music", "singing",
        "photography", "animation",
        "fashion", "drawing",
        "painting", "theatre"
    ],

    "Business": [
        "finance", "marketing",
        "sales", "management",
        "accounting", "leadership"
    ]
}

# -----------------------------
# CAREER DOMAINS
# -----------------------------
career_domains = {

    "data scientist": "Tech",
    "ai engineer": "Tech",
    "frontend developer": "Tech",
    "backend developer": "Tech",
    "full stack developer": "Tech",
    "software engineer": "Tech",
    "cybersecurity analyst": "Tech",
    "cloud engineer": "Tech",
    "mobile app developer": "Tech",
    "robotics engineer": "Tech",
    "iot engineer": "Tech",

    "doctor": "Medical",
    "nurse": "Medical",
    "pharmacist": "Medical",
    "dentist": "Medical",
    "psychologist": "Medical",
    "lab technician": "Medical",
    "surgeon": "Medical",

    "actor": "Creative",
    "artist": "Creative",
    "musician": "Creative",
    "photographer": "Creative",
    "animator": "Creative",
    "fashion designer": "Creative",
    "content creator": "Creative",

    "accountant": "Business",
    "marketing manager": "Business",
    "business analyst": "Business",
    "hr manager": "Business"
}

# -----------------------------
# CAREER ROADMAPS
# -----------------------------
career_roadmaps = {

    "data scientist": [
        "Learn Python",
        "Study Statistics",
        "Master Machine Learning",
        "Learn SQL & Data Analysis",
        "Build ML Projects",
        "Deploy AI Models"
    ],

    "ai engineer": [
        "Learn Python",
        "Study Deep Learning",
        "Master TensorFlow/PyTorch",
        "Build AI Applications",
        "Deploy AI Systems"
    ],

    "frontend developer": [
        "Learn HTML",
        "Learn CSS",
        "Master JavaScript",
        "Study React",
        "Build Frontend Projects"
    ],

    "doctor": [
        "Study Biology",
        "Prepare for Medical Exams",
        "Complete MBBS",
        "Practice Clinical Skills",
        "Gain Hospital Experience"
    ],

    "actor": [
        "Practice Acting",
        "Join Theatre",
        "Learn Expression Skills",
        "Build Portfolio",
        "Attend Auditions"
    ],

    "musician": [
        "Learn Music Theory",
        "Practice Instruments",
        "Improve Vocals",
        "Record Songs",
        "Perform Live"
    ],

    "machine learning engineer": [
        "Learn Python",
        "Study Data Preprocessing",
        "Master Machine Learning Algorithms",
        "Build ML Pipelines",
        "Deploy ML Models"
    ],

    "web developer": [
        "Learn HTML & CSS",
        "Master JavaScript",
        "Learn React",
        "Learn Backend (Node.js, Django)",
        "Build Full Stack Projects",
        "Deploy Websites"
    ],

    "software engineer": [
        "Learn Programming (Python, Java, C++)",
        "Study Data Structures & Algorithms",
        "Master Software Design Principles",
        "Build Software Projects",
        "Contribute to Open Source"
    ],

    "cybersecurity analyst": [
        "Learn Networking",
        "Understand Linux",
        "Study Cybersecurity Concepts",
        "Practice Ethical Hacking",
        "Learn Penetration Testing",
        "Earn Security Certifications"
    ],

    "cloud engineer": [
        "Learn Cloud Basics",
        "Master AWS/Azure/GCP",
        "Study Cloud Architecture",
        "Build Cloud Projects",
        "Earn Cloud Certifications"
    ],

    "ui/ux designer": [
        "Learn Design Principles",
        "Master Figma/Sketch",
        "Create Wirerames",
        "Study User Research",
        "Build Design Portfolio",
        "Work on Real Projects"
    ],

    "mobile app developer": [
        "Learn Java/Kotlin (Android) or Swift (iOS)",
        "Study Mobile App Design",
        "Build Mobile Projects",
        "Work with APIs",
        "Learn Firebase/Backend for Mobile",
        "Publish Apps on Play Store/App Store"
    ],

    "data analyst": [
        "Learn Excel",
        "Master SQL",
        "Learn Data Visualization (Tableau, Power BI)",
        "Study Python for Data Analysis",
        "Analyze Datasets",
        "Create Dashboards"
    ],

    "nurse": [
        "Complete Nursing Diploma/Degree",
        "Gain Clinical Experience",
        "Learn Patient Care",
        "Study Medical Procedures",
        "Work in Hospitals",
        "Earn Nursing License"
    ],

    "dentist": [
        "Complete Dental Degree",
        "Gain Clinical Experience",
        "Learn Dental Procedures",
        "Study Oral Health",
        "Work in Dental Clinics",
        "Earn Dental License"
    ],

    "pharmacist": [
        "Complete Pharmacy Degree",
        "Gain Experience in Pharmacies",
        "Learn Drug Interactions",
        "Study Pharmacology",
        "Work in Healthcare Settings",
        "Earn Pharmacy License"
    ],

    "surgeon": [
        "Complete Medical Degree",
        "Gain Surgical Experience",
        "Learn Surgical Techniques",
        "Study Anatomy",
        "Work in Hospitals",
        "Earn Surgical License"
    ],

    "pilot": [
        "Study Physics & Mathematics",
        "Join Flying School",
        "Complete Flight Training",
        "Earn Pilot License",
        "Gain Flight Experience",
    ],

    "cabin crew": [
        "Learn Communication Skills",
        "Study Aviation Safety",
        "Complete Cabin Crew Training",
        "Gain Customer Service Experience",
        "Apply to Airlines"
    ],

    "graphic designer": [
        "Learn Design Software (Adobe Photoshop, Illustrator)",
        "Study Design Principles",
        "Build Design Portfolio",
        "Work on Real Projects",
        "Specialize in a Design Niche"
    ],

    "content creator": [
        "Choose Your Niche",
        "Learn Video Editing",
        "Study Social Media Trends",
        "Create Consistent Content",
        "Engage with Audience",
        "Monetize Your Channel"
    ],

    "video editor": [
        "Learn Video Editing Software (Adobe Premiere, Final Cut Pro)",
        "Study Editing Techniques",
        "Build Editing Portfolio",
        "Work on Real Projects",
        "Specialize in a Video Niche"
    ],

    "accountant": [
        "Complete Accounting Degree",
        "Gain Experience in Accounting Firms",
        "Learn Financial Reporting",
        "Study Taxation",
        "Work in Corporate Finance",
        "Earn CPA License"
    ],

    "marketing manager": [
        "Study Marketing Principles",
        "Gain Experience in Marketing Roles",
        "Learn Digital Marketing",
        "Study Consumer Behavior",
        "Work on Marketing Campaigns",
        "Lead Marketing Teams"
    ],

    "hr manager": [
        "Study Human Resources Management",
        "Gain Experience in HR Roles",
        "Learn Recruitment & Talent Acquisition",
        "Study Employee Relations",
        "Work on HR Projects",
        "Lead HR Teams"
    ]
}

# -----------------------------
# SKILL GAP ANALYZER
# -----------------------------
career_required_skills = {

    # -----------------------------
    # TECH CAREERS
    # -----------------------------

    "data scientist": [
        "python",
        "machine learning",
        "deep learning",
        "sql",
        "statistics",
        "pandas",
        "numpy",
        "data visualization",
        "feature engineering"
    ],

    "ai engineer": [
        "python",
        "tensorflow",
        "pytorch",
        "deep learning",
        "neural networks",
        "nlp",
        "computer vision",
        "model deployment"
    ],

    "frontend developer": [
        "html",
        "css",
        "javascript",
        "react",
        "responsive design",
        "ui design",
        "tailwind css",
        "api integration"
    ],

    "backend developer": [
        "nodejs",
        "express",
        "mongodb",
        "rest api",
        "authentication",
        "database management",
        "server deployment"
    ],

    "full stack developer": [
        "html",
        "css",
        "javascript",
        "react",
        "nodejs",
        "mongodb",
        "sql",
        "api development"
    ],

    "software engineer": [
        "java",
        "c++",
        "dsa",
        "algorithms",
        "oop",
        "problem solving",
        "system design"
    ],

    "cybersecurity analyst": [
        "network security",
        "ethical hacking",
        "penetration testing",
        "kali linux",
        "firewalls",
        "vulnerability assessment"
    ],

    "cloud engineer": [
        "aws",
        "docker",
        "kubernetes",
        "cloud security",
        "devops",
        "linux",
        "ci cd"
    ],

    "mobile app developer": [
        "android",
        "flutter",
        "firebase",
        "kotlin",
        "api integration",
        "ui development"
    ],

    "game developer": [
        "unity",
        "unreal engine",
        "game physics",
        "3d graphics",
        "c#",
        "animation systems"
    ],

    "robotics engineer": [
        "robotics",
        "arduino",
        "automation",
        "sensors",
        "embedded systems",
        "control systems"
    ],

    "iot engineer": [
        "iot",
        "microcontrollers",
        "arduino",
        "raspberry pi",
        "embedded c",
        "sensor integration"
    ],

    "blockchain developer": [
        "blockchain",
        "smart contracts",
        "solidity",
        "web3",
        "cryptography",
        "ethereum"
    ],

    # -----------------------------
    # MEDICAL CAREERS
    # -----------------------------

    "doctor": [
        "anatomy",
        "physiology",
        "clinical diagnosis",
        "patient management",
        "medical ethics",
        "pharmacology",
        "healthcare"
    ],

    "nurse": [
        "critical care",
        "patient monitoring",
        "emergency response",
        "clinical support",
        "medical assistance",
        "hospital management"
    ],

    "surgeon": [
        "surgical procedures",
        "operation theatre",
        "anatomy",
        "clinical surgery",
        "patient care",
        "emergency surgery"
    ],

    "pharmacist": [
        "drug management",
        "prescriptions",
        "pharmacology",
        "medicine dispensing",
        "patient counseling"
    ],

    "dentist": [
        "oral surgery",
        "dental care",
        "tooth extraction",
        "orthodontics",
        "patient treatment"
    ],

    "psychologist": [
        "mental health",
        "therapy",
        "counseling",
        "behavior analysis",
        "patient communication"
    ],

    "lab technician": [
        "pathology",
        "blood testing",
        "laboratory equipment",
        "microbiology",
        "sample analysis"
    ],

    "nutritionist": [
        "diet planning",
        "nutrition analysis",
        "healthcare",
        "meal planning",
        "fitness nutrition"
    ],

    # -----------------------------
    # CREATIVE CAREERS
    # -----------------------------

    "actor": [
        "theatre",
        "screen acting",
        "dialogue delivery",
        "stage performance",
        "body language",
        "emotional expression"
    ],

    "musician": [
        "music theory",
        "instrument mastery",
        "vocals",
        "composition",
        "music production",
        "live performance"
    ],

    "artist": [
        "drawing",
        "painting",
        "sketching",
        "creative design",
        "color theory",
        "visual storytelling"
    ],

    "photographer": [
        "camera handling",
        "photo editing",
        "lightroom",
        "lighting techniques",
        "composition",
        "portrait photography"
    ],

    "animator": [
        "3d animation",
        "blender",
        "storyboarding",
        "motion graphics",
        "character animation"
    ],

    "fashion designer": [
        "fashion styling",
        "textile design",
        "creative sketching",
        "fashion trends",
        "garment construction"
    ],

    "content creator": [
        "video editing",
        "social media",
        "storytelling",
        "youtube",
        "content strategy",
        "branding"
    ],

    # -----------------------------
    # BUSINESS CAREERS
    # -----------------------------

    "accountant": [
        "finance",
        "taxation",
        "tally",
        "auditing",
        "bookkeeping",
        "financial reporting"
    ],

    "marketing manager": [
        "branding",
        "digital marketing",
        "seo",
        "communication",
        "campaign management",
        "market research"
    ],

    "business analyst": [
        "business strategy",
        "data analysis",
        "problem solving",
        "stakeholder management",
        "reporting"
    ],

    "sales executive": [
        "sales strategy",
        "customer handling",
        "negotiation",
        "lead generation",
        "communication"
    ],

    "hr manager": [
        "recruitment",
        "employee management",
        "leadership",
        "communication",
        "organizational behavior"
    ],

    "bank manager": [
        "banking",
        "finance",
        "customer service",
        "risk management",
        "investment planning"
    ],

    # -----------------------------
    # OTHER CAREERS
    # -----------------------------

    "teacher": [
        "classroom management",
        "teaching methods",
        "communication",
        "student mentoring",
        "subject expertise"
    ],

    "lawyer": [
        "legal studies",
        "courtroom practice",
        "debate",
        "legal drafting",
        "case analysis"
    ],

    "pilot": [
        "aviation",
        "aircraft navigation",
        "flight control",
        "communication systems",
        "air safety"
    ],

    "chef": [
        "cooking",
        "food preparation",
        "recipe creation",
        "kitchen management",
        "food safety"
    ],

    "architect": [
        "autocad",
        "building planning",
        "3d design",
        "construction",
        "structural design"
    ],

    "civil engineer": [
        "construction",
        "autocad",
        "surveying",
        "project management",
        "structural analysis"
    ],

    "mechanical engineer": [
        "cad",
        "solidworks",
        "manufacturing",
        "machine design",
        "thermodynamics"
    ],

    "electrical engineer": [
        "circuits",
        "electronics",
        "embedded systems",
        "power systems",
        "electrical design"
    ]
}
# -----------------------------
# SALARY PREDICTION DATA
# -----------------------------
salary_data = {

    "data scientist": "₹12 - ₹25 LPA",
    "ai engineer": "₹15 - ₹35 LPA",
    "frontend developer": "₹6 - ₹15 LPA",
    "backend developer": "₹8 - ₹18 LPA",
    "full stack developer": "₹10 - ₹22 LPA",
    "software engineer": "₹7 - ₹20 LPA",
    "cybersecurity analyst": "₹9 - ₹22 LPA",
    "cloud engineer": "₹12 - ₹28 LPA",
    "mobile app developer": "₹7 - ₹18 LPA",
    "game developer": "₹6 - ₹16 LPA",
    "doctor": "₹10 - ₹40 LPA",
    "surgeon": "₹20 - ₹60 LPA",
    "nurse": "₹4 - ₹10 LPA",
    "pharmacist": "₹5 - ₹12 LPA",
    "dentist": "₹8 - ₹25 LPA",
    "actor": "₹3 - ₹50 LPA",
    "musician": "₹3 - ₹30 LPA",
    "photographer": "₹4 - ₹15 LPA",
    "content creator": "₹5 - ₹40 LPA",
    "marketing manager": "₹8 - ₹25 LPA",
    "business analyst": "₹10 - ₹22 LPA",
    "pilot": "₹20 - ₹50 LPA",
    "teacher": "₹4 - ₹12 LPA",
    "lawyer": "₹8 - ₹30 LPA",
    "chef": "₹5 - ₹18 LPA"
}
# -----------------------------
# JOB DEMAND DATA
# -----------------------------
job_demand = {

    "data scientist": "🔥 Very High Demand",
    "ai engineer": "🔥 Very High Demand",
    "frontend developer": "📈 High Demand",
    "backend developer": "📈 High Demand",
    "full stack developer": "🔥 Very High Demand",
    "software engineer": "📈 High Demand",
    "cybersecurity analyst": "🔥 Very High Demand",
    "cloud engineer": "🔥 Very High Demand",
    "doctor": "🔥 Very High Demand",
    "nurse": "📈 High Demand",
    "surgeon": "📈 High Demand",
    "teacher": "📈 Stable Demand",
    "actor": "📉 Competitive Industry",
    "musician": "📉 Competitive Industry",
    "pilot": "📈 High Demand",
    "marketing manager": "📈 High Demand",
    "business analyst": "📈 High Demand",
    "lawyer": "📈 Stable Demand",
    "chef": "📈 Growing Demand"
}

# -----------------------------
# INPUT SECTION
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# RESUME UPLOAD
# -----------------------------
with col1:

    st.markdown("## 📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"]
    )

    resume_text = ""

    if uploaded_file is not None:

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text

        st.success("✅ Resume Uploaded Successfully")

# -----------------------------
# MANUAL SKILLS
# -----------------------------
with col2:

    st.markdown("## 💡 Enter Skills/Interests Manually")

    manual_input = st.text_area(
        "Enter your skills",
        height=250,
        placeholder="Example: Python, Machine Learning, SQL..."
    )

# -----------------------------
# COMBINE INPUTS
# -----------------------------
final_input = ""

if resume_text:
    final_input += resume_text.lower()

if manual_input:
    final_input += " " + manual_input.lower()

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("🔍 Analyze Career Path"):

    if final_input.strip() == "":

        st.warning("⚠ Please upload resume or enter skills")

    else:

        # -----------------------------
        # DOMAIN DETECTION
        # -----------------------------
        domain_scores = {}

        for domain, keywords in domains.items():

            score = 0

            for word in keywords:

                if word in final_input:
                    score += 1

            domain_scores[domain] = score

        detected_domain = max(
            domain_scores,
            key=domain_scores.get
        )

        st.markdown(f"""
        <div class="result-card">

        <h2 style="color:white;">
        🧠 Detected Career Domain
        </h2>

        <h1 style="color:#38BDF8;">
        {detected_domain}
        </h1>

        </div>
        """, unsafe_allow_html=True)

        # -----------------------------
        # MODEL PREDICTION
        # -----------------------------
        transformed = vectorizer.transform([final_input])

        probabilities = model.predict_proba(transformed)[0]

        career_probs = []

        for i, career in enumerate(model.classes_):

            career_name = career.strip().lower()

            career_domain = career_domains.get(
                career_name,
                "General"
            )

            if career_domain == detected_domain:

                career_probs.append(
                    (career_name, probabilities[i])
                )

        career_probs = sorted(
            career_probs,
            key=lambda x: x[1],
            reverse=True
        )

        top_predictions = career_probs[:3]

        st.markdown(
            '<div class="section-title">🎯 Top Career Matches</div>',
            unsafe_allow_html=True
        )


        top_career = None
        st.balloons()

        

        for i, (career, prob) in enumerate(top_predictions):

            confidence = prob * 100

            if i == 0:
                top_career = career

            st.markdown(f"""
            <div class="result-card">

            <h2 style="color:white;">
            🚀 {career.title()}
            </h2>

            <h3 style="color:#38BDF8;">
            Confidence Score: {confidence:.2f}%
            </h3>

            </div>
            """, unsafe_allow_html=True)

            st.progress(min(confidence / 100, 1.0))

                    # -----------------------------
        # CAREER PREDICTION ANALYTICS
        # -----------------------------
        st.markdown(
            '<div class="section-title">📊 Career Prediction Analytics</div>',
            unsafe_allow_html=True
        )

        career_names = [
            career.title()
            for career, prob in top_predictions
        ]

        career_scores = [
            round(prob * 100, 2)
            for career, prob in top_predictions
        ]

        pie_df = pd.DataFrame({
            "Career": career_names,
            "Confidence": career_scores
        })

        # -----------------------------
        # PIE CHART
        # -----------------------------
        fig_pie = px.pie(
            pie_df,
            names="Career",
            values="Confidence",
            title="Career Prediction Distribution",
            hole=0.4
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

        # -----------------------------
        # BAR GRAPH
        # -----------------------------
        fig_bar = px.bar(
            pie_df,
            x="Career",
            y="Confidence",
            text="Confidence",
            title="Confidence Scores"
        )

        fig_bar.update_traces(
            textposition='outside'
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

        # -----------------------------
        # CAREER EXPLANATION
        # -----------------------------
        st.markdown(
            '<div class="section-title">🎯 Why This Career?</div>',
            unsafe_allow_html=True
        )

        reasons = []

        if "python" in final_input:
            reasons.append("Strong Python skills detected")

        if "machine learning" in final_input:
            reasons.append("Machine Learning knowledge identified")

        if "hospital" in final_input:
            reasons.append("Medical and healthcare keywords found")

        if "javascript" in final_input:
            reasons.append("Frontend/Web development skills detected")

        if "acting" in final_input:
            reasons.append("Creative acting-related skills identified")

        for reason in reasons:
            st.write(f"✔ {reason}")

               # -----------------------------
                # -----------------------------
        # RESUME SCORE ANALYZER
        # -----------------------------
        score = 0

        found_skills = []

        for skill in skill_database:

            if skill.lower() in final_input.lower():
                found_skills.append(skill)

        if resume_text.strip() != "":

            st.markdown(
                '<div class="section-title">📊 Resume Score Analyzer</div>',
                unsafe_allow_html=True
            )

            score = min(len(found_skills) * 4, 100)

            st.markdown(f"## ✅ Resume Score: {score}/100")

            st.progress(score / 100)

            st.markdown("## 🔥 Detected Skills")

            st.write(found_skills)
                        # -----------------------------
            # SKILLS ANALYTICS GRAPH
            # -----------------------------
            st.markdown(
                '<div class="section-title">🧠 Skills Analytics</div>',
                unsafe_allow_html=True
            )

            skill_counts = {}

            for skill in found_skills:

                skill_counts[skill] = (
                    skill_counts.get(skill, 0) + 1
                )

            skill_df = pd.DataFrame({
                "Skill": list(skill_counts.keys()),
                "Count": list(skill_counts.values())
            })

            fig_skills = px.bar(
                skill_df,
                x="Skill",
                y="Count",
                title="Detected Skills Distribution"
            )

            st.plotly_chart(
                fig_skills,
                use_container_width=True
            )

                    # -----------------------------
        # RESUME IMPROVEMENT SUGGESTIONS
        # -----------------------------
        st.markdown(
            '<div class="section-title">📝 Resume Improvement Suggestions</div>',
            unsafe_allow_html=True
        )

        suggestions = []

        # -----------------------------
        # BASIC CHECKS
        # -----------------------------
        if "project" not in final_input:
            suggestions.append(
                "Add Projects section to showcase practical experience."
            )

        if "internship" not in final_input:
            suggestions.append(
                "Add Internship experience to strengthen your resume."
            )

        if "certification" not in final_input:
            suggestions.append(
                "Add Certifications to improve credibility."
            )

        if "github" not in final_input:
            suggestions.append(
                "Add GitHub profile link."
            )

        if "linkedin" not in final_input:
            suggestions.append(
                "Add LinkedIn profile link."
            )

        if len(found_skills) < 5:
            suggestions.append(
                "Try adding more technical skills."
            )

        if score < 60:
            suggestions.append(
                "Resume score is low. Improve ATS keywords and technical content."
            )

        # -----------------------------
        # SHOW SUGGESTIONS
        # -----------------------------
        if suggestions:

            for suggestion in suggestions:

                st.markdown(f"""
                <div class="result-card">
                ⚡ {suggestion}
                </div>
                """, unsafe_allow_html=True)

        else:

            st.success(
                "✅ Excellent Resume! Your resume looks strong and professional."
            )

        # -----------------------------
        # SKILL GAP ANALYZER
        # -----------------------------
        st.markdown(
            '<div class="section-title">🧠 Skill Gap Analyzer</div>',
            unsafe_allow_html=True
        )

        required_skills = career_required_skills.get(
            top_career,
            []
        )

        missing_skills = []

        for skill in required_skills:

            if skill.lower() not in final_input:
                missing_skills.append(skill)

        if missing_skills:

            for skill in missing_skills:
                st.write(f"❌ {skill}")

        else:
            st.success(
                "✅ You already have major required skills!"
            )

                    # -----------------------------
        # SALARY PREDICTION
        # -----------------------------
        st.markdown(
            '<div class="section-title">💰 Salary Prediction</div>',
            unsafe_allow_html=True
        )

        predicted_salary = salary_data.get(
            top_career.lower(),
            "Salary data not available"
        )

        st.markdown(f"""
        <div class="result-card">

        <h2 style="color:white;">
        💵 Estimated Salary Range
        </h2>

        <h1 style="color:#38BDF8;">
        {predicted_salary}
        </h1>

        </div>
        """, unsafe_allow_html=True)

                # -----------------------------
        # JOB DEMAND METER
        # -----------------------------
        st.markdown(
            '<div class="section-title">📈 Job Demand Meter</div>',
            unsafe_allow_html=True
        )

        demand = job_demand.get(
            top_career.lower(),
            "Demand data not available"
        )

        st.markdown(f"""
        <div class="result-card">

        <h2 style="color:white;">
        🌍 Current Market Demand
        </h2>

        <h1 style="color:#38BDF8;">
        {demand}
        </h1>

        </div>
        """, unsafe_allow_html=True)

        # -----------------------------
        # ROADMAP GENERATOR
        # -----------------------------
        st.markdown(
            '<div class="section-title">🛣 Career Roadmap</div>',
            unsafe_allow_html=True
        )

        roadmap = career_roadmaps.get(
            top_career.lower(),
            []
        )

        if roadmap:

            for i, step in enumerate(roadmap, start=1):

                st.markdown(f"""
                <div class="result-card">
                <h3>{i}. {step}</h3>
                </div>
                """, unsafe_allow_html=True)

            # -----------------------------
            # PDF DOWNLOAD
            # -----------------------------
            generate_pdf(
                top_career.title(),
                score,
                roadmap
            )

            with open(
                "career_report.pdf",
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="⬇ Download Career Report PDF",
                    data=pdf_file,
                    file_name="career_report.pdf",
                    mime="application/pdf"
                )

        else:

            st.info(
                "Roadmap not available for this career yet"
            )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    """
    <div class='footer'>
    Made with ❤️ using Streamlit & AI
    </div>
    """,
    unsafe_allow_html=True
)
