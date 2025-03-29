<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vihari Farms</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* All existing styles remain exactly the same */
        .hero {
            position: relative;
            height: 100vh;
            overflow: hidden;
        }

        .hero-slider {
            display: flex;
            width: 200%;
            height: 100%;
            transition: transform 0.5s ease;
        }

        .hero-slide {
            width: 50%;
            height: 100vh;
            background-size: cover;
            background-position: center;
        }

        .logo-slider {
            display: flex;
            width: 200%;
            transition: transform 0.5s ease;
        }

        .logo-slide {
            width: 50%;
            display: flex;
            align-items: center;
        }

        .logo-slide img {
            max-height: 50px;
            margin-right: 10px;
        }

        .hero-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 10;
        }

        .cta-btn {
            display: inline-block;
            padding: 12px 30px;
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .cta-btn:hover {
            background: linear-gradient(45deg, #45a049, #4CAF50);
            transform: scale(1.05);
            box-shadow: 0 6px 8px rgba(0,0,0,0.2);
        }

        /* Social media icons styles */
        .social-icons {
            position: fixed;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 15px;
            z-index: 1000;
        }

        .social-icons a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            color: white;
            transition: transform 0.3s ease;
            text-decoration: none;
        }

        .social-icons a:hover {
            transform: scale(1.1);
        }

        .facebook { background: #3b5998; }
        .instagram { background: #e4405f; }
        .youtube { background: #ff0000; }
        .whatsapp { background: #25D366; }

        /* Nearby attractions styles */
        .nearby-places {
            padding: 50px 20px;
            background-color: #fff;
        }

        .nearby-places h2 {
            text-align: center;
            margin-bottom: 40px;
            color: #333;
        }

        .places-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .place-card {
            background: #fff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .place-card:hover {
            transform: translateY(-5px);
        }

        .place-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .place-card h3 {
            padding: 15px;
            margin: 0;
            color: #333;
        }

        .place-card p {
            padding: 0 15px 15px;
            color: #666;
        }

        /* New Additional Sections Styles */
        .section-cards {
            padding: 50px 20px;
            background-color: #fff;
        }

        .section-cards h2 {
            text-align: center;
            margin-bottom: 40px;
            color: #333;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .info-card {
            background: #fff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .info-card:hover {
            transform: translateY(-5px);
        }

        .info-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .info-card h3 {
            padding: 15px;
            margin: 0;
            color: #333;
        }

        .info-card p {
            padding: 0 15px 15px;
            color: #666;
        }

        .contact-section {
            padding: 50px 20px;
            background-color: #f9f9f9;
        }

        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        .contact-form input {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .contact-form button {
            width: 100%;
            padding: 12px;
            background: #3a4a29;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .contact-form button:hover {
            background: #4c6237;
        }
    </style>
</head>
<body>
    <!-- All existing header, social icons, hero section and nearby places section remain exactly the same -->
    <header>
        <div class="logo">
            <div class="logo-slider" id="logoSlider">
                <div class="logo-slide">
                    <h1>Vihari Farms</h1>
                </div>
                <div class="logo-slide">
                    <img src="images/vihari_logo.jpg" alt="Vihari Farms Logo">
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="experience.html">Farm Experience</a></li>
                    <li><a href="events.html">Events</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
        </nav>
    </header>

    <div class="social-icons">
        <a href="https://www.facebook.com/p/Vihari-Natures-Nest-Farm-61562907878911/" class="facebook" target="_blank">
            <i class="fab fa-facebook-f"></i>
        </a>
        <a href="https://www.instagram.com/viharinaturesnest/" class="instagram" target="_blank">
            <i class="fab fa-instagram"></i>
        </a>
        <a href="https://youtube.com/YOUR_YOUTUBE_CHANNEL" class="youtube" target="_blank">
            <i class="fab fa-youtube"></i>
        </a>
        <a href="https://wa.me/917569529960" class="whatsapp" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    </div>

    <section class="hero">
        <div class="hero-slider" id="heroSlider">
            <div class="hero-slide" style="background-image: url('images/main.jpg')"></div>
            <div class="hero-slide" style="background-image: url('images/main_2.jpg')"></div>
        </div>
        <div class="hero-content">
            <a href="https://wa.me/917569529960" class="cta-btn">Book Your Stay</a>
        </div>
    </section>

    <section class="nearby-places">
        <h2>Nearby Attractions</h2>
        <div class="places-grid">
            <div class="place-card">
                <img src="images/swarnagiri.jpg" alt="Swarnagiri Temple">
                <h3>Swarnagiri Temple</h3>
                <p>Distance: 15 km</p>
            </div>
            <div class="place-card">
                <img src="images/yadadri.jpg" alt="Yadadri Temple">
                <h3>Yadadri Temple</h3>
                <p>Distance: 30 km</p>
            </div>
            <div class="place-card">
                <img src="images/ananthagiri2.jpg" alt="Ananthagiri Hills">
                <h3>Ananthagiri Hills</h3>
                <p>Distance: 25 km</p>
            </div>
        </div>
    </section>

    <!-- New Farm Experience Section -->
    <section class="section-cards">
        <h2>Farm Experience</h2>
        <div class="cards-grid">
            <div class="info-card">
                <img src="images/download (1).jpg" alt="Swimming Pool">
                <h3>Swimming Pool</h3>
                <p>Take a refreshing dip in our pristine swimming pool surrounded by nature.</p>
            </div>
            <div class="info-card">
                <img src="images/camp_fire.jpg" alt="Campfire">
                <h3>Campfire</h3>
                <p>Enjoy evening gatherings around a cozy campfire under the stars.</p>
            </div>
            <div class="info-card">
                <img src="images/barbequie.jpeg" alt="BBQ">
                <h3>Barbecue Station</h3>
                <p>Perfect spot for grilling and outdoor dining experiences.</p>
            </div>
            <div class="info-card">
                <img src="images/cricket-practice-nets.jpg" alt="Cricket Nets">
                <h3>Cricket Nets</h3>
                <p>Professional cricket nets for sports enthusiasts.</p>
            </div>
            <div class="info-card">
                <img src="images/kitchen.jpg" alt="Open Kitchen">
                <h3>Open Kitchen</h3>
                <p>Fully equipped open kitchen for a complete cooking experience.</p>
            </div>
        </div>
    </section>

    <!-- New About Us Section -->
    <section class="section-cards" style="background-color: #f9f9f9;">
        <h2>About Us</h2>
        <div class="cards-grid">
            <div class="info-card">
                <img src="images/main.jpg" alt="Our Story">
                <h3>Our Story</h3>
                <p>Established in 2020, Vihari Farms offers a peaceful retreat amidst nature, perfect for families and friends seeking a break from city life.</p>
            </div>
            <div class="info-card">
                <img src="images/main_2.jpg" alt="Our Mission">
                <h3>Our Mission</h3>
                <p>We strive to provide an authentic farm experience while ensuring comfort and modern amenities for our guests.</p>
            </div>
            <div class="info-card">
                <img src="farmhouse.jpg" alt="Location">
                <h3>Location</h3>
                <p>Conveniently located near major attractions while maintaining the serenity of a countryside retreat.</p>
            </div>
        </div>
    </section>

    <!-- New Contact Section -->
    <section class="contact-section">
        <h2>Contact Us</h2>
        <div class="contact-form">
            <form id="contactForm" onsubmit="sendEmail(); return false;">
                <input type="text" id="name" placeholder="Your Name" required>
                <input type="tel" id="phone" placeholder="Your Mobile Number" pattern="[0-9]{10}" required>
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Existing script section -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const heroSlider = document.getElementById('heroSlider');
            let heroCurrentSlide = 0;
            const heroSlides = heroSlider.querySelectorAll('.hero-slide');
            const heroTotalSlides = heroSlides.length;

            function nextHeroSlide() {
                heroCurrentSlide = (heroCurrentSlide + 1) % heroTotalSlides;
                heroSlider.style.transform = `translateX(-${heroCurrentSlide * 50}%)`;
            }

            const logoSlider = document.getElementById('logoSlider');
            let logoCurrentSlide = 0;
            const logoSlides = logoSlider.querySelectorAll('.logo-slide');
            const logoTotalSlides = logoSlides.length;

            function nextLogoSlide() {
                logoCurrentSlide = (logoCurrentSlide + 1) % logoTotalSlides;
                logoSlider.style.transform = `translateX(-${logoCurrentSlide * 50}%)`;
            }

            const titles = [
                'Vihari Farms', 
                'Farmhouse Retreat',                'Peaceful Getaway'
            ];
            let currentTitleIndex = 0;

            function changeTitleAnimation() {
                document.title = titles[currentTitleIndex];
                currentTitleIndex = (currentTitleIndex + 1) % titles.length;
            }

            document.title = 'Vihari Farms';

            setInterval(nextHeroSlide, 3000);
            setInterval(nextLogoSlide, 2000);
            setInterval(changeTitleAnimation, 3000);
        });
    </script>

    <footer>
        © 2024 Farmhouse Escape. All rights reserved.
    </footer>
</body>
</html>

