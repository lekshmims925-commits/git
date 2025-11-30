# -*- coding: utf-8 -*-
import streamlit as st

# --- Image URLs (UPDATE THESE WITH YOUR RAW GITHUB IMAGE LINKS) ---
# Example: 'https://raw.githubusercontent.com/your_username/your_repo/main/images/standard.jpg'
HERO_IMAGE_URL = 'https://images.unsplash.com/photo-1542314831-068cd1dbf3ce?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80' # Placeholder, replace with your actual hero image
STANDARD_ROOM_IMAGE_URL = 'https://images.unsplash.com/photo-1560003058-294025f0e9d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80' # This will be your 'standard.jpg'
DELUXE_ROOM_IMAGE_URL = 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80'
FAMILY_ROOM_IMAGE_URL = 'https://images.unsplash.com/photo-1544078864-77e7709565ec?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80'


# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="The Grandview Hotel",
    layout="wide", # Use wide layout for more space
    initial_sidebar_state="auto" # Keep sidebar open initially
)

# --- Custom CSS for Theming and Minimal Styling ---
st.markdown(
    f"""
    <style>
    /* Global Streamlit App Background & Font */
    .stApp {{
        background-color: #f8f8f8;
        color: #333;
        font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
    }}
    
    /* Hide default Streamlit header/footer */
    header {{ display: none !important; }}
    #MainMenu {{ visibility: hidden !important; }}
    footer {{ visibility: hidden !important; }}

    /* Streamlit Sidebar Customization */
    .st-emotion-cache-vk3wpn {{ /* This class targets the sidebar container */
        background-color: #004c4c; 
        color: white;
    }}
    .st-emotion-cache-vk3wpn .stRadio > label, 
    .st-emotion-cache-vk3wpn .stMarkdown p,
    .st-emotion-cache-vk3wpn .stMarkdown h1,
    .st-emotion-cache-vk3wpn .stMarkdown h2,
    .st-emotion-cache-vk3wpn .stMarkdown h3 {{
        color: white !important;
    }}
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:last-child {{
        color: white !important;
    }}
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:first-child {{
        border-color: #ffcc00 !important; /* Radio button border */
    }}
    .st-emotion-cache-vk3wpn .stAlert {{
        background-color: #1a6f6f !important;
        color: white !important;
    }}

    /* --- Hero Section Styling --- */
    /* Using Streamlit's st.image for the hero, so this CSS is for the overlay text */
    .hero-text-overlay {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
        background: rgba(0, 0, 0, 0.6);
        padding: 40px 60px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
        width: 80%;
        max-width: 800px;
    }}
    .hero-text-overlay h2 {{
        font-size: 3.5em;
        margin-bottom: 15px;
        font-weight: 700;
        color: white !important; /* Override Streamlit header color */
    }}
    .hero-text-overlay p {{
        font-size: 1.4em;
        font-weight: 300;
        color: white !important;
    }}

    /* Primary Button (for "Explore Rooms" in hero) */
    .btn-primary {{
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
    }}
    .btn-primary:hover {{
        background: #e6b800;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
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
        height: 100%; 
        margin-bottom: 20px;
    }}
    .room-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.25);
    }}
    /* Streamlit's st.image inside .room-card */
    .room-card img {{
        border-radius: 10px 10px 0 0; /* Only top corners rounded for image */
        object-fit: cover; /* Ensures image covers area without distortion */
        height: 250px; /* Fixed height for uniformity */
    }}
    .room-card h3 {{
        padding: 15px 20px 5px 20px; /* More space above h3 */
        font-size: 1.5em;
        color: #004c4c;
    }}
    .room-card p {{
        padding: 0 20px 20px 20px;
    }}

    /* Amenities List Styling */
    .amenities-list {{
        list-style: none;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding-top: 20px;
        padding-left: 0; /* Ensure no default list padding */
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
        display: flex; /* Allow icon and text to align */
        align-items: center;
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
    
    /* Custom Footer Styling */
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

# --- Streamlit Sidebar Navigation ---
st.sidebar.title("The Grandview Hotel 🏨")
st.sidebar.markdown("---") 

page = st.sidebar.radio(
    "Explore our hotel:",
    ["Home", "Rooms & Suites", "Book a Room", "Amenities", "Contact Us"]
)

st.sidebar.markdown("---")
st.sidebar.info("Experience luxury with seamless web deployment!")

# --- Main Page Content ---

if page == "Home":
    # Use st.container for the hero image and overlay text
    st.container(height=500, border=False) # Make a container to hold the image
    st.image(HERO_IMAGE_URL, use_column_width=True, caption="Experience unparalleled luxury")
    
    # Text overlay directly below the image for simplicity, or use CSS for absolute positioning
    st.markdown(
        """
        <div class="hero-text-overlay" style="position: relative; top: -300px; left: 0; transform: none; width: 100%; max-width: none;">
            <h2>Your Luxurious Escape Awaits</h2>
            <p>Experience world-class hospitality in the heart of the city.</p>
            <a href="?page=Rooms+%26+Suites" class="btn-primary">Explore Rooms</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h2>Why Choose The Grandview?</h2>", unsafe_allow_html=True)
    st.write("With unparalleled service, breathtaking views, and modern amenities, your stay with us will be an unforgettable experience. We pride ourselves on exceptional hospitality and a tranquil environment.")

elif page == "Rooms & Suites":
    st.markdown("<h2>Our Luxurious Accommodations</h2>", unsafe_allow_html=True)
    st.write("Each room and suite is designed with your comfort in mind, blending elegant decor with modern conveniences.")

    col1, col2, col3 = st.columns(3) # Create three columns for the room cards

    # Room Card 1: Standard Double (using standard.jpg)
    with col1:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(STANDARD_ROOM_IMAGE_URL, caption="A cozy retreat for two.", use_column_width="always")
        st.markdown("<h3>Standard Double</h3>", unsafe_allow_html=True)
        st.markdown("<p>Comfortable and elegantly designed for a restful stay, featuring a plush queen-sized bed and city views.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Room Card 2: Deluxe Suite
    with col2:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(DELUXE_ROOM_IMAGE_URL, caption="Indulge in extra space and luxury.", use_column_width="always")
        st.markdown("<h3>Deluxe Suite</h3>", unsafe_allow_html=True)
        st.markdown("<p>Spacious living area, premium views, and exclusive services for an elevated experience. Perfect for extended stays.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Room Card 3: Family Room
    with col3:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(FAMILY_ROOM_IMAGE_URL, caption="Comfort for the whole family.", use_column_width="always")
        st.markdown("<h3>Family Room</h3>", unsafe_allow_html=True)
        st.markdown("<p>Ideal for families, offering extra space, multiple beds, and amenities tailored for a comfortable group stay.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Ready to Book Your Stay?", use_container_width=True):
        st.query_params["page"] = "Book a Room" # Navigate to the booking page via URL param

elif page == "Book a Room":
    st.markdown("<h2>Secure Your Reservation 📝</h2>", unsafe_allow_html=True)
    st.info("Your booking form will go here.")
    # Add your st.form booking logic here

elif page == "Amenities":
    st.markdown("<h2>Luxury Amenities ✨</h2>", unsafe_allow_html=True)
    st.write("We offer a range of premium amenities to ensure your stay is comfortable.")
    st.markdown(
        """
        <ul class="amenities-list">
            <li><i class="icon">★</i> Complimentary High-Speed Wi-Fi</li>
            <li><i class="icon">★</i> Rooftop Pool & Lounge</li>
            <li><i class="icon">★</i> Fine Dining Restaurant</li>
            <li><i class="icon">★</i> 24/7 Concierge Service</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    
elif page == "Contact Us":
    st.markdown("<h2>Contact The Grandview Hotel 📞</h2>", unsafe_allow_html=True)
    st.info("Your contact information and form will go here.")

# --- Custom Footer ---
st.markdown(
    """
    <div class="custom-footer">
        <p>&copy; 2025 The Grandview Hotel. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
