import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Astrophysics Portal", layout="wide")

# Valid Credentials
VALID_EMAIL = "astro@user.com"
VALID_PASSWORD = "starlight2026"

# Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "dashboard"
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None

# Comprehensive Data Dictionary
data = {
    "Mercury": {
        "image": "https://images-assets.nasa.gov/image/PIA11364/PIA11364~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Mercury_(planet)",
        "facts": [
            "Mercury is the smallest planet in our solar system and closest to the Sun.",
            "Despite being closest to the Sun, it is not the hottest planet (Venus is).",
            "It has a very thin atmosphere known as an exosphere.",
            "Mercury completes one orbit around the Sun in just 88 Earth days.",
            "It has no moons or rings."
        ]
    },
    "Venus": {
        "image": "https://images-assets.nasa.gov/image/PIA00271/PIA00271~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Venus",
        "facts": [
            "Venus is the hottest planet in our solar system due to a runaway greenhouse effect.",
            "It spins in the opposite direction of most planets (retrograde rotation).",
            "A day on Venus is longer than a year on Venus.",
            "Its surface pressure is about 90 times greater than Earth's.",
            "It is named after the Roman goddess of love and beauty."
        ]
    },
    "Earth": {
        "image": "https://images-assets.nasa.gov/image/PIA18033/PIA18033~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Earth",
        "facts": [
            "Earth is the only astronomical object known to harbor life.",
            "About 71% of Earth's surface is covered by liquid water.",
            "Its atmosphere is composed mostly of nitrogen (78%) and oxygen (21%).",
            "Earth has one natural satellite, the Moon.",
            "It has a powerful magnetic field that protects it from solar radiation."
        ]
    },
    "Mars": {
        "image": "https://images-assets.nasa.gov/image/PIA02820/PIA02820~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Mars",
        "facts": [
            "Mars is known as the Red Planet due to iron oxide (rust) on its surface.",
            "It hosts Olympus Mons, the largest volcano in the solar system.",
            "Mars has two small moons named Phobos and Deimos.",
            "It has a very thin atmosphere made primarily of carbon dioxide.",
            "Evidence suggests Mars once had liquid water flowing on its surface."
        ]
    },
    "Jupiter": {
        "image": "https://images-assets.nasa.gov/image/PIA02873/PIA02873~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Jupiter",
        "facts": [
            "Jupiter is the largest planet in our solar system.",
            "Its Great Red Spot is a giant storm larger than Earth that has raged for centuries.",
            "It is a gas giant primarily made of hydrogen and helium.",
            "Jupiter has more than 90 confirmed moons, including Ganymede.",
            "It has a weak ring system that is difficult to see."
        ]
    },
    "Saturn": {
        "image": "https://images-assets.nasa.gov/image/PIA14922/PIA14922~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Saturn",
        "facts": [
            "Saturn is famous for its complex and bright ring system made of ice and rock.",
            "It is the second-largest planet in the solar system.",
            "Saturn is a gas giant with a density so low it could float in water.",
            "Its largest moon, Titan, has a thick atmosphere and liquid methane lakes.",
            "A year on Saturn lasts about 29.5 Earth years."
        ]
    },
    "Uranus": {
        "image": "https://images-assets.nasa.gov/image/PIA18182/PIA18182~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Uranus",
        "facts": [
            "Uranus is an ice giant with an atmosphere rich in methane, giving it a blue-green color.",
            "It rotates on its side with an axial tilt of nearly 98 degrees.",
            "It has the coldest atmosphere of any planet in the solar system.",
            "Uranus has 13 faint, dark rings.",
            "It was the first planet discovered using a telescope (in 1781)."
        ]
    },
    "Neptune": {
        # AI/Digital render artwork of Neptune
        "image": "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?auto=format&fit=crop&w=1200&q=80",
        "wiki": "https://en.wikipedia.org/wiki/Neptune",
        "facts": [
            "Neptune is the most distant planet from the Sun in our solar system.",
            "It experiences the strongest winds of any planet, reaching supersonic speeds.",
            "Neptune is an ice giant with a deep blue color caused by methane.",
            "It takes about 165 Earth years to complete one orbit around the Sun.",
            "Its largest moon, Triton, orbits the planet backwards relative to its rotation."
        ]
    },
    "Black Hole": {
        "image": "https://images-assets.nasa.gov/image/PIA23122/PIA23122~orig.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Black_hole",
        "facts": [
            "A black hole is a region of space where gravity is so strong that nothing, not even light, can escape.",
            "The boundary beyond which nothing can escape is called the event horizon.",
            "They form when massive stars collapse under their own gravity at the end of their life cycle.",
            "Supermassive black holes exist at the center of almost every large galaxy.",
            "In 2019, the Event Horizon Telescope captured the first-ever direct image of a black hole (M87*)."
        ]
    },
    "Galaxy": {
        # AI/Digital render artwork of a spiral Galaxy
        "image": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1200&q=80",
        "wiki": "https://en.wikipedia.org/wiki/Galaxy",
        "facts": [
            "A galaxy is a massive system of stars, stellar remnants, interstellar gas, dust, and dark matter.",
            "Our home galaxy is the Milky Way, a barred spiral galaxy containing over 100 billion stars.",
            "Galaxies come in four main shapes: spiral, elliptical, lenticular, and irregular.",
            "The observable universe contains an estimated 2 trillion galaxies.",
            "The nearest major galaxy to the Milky Way is the Andromeda Galaxy."
        ]
    }
}

# --- PAGE 1: SIGN-IN PAGE ---
if not st.session_state.logged_in:
    st.title("🌌 Astrophysics Portal Sign-In")

    email_input = st.text_input("Email Address")
    password_input = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if email_input == VALID_EMAIL and password_input == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid email or password. Please try again.")

# --- PAGE 2: MAIN DASHBOARD ---
elif st.session_state.current_page == "dashboard":
    st.title("✨ Astrophysics Knowledge Hub")
    st.write("Click on any topic button below to navigate to its dedicated information page:")

    cols = st.columns(5)
    topics = list(data.keys())

    for idx, topic in enumerate(topics):
        col = cols[idx % 5]
        if col.button(topic, key=topic, use_container_width=True):
            st.session_state.selected_topic = topic
            st.session_state.current_page = "topic_detail"
            st.rerun()

# --- PAGE 3: DEDICATED TOPIC PAGE ---
elif st.session_state.current_page == "topic_detail":
    selected = st.session_state.selected_topic
    topic_info = data[selected]

    if st.button("⬅️ Back to Dashboard"):
        st.session_state.current_page = "dashboard"
        st.session_state.selected_topic = None
        st.rerun()

    st.title(f"📖 {selected}")
    
    st.image(topic_info["image"], caption=f"Image/Artwork representation of {selected}", use_container_width=True)

    st.subheader(f"5 Key Information Points about {selected}:")
    for fact in topic_info["facts"]:
        st.markdown(f"- {fact}")

    st.markdown("---")
    st.markdown(f"🔗 **Learn More:** [Read full article on Wikipedia]({topic_info['wiki']})")
