from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# 1. RESUME - JOB MATCH SCORE
# ==========================================

def calculate_match_score(resume_text, job_description):

    if not resume_text or not job_description:
        return 0

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform([
        resume_text,
        job_description
    ])

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(similarity * 100, 1)


# ==========================================
# 2. ATS SCORE
# ==========================================

def calculate_ats_score(text):

    if not text:
        return 0

    lower_text = text.lower()

    # Important resume sections
    sections = [
        "education",
        "experience",
        "skills",
        "projects",
        "certification",
        "summary",
        "objective"
    ]

    section_score = 0

    for section in sections:

        if section in lower_text:
            section_score += 8

    # Contact information
    contact_score = 0

    if "@" in text:
        contact_score += 10

    if any(char.isdigit() for char in text):
        contact_score += 5

    # Resume length
    words = len(text.split())

    if words >= 300:
        length_score = 15

    elif words >= 150:
        length_score = 10

    else:
        length_score = 5

    total_score = (
        section_score
        + contact_score
        + length_score
    )

    return round(
        min(total_score, 100),
        1
    )


# ==========================================
# 3. OVERALL RESUME SCORE
# ==========================================

def calculate_resume_score(
    text,
    match_score,
    ats_score,
    skill_count
):

    if not text:
        return 0

    # Skill score
    skill_score = min(
        skill_count * 10,
        100
    )

    # Resume completeness
    word_count = len(text.split())

    if word_count >= 300:
        completeness_score = 100

    elif word_count >= 150:
        completeness_score = 80

    else:
        completeness_score = 60

    # Final weighted score
    final_score = (
        match_score * 0.45
        + ats_score * 0.30
        + skill_score * 0.15
        + completeness_score * 0.10
    )

    return round(
        min(final_score, 100),
        1
    )


# ==========================================
# 4. JOB RECOMMENDATION
# ==========================================

def recommend_jobs(
    resume_text,
    jobs,
    limit=5
):

    if not resume_text or not jobs:
        return []

    documents = [resume_text]

    # Create searchable text for every job
    for job in jobs:

        job_text = (
            job.get("title", "")
            + " "
            + job.get("description", "")
            + " "
            + " ".join(
                job.get("skills", [])
            )
        )

        documents.append(job_text)

    # TF-IDF
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        documents
    )

    # Calculate similarity
    similarities = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    )[0]

    recommendations = []

    for job, similarity in zip(
        jobs,
        similarities
    ):

        job_result = dict(job)

        job_result["match"] = round(
            float(similarity) * 100,
            1
        )

        recommendations.append(
            job_result
        )

    # Highest match first
    recommendations.sort(
        key=lambda x: x["match"],
        reverse=True
    )

    return recommendations[:limit]
