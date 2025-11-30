# -*- coding: utf-8 -*-
import streamlit as st

# --- Configuration & Styling ---
st.set_page_config(
    page_title="The Grandview Hotel",
    layout="wide",
    # Changed to 'auto' or 'expanded' so the sidebar navigation works
    initial_sidebar_state="auto"
)

# --- Define Image URLs (REPLACE THESE WITH YOUR ACTUAL IMAGE URLs) ---
HERO_IMAGE = 'https://images.unsplash.com/photo-1542314831-068cd1dbf3ce?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80'
STANDARD_ROOM_IMG = 'https://images.unsplash.com/photo-1560003058-294025f0e9d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80'
DELUXE_SUITE_IMG = 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80'
FAMILY_ROOM_IMG = 'https://images.unsplash.com/photo-1544078864-77e7709565ec?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80'


# --- Custom CSS for Styling (Based on your enhanced style.css) ---
# We use the CSS from the previous step to apply the attractive styles.
st.markdown(
    f"""
    <style>
    /* Global Styles */
    .stApp {{
        background-color: #f8f8f8; /* Very light gray background for depth */
        color: #333;
        font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
    }}
    
    /* HIDE the default Streamlit header/footer */
    .stApp > header {{ display: none; }}
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    /* Streamlit Sidebar Customization */
    .st-emotion-cache-vk3wpn {{ /* Sidebar background color */
        background-color: #004c4c; 
        color: white;
    }}
    .st-emotion-cache-vk3wpn .stRadio > label, 
    .st-emotion-cache-vk3wpn .stMarkdown p {{
        color: white !important;
    }}
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:last-child {{
        color: white !important;
    }}
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:first-child {{
        border-color: #ffcc00 !important;
    }}
    .st-emotion-cache-vk3wpn .stAlert {{ /* Info box in sidebar */
        background-color: #1a6f6f !important;
        color: white !important;
    }}
    
    /* --- Hero Section --- */
    .hero-section {{
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('{HERO_IMAGE}') no-repeat center center/cover;
        height: 70vh;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 40px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }}

    .hero-content {{
        background: rgba(0, 0, 0, 0.6);
        padding: 40px 60px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
    }}
    .hero-content h2 {{
        font-size: 3.5em;
        margin-bottom: 15px;
        font-weight: 700;
        color: white;
    }}
    .hero-content p {{
        font-size: 1.4em;
        font-weight: 300;
        color: white;
    }}

    /* Primary Button (To style the Streamlit button) */
    .stButton>button {{
        display: inline-block;
        background: #ffcc00;
        color: #004c4c !important;
        padding: 15px 30px;
        text-decoration: none;
        border-radius: 8px;
        margin-top: 25px;
        font-size: 18px;
        font-weight: bold;
        transition: background 0.3s, box-shadow 0.3s;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        border: none; /* Remove default Streamlit border */
    }}
    .stButton>button:hover {{
        background: #e6b800;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }}
    /* Center the button inside the hero content */
    .hero-button-container {{
        text-align: center;
        margin-top: 25px;
    }}
    
    /* Section Headers */
    h2 {{
        font-size: 3em;
        color: #004c4c;
        margin-bottom: 50px;
        font-weight: 600;
        text-align: center;
    }}
    
    /* Room Card Styling */
    .room-card {{
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        overflow: hidden;
        transition: transform 0.3s, box-shadow 0.3s;
        height: 100%; /* Important for column alignment */
        margin-bottom: 20px;
    }}
    .room-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.25);
    }}
    .room-card h3 {{
        padding: 0 20px;
        font-size: 1.5em;
        color: #004c4c;
    }}
    .room-card p {{
        padding: 0 20px 20px 20px;
    }}

    /* --- Amenities Section --- */
    .amenities-list {{
        list-style: none;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding-top: 20px;
    }}
    .amenities-list li {{
        background: #ffffff;
        color: #004c4c;
        padding: 18px 30px; 
        margin: 12px;
        border-radius: 30px;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: background 0.3s;
    }}
    .amenities-list li:hover {{
        background: #ffcc00;
        color: #333;
    }}
    .icon {{
        margin-right: 10px;
        color: #ffcc00;
        font-size: 1.4em;
        line-height: 1;
    }}
    
    /* --- Footer --- */
    .custom-footer {{
        background: #1c1c1c; 
        color: #ccc;
        padding: 20px 0;
        text-align: center;
        width: 100%;
        margin-top: 40px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# --- Initialize Session State for Navigation ---
if 'page' not in st.session_state:
    st.session_state['page'] = "Home"

# Function to navigate
def navigate_to(page_name):
    st.session_state['page'] = page_name

# --- 1. Functional Navigation (Streamlit Sidebar) ---
st.sidebar.title("The Grandview Hotel 🏨")
st.sidebar.markdown("---") 

# Use the session state variable to control the radio button
page = st.sidebar.radio(
    "Explore our hotel:",
    ["Home", "Rooms & Suites", "Book a Room", "Amenities", "Contact Us"],
    key="page", # Link radio to session state
    on_change=lambda: navigate_to(st.session_state['page']) # Re-run app on change
)

st.sidebar.markdown("---")
st.sidebar.info("Experience luxury with seamless web deployment!")

# --- 2. Page Rendering Logic ---

if st.session_state['page'] == "Home":
    # Hero Section with embedded image URL from CSS
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    # Use st.container to center the button visually
    st.markdown(
        """
        <div class="hero-content">
            <h2>Your Luxurious Escape Awaits</h2>
            <p>Experience world-class hospitality in the heart of the city.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Place the button inside a container for styling control
    with st.container():
        # The button to trigger navigation
        if st.button("Explore Rooms"):
            navigate_to("Rooms & Suites")
            st.rerun() # Force re-run to update the page immediately

    st.markdown('</div>', unsafe_allow_html=True)
    
    # Text content for Home
    st.markdown("<h2>Why Choose The Grandview?</h2>", unsafe_allow_html=True)
    st.write("With unparalleled service, breathtaking views, and modern amenities, your stay with us will be an unforgettable experience. We pride ourselves on exceptional hospitality and a tranquil environment.")

# --- Rooms Section with st.image() ---
elif st.session_state['page'] == "Rooms & Suites":
    st.markdown("<h2>Our Luxurious Accommodations</h2>", unsafe_allow_html=True)
    st.write("Each room and suite is designed with your comfort in mind, blending elegant decor with modern conveniences.")

    col1, col2, col3 = st.columns(3) # Create three columns

    # Room Card 1: Standard Double
    with col1:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        # Using st.image() for easy image loading
        st.image(STANDARD_ROOM_IMG, caption="A cozy retreat for two.", use_column_width="always")
        st.markdown("<h3>Standard Double</h3>", unsafe_allow_html=True)
        st.markdown("<p>Comfortable and elegantly designed for a restful stay, featuring a plush queen-sized bed and city views.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Room Card 2: Deluxe Suite
    with col2:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(DELUXE_SUITE_IMG, caption="Indulge in extra space and luxury.", use_column_width="always")
        st.markdown("<h3>Deluxe Suite</h3>", unsafe_allow_html=True)
        st.markdown("<p>Spacious living area, premium views, and exclusive services for an elevated experience. Perfect for extended stays.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Room Card 3: Family Room
    with col3:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(FAMILY_ROOM_IMG, caption="Comfort for the whole family.", use_column_width="always")
        st.markdown("<h3>Family Room</h3>", unsafe_allow_html=True)
        st.markdown("<p>Ideal for families, offering extra space, multiple beds, and amenities tailored for a comfortable group stay.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Ready to Book Your Stay?") # Placeholder button

# --- Placeholder Pages for the rest of the navigation ---
elif st.session_state['page'] == "Book a Room":
    st.markdown("<h2>Secure Your Reservation 📝</h2>", unsafe_allow_html=True)
    st.info("Here you will place your interactive booking form using `st.form()` and widgets.")
    # Add your booking form logic here if needed

elif st.session_state['page'] == "Amenities":
    st.markdown("<h2>Luxury Amenities ✨</h2>", unsafe_allow_html=True)
    st.write("We offer a range of premium amenities to ensure your stay is comfortable.")
    st.markdown(
        """
        <div class="amenities-list">
            <li><i class="icon">★</i> Complimentary High-Speed Wi-Fi</li>
            <li><i class="icon">★</i> Rooftop Pool & Lounge</li>
            <li><i class="icon">★</i> Fine Dining Restaurant</li>
        </div>
        """,
        unsafe_allow_html=True
    )
    
elif st.session_state['page'] == "Contact Us":
    st.markdown("<h2>Contact The Grandview Hotel 📞</h2>", unsafe_allow_html=True)
    st.info("Here you will place your contact information and contact form.")


# --- Footer ---
st.markdown(
    """
    <div class="custom-footer">
        <p>&copy; 2025 The Grandview Hotel. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
