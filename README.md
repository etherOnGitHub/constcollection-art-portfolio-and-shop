# ConstCollection Art Portfolio and Shop

A portfolio and e-commerce MVP for artists to showcase their work and sell pieces online. Built with Django, featuring a gallery page and integrated payment system.

---

## Table of Contents
- [Project Overview](#project-overview)
- [MVP Features](#mvp-features)
- [UX & Design](#ux--design)
- [Gallery Page](#gallery-page)
- [Payment System](#payment-system)
- [Features Left to Implement](#features-left-to-implement)
- [User Stories & Kanban Board](#user-stories--kanban-board)
- [Database & ERD Diagram](#database--erd-diagram)
- [Technologies Used](#technologies-used)
- [Testing & Validation](#testing--validation)
- [Deployment](#deployment)
- [Credits & Acknowledgements](#credits--acknowledgements)

---

## Project Overview
ConstCollection is a Django web application for artists to display their artwork and offer pieces for sale. The MVP includes a gallery page for browsing art and a payment system for secure purchases.

## MVP Features
- 🖼️ Gallery Page: Browse and view artwork with details and images.
- 💳 Payment System: Purchase art securely through integrated payment processing.

## UX & Design
- Clean, modern layout focused on artwork presentation
- Responsive design for desktop and mobile
- Simple navigation between gallery and shop

## Gallery Page
- Grid or card-based display of artworks
- Artwork details: title, artist, medium, price, image
- Click to view larger image and more info

## Payment System
- Add artwork to cart
- Checkout with secure payment (e.g., Stripe integration)
- Order confirmation and receipt

## Features Left to Implement
- User authentication and profiles
- Order history and tracking
- Admin dashboard for managing artworks and orders
- Wishlist/favorites
- Reviews and ratings

## User Stories & Kanban Board

### Must-have

1. **Gallery Browsing & Purchase**
   - As a user, I want to browse a gallery of artworks and click on any image to view detailed information so that I can explore and potentially purchase pieces I like.
   - Acceptance Criteria:
     - Gallery displays artworks in a responsive grid layout.
     - Clicking an artwork opens a detail view with full metadata.
     - Each artwork has a clear “Buy” or “Add to cart” option.
   - Tasks:
     - Create gallery layout using responsive CSS.
     - Implement artwork detail view with title, year, technique, dimensions, story, and price.
     - Add purchase button to each artwork detail view.

2. **Admin Artwork Management**
   - As a Site Admin, I want to create, read, update, and delete artwork entries so that I can fully manage the gallery content and keep the shop up to date.
   - Acceptance Criteria:
     - Admin can add new artworks with all required fields (title, image, dimensions, price etc).
     - Admin can view a list of all artworks in the admin panel.
     - Admin can edit existing artwork details.
     - Admin can delete artworks from the system.
     - Changes are reflected immediately on the public gallery view.
   - Tasks:
     - Create Artwork model with relevant fields.
     - Register Artwork model in Django admin.
     - Customize admin form for better usability.
     - Test all CRUD operations in the admin interface.

3. **Contact Form**
   - As a user, I want to contact the artist directly so that I can ask questions or share feedback.
   - Acceptance Criteria:
     - Contact page includes a form with name, email, and message.
     - Form includes validation and confirmation message.
   - Tasks:
     - Create contact form using Django forms.
     - Add email backend or store messages in database.
     - Display success message after submission.

4. **User Registration & Login**
   - As a new user, I want to register and log in so that I can save my purchases and access member-only features.
   - Acceptance Criteria:
     - Users can register with email and password.
     - Users can log in and log out securely.
   - Tasks:
     - Create registration and login forms.
     - Implement Django authentication.

5. **Responsive Design**
   - As a user, I want the site to work well on all devices so that I can browse and shop from anywhere.
   - Acceptance Criteria:
     - Layout adapts to desktop, tablet, and mobile screens.
     - Buttons and text are readable and accessible.
   - Tasks:
     - Apply responsive CSS and media queries.
     - Test layout on multiple screen sizes.

### Should-have

6. **Stripe Payment Integration**
   - As a registered user, I want to purchase an artwork securely using Stripe so that I can complete my order.
   - Acceptance Criteria:
     - Stripe Checkout is triggered from the artwork detail view.
     - Stripe test mode is used for development.
     - Confirmation message is shown after successful payment.
   - Tasks:
     - Set up Stripe API keys (test mode).
     - Create checkout session using Stripe SDK.
     - Handle success and cancel URLs.
     - Display confirmation message after purchase.

7. **Social Media Links**
   - As a site visitor, I want to see links to the artist’s social media profiles so that I can follow and stay updated on new artworks and events.
   - Acceptance Criteria:
     - Icons for Facebook, Instagram, and YouTube are visible in the footer or artist profile.
     - Links open in a new tab.
     - Icons are styled to match the site’s branding.
   - Tasks:
     - Decide where the social media links will appear (e.g. footer, header, artist profile).
     - Add static HTML links to Facebook, Instagram, and YouTube.
     - Insert icons for each platform (SVG or image).
     - Style the icons to match the site’s branding and layout.
     - Ensure links open in a new tab and include accessibility labels.
     - Test the layout and behavior across different devices.

### Could-have

8. **About Page**
   - As a site visitor, I want to learn more about the artist so that I can connect with their work.
   - Acceptance Criteria:
     - About page includes artist bio, philosophy, and process.
     - Page is styled consistently with the rest of the site.
   - Tasks:
     - Write and format content for About page.
     - Add navigation link to About page.

9. **Gallery Pagination**
   - As a site visitor, I want the gallery to load artworks in smaller sections so that the page stays fast and easy to browse.
   - Acceptance Criteria:
     - Gallery view displays a limited number of artworks per page (e.g. 6 or 9).
     - Pagination controls (e.g. "Next", "Previous", page numbers) are visible and styled consistently.
     - Pagination is responsive and works on mobile devices.
   - Tasks:
     - Add pagination logic to `gallery/views.py`.
     - Update gallery template to include pagination controls.
     - Test navigation between pages.

10. **Order History**
    - As a logged in User, I want to see a list of my past orders so that I can keep track of what I’ve purchased and when.
    - Acceptance Criteria:
      - Logged-in users can access a "My Orders" page.
      - Each order shows key details: artwork name, date, quantity, total price, and status.
      - Orders are listed in reverse chronological order.
      - Admin can view all user orders in the backend.
    - Tasks:
      - Create Order model linked to User and Artwork.
      - Build view and template for displaying order history.
      - Add navigation link to "My Orders" in user dashboard.
      - Test with multiple users and orders.

## Kanban board

![Initial Project Board](<assets/readme_docs/images/Screenshot 2025-10-15 at 16.05.05.png>)

## Database & ERD Diagram
- MVP ERD: User, Artwork, Order models and relationships
![MVP ERD WITH PAYMENT](<assets/readme_docs/images/Screenshot 2025-10-15 at 16.04.28.png>)


## Technologies Used
- Backend: Python 3.12, Django 5+
- Database: PostgreSQL
- Frontend: HTML5, CSS3, JavaScript
- Payment: Stripe API
- Deployment: Heroku, Cloudinary, WhiteNoise

## Testing & Validation
- Manual testing of gallery and payment flows
- Automated Django tests for models and views

## Deployment
- Heroku for hosting
- Cloudinary for image storage
- Environment variables for secrets and API keys

## Credits & Acknowledgements
- Art content by ConstCollection users
- Libraries: Django, Stripe, Cloudinary
- Icons: FontAwesome
- Special thanks to the Django and open-source community