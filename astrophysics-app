import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Astrophysics Portal", layout="wide")

# Valid Credentials (stored in Python logic)
VALID_EMAIL = "astro@user.com"
VALID_PASSWORD = "starlight2026"

# Initialize Session State for login tracking
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None

# --- SIGN-IN PAGE ---
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

# --- DASHBOARD PAGE ---
else:
    st.title("✨ Astrophysics Knowledge Hub")
    st.write("Click on any topic below to display its image and facts:")

    # Data dictionary for images (NASA/Public Domain sources), Wikipedia links, and 5 facts each
    data = {
        "Mercury": {
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Uranus",
            "facts": [
                "Uranus is an ice giant with a atmosphere rich in methane, giving it a blue-green color.",
                "It rotates on its side with an axial tilt of nearly 98 degrees.",
                "It has the coldest atmosphere of any planet in the solar system.",
                "Uranus has 13 faint, dark rings.",
                "It was the first planet discovered using a telescope (in 1781)."
            ]
        },
        "Neptune": {
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/63/Neptune_-_Full_Disk_Visible_Inbound.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Black_hole_-_Messier_87_crop_max_res.jpg",
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
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Milky_Way_Night_Sky_Black_Rock_Desert_Nevada.jpg",
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

    # Render Buttons Grid
    cols = st.columns(5)
    topics = list(data.keys())

    for idx, topic in enumerate(topics):
        col = cols[idx % 5]
        if col.button(topic, key=topic, use_container_width=True):
            st.session_state.selected_topic = topic

    st.markdown("---")

    # Display content based on button selection
    if st.session_state.selected_topic:
        selected = st.session_state.selected_topic
        topic_info = data[selected]

        st.header(f"Information on {selected}")
        st.image(topic_info["image"], caption=f"Public domain image of {selected}", use_container_width=True)

        st.subheader(f"5 Key Facts about {selected}:")
        for fact in topic_info["facts"]:
            st.markdown(f"- {fact}")

        st.markdown(f"👉 [Read full article on Wikipedia]({topic_info['wiki']})")
    else:
        st.info("Please click any of the 10 topic buttons above to view its image and information.")
