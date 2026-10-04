# ==========================================
# ResumeSense - Skill Extractor
# ==========================================

import re


# ------------------------------------------
# Skills Database
# ------------------------------------------

SKILLS = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "kotlin",
    "swift",
    "go",
    "r",

    # Web Development
    "html",
    "css",
    "bootstrap",
    "tailwind css",
    "react",
    "react.js",
    "angular",
    "angularjs",
    "vue",
    "node.js",
    "node",
    "express",
    "django",
    "flask",

    # Database
    "mysql",
    "postgresql",
    "mongodb",
    "firebase",
    "firestore",
    "oracle",
    "sql",
    "sqlite",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "nlp",
    "natural language processing",
    "computer vision",
    "tensorflow",
    "keras",
    "pytorch",
    "scikit-learn",
    "sklearn",
    "pandas",
    "numpy",
    "matplotlib",

    # Data
    "data analysis",
    "data science",
    "data visualization",
    "excel",
    "power bi",
    "tableau",

    # Cloud / DevOps
    "aws",
    "azure",
    "google cloud",
    "gcp",
    "docker",
    "kubernetes",
    "git",
    "github",
    "gitlab",
    "jenkins",

    # Mobile Development
    "android",
    "android studio",
    "android development",
    "flutter",
    "react native",

    # Other Technical Skills
    "rest api",
    "api",
    "json",
    "xml",
    "linux",
    "windows",
    "networking",
    "cybersecurity",
    "software testing",
    "debugging",

    # Soft Skills
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "time management",
    "creativity",
    "critical thinking",
    "adaptability",
    "project management"
]


# ------------------------------------------
# Extract Skills From Resume
# ------------------------------------------

def extract_skills(text):

    if not text:
        return []

    text = text.lower()

    found_skills = []

    for
