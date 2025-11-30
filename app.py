# -*- coding: utf-8 -*-
# The encoding fix remains for the '★' character.
import streamlit as st

# --- Configuration & Styling ---
st.set_page_config(
    page_title="The Grandview Hotel",
    layout="wide",
    initial_sidebar_state="auto" # Changed to 'auto' to show the sidebar
)

# Custom CSS for theme colors, buttons, and layout (same as before)
# The full CSS block (st.markdown(..., unsafe_allow_html=True)) goes here.
# (I'll omit the long CSS block here for brevity, but assume it's included.)
st.markdown(
    """
    <style>
    /* Global Styles */
    .stApp {
        background-color: #fff;
        color: #333;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }

    /* --- Header (Removed standard header as sidebar handles nav now) --- */
    
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
        color: white; 
    }
    .hero-content p {
        font-size: 1.2em;
        color: white; 
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


# --- 1. Functional Navigation (NEW FEATURE) ---
st.sidebar.title("The Grandview Hotel 🏨")

# Use st.sidebar.radio for easy page navigation
# This stores the user's current selection in the `page` variable
page = st.sidebar.radio(
    "Go to",
    ["Home", "Rooms & Suites", "Book a Room", "Amenities", "Contact Us"]
)

st.sidebar.markdown("---")
st.sidebar.info("Learn how to deploy this simple website on Streamlit Cloud and GitHub!")

# --- 2. Page Rendering Logic ---
if page == "Home":
    st.markdown('<a id="home"></a>', unsafe_allow_html=True)
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="hero-content">
            <h2>Your Luxurious Escape Awaits</h2>
            <p>Experience world-class hospitality in the heart of the city.</p>
            <a href="?page=Rooms & Suites" class="btn-primary">Explore Rooms</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Simple call-to-action on the Home page
    st.subheader("Why Choose The Grandview?")
    st.write("With unparalleled service and breathtaking views, your stay with us will be unforgettable.")
    st.image('https://via.placeholder.com/800x200?text=Grandview+Hotel+Feature+Banner')


elif page == "Rooms & Suites":
    st.markdown('<a id="rooms"></a>', unsafe_allow_html=True)
    st.header("Our Accommodations")
    st.write("Select a room type to see details and book.")

    col1, col2, col3 = st.columns(3)
    
    # Room Cards (with simple Python content, not just raw HTML)
    with col1:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x200?text=Standard+Room")
        st.subheader("Standard Double")
        st.write("Comfortable and elegantly designed for a restful stay.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x200?text=Deluxe+Suite")
        st.subheader("Deluxe Suite")
        st.write("Spacious living area, premium views, and exclusive services.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x200?text=Family+Room")
        st.subheader("Family Room")
        st.write("Perfect for families, offering extra space and amenities.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.button("Click here to Book Now", key="book_from_rooms") # Action that can be tied to a function


# --- 3. Interactive Room Booker (NEW FEATURE) ---
elif page == "Book a Room":
    st.markdown('<a id="book"></a>', unsafe_allow_html=True)
    st.header("Secure Your Reservation 📝")

    # Booking Form using st.form
    with st.form(key='booking_form'):
        st.subheader("Reservation Details")

        room_type = st.selectbox(
            "Select Room Type:",
            ("Standard Double - $150/night", "Deluxe Suite - $300/night", "Family Room - $220/night")
        )

        num_nights = st.slider("Number of Nights:", min_value=1, max_value=14, value=3)
        check_in_date = st.date_input("Check-in Date:")
        
        # User details
        st.subheader("Guest Information")
        name = st.text_input("Full Name:")
        email = st.text_input("Email:")
        special_requests = st.text_area("Special Requests:")
        
        submit_button = st.form_submit_button(label='Confirm Booking')

    if submit_button:
        # Simple calculation and confirmation message
        price_map = {"Standard Double - $150/night": 150, "Deluxe Suite - $300/night": 300, "Family Room - $220/night": 220}
        base_price = price_map[room_type]
        total_cost = base_price * num_nights

        st.success(f"🎉 Thank you, **{name}**! Your reservation is confirmed.")
        st.info(f"""
        **Room:** {room_type}
        **Check-in:** {check_in_date}
        **Nights:** {num_nights}
        **Estimated Total Cost:** ${total_cost}
        A confirmation email has been sent to **{email}**.
        """)


elif page == "Amenities":
    st.markdown('<a id="amenities"></a>', unsafe_allow_html=True)
    st.header("Luxury Amenities ✨")
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
    st.markdown("---")
    st.subheader("View Our Location")
    # Interactive Map (NEW FEATURE)
    st.map(
        data=st.session_state.get('hotel_location', {'lat': [34.0522], 'lon': [-118.2437]}), # Default to a generic location (e.g., LA)
        zoom=10
    )


elif page == "Contact Us":
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.header("Contact Us 📞")
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
    st.markdown("---")
    # Simple form for Contact Us (NEW FEATURE)
    with st.expander("Send us a Quick Message"):
        contact_name = st.text_input("Your Name")
        contact_email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        if st.button("Submit Message"):
            st.success(f"Thank you, {contact_name}! We have received your message and will respond to {contact_email} shortly.")


# --- Footer ---
st.markdown(
    """
    <div class="footer-bar">
        <p>&copy; 2025 The Grandview Hotel. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
