from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>💰 PaiseKamao.in – 15 Best Ways to Earn Money Online in India</title>
<meta name="description" content="Earn money online from home in India. 15 proven ways including Freelancing, YouTube, Blogging, Affiliate Marketing and more.">
<meta name="keywords" content="earn money online india, work from home, freelancing india, youtube earn money, blogging income 2025">
<meta name="google-site-verification" content="TPjYlLn0L0W216UNfKt9sg2n9McE-NvepGERkWEtZVU" />
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1709475506645918" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Hind:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root { --gold: #f5c518; --gold2: #e8a900; --dark: #0a0a12; --card: #12121f; --accent: #00e5ff; --green: #00ff88; --text: #e8e8f0; --muted: #7a7a9a; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--dark); color: var(--text); font-family: 'Hind', sans-serif; overflow-x: hidden; }
  .hero { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem; background: radial-gradient(ellipse at 50% 0%, rgba(245,197,24,0.15) 0%, transparent 70%); }
  .badge { display: inline-block; background: rgba(245,197,24,0.15); border: 1px solid var(--gold); color: var(--gold); padding: 0.4rem 1.2rem; border-radius: 100px; font-size: 0.85rem; margin-bottom: 1.5rem; }
  h1 { font-family: 'Baloo 2', cursive; font-size: clamp(2.5rem, 7vw, 5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; }
  h1 span { color: var(--gold); }
  .hero p { font-size: 1.2rem; color: var(--muted); max-width: 600px; line-height: 1.7; margin-bottom: 2.5rem; }
  .stats-row { display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; }
  .stat .num { font-family: 'Baloo 2', cursive; font-size: 2rem; font-weight: 800; color: var(--gold); }
  .stat .label { font-size: 0.8rem; color: var(--muted); }
  .section { max-width: 1100px; margin: 0 auto; padding: 5rem 1.5rem; }
  .section-title { font-family: 'Baloo 2', cursive; font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 0.5rem; }
  .section-title span { color: var(--gold); }
  .section-sub { text-align: center; color: var(--muted); margin-bottom: 3rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 1.5rem; }
  .card { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 1.8rem; transition: transform 0.3s ease, border-color 0.3s ease; position: relative; overflow: hidden; }
  .card:hover { transform: translateY(-5px); border-color: rgba(245,197,24,0.3); }
  .card-icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
  .card-num { position: absolute; top: 1.2rem; right: 1.5rem; font-family: 'Baloo 2', cursive; font-size: 3rem; font-weight: 800; color: rgba(255,255,255,0.04); }
  .card h3 { font-family: 'Baloo 2', cursive; font-size: 1.3rem; font-weight: 700; margin-bottom: 0.6rem; color: #fff; }
  .card p { font-size: 0.92rem; color: var(--muted); line-height: 1.7; margin-bottom: 1rem; }
  .earn-tag { display: inline-block; background: rgba(0,255,136,0.1); border: 1px solid rgba(0,255,136,0.3); color: var(--green); font-size: 0.75rem; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 100px; }
  .diff-tag { display: inline-block; margin-left: 0.5rem; background: rgba(245,197,24,0.1); border: 1px solid rgba(245,197,24,0.3); color: var(--gold); font-size: 0.75rem; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 100px; }
  .steps { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 20px; padding: 3rem; margin-top: 4rem; }
  .steps h2 { font-family: 'Baloo 2', cursive; font-size: 1.8rem; font-weight: 800; margin-bottom: 2rem; text-align: center; }
  .step-list { display: flex; flex-direction: column; gap: 1.2rem; max-width: 700px; margin: 0 auto; }
  .step { display: flex; gap: 1.2rem; align-items: flex-start; }
  .step-num { width: 40px; height: 40px; min-width: 40px; background: linear-gradient(135deg, var(--gold), var(--gold2)); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Baloo 2', cursive; font-weight: 800; color: #000; }
  .step-content h4 { font-family: 'Baloo 2', cursive; font-weight: 700; margin-bottom: 0.2rem; }
  .step-content p { font-size: 0.9rem; color: var(--muted); }
  .ticker-wrap { background: var(--gold); overflow: hidden; padding: 0.7rem 0; white-space: nowrap; }
  .ticker { display: inline-block; animation: ticker 25s linear infinite; }
  .ticker span { color: #000; font-weight: 700; font-family: 'Baloo 2', cursive; margin: 0 2rem; font-size: 0.95rem; }
  footer { text-align: center; padding: 3rem 1.5rem; border-top: 1px solid rgba(255,255,255,0.07); color: var(--muted); }
  .articles-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
  .article-card { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 1.5rem; text-decoration: none; color: var(--text); display: block; transition: transform 0.3s, border-color 0.3s; }
  .article-card:hover { transform: translateY(-4px); border-color: rgba(245,197,24,0.4); }
  .article-card h3 { font-family: 'Baloo 2', cursive; font-size: 1.1rem; color: var(--gold); margin-bottom: 0.5rem; }
  .article-card p { font-size: 0.88rem; color: var(--muted); line-height: 1.6; }
  @keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
</style>
</head>
<body>
<div class="ticker-wrap">
  <div class="ticker">
    <span>💰 Earn 50,000/month with Freelancing</span><span>📹 Make Lakhs on YouTube</span><span>✍️ Passive Income from Blogging</span><span>🛒 Affiliate Marketing</span><span>📱 Earn by Building Apps</span><span>🎓 Online Teaching</span><span>💰 Earn 50,000/month with Freelancing</span><span>📹 Make Lakhs on YouTube</span><span>✍️ Passive Income from Blogging</span><span>🛒 Affiliate Marketing</span><span>📱 Earn by Building Apps</span><span>🎓 Online Teaching</span>
  </div>
</div>
<section class="hero">
  <div class="badge">🇮🇳 Made for Indians</div>
  <h1>Earn Money <span>Online</span><br>From Home!</h1>
  <p>15 proven ways to earn Rs.10,000 to Rs.1,00,000+ per month in 2025 — many with zero investment required.</p>
  <div class="stats-row">
    <div class="stat"><div class="num">50K+</div><div class="label">People Earning</div></div>
    <div class="stat"><div class="num">15</div><div class="label">Methods</div></div>
    <div class="stat"><div class="num">Rs.0</div><div class="label">Investment Needed</div></div>
    <div class="stat"><div class="num">24/7</div><div class="label">Passive Income</div></div>
  </div>
</section>
<section class="section">
  <div class="section-title">15 Ways to <span>Earn Online</span></div>
  <p class="section-sub">Earnings info and how to get started for each method</p>
  <div class="grid">
    <div class="card"><span class="card-num">01</span><span class="card-icon">💻</span><h3>Freelancing</h3><p>Sell your skills on Upwork, Fiverr, Freelancer. Web design, writing, video editing, coding.</p><span class="earn-tag">Rs.20K-Rs.1L/month</span><span class="diff-tag">Easy Start</span></div>
    <div class="card"><span class="card-num">02</span><span class="card-icon">📹</span><h3>YouTube Channel</h3><p>Create videos on any topic. Earn via AdSense and sponsorships.</p><span class="earn-tag">Rs.10K-Rs.5L/month</span><span class="diff-tag">Needs Patience</span></div>
    <div class="card"><span class="card-num">03</span><span class="card-icon">✍️</span><h3>Blogging</h3><p>Start a blog, drive SEO traffic, earn passive income through AdSense and Affiliate Marketing.</p><span class="earn-tag">Rs.5K-Rs.2L/month</span><span class="diff-tag">6-12 Months</span></div>
    <div class="card"><span class="card-num">04</span><span class="card-icon">🛒</span><h3>Affiliate Marketing</h3><p>Promote Amazon or Flipkart products and earn a commission on every sale.</p><span class="earn-tag">Rs.5K-Rs.3L/month</span><span class="diff-tag">Medium</span></div>
    <div class="card"><span class="card-num">05</span><span class="card-icon">🎓</span><h3>Online Teaching</h3><p>Teach on Udemy or create your own course. Create once, sell forever.</p><span class="earn-tag">Rs.15K-Rs.2L/month</span><span class="diff-tag">Easy</span></div>
    <div class="card"><span class="card-num">06</span><span class="card-icon">📱</span><h3>Social Media Management</h3><p>Manage Instagram and Facebook pages for local businesses.</p><span class="earn-tag">Rs.20K-Rs.80K/month</span><span class="diff-tag">Easy</span></div>
    <div class="card"><span class="card-num">07</span><span class="card-icon">📸</span><h3>Stock Photography</h3><p>Sell your photos on Shutterstock. One photo sells again and again.</p><span class="earn-tag">Rs.2K-Rs.30K/month</span><span class="diff-tag">Beginner</span></div>
    <div class="card"><span class="card-num">08</span><span class="card-icon">🎨</span><h3>Graphic Design</h3><p>Learn Canva and sell logos, banners, and social media posts on Fiverr.</p><span class="earn-tag">Rs.15K-Rs.1L/month</span><span class="diff-tag">Medium</span></div>
    <div class="card"><span class="card-num">09</span><span class="card-icon">🖥️</span><h3>Web Development</h3><p>Learn HTML, CSS, Python and build websites for small businesses.</p><span class="earn-tag">Rs.30K-Rs.2L/month</span><span class="diff-tag">Hard but Worth It</span></div>
    <div class="card"><span class="card-num">10</span><span class="card-icon">🤖</span><h3>AI Tools</h3><p>Master ChatGPT and offer content creation and image generation services.</p><span class="earn-tag">Rs.20K-Rs.1.5L/month</span><span class="diff-tag">New Trend</span></div>
    <div class="card"><span class="card-num">11</span><span class="card-icon">📦</span><h3>Dropshipping</h3><p>Run an online store without holding stock. Customer orders, supplier ships.</p><span class="earn-tag">Rs.10K-Rs.3L/month</span><span class="diff-tag">Medium Risk</span></div>
    <div class="card"><span class="card-num">12</span><span class="card-icon">🎙️</span><h3>Podcast</h3><p>Start a podcast on Spotify. Earn through sponsorships and affiliate marketing.</p><span class="earn-tag">Rs.5K-Rs.1L/month</span><span class="diff-tag">Long Term</span></div>
    <div class="card"><span class="card-num">13</span><span class="card-icon">💹</span><h3>Stock Market</h3><p>Invest on Zerodha or Groww. Build long-term wealth through smart investing.</p><span class="earn-tag">Variable Returns</span><span class="diff-tag">Has Risk</span></div>
    <div class="card"><span class="card-num">14</span><span class="card-icon">📝</span><h3>Content Writing</h3><p>Write blogs and articles. High demand for English writers on LinkedIn.</p><span class="earn-tag">Rs.10K-Rs.60K/month</span><span class="diff-tag">Easy Start</span></div>
    <div class="card"><span class="card-num">15</span><span class="card-icon">🌐</span><h3>Domain Flipping</h3><p>Buy domains cheap and sell them for profit on GoDaddy Auctions.</p><span class="earn-tag">Rs.5K-Rs.10L/sale</span><span class="diff-tag">Smart Investment</span></div>
  </div>
  <div class="steps">
    <h2>How to Get Started?</h2>
    <div class="step-list">
      <div class="step"><div class="step-num">1</div><div class="step-content"><h4>Identify Your Skill</h4><p>Writing, Design, Teaching, Coding — any skill can make money online.</p></div></div>
      <div class="step"><div class="step-num">2</div><div class="step-content"><h4>Choose One Platform</h4><p>Start with just one — YouTube, Fiverr, or your own Blog. Expand one at a time.</p></div></div>
      <div class="step"><div class="step-num">3</div><div class="step-content"><h4>Take Free Courses</h4><p>Learn for free on YouTube. Stay consistent for at least 90 days.</p></div></div>
      <div class="step"><div class="step-num">4</div><div class="step-content"><h4>Earn Your First Rs.1</h4><p>Don't target Rs.1 lakh first — just earn your first rupee. Confidence follows.</p></div></div>
      <div class="step"><div class="step-num">5</div><div class="step-content"><h4>Scale Up</h4><p>Double down on what works. Build multiple income streams.</p></div></div>
    </div>
  </div>
  <div style="margin-top:4rem;">
    <div class="section-title">Latest <span>Articles</span></div>
    <p class="section-sub">In-depth guides on every method</p>
    <div class="articles-grid">
      <a href="/how-to-earn-on-fiverr" class="article-card">
        <h3>💻 How to Earn Money on Fiverr?</h3>
        <p>Complete guide from creating your account to landing your first order.</p>
      </a>
      <a href="/how-to-start-youtube-channel" class="article-card">
        <h3>📹 How to Start a YouTube Channel?</h3>
        <p>Step-by-step guide to starting a channel and getting monetized in 2025.</p>
      </a>
      <a href="/how-to-earn-from-blogging" class="article-card">
        <h3>✍️ How to Earn Money from Blogging?</h3>
        <p>Start a blog, rank on Google, and earn passive income through AdSense.</p>
      </a>
    </div>
  </div>
</section>
<footer>
  <p style="font-family:\'Baloo 2\',cursive; font-size:1.5rem; font-weight:800; color:var(--gold);">💰 PaiseKamao.in</p>
  <p>India\'s most trusted platform for earning money online</p>
  <p style="margin-top:0.5rem;">2025 PaiseKamao.in</p>
</footer>
<script src="https://pl28794442.effectivegatecpm.com/a9/88/ee/a988ee17c2e78b58e12c025a8562a1da.js"></script>
</body>
</html>'''

FIVERR_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>How to Earn Money on Fiverr? - PaiseKamao.in</title>
<meta name="description" content="Complete guide to earning money on Fiverr in 2025.">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1709475506645918" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Hind:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root { --gold: #f5c518; --dark: #0a0a12; --card: #12121f; --text: #e8e8f0; --muted: #7a7a9a; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--dark); color: var(--text); font-family: 'Hind', sans-serif; }
  .container { max-width: 800px; margin: 0 auto; padding: 3rem 1.5rem; }
  .back { color: var(--gold); text-decoration: none; font-size: 0.9rem; display: inline-block; margin-bottom: 2rem; }
  h1 { font-family: 'Baloo 2', cursive; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; line-height: 1.2; }
  h1 span { color: var(--gold); }
  h2 { font-family: 'Baloo 2', cursive; font-size: 1.5rem; font-weight: 700; color: var(--gold); margin: 2rem 0 1rem; }
  p { color: var(--muted); line-height: 1.8; margin-bottom: 1rem; }
  .highlight { background: var(--card); border-left: 4px solid var(--gold); padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
  .step-box { background: var(--card); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255,255,255,0.07); }
  .step-box h3 { font-family: 'Baloo 2', cursive; color: #fff; margin-bottom: 0.5rem; }
  footer { text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.07); color: var(--muted); margin-top: 3rem; }
</style>
</head>
<body>
<div class="container">
  <a href="/" class="back">Back to Home</a>
  <h1>How to Earn Money on <span>Fiverr</span>?</h1>
  <p>Fiverr is the world's largest freelancing platform. Sell any skill and earn Rs.20,000 to Rs.1,00,000+ per month from home.</p>
  <div class="highlight">Earnings: Rs.20,000 to Rs.1,00,000+ per month | Getting started: Completely free</div>
  <h2>What is Fiverr?</h2>
  <p>Fiverr is an online marketplace where freelancers sell their services called Gigs. Graphic design, writing, video editing, coding — every type of service sells here.</p>
  <h2>How to Create a Fiverr Account?</h2>
  <div class="step-box"><h3>Step 1: Register</h3><p>Go to Fiverr.com, click Become a Seller and sign up with your email.</p></div>
  <div class="step-box"><h3>Step 2: Complete Your Profile</h3><p>Add your photo, bio, and skills. Use a professional photo to increase your chances of getting orders.</p></div>
  <div class="step-box"><h3>Step 3: Create Your First Gig</h3><p>Offer a service you are good at. Keep the title clear.</p></div>
  <div class="step-box"><h3>Step 4: Set Your Pricing</h3><p>Start at Rs.500 to Rs.1000. Raise prices once you get reviews.</p></div>
  <h2>Which Skills Get the Most Orders?</h2>
  <p>Logo Design, Video Editing, Content Writing, Social Media Posts, WordPress Websites, Voice Over, Data Entry, Translation.</p>
  <h2>When Do You Get Paid?</h2>
  <p>Funds are released 14 days after order completion. Withdraw via PayPal, Bank Transfer, or Payoneer.</p>
  <div class="highlight">Pro Tip: Deliver excellent service for your first 10 orders and earn 5-star reviews. After that, orders come automatically!</div>
</div>
<footer>
  <p style="font-family:'Baloo 2',cursive; color:var(--gold); font-size:1.2rem;">PaiseKamao.in</p>
  <p><a href="/" style="color:var(--gold);">Back to Home</a></p>
</footer>
<script src="https://pl28794442.effectivegatecpm.com/a9/88/ee/a988ee17c2e78b58e12c025a8562a1da.js"></script>
</body>
</html>'''

YOUTUBE_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>How to Start a YouTube Channel? - PaiseKamao.in</title>
<meta name="description" content="Complete guide to starting a YouTube channel in India 2025.">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1709475506645918" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Hind:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root { --gold: #f5c518; --dark: #0a0a12; --card: #12121f; --text: #e8e8f0; --muted: #7a7a9a; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--dark); color: var(--text); font-family: 'Hind', sans-serif; }
  .container { max-width: 800px; margin: 0 auto; padding: 3rem 1.5rem; }
  .back { color: var(--gold); text-decoration: none; font-size: 0.9rem; display: inline-block; margin-bottom: 2rem; }
  h1 { font-family: 'Baloo 2', cursive; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; line-height: 1.2; }
  h1 span { color: var(--gold); }
  h2 { font-family: 'Baloo 2', cursive; font-size: 1.5rem; font-weight: 700; color: var(--gold); margin: 2rem 0 1rem; }
  p { color: var(--muted); line-height: 1.8; margin-bottom: 1rem; }
  .highlight { background: var(--card); border-left: 4px solid var(--gold); padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
  .step-box { background: var(--card); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255,255,255,0.07); }
  .step-box h3 { font-family: 'Baloo 2', cursive; color: #fff; margin-bottom: 0.5rem; }
  footer { text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.07); color: var(--muted); margin-top: 3rem; }
</style>
</head>
<body>
<div class="container">
  <a href="/" class="back">Back to Home</a>
  <h1>How to Start a <span>YouTube Channel</span>?</h1>
  <p>YouTube is India's most popular platform. With the right niche and consistency, earn lakhs with zero investment!</p>
  <div class="highlight">YouTube Earnings: Rs.10,000 to Rs.5,00,000+ per month | Investment: Rs.0</div>
  <h2>How to Create a YouTube Channel?</h2>
  <div class="step-box"><h3>Step 1: Create Channel with Gmail</h3><p>Go to YouTube.com, sign in, click your name and select Create a channel.</p></div>
  <div class="step-box"><h3>Step 2: Choose Your Niche</h3><p>Pick a topic you enjoy. Education, Cooking, Tech, Finance, Comedy — whatever your passion is.</p></div>
  <div class="step-box"><h3>Step 3: Make Your First Video</h3><p>Start with your smartphone. Use good lighting. Videos of 8 to 15 minutes perform best.</p></div>
  <div class="step-box"><h3>Step 4: Thumbnails and Titles</h3><p>Create eye-catching thumbnails. Put keywords in your title that people search for.</p></div>
  <div class="step-box"><h3>Step 5: Monetization</h3><p>Reach 1,000 Subscribers and 4,000 Watch Hours to apply for the YouTube Partner Program.</p></div>
  <h2>How Much Can You Earn?</h2>
  <p>10K subscribers: Rs.3,000 to Rs.10,000 per month. 1 Lakh subscribers: Rs.30,000 to Rs.1,00,000 per month.</p>
  <div class="highlight">Pro Tip: Upload at least 2 videos per week. After 1 year your channel can explode!</div>
</div>
<footer>
  <p style="font-family:'Baloo 2',cursive; color:var(--gold); font-size:1.2rem;">PaiseKamao.in</p>
  <p><a href="/" style="color:var(--gold);">Back to Home</a></p>
</footer>
<script src="https://pl28794442.effectivegatecpm.com/a9/88/ee/a988ee17c2e78b58e12c025a8562a1da.js"></script>
</body>
</html>'''

BLOGGING_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>How to Earn Money from Blogging? - PaiseKamao.in</title>
<meta name="description" content="Start a blog, rank on Google and earn passive income through AdSense in India 2025.">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1709475506645918" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Hind:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root { --gold: #f5c518; --dark: #0a0a12; --card: #12121f; --text: #e8e8f0; --muted: #7a7a9a; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--dark); color: var(--text); font-family: 'Hind', sans-serif; }
  .container { max-width: 800px; margin: 0 auto; padding: 3rem 1.5rem; }
  .back { color: var(--gold); text-decoration: none; font-size: 0.9rem; display: inline-block; margin-bottom: 2rem; }
  h1 { font-family: 'Baloo 2', cursive; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; line-height: 1.2; }
  h1 span { color: var(--gold); }
  h2 { font-family: 'Baloo 2', cursive; font-size: 1.5rem; font-weight: 700; color: var(--gold); margin: 2rem 0 1rem; }
  p { color: var(--muted); line-height: 1.8; margin-bottom: 1rem; }
  .highlight { background: var(--card); border-left: 4px solid var(--gold); padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
  .step-box { background: var(--card); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255,255,255,0.07); }
  .step-box h3 { font-family: 'Baloo 2', cursive; color: #fff; margin-bottom: 0.5rem; }
  footer { text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.07); color: var(--muted); margin-top: 3rem; }
</style>
</head>
<body>
<div class="container">
  <a href="/" class="back">Back to Home</a>
  <h1>How to Earn Money from <span>Blogging</span>?</h1>
  <p>Write an article once and earn money from it for years — passive income while you sleep!</p>
  <div class="highlight">Blogging Earnings: Rs.5,000 to Rs.2,00,000+ per month | Timeline: 6 to 12 months</div>
  <h2>How to Start a Blog?</h2>
  <div class="step-box"><h3>Step 1: Choose Your Niche</h3><p>Pick a specific topic — Health, Finance, Technology, Travel, Food.</p></div>
  <div class="step-box"><h3>Step 2: Choose a Platform</h3><p>WordPress.org is highly recommended. Blogger is a free option.</p></div>
  <div class="step-box"><h3>Step 3: Get Domain and Hosting</h3><p>Domain: Rs.500 to Rs.1000 per year. Hosting: Rs.1500 to Rs.3000 per year.</p></div>
  <div class="step-box"><h3>Step 4: Write Content</h3><p>Write 2 to 3 articles per week. Each article should be 1000 to 2000 words with SEO keywords.</p></div>
  <div class="step-box"><h3>Step 5: Apply for AdSense</h3><p>Once you have 20 to 30 articles, apply for Google AdSense.</p></div>
  <h2>Traffic vs Earnings</h2>
  <p>1,000 visitors per day: Rs.5,000 to Rs.15,000 per month. 10,000+ visitors per day: Rs.1,00,000+ per month.</p>
  <div class="highlight">Pro Tip: Focus on solving real problems people search for and Google will reward you!</div>
</div>
<footer>
  <p style="font-family:'Baloo 2',cursive; color:var(--gold); font-size:1.2rem;">PaiseKamao.in</p>
  <p><a href="/" style="color:var(--gold);">Back to Home</a></p>
</footer>
<script src="https://pl28794442.effectivegatecpm.com/a9/88/ee/a988ee17c2e78b58e12c025a8562a1da.js"></script>
</body>
</html>'''


@app.route('/')
def home():
    return render_template_string(HTML)


@app.route('/how-to-earn-on-fiverr')
def fiverr():
    return render_template_string(FIVERR_HTML)


@app.route('/how-to-start-youtube-channel')
def youtube():
    return render_template_string(YOUTUBE_HTML)


@app.route('/how-to-earn-from-blogging')
def blogging():
    return render_template_string(BLOGGING_HTML)


@app.route('/sitemap.xml')
def sitemap():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://paisekamao.onrender.com/</loc><priority>1.0</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-on-fiverr</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-start-youtube-channel</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-from-blogging</loc><priority>0.8</priority></url>
</urlset>''', 200, {'Content-Type': 'application/xml'}


@app.route('/ads.txt')
def ads_txt():
    return "google.com, pub-1709475506645918, DIRECT, f08c47fec0942fa0", 200, {'Content-Type': 'text/plain'}


@app.route('/205f96ddcb0db02da8bf.txt')
def hilltopads_verify():
    return "205f96ddcb0db02da8bf", 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
