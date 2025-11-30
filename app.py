# -*- coding: utf-8 -*-
# This line is CRUCIAL! It fixes the '★' Unicode error.
import streamlit as st

# --- Configuration ---
# Set the page title and layout
st.set_page_config(
    page_title="The Grandview Hotel",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Styling (Mimics style.css) ---
st.markdown(
    """
    <style>
    /* Global Styles */
    .stApp {
        background-color: #fff;
        color: #333;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }

    /* --- Header & Navigation --- */
    .header-bar {
        background: #004c4c; /* Dark Teal */
        color: #ffffff;
        padding: 15px 0;
        border-bottom: 3px solid #ffcc00; /* Gold accent */
        margin-bottom: 20px;
    }
    .header-content {
        width: 80%;
        margin: auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header-content h1 {
        font-size: 2em;
        margin: 0;
    }
    .nav-links {
        display: flex;
        gap: 20px;
    }
    .nav-links a {
        color: #ffffff;
        text-decoration: none;
        text-transform: uppercase;
        font-size: 14px;
        transition: color 0.3s;
    }
    .nav-links a:hover {
        color: #ffcc00;
    }

    /* BOOK NOW Button */
    .btn-book {
        background: #ffcc00;
        color: #004c4c !important;
        padding: 8px 15px;
        border-radius: 5px;
        font-weight: bold;
        text-decoration: none !important;
    }

    /* --- Hero Section --- */
    .hero-section {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://via.placeholder.com/1500x500?text=Hotel+Lobby+Image');
        background-size: cover;
        background-position: center;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 40px;
    }
    .hero-content h2 {
        font-size: 3em;
        margin-bottom: 10px;
        color: white; /* Force white text */
    }
    .hero-content p {
        font-size: 1.2em;
        color: white; /* Force white text */
    }
    
    /* Primary Button */
    .btn-primary {
        display: inline-block;
        background: #ffcc00;
        color: #004c4c !important;
        padding: 12px 25px;
        text-decoration: none;
        border-radius: 5px;
        margin-top: 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background 0.3s;
    }
    .btn-primary:hover {
        background: #e6b800;
    }
    
    /* --- Section Styling --- */
    section {
        padding: 40px 0;
        text-align: center;
    }
    
    h2 {
        font-size: 2.5em;
        color: #004c4c;
        margin-bottom: 40px;
    }
    
    /* --- Rooms Section --- */
    .room-card-container {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        padding: 20px;
    }
    .room-card {
        background: #ffffff;
        border: 1px solid #ddd;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 30%;
    }
    .room-card img {
        max-width: 100%;
        height: auto;
        border-radius: 4px;
        margin-bottom: 15px;
    }

    /* --- Amenities Section --- */
    .amenities-list {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding: 20px;
    }
    .amenities-list li {
        list-style: none;
        background: #ffffff;
        color: #004c4c;
        padding: 15px 25px;
        margin: 10px;
        border-radius: 50px;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    .icon {
        margin-right: 8px;
        color: #ffcc00;
        font-size: 1.2em;
    }

    /* --- Contact & Footer --- */
    .section-contact p {
        font-size: 1.1em;
        margin-bottom: 10px;
    }
    .footer-bar {
        background: #333;
        color: #ffffff;
        padding: 20px 0;
        text-align: center;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Content ---

# Header (Replicated with Markdown for HTML Structure)
st.markdown(
    f"""
    <div class="header-bar">
        <div class="header-content">
            <h1>The Grandview Hotel</h1>
            <div class="nav-links">
                <a href="#home">Home</a>
                <a href="#rooms">Rooms & Suites</a>
                <a href="#amenities">Amenities</a>
                <a href="#contact">Contact</a>
                <a href="#" class="btn-book">BOOK NOW</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="hero-content">
        <h2>Your Luxurious Escape Awaits</h2>
        <p>Experience world-class hospitality in the heart of the city.</p>
        <a href="#rooms" class="btn-primary">Explore Rooms</a>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)


# --- Rooms Section ---
st.markdown('<a id="rooms"></a>', unsafe_allow_html=True)
st.header("Our Accommodations")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="room-card">
            <img src="https://via.placeholder.com/300x200?text=Standard+Room" alt="Standard Room">
            <h3>Standard Double</h3>
            <p>Comfortable and elegantly designed for a restful stay.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="room-card">
            <img src="https://via.placeholder.com/300x200?text=Deluxe+Suite" alt="Deluxe Suite">
            <h3>Deluxe Suite</h3>
            <p>Spacious living area, premium views, and exclusive services.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="room-card">
            <img src="https://via.placeholder.com/300x200?text=Family+Room" alt="Family Room">
            <h3>Family Room</h3>
            <p>Perfect for families, offering extra space and amenities.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Amenities Section ---
st.markdown('<a id="amenities"></a>', unsafe_allow_html=True)
st.header("Luxury Amenities")

# Note: We use the UTF-8 character '★' here, which is now safe because of line 2.
st.markdown(
    """
    <div class="amenities-list">
        <li><i class="icon">★</i> Free Wi-Fi</li>
        <li><i class="icon">★</i> Rooftop Pool</li>
        <li><i class="icon">★</i> Fine Dining Restaurant</li>
        <li><i class="icon">★</i> 24/7 Concierge</li>
        <li><i class="icon">★</i> Fitness Center</li>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Contact Section ---
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("Contact Us")

st.markdown(
    """
    <div class="section-contact">
        <p>Ready to book? Have questions? Reach out to us!</p>
        <p>Email: <a href="mailto:info@grandview.com">info@grandview.com</a></p>
        <p>Phone: (555) 123-4567</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Footer ---
st.markdown(
    """
    <div class="footer-bar">
        <p>&copy; 2025 The Grandview Hotel. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
