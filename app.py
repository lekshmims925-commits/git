
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np # For the map data

# --- Configuration & Page Setup ---
st.set_page_config(
    page_title="The Grandview Hotel",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Embedded CSS for Enhanced Styling (Copied from the previous response) ---
# This makes your Streamlit app look like the styled HTML page.
st.markdown(
    """
    <style>
    /* Global Reset and Setup */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f8f8f8; /* Very light gray background for depth */
    }

    .container {
        width: 90%; /* Slightly wider container for better screen utilization */
        max-width: 1200px; /* Max width constraint */
        margin: auto;
        overflow: hidden;
    }

    /* --- Streamlit Specific Overrides --- */
    /* Remove default Streamlit header/footer/sidebar styling if needed */
    .stApp > header { /* Hides Streamlit's default header */
        display: none;
    }
    
    /* Make the Streamlit sidebar match our theme */
    .st-emotion-cache-vk3wpn { /* This class might change with Streamlit updates, use judiciously */
        background-color: #004c4c; /* Dark Teal for sidebar */
        color: white;
    }
    .st-emotion-cache-vk3wpn .stButton > button { /* Sidebar button styling */
        background-color: #ffcc00;
        color: #004c4c;
    }
    .st-emotion-cache-vk3wpn .stRadio > label { /* Sidebar radio options */
        color: white;
        font-size: 1.1em;
        padding: 5px 0;
    }
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] { /* Adjust spacing for radio buttons */
        padding-top: 5px;
        padding-bottom: 5px;
    }
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:first-child { /* Radio circle color */
        border-color: #ffcc00 !important;
    }
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:first-child:hover { /* Radio circle hover color */
        border-color: #e6b800 !important;
    }
    .st-emotion-cache-vk3wpn .stRadio [data-baseweb="radio"] span:last-child {
        color: white !important; /* Ensure text is white */
    }
    
    .st-emotion-cache-vk3wpn .stMarkdown p, .st-emotion-cache-vk3wpn .stMarkdown h1, .st-emotion-cache-vk3wpn .stMarkdown h2, .st-emotion-cache-vk3wpn .stMarkdown h3 {
        color: white !important;
    }
    .st-emotion-cache-vk3wpn .stAlert {
        background-color: #1a6f6f !important; /* Slightly lighter teal for alerts */
        color: white !important;
    }
    .st-emotion-cache-vk3wpn .stAlert a {
        color: #ffcc00 !important;
    }


    /* --- Custom Styles for Page Content --- */
    /* Note: 'header' and 'nav' HTML elements are no longer used directly in Streamlit's main content area.
             Streamlit's sidebar handles navigation. */

    /* Button Styling (Reusable) */
    .btn-book { /* This specific class might be used in embedded markdown if you add a 'book now' link */
        background: #ffcc00;
        color: #004c4c !important;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        transition: background 0.3s, transform 0.2s;
        text-decoration: none; /* Ensure no underline */
    }

    .btn-book:hover {
        background: #e6b800;
        transform: translateY(-2px);
    }

    .btn-primary { /* For the hero section button */
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
    }

    .btn-primary:hover {
        background: #e6b800;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    /* --- Hero Section --- */
    .hero-section {
        /* UPDATED: Directly put the image URL here */
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('https://images.unsplash.com/photo-1542314831-068cd1dbf3ce?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80') no-repeat center center/cover;
        height: 70vh;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        text-align: center;
        border-radius: 12px; /* Softened edges for the hero block */
        margin-bottom: 40px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); /* Added shadow for lift */
    }

    .hero-content {
        background: rgba(0, 0, 0, 0.6);
        padding: 40px 60px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
    }

    .hero-content h2 {
        font-size: 3.5em;
        margin-bottom: 15px;
        font-weight: 700;
        color: white; /* Ensure text is white */
    }

    .hero-content p {
        font-size: 1.4em;
        font-weight: 300;
        color: white; /* Ensure text is white */
    }

    /* --- General Section Styling --- */
    section {
        padding: 80px 0;
        text-align: center;
    }

    h2 {
        font-size: 3em;
        color: #004c4c;
        margin-bottom: 50px;
        font-weight: 600;
    }

    /* --- Rooms Section --- */
    .section-rooms {
        background: #ffffff;
    }

    .room-grid { /* This class is now implicitly handled by st.columns */
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
    }

    .room-card {
        background: #ffffff;
        border: none;
        padding: 0;
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        width: 100%; /* Important for st.columns - each column is 100% of its allocated space */
        overflow: hidden;
        transition: transform 0.3s, box-shadow 0.3s;
        margin-bottom: 30px; /* Space between cards in columns */
    }

    .room-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.25);
    }

    /* Note: st.image generates its own img tag, so direct styling is minimal here */
    .room-card img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 10px 10px 0 0;
        margin-bottom: 15px;
    }

    .room-card h3 {
        padding: 0 20px;
        font-size: 1.5em;
        color: #004c4c;
    }

    .room-card p {
        padding: 0 20px 20px 20px;
    }

    /* --- Amenities Section --- */
    .section-amenities {
        background: #e6f7f7;
    }

    .amenities-list {
        list-style: none;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding-top: 20px;
    }

    .amenities-list li {
        background: #ffffff;
        color: #004c4c;
        padding: 18px 30px;
        margin: 12px;
        border-radius: 30px;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: background 0.3s;
    }

    .amenities-list li:hover {
        background: #ffcc00;
        color: #333;
    }

    .icon {
        margin-right: 10px;
        color: #ffcc00;
        font-size: 1.4em;
        line-height: 1;
    }

    /* --- Contact Section --- */
    .section-contact {
        padding-bottom: 80px;
    }
    .section-contact p {
        font-size: 1.2em;
        margin-bottom: 15px;
    }

    .section-contact a {
        color: #ffcc00;
        text-decoration: underline;
        font-weight: bold;
        transition: color 0.3s;
    }
    .section-contact a:hover {
        color: #e6b800;
    }

    /* --- Footer --- */
    .footer-bar {
        background: #1c1c1c;
        color: #ccc;
        padding: 30px 0;
        text-align: center;
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Functional Navigation (Streamlit Sidebar) ---
# This replaces your old HTML header navigation.
st.sidebar.title("The Grandview Hotel 🏨")
st.sidebar.markdown("---") # Separator

page = st.sidebar.radio(
    "Explore our hotel:",
    ["Home", "Rooms & Suites", "Book a Room", "Amenities", "Contact Us"]
)

st.sidebar.markdown("---")
st.sidebar.info("Experience luxury with seamless web deployment!")

# --- Page Rendering Logic ---

if page == "Home":
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="hero-content">
            <h2>Your Luxurious Escape Awaits</h2>
            <p>Experience world-class hospitality in the heart of the city.</p>
            <a href="?page=Rooms+%26+Suites" class="btn-primary">Explore Rooms</a> 
            </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<h2>Why Choose The Grandview?</h2>", unsafe_allow_html=True)
    st.write("With unparalleled service, breathtaking views, and modern amenities, your stay with us will be an unforgettable experience. We pride ourselves on exceptional hospitality and a tranquil environment.")
    
    # Placeholder for a feature banner
    st.image('https://images.unsplash.com/photo-1571896349882-378893122c67?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80', 
             caption="Experience our grand lobby", use_column_width=True)


elif page == "Rooms & Suites":
    st.markdown("<h2>Our Luxurious Accommodations</h2>", unsafe_allow_html=True)
    st.write("Each room and suite is designed with your comfort in mind, blending elegant decor with modern conveniences.")

    col1, col2, col3 = st.columns(3) # Create three columns for the room cards

    with col1:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1560003058-294025f0e9d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80", 
                 caption="A cozy retreat for two.", use_column_width=True)
        st.subheader("Standard Double")
        st.write("Comfortable and elegantly designed for a restful stay, featuring a plush queen-sized bed and city views.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80", 
                 caption="Indulge in extra space and luxury.", use_column_width=True)
        st.subheader("Deluxe Suite")
        st.write("Spacious living area, premium views, and exclusive services for an elevated experience. Perfect for extended stays.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1544078864-77e7709565ec?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80", 
                 caption="Comfort for the whole family.", use_column_width=True)
        st.subheader("Family Room")
        st.write("Ideal for families, offering extra space, multiple beds, and amenities tailored for a comfortable group stay.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) # Add some space
    if st.button("Ready to Book Your Stay?"):
        st.query_params["page"] = "Book a Room" # Navigate to the booking page

elif page == "Book a Room":
    st.markdown("<h2>Secure Your Reservation 📝</h2>", unsafe_allow_html=True)

    with st.form(key='booking_form', clear_on_submit=False): # Set clear_on_submit to False for testing
        st.subheader("Reservation Details")

        room_options = {
            "Standard Double": 150,
            "Deluxe Suite": 300,
            "Family Room": 220
        }
        selected_room_name = st.selectbox(
            "Select Room Type:",
            list(room_options.keys())
        )
        base_price = room_options[selected_room_name]
        st.write(f"Price: ${base_price}/night")

        num_guests = st.number_input("Number of Guests:", min_value=1, max_value=6, value=2)
        num_nights = st.slider("Number of Nights:", min_value=1, max_value=14, value=3)
        check_in_date = st.date_input("Check-in Date:")
        
        st.subheader("Guest Information")
        name = st.text_input("Full Name:")
        email = st.text_input("Email:")
        phone = st.text_input("Phone Number:")
        special_requests = st.text_area("Special Requests:")
        
        submit_button = st.form_submit_button(label='Confirm Booking')

    if submit_button:
        if name and email and phone: # Basic validation
            total_cost = base_price * num_nights

            st.success(f"🎉 Thank you, **{name}**! Your reservation is confirmed.")
            st.info(f"""
            **Room:** {selected_room_name}
            **Guests:** {num_guests}
            **Check-in:** {check_in_date}
            **Nights:** {num_nights}
            **Estimated Total Cost:** **${total_cost}**
            A detailed confirmation and payment link has been sent to **{email}**.
            """)
            st.balloons() # Fun animation!
        else:
            st.warning("Please fill in all required guest information (Name, Email, Phone).")


elif page == "Amenities":
    st.markdown("<h2>Luxury Amenities ✨</h2>", unsafe_allow_html=True)
    st.write("We offer a range of premium amenities to ensure your stay is as comfortable and enjoyable as possible.")
    
    st.markdown(
        """
        <div class="amenities-list">
            <li><i class="icon">★</i> Complimentary High-Speed Wi-Fi</li>
            <li><i class="icon">★</i> Stunning Rooftop Pool & Lounge</li>
            <li><i class="icon">★</i> Award-Winning Fine Dining Restaurant</li>
            <li><i class="icon">★</i> Dedicated 24/7 Concierge Service</li>
            <li><i class="icon">★</i> State-of-the-Art Fitness Center</li>
            <li><i class="icon">★</i> Luxurious Spa & Wellness Treatments</li>
            <li><i class="icon">★</i> Valet Parking & Airport Shuttle</li>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.subheader("Find Us on the Map")
    # Hotel Location (example: New York City)
    hotel_location = pd.DataFrame(
        {'lat': [40.7580], 'lon': [-73.9855]} # Example: Times Square, NYC
    )
    st.map(hotel_location, zoom=12)


elif page == "Contact Us":
    st.markdown("<h2>Contact The Grandview Hotel 📞</h2>", unsafe_allow_html=True)
    st.write("We are here to assist you with any inquiries or special requests.")
    
    st.markdown(
        """
        <div class="section-contact">
            <p>Our friendly staff is available 24/7.</p>
            <p><strong>Email:</strong> <a href="mailto:info@grandviewhotel.com">info@grandviewhotel.com</a></p>
            <p><strong>Phone:</strong> (123) 456-7890</p>
            <p><strong>Address:</strong> 123 Grandview Avenue, Metropolis, GR 10001</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.subheader("Send Us a Message")
    with st.form(key='contact_form', clear_on_submit=True):
        contact_name = st.text_input("Your Name:")
        contact_email = st.text_input("Your Email:")
        subject = st.text_input("Subject:")
        message = st.text_area("Your Message:")
        
        contact_submit_button = st.form_submit_button(label="Send Message")

    if contact_submit_button:
        if contact_name and contact_email and message:
            st.success(f"Thank you, {contact_name}! Your message regarding '{subject}' has been sent.")
            st.info("We aim to respond to all inquiries within 24 hours.")
        else:
            st.warning("Please fill in your Name, Email, and Message to send your inquiry.")


# --- Footer ---
st.markdown(
    """
    <div class="footer-bar">
        <p>&copy; 2025 The Grandview Hotel. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
