from flask import Flask, render_template_string
import os

app = Flask(__name__)

BASE_HEAD = '''
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1709475506645918" crossorigin="anonymous"></script>
<script src="https://belfrybreathrich.com/a9/88/ee/a988ee17c2e78b58e12c025a8562a1da.js"></script>
<script src="https://belfrybreathrich.com/a2/48/16/a24816a0f456309584d6832492ac79a7.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Hind:wght@300;400;500;600&display=swap" rel="stylesheet">
'''

BASE_STYLE = '''
<style>
  :root { --gold: #f5c518; --gold2: #e8a900; --dark: #0a0a12; --card: #12121f; --green: #00ff88; --text: #e8e8f0; --muted: #7a7a9a; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--dark); color: var(--text); font-family: 'Hind', sans-serif; }
  .container { max-width: 860px; margin: 0 auto; padding: 3rem 1.5rem; }
  .back { color: var(--gold); text-decoration: none; font-size: 0.9rem; display: inline-block; margin-bottom: 2rem; }
  h1 { font-family: 'Baloo 2', cursive; font-size: 2.4rem; font-weight: 800; margin-bottom: 1rem; line-height: 1.2; }
  h1 span { color: var(--gold); }
  h2 { font-family: 'Baloo 2', cursive; font-size: 1.5rem; font-weight: 700; color: var(--gold); margin: 2rem 0 1rem; }
  h3 { font-family: 'Baloo 2', cursive; font-size: 1.2rem; font-weight: 700; color: #fff; margin: 1.5rem 0 0.5rem; }
  p { color: var(--muted); line-height: 1.85; margin-bottom: 1rem; font-size: 1rem; }
  ul, ol { color: var(--muted); padding-left: 1.5rem; margin-bottom: 1rem; line-height: 1.85; }
  li { margin-bottom: 0.4rem; }
  .highlight { background: var(--card); border-left: 4px solid var(--gold); padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
  .step-box { background: var(--card); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255,255,255,0.07); }
  .step-box h3 { margin-top: 0; }
  .ad-banner { text-align: center; margin: 2rem auto; }
  .nav { background: #0d0d1a; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.07); }
  .nav a { color: var(--gold); text-decoration: none; font-family: 'Baloo 2', cursive; font-weight: 700; font-size: 1.2rem; }
  .nav-links { display: flex; gap: 1.5rem; }
  .nav-links a { font-size: 0.85rem; font-family: 'Hind', sans-serif; font-weight: 500; color: var(--muted); }
  .nav-links a:hover { color: var(--gold); }
  footer { text-align: center; padding: 3rem 1.5rem; border-top: 1px solid rgba(255,255,255,0.07); color: var(--muted); margin-top: 3rem; }
  footer a { color: var(--gold); text-decoration: none; margin: 0 0.5rem; }
  .tag { display: inline-block; background: rgba(0,255,136,0.1); border: 1px solid rgba(0,255,136,0.3); color: var(--green); font-size: 0.75rem; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 100px; margin-right: 0.5rem; }
  .tag-gold { background: rgba(245,197,24,0.1); border-color: rgba(245,197,24,0.3); color: var(--gold); }
</style>
'''

NAV = '''
<nav class="nav">
  <a href="/">💰 PaiseKamao</a>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
  </div>
</nav>
'''

FOOTER = '''
<footer>
  <p style="font-family:'Baloo 2',cursive; font-size:1.3rem; font-weight:800; color:var(--gold);">💰 PaiseKamao.in</p>
  <p style="margin:0.5rem 0;">India's trusted platform for earning money online</p>
  <p><a href="/">Home</a> | <a href="/about">About</a> | <a href="/contact">Contact</a> | <a href="/privacy-policy">Privacy Policy</a></p>
  <p style="margin-top:1rem; font-size:0.8rem;">© 2025 PaiseKamao.in — All Rights Reserved</p>
</footer>
'''

AD_BANNER = '''
<div class="ad-banner">
  <script>atOptions = {'key':'83e5a950bf9f95c1271a7793c2b8354d','format':'iframe','height':60,'width':468,'params':{}};</script>
  <script src="https://belfrybreathrich.com/83e5a950bf9f95c1271a7793c2b8354d/invoke.js"></script>
</div>
'''

AD_NATIVE = '''
<div class="ad-banner">
  <script async="async" data-cfasync="false" src="https://belfrybreathrich.com/0281362ccc7214547b37534dcd6d1f33/invoke.js"></script>
  <div id="container-0281362ccc7214547b37534dcd6d1f33"></div>
</div>
'''

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
''' + BASE_HEAD + '''
<title>PaiseKamao.in - 15 Best Ways to Earn Money Online in India</title>
<meta name="description" content="Earn money online from home in India. 15 proven ways including Freelancing, YouTube, Blogging, Affiliate Marketing and more. Zero investment needed.">
<meta name="keywords" content="earn money online india, work from home india, freelancing india, youtube earn money, blogging income 2025">
<meta name="google-site-verification" content="TPjYlLn0L0W216UNfKt9sg2n9McE-NvepGERkWEtZVU" />
''' + BASE_STYLE + '''
<style>
  .hero { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem; background: radial-gradient(ellipse at 50% 0%, rgba(245,197,24,0.15) 0%, transparent 70%); }
  .badge { display: inline-block; background: rgba(245,197,24,0.15); border: 1px solid var(--gold); color: var(--gold); padding: 0.4rem 1.2rem; border-radius: 100px; font-size: 0.85rem; margin-bottom: 1.5rem; }
  .hero h1 { font-size: clamp(2.5rem, 7vw, 5rem); }
  .hero p { font-size: 1.2rem; max-width: 600px; margin: 0 auto 2.5rem; }
  .stats-row { display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; }
  .stat .num { font-family: 'Baloo 2', cursive; font-size: 2rem; font-weight: 800; color: var(--gold); }
  .stat .label { font-size: 0.8rem; color: var(--muted); }
  .section { max-width: 1100px; margin: 0 auto; padding: 4rem 1.5rem; }
  .section-title { font-family: 'Baloo 2', cursive; font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 0.5rem; }
  .section-title span { color: var(--gold); }
  .section-sub { text-align: center; color: var(--muted); margin-bottom: 3rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 1.5rem; }
  .card { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 1.8rem; transition: transform 0.3s, border-color 0.3s; position: relative; overflow: hidden; }
  .card:hover { transform: translateY(-5px); border-color: rgba(245,197,24,0.3); }
  .card-icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
  .card-num { position: absolute; top: 1.2rem; right: 1.5rem; font-family: 'Baloo 2', cursive; font-size: 3rem; font-weight: 800; color: rgba(255,255,255,0.04); }
  .card h3 { font-family: 'Baloo 2', cursive; font-size: 1.3rem; margin-bottom: 0.6rem; color: #fff; margin-top: 0; }
  .articles-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
  .article-card { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 1.5rem; text-decoration: none; color: var(--text); display: block; transition: transform 0.3s, border-color 0.3s; }
  .article-card:hover { transform: translateY(-4px); border-color: rgba(245,197,24,0.4); }
  .article-card h3 { font-family: 'Baloo 2', cursive; font-size: 1.1rem; color: var(--gold); margin-bottom: 0.5rem; margin-top: 0; }
  .article-card p { font-size: 0.88rem; margin-bottom: 0; }
  .steps { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 20px; padding: 3rem; margin-top: 4rem; }
  .steps h2 { text-align: center; margin-top: 0; }
  .step-list { display: flex; flex-direction: column; gap: 1.2rem; max-width: 700px; margin: 0 auto; }
  .step { display: flex; gap: 1.2rem; align-items: flex-start; }
  .step-num { width: 40px; height: 40px; min-width: 40px; background: linear-gradient(135deg, var(--gold), var(--gold2)); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Baloo 2', cursive; font-weight: 800; color: #000; }
  .step-content h4 { font-family: 'Baloo 2', cursive; font-weight: 700; margin-bottom: 0.2rem; }
  .step-content p { font-size: 0.9rem; margin-bottom: 0; }
  .ticker-wrap { background: var(--gold); overflow: hidden; padding: 0.7rem 0; white-space: nowrap; }
  .ticker { display: inline-block; animation: ticker 25s linear infinite; }
  .ticker span { color: #000; font-weight: 700; font-family: 'Baloo 2', cursive; margin: 0 2rem; font-size: 0.95rem; }
  @keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
</style>
</head>
<body>
''' + NAV + '''
<div class="ticker-wrap">
  <div class="ticker">
    <span>💰 Earn Rs.50,000/month with Freelancing</span><span>📹 Make Lakhs on YouTube</span><span>✍️ Passive Income from Blogging</span><span>🛒 Affiliate Marketing</span><span>📱 Social Media Income</span><span>🎓 Teach Online</span><span>💰 Earn Rs.50,000/month with Freelancing</span><span>📹 Make Lakhs on YouTube</span><span>✍️ Passive Income from Blogging</span><span>🛒 Affiliate Marketing</span><span>📱 Social Media Income</span><span>🎓 Teach Online</span>
  </div>
</div>
<section class="hero">
  <div class="badge">🇮🇳 Made for Indians — 100% Free Guides</div>
  <h1>Earn Money <span>Online</span><br>From Home!</h1>
  <p style="color:var(--muted);">15 proven ways to earn Rs.10,000 to Rs.1,00,000+ per month in 2025. No experience needed — start today!</p>
  <div class="stats-row">
    <div class="stat"><div class="num">50K+</div><div class="label">People Earning</div></div>
    <div class="stat"><div class="num">15</div><div class="label">Methods</div></div>
    <div class="stat"><div class="num">Rs.0</div><div class="label">Investment Needed</div></div>
    <div class="stat"><div class="num">24/7</div><div class="label">Passive Income</div></div>
  </div>
</section>

''' + AD_BANNER + '''

<section class="section">
  <div class="section-title">15 Ways to <span>Earn Online</span></div>
  <p class="section-sub">Real earnings data and step-by-step guidance for every method</p>
  <div class="grid">
    <div class="card"><span class="card-num">01</span><span class="card-icon">💻</span><h3>Freelancing</h3><p>Sell your skills on Upwork, Fiverr, Freelancer. Web design, writing, video editing, coding — all in demand.</p><span class="tag">Rs.20K-Rs.1L/month</span><span class="tag tag-gold">Easy Start</span></div>
    <div class="card"><span class="card-num">02</span><span class="card-icon">📹</span><h3>YouTube Channel</h3><p>Create videos on any topic. Earn via AdSense, sponsorships, and affiliate marketing.</p><span class="tag">Rs.10K-Rs.5L/month</span><span class="tag tag-gold">Needs Patience</span></div>
    <div class="card"><span class="card-num">03</span><span class="card-icon">✍️</span><h3>Blogging</h3><p>Start a blog, drive SEO traffic, earn passive income through AdSense and Affiliate Marketing.</p><span class="tag">Rs.5K-Rs.2L/month</span><span class="tag tag-gold">6-12 Months</span></div>
    <div class="card"><span class="card-num">04</span><span class="card-icon">🛒</span><h3>Affiliate Marketing</h3><p>Promote Amazon or Flipkart products and earn a commission on every sale you refer.</p><span class="tag">Rs.5K-Rs.3L/month</span><span class="tag tag-gold">Medium</span></div>
    <div class="card"><span class="card-num">05</span><span class="card-icon">🎓</span><h3>Online Teaching</h3><p>Teach on Udemy or create your own course. Create once, sell to thousands forever.</p><span class="tag">Rs.15K-Rs.2L/month</span><span class="tag tag-gold">Easy</span></div>
    <div class="card"><span class="card-num">06</span><span class="card-icon">📱</span><h3>Instagram Earning</h3><p>Build a niche Instagram page, get brand deals, promote affiliate products and earn.</p><span class="tag">Rs.10K-Rs.1L/month</span><span class="tag tag-gold">Easy</span></div>
    <div class="card"><span class="card-num">07</span><span class="card-icon">📸</span><h3>Stock Photography</h3><p>Sell your photos on Shutterstock and Adobe Stock. One photo can sell hundreds of times.</p><span class="tag">Rs.2K-Rs.30K/month</span><span class="tag tag-gold">Beginner</span></div>
    <div class="card"><span class="card-num">08</span><span class="card-icon">🎨</span><h3>Graphic Design</h3><p>Learn Canva or Photoshop and sell logos, banners, and social media posts on Fiverr.</p><span class="tag">Rs.15K-Rs.1L/month</span><span class="tag tag-gold">Medium</span></div>
    <div class="card"><span class="card-num">09</span><span class="card-icon">🖥️</span><h3>Web Development</h3><p>Learn HTML, CSS, Python and build websites for small businesses in India and abroad.</p><span class="tag">Rs.30K-Rs.2L/month</span><span class="tag tag-gold">Hard but Worth It</span></div>
    <div class="card"><span class="card-num">10</span><span class="card-icon">🤖</span><h3>Earn with ChatGPT</h3><p>Master AI tools like ChatGPT and offer content creation, automation, and consulting services.</p><span class="tag">Rs.20K-Rs.1.5L/month</span><span class="tag tag-gold">New Trend</span></div>
    <div class="card"><span class="card-num">11</span><span class="card-icon">📦</span><h3>Dropshipping</h3><p>Run an online store without holding any stock. Customer orders, supplier ships directly.</p><span class="tag">Rs.10K-Rs.3L/month</span><span class="tag tag-gold">Medium Risk</span></div>
    <div class="card"><span class="card-num">12</span><span class="card-icon">🎙️</span><h3>Podcast</h3><p>Start a podcast on Spotify. Earn through sponsorships, affiliate marketing and donations.</p><span class="tag">Rs.5K-Rs.1L/month</span><span class="tag tag-gold">Long Term</span></div>
    <div class="card"><span class="card-num">13</span><span class="card-icon">💹</span><h3>Stock Market</h3><p>Invest wisely on Zerodha or Groww. Build long-term wealth through systematic investing.</p><span class="tag">Variable Returns</span><span class="tag tag-gold">Has Risk</span></div>
    <div class="card"><span class="card-num">14</span><span class="card-icon">📝</span><h3>Content Writing</h3><p>Write blogs and articles for websites. High demand for English and Hindi writers online.</p><span class="tag">Rs.10K-Rs.60K/month</span><span class="tag tag-gold">Easy Start</span></div>
    <div class="card"><span class="card-num">15</span><span class="card-icon">🌐</span><h3>Domain Flipping</h3><p>Buy good domain names cheap and sell them for a profit on GoDaddy Auctions.</p><span class="tag">Rs.5K-Rs.10L/sale</span><span class="tag tag-gold">Smart Investment</span></div>
  </div>

  ''' + AD_NATIVE + '''

  <div class="steps">
    <h2>How to Get Started?</h2>
    <div class="step-list">
      <div class="step"><div class="step-num">1</div><div class="step-content"><h4>Identify Your Skill</h4><p>Writing, Design, Teaching, Coding — any skill can make money online. Pick what you enjoy.</p></div></div>
      <div class="step"><div class="step-num">2</div><div class="step-content"><h4>Choose One Platform</h4><p>Start with just one — YouTube, Fiverr, or your own Blog. Master it before expanding.</p></div></div>
      <div class="step"><div class="step-num">3</div><div class="step-content"><h4>Learn for Free on YouTube</h4><p>Every skill can be learned for free. Stay consistent for at least 90 days.</p></div></div>
      <div class="step"><div class="step-num">4</div><div class="step-content"><h4>Earn Your First Rs.1</h4><p>Don't target Rs.1 lakh first — just earn your first rupee online. Confidence follows.</p></div></div>
      <div class="step"><div class="step-num">5</div><div class="step-content"><h4>Scale Up</h4><p>Double down on what works. Slowly build multiple income streams for financial freedom.</p></div></div>
    </div>
  </div>

  <div style="margin-top:4rem;">
    <div class="section-title">Latest <span>Articles</span></div>
    <p class="section-sub">In-depth step-by-step guides on every earning method</p>
    <div class="articles-grid">
      <a href="/how-to-earn-on-fiverr" class="article-card"><h3>💻 How to Earn Money on Fiverr?</h3><p>Complete guide from creating your account to landing your first order.</p></a>
      <a href="/how-to-start-youtube-channel" class="article-card"><h3>📹 How to Start a YouTube Channel?</h3><p>Step-by-step guide to starting a channel and getting monetized in 2025.</p></a>
      <a href="/how-to-earn-from-blogging" class="article-card"><h3>✍️ How to Earn from Blogging?</h3><p>Start a blog, rank on Google, and earn passive income through AdSense.</p></a>
      <a href="/how-to-earn-on-instagram" class="article-card"><h3>📱 How to Earn Money on Instagram?</h3><p>Build a following, get brand deals and earn from Instagram in India.</p></a>
      <a href="/how-to-earn-with-chatgpt" class="article-card"><h3>🤖 How to Earn Money with ChatGPT?</h3><p>Use AI tools to offer services and earn Rs.50,000+ per month in 2025.</p></a>
      <a href="/how-to-start-freelancing" class="article-card"><h3>🖥️ Complete Freelancing Guide for Beginners</h3><p>Everything you need to start freelancing from zero and earn your first client.</p></a>
      <a href="/how-to-earn-from-affiliate-marketing" class="article-card"><h3>🛒 How to Earn from Affiliate Marketing?</h3><p>Promote products online and earn commission on every sale.</p></a>
    </div>
  </div>
</section>
''' + FOOTER + '''
</body>
</html>'''

FIVERR_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>How to Earn Money on Fiverr in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Complete guide to earning money on Fiverr in India 2025. Create your gig, get orders and withdraw money to your Indian bank account.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>How to Earn Money on <span>Fiverr</span> in India?</h1>
  <p>Fiverr is the world's largest freelancing marketplace with over 4 million buyers. You can sell almost any skill and earn Rs.20,000 to Rs.1,00,000+ per month from home with zero investment.</p>
  <div class="highlight">💰 Earnings: Rs.20,000 to Rs.1,00,000+ per month | ✅ Investment: Completely Free</div>
  ''' + AD_BANNER + '''
  <h2>What is Fiverr?</h2>
  <p>Fiverr is an online marketplace where freelancers offer their services to clients worldwide. Graphic design, writing, video editing, coding, voice over — every type of service is in demand. India is one of the top countries on Fiverr and Indian freelancers earn millions every year.</p>
  <h2>How to Create Your Fiverr Account</h2>
  <div class="step-box"><h3>Step 1: Sign Up for Free</h3><p>Go to Fiverr.com and click "Become a Seller". Sign up using your Gmail or Facebook account. Takes less than 2 minutes.</p></div>
  <div class="step-box"><h3>Step 2: Complete Your Seller Profile</h3><p>Add a clear professional photo. Write a bio explaining your skills. A complete profile gets 3x more orders than an incomplete one.</p></div>
  <div class="step-box"><h3>Step 3: Create Your First Gig</h3><p>Choose a category matching your skill. Write a clear title like "I will design a professional logo for your business". Add a detailed description and FAQ.</p></div>
  <div class="step-box"><h3>Step 4: Set Competitive Pricing</h3><p>Start with a Basic package at Rs.500-Rs.1000 to attract first orders. Once you get 5-star reviews, gradually increase your prices.</p></div>
  <div class="step-box"><h3>Step 5: Add Portfolio Samples</h3><p>Upload examples of your work. If new, create 2-3 sample projects. Good portfolio images dramatically increase chances of getting orders.</p></div>
  ''' + AD_NATIVE + '''
  <h2>Which Skills Earn the Most on Fiverr?</h2>
  <ul>
    <li><strong>Logo and Graphic Design</strong> — High demand, good pay</li>
    <li><strong>Video Editing and Animation</strong> — Highest paying category</li>
    <li><strong>Content Writing and Copywriting</strong> — Always in demand</li>
    <li><strong>WordPress and Web Development</strong> — Premium pricing</li>
    <li><strong>Social Media Management</strong> — Recurring monthly clients</li>
    <li><strong>Voice Over</strong> — Easy to start with just a phone</li>
    <li><strong>Data Entry and Virtual Assistant</strong> — Beginner friendly</li>
    <li><strong>SEO Services</strong> — High value, great income</li>
  </ul>
  <h2>How Payments Work</h2>
  <p>When a buyer places an order, Fiverr holds the payment. Once you deliver and the buyer approves, funds are released after 14 days. Withdraw via Payoneer (best for India), PayPal, or direct bank transfer. Fiverr charges 20% commission.</p>
  <div class="highlight">🚀 Pro Tip: Focus on delivering 5-star service for your first 10 orders. Reviews are everything on Fiverr — they decide whether new buyers trust you!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

YOUTUBE_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>How to Start a YouTube Channel and Earn Money in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Complete guide to starting a YouTube channel in India 2025. Learn how to get 1000 subscribers, get monetized and earn money from YouTube.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>How to Start a <span>YouTube Channel</span> and Earn Money?</h1>
  <p>YouTube is India's most watched video platform with over 450 million users. Starting a YouTube channel in 2025 is still one of the best ways to build long-term income from home with zero investment.</p>
  <div class="highlight">📹 Earnings: Rs.10,000 to Rs.5,00,000+ per month | Investment: Rs.0 — just your smartphone!</div>
  ''' + AD_BANNER + '''
  <h2>Why Start a YouTube Channel in 2025?</h2>
  <p>YouTube pays Indian creators between Rs.200 to Rs.400 per 1,000 views through AdSense. Top creators also earn from brand sponsorships, affiliate marketing, merchandise, and paid memberships. A channel with 1 lakh subscribers can easily earn Rs.50,000 to Rs.2,00,000 per month.</p>
  <h2>Step-by-Step: How to Start Your YouTube Channel</h2>
  <div class="step-box"><h3>Step 1: Create Your Channel</h3><p>Go to YouTube.com, sign in with Gmail, click your profile picture then "Create a channel". Choose a memorable name reflecting your niche.</p></div>
  <div class="step-box"><h3>Step 2: Choose Your Niche</h3><p>Popular niches in India: Finance, Tech reviews, Cooking, Education, Health, Comedy, Gaming. Choose something you genuinely enjoy — you will make 100+ videos.</p></div>
  <div class="step-box"><h3>Step 3: Plan Your First 10 Videos</h3><p>Research what people search for on YouTube. Look for high search volume but less competition topics. Consistency in your first 3 months is critical.</p></div>
  <div class="step-box"><h3>Step 4: Create and Edit Videos</h3><p>Start with your smartphone. Use natural light or a cheap LED ring light. Use free editing apps like CapCut. Videos of 8 to 15 minutes perform best for AdSense.</p></div>
  <div class="step-box"><h3>Step 5: Optimize for Search</h3><p>Put your main keyword in title, description, and tags. Create eye-catching thumbnails on Canva. Write a detailed 200+ word description.</p></div>
  <div class="step-box"><h3>Step 6: Upload Consistently</h3><p>Upload at least 2 videos per week. Channels that upload regularly grow 3x faster. Set a schedule and stick to it for at least 6 months.</p></div>
  ''' + AD_NATIVE + '''
  <h2>How to Get Monetized</h2>
  <ul>
    <li>1,000 subscribers on your channel</li>
    <li>4,000 watch hours in the last 12 months</li>
    <li>No community guideline strikes</li>
    <li>Linked AdSense account</li>
  </ul>
  <h2>YouTube Earnings by Subscriber Count</h2>
  <ul>
    <li><strong>1,000 subscribers:</strong> Rs.500 to Rs.2,000 per month</li>
    <li><strong>10,000 subscribers:</strong> Rs.3,000 to Rs.15,000 per month</li>
    <li><strong>1,00,000 subscribers:</strong> Rs.30,000 to Rs.1,50,000 per month</li>
    <li><strong>10,00,000 subscribers:</strong> Rs.3,00,000 to Rs.15,00,000 per month</li>
  </ul>
  <div class="highlight">🔥 Pro Tip: The first 6 months may feel slow. Almost every successful YouTuber felt like quitting in the beginning. Those who push through to 12 months of consistent effort see their channels grow rapidly!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

BLOGGING_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>How to Earn Money from Blogging in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Start a blog, rank on Google and earn passive income through AdSense and affiliate marketing in India 2025. Complete beginner guide.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>How to Earn Money from <span>Blogging</span> in India?</h1>
  <p>Blogging is one of the best ways to build passive income online. You write an article once, and it earns money for years. Many Indian bloggers earn Rs.50,000 to Rs.5,00,000 per month.</p>
  <div class="highlight">✍️ Earnings: Rs.5,000 to Rs.2,00,000+ per month | Timeline: Results in 6 to 12 months</div>
  ''' + AD_BANNER + '''
  <h2>What is Blogging?</h2>
  <p>A blog is a website where you regularly publish articles on a specific topic. When people search on Google, they land on your blog. You earn money by showing ads (Google AdSense) and recommending products (affiliate marketing). More traffic = more earnings.</p>
  <h2>How to Start a Blog — Step by Step</h2>
  <div class="step-box"><h3>Step 1: Choose Your Niche</h3><p>Best blogging niches in India: Personal Finance, Health and Fitness, Technology, Travel, Food, Education, Make Money Online. The more specific your niche, the easier to rank on Google.</p></div>
  <div class="step-box"><h3>Step 2: Get a Domain Name</h3><p>Your domain is your website address. Choose a short, memorable name. Buy from GoDaddy or Namecheap. A .com or .in domain costs Rs.500 to Rs.1,000 per year.</p></div>
  <div class="step-box"><h3>Step 3: Get Web Hosting</h3><p>Hosting stores your website files. Hostinger is most affordable for beginners — plans from Rs.79/month. Always choose hosting with a free SSL certificate.</p></div>
  <div class="step-box"><h3>Step 4: Install WordPress</h3><p>WordPress powers 43% of all websites. Most hosting offers one-click installation. Use a fast theme like Astra or GeneratePress. Install Yoast SEO, WP Rocket, and Akismet plugins.</p></div>
  <div class="step-box"><h3>Step 5: Write Quality Articles</h3><p>Each article should be 1,000 to 2,500 words. Research keywords using Google Keyword Planner. Publish 2 to 3 new articles every week for the first 6 months.</p></div>
  <div class="step-box"><h3>Step 6: Apply for Google AdSense</h3><p>Once you have 20 to 30 quality articles, apply for AdSense. Approval takes 2 to 4 weeks. Once approved, ads will automatically display and pay you for every click.</p></div>
  ''' + AD_NATIVE + '''
  <h2>How Much Can You Earn?</h2>
  <ul>
    <li><strong>500 visitors/day:</strong> Rs.2,000 to Rs.8,000 per month</li>
    <li><strong>1,000 visitors/day:</strong> Rs.5,000 to Rs.15,000 per month</li>
    <li><strong>5,000 visitors/day:</strong> Rs.25,000 to Rs.75,000 per month</li>
    <li><strong>10,000 visitors/day:</strong> Rs.1,00,000+ per month</li>
  </ul>
  <div class="highlight">💡 Pro Tip: An English blog earns 5x to 10x more from AdSense than a Hindi blog because international advertisers pay much higher rates. If you can write in English, always choose English!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

INSTAGRAM_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>How to Earn Money on Instagram in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Complete guide to earning money on Instagram in India 2025. Build followers, get brand deals and earn Rs.10,000 to Rs.1,00,000 per month.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>How to Earn Money on <span>Instagram</span> in India?</h1>
  <p>Instagram has over 230 million users in India. Many Indian creators earn lakhs per month — and you do not need millions of followers to start earning!</p>
  <div class="highlight">📱 Earnings: Rs.10,000 to Rs.5,00,000+ per month | Investment: Rs.0 — just your smartphone</div>
  ''' + AD_BANNER + '''
  <h2>Ways to Earn Money on Instagram</h2>
  <h3>1. Brand Sponsorships</h3>
  <p>Brands pay creators to promote products in posts, reels, and stories. A micro-influencer with 10,000 followers can earn Rs.2,000 to Rs.10,000 per sponsored post. Creators with 1,00,000+ followers earn Rs.20,000 to Rs.2,00,000 per post.</p>
  <h3>2. Affiliate Marketing</h3>
  <p>Promote products from Amazon, Flipkart, or Meesho and earn commission on every sale through your unique link. Commission rates range from 5% to 30%.</p>
  <h3>3. Sell Your Own Products</h3>
  <p>Sell digital products like presets, courses, or ebooks directly through Instagram Shopping. This is the most profitable model as you keep 100% of the revenue.</p>
  <h3>4. Reels Bonus Program</h3>
  <p>Instagram pays creators directly for popular Reels through its bonus program based on the number of views your Reels receive.</p>
  <h2>How to Grow Your Instagram Following</h2>
  <div class="step-box"><h3>Step 1: Choose a Clear Niche</h3><p>Pick one topic — fitness, food, travel, finance, fashion, or motivation. People follow accounts that consistently deliver value on a specific topic.</p></div>
  <div class="step-box"><h3>Step 2: Post Reels Daily</h3><p>Reels get 3x more reach than regular posts. Post at least one Reel every day when starting. Use trending audio and relevant hashtags.</p></div>
  <div class="step-box"><h3>Step 3: Engage with Your Audience</h3><p>Reply to every comment and DM, especially in your first year. Engagement rate matters more than follower count to brands.</p></div>
  <div class="step-box"><h3>Step 4: Use Hashtags Strategically</h3><p>Use 5 to 10 highly relevant hashtags per post. Mix popular hashtags with niche ones. Avoid using the same hashtags every post.</p></div>
  ''' + AD_NATIVE + '''
  <h2>Earnings by Follower Count</h2>
  <ul>
    <li><strong>1,000 followers:</strong> Rs.500-Rs.2,000 per post</li>
    <li><strong>10,000 followers:</strong> Rs.2,000-Rs.15,000 per post</li>
    <li><strong>1,00,000 followers:</strong> Rs.20,000-Rs.2,00,000 per post</li>
    <li><strong>10,00,000 followers:</strong> Rs.2,00,000-Rs.20,00,000 per post</li>
  </ul>
  <div class="highlight">🌟 Pro Tip: Brands prefer a micro-influencer with 10,000 loyal niche followers over a general account with 1,00,000 random followers. Engagement rate is king!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

CHATGPT_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>How to Earn Money with ChatGPT in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Learn how to use ChatGPT and AI tools to earn money online in India 2025. 8 proven methods to make Rs.50,000+ per month with AI.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>How to Earn Money with <span>ChatGPT</span> and AI Tools?</h1>
  <p>Artificial Intelligence is the biggest opportunity of this decade. People who learn to use AI tools like ChatGPT are earning lakhs per month — by working smarter, not harder.</p>
  <div class="highlight">🤖 Earnings: Rs.20,000 to Rs.2,00,000+ per month | Tools: ChatGPT (free version available)</div>
  ''' + AD_BANNER + '''
  <h2>8 Ways to Earn Money with ChatGPT in 2025</h2>
  <h3>1. AI Content Writing Service</h3>
  <p>Use ChatGPT to write blog articles, website content, and social media posts for clients. Charge Rs.500 to Rs.3,000 per article and use ChatGPT to produce them in minutes.</p>
  <h3>2. AI-Powered Freelancing on Fiverr</h3>
  <p>Offer services on Fiverr powered by AI — script writing, email writing, business plans, cover letters. With ChatGPT, complete gigs in a fraction of the time and take on more clients.</p>
  <h3>3. Create and Sell AI-Written Ebooks</h3>
  <p>Use ChatGPT to write ebooks on popular topics. Sell them on Amazon Kindle, Gumroad, or Instamojo. Once published, ebooks generate passive income indefinitely.</p>
  <h3>4. AI YouTube Channel</h3>
  <p>Use ChatGPT for scripts, AI tools for images and voiceovers to create faceless YouTube channels. Many creators earn Rs.30,000 to Rs.2,00,000 per month from these channels.</p>
  <h3>5. AI Blog with AdSense</h3>
  <p>Use ChatGPT to write SEO-optimized blog posts at scale. A blog publishing 3 to 5 articles per week can rank on Google faster and earn significant AdSense revenue.</p>
  <h3>6. Prompt Engineering Consulting</h3>
  <p>Businesses pay Rs.10,000 to Rs.1,00,000 for someone who can set up AI workflows and train teams to use AI tools. Very little competition in India right now.</p>
  <h3>7. AI Social Media Management</h3>
  <p>Use ChatGPT to create content calendars, captions, and hashtag strategies for small businesses. Charge Rs.5,000 to Rs.20,000 per month per client.</p>
  <h3>8. Sell AI Prompt Packs</h3>
  <p>Create collections of high-quality ChatGPT prompts for specific uses. Sell on Gumroad for Rs.299 to Rs.999 per pack.</p>
  ''' + AD_NATIVE + '''
  <h2>Getting Started with ChatGPT</h2>
  <div class="step-box"><h3>Step 1: Create a Free Account</h3><p>Go to chat.openai.com and create a free account. The free version is powerful enough to start earning.</p></div>
  <div class="step-box"><h3>Step 2: Learn Prompt Writing</h3><p>The quality of output depends on how well you write prompts. Be specific, provide context, and ask for the format you want.</p></div>
  <div class="step-box"><h3>Step 3: Choose One Service to Start</h3><p>Pick one service — like AI content writing — and master it. Create 3 to 5 samples, then start offering on Fiverr or to local businesses.</p></div>
  <div class="highlight">⚡ Pro Tip: AI skills are the most in-demand skill of 2025. Those who learn AI tools now will have a massive advantage. The best time to start is today!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

FREELANCING_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>Complete Freelancing Guide for Beginners in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Complete guide to starting freelancing from zero in India 2025. Find clients, earn money and build a full-time freelancing career.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>Complete <span>Freelancing</span> Guide for Beginners in India</h1>
  <p>Freelancing means selling your skills directly to clients without being a full-time employee. India has over 15 million freelancers — the second largest freelancing nation in the world.</p>
  <div class="highlight">💻 Earnings: Rs.20,000 to Rs.2,00,000+ per month | Investment: Rs.0 — your skills are all you need</div>
  ''' + AD_BANNER + '''
  <h2>Most In-Demand Freelancing Skills in India 2025</h2>
  <ul>
    <li><strong>Writing and Content Creation</strong> — Blog writing, copywriting, script writing</li>
    <li><strong>Graphic Design</strong> — Logo design, social media graphics, UI/UX</li>
    <li><strong>Web Development</strong> — HTML, CSS, WordPress, React</li>
    <li><strong>Video Editing</strong> — YouTube videos, Reels, promotional videos</li>
    <li><strong>Digital Marketing</strong> — SEO, social media, paid ads</li>
    <li><strong>Data Entry and Virtual Assistance</strong> — Simple tasks, great for beginners</li>
    <li><strong>Translation</strong> — English to Hindi, regional languages</li>
    <li><strong>Accounting and Finance</strong> — Bookkeeping, GST filing, tax consulting</li>
  </ul>
  <h2>Best Platforms for Indian Freelancers</h2>
  <div class="step-box"><h3>Fiverr</h3><p>Best for beginners. Create a profile, list your services as gigs, and wait for clients. Great for design, writing, and tech services.</p></div>
  <div class="step-box"><h3>Upwork</h3><p>More professional with higher paying clients. You apply for jobs posted by clients. Best for experienced freelancers seeking long-term contracts.</p></div>
  <div class="step-box"><h3>Freelancer.com</h3><p>Similar to Upwork but more beginner-friendly. Bid on projects matching your skills.</p></div>
  <div class="step-box"><h3>LinkedIn</h3><p>Excellent for finding high-paying Indian corporate clients. Works best for writing, marketing, and consulting.</p></div>
  ''' + AD_NATIVE + '''
  <h2>How to Start Freelancing from Zero</h2>
  <div class="step-box"><h3>Step 1: Identify Your Best Skill</h3><p>Pick one skill you are good at and enjoy. Do not try to offer 10 services when starting.</p></div>
  <div class="step-box"><h3>Step 2: Build a Basic Portfolio</h3><p>Create 3 to 5 sample projects demonstrating your skill. These can be self-initiated projects — write sample articles, design sample logos.</p></div>
  <div class="step-box"><h3>Step 3: Set Your Pricing</h3><p>Research what others charge on Fiverr and Upwork. As a beginner, price slightly lower to attract first clients. Increase rates once you have reviews.</p></div>
  <div class="step-box"><h3>Step 4: Find Your First Client</h3><p>Tell friends and family, join Facebook entrepreneur groups, send personalized cold emails to local businesses, post on LinkedIn about your service.</p></div>
  <div class="step-box"><h3>Step 5: Over-Deliver and Ask for Reviews</h3><p>For your first 10 clients, give more than expected. Then politely ask for a review. Positive reviews make getting future clients 10x easier.</p></div>
  <h2>Freelancer Earnings in India</h2>
  <ul>
    <li><strong>Beginner (0-6 months):</strong> Rs.5,000 to Rs.20,000 per month</li>
    <li><strong>Intermediate (6-18 months):</strong> Rs.20,000 to Rs.60,000 per month</li>
    <li><strong>Experienced (2+ years):</strong> Rs.60,000 to Rs.2,00,000+ per month</li>
  </ul>
  <div class="highlight">💪 Pro Tip: Start with the skills you have today. Your first client will teach you more than any course. Do not wait until you feel ready!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

AFFILIATE_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>How to Earn Money from Affiliate Marketing in India 2025 - PaiseKamao.in</title>
<meta name="description" content="Complete affiliate marketing guide for beginners in India 2025. Earn commission by promoting Amazon, Flipkart and other products online.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <a href="/" class="back">← Back to Home</a>
  <h1>How to Earn Money from <span>Affiliate Marketing</span> in India?</h1>
  <p>Affiliate marketing is one of the most powerful ways to earn passive income. Promote other companies' products and earn a commission every time someone buys through your link. No investment, no inventory, no customer support needed.</p>
  <div class="highlight">🛒 Earnings: Rs.5,000 to Rs.5,00,000+ per month | Investment: Rs.0 — completely free to start</div>
  ''' + AD_BANNER + '''
  <h2>How Affiliate Marketing Works</h2>
  <p>Simple process: Join an affiliate program → Get a unique tracking link → Share that link on your blog, YouTube, Instagram, or WhatsApp → Someone clicks and buys → You earn a commission. Commission rates range from 2% to 70% depending on the product.</p>
  <h2>Best Affiliate Programs for Indians in 2025</h2>
  <div class="step-box"><h3>Amazon Associates India</h3><p>Most popular in India. Promote any of Amazon's millions of products. Commission 1% to 10% depending on category. Easy to join, trusted by buyers, great for beginners.</p></div>
  <div class="step-box"><h3>Flipkart Affiliate Program</h3><p>Focused on the Indian market. Strong for electronics and fashion. Commission rates up to 12%.</p></div>
  <div class="step-box"><h3>Hostinger / Bluehost Affiliate</h3><p>Promote web hosting and earn Rs.3,000 to Rs.10,000 per sale. One of the highest paying affiliate categories.</p></div>
  <div class="step-box"><h3>Zerodha / Groww Affiliate</h3><p>Earn Rs.300 to Rs.500 for every new investor who signs up. Finance affiliates pay well due to high lifetime value.</p></div>
  ''' + AD_NATIVE + '''
  <h2>How to Promote Affiliate Links</h2>
  <h3>Through a Blog</h3>
  <p>Write detailed product reviews, comparison articles, and buying guides. A blog post can earn commission for years after it is published.</p>
  <h3>Through YouTube</h3>
  <p>Create product review videos and tutorials. Add your affiliate link in the video description. YouTube videos rank on both YouTube and Google search.</p>
  <h3>Through Instagram and Facebook</h3>
  <p>Share product recommendations in posts, stories, and reels. Put your affiliate link in bio using tools like Linktree.</p>
  <h3>Through WhatsApp Groups</h3>
  <p>Join niche WhatsApp groups and share relevant product deals with your affiliate link. Works well during Diwali and Big Billion Days sales.</p>
  <h2>Affiliate Earnings Potential</h2>
  <ul>
    <li><strong>Beginner (first 6 months):</strong> Rs.1,000 to Rs.10,000 per month</li>
    <li><strong>Intermediate (6-18 months):</strong> Rs.10,000 to Rs.50,000 per month</li>
    <li><strong>Advanced (2+ years):</strong> Rs.50,000 to Rs.5,00,000+ per month</li>
  </ul>
  <div class="highlight">🎯 Pro Tip: Only recommend products you have genuinely used or researched. Your audience trusts your recommendations — if you send them to a bad product, you lose that trust permanently!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

ABOUT_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>About Us - PaiseKamao.in</title>
<meta name="description" content="Learn about PaiseKamao.in - India's trusted platform for earning money online. Our mission is to help every Indian achieve financial freedom.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <h1>About <span>PaiseKamao.in</span></h1>
  <p>Welcome to PaiseKamao.in — India's trusted guide for earning money online. We are dedicated to helping every Indian discover legitimate, proven methods to build income from the comfort of their home.</p>
  <h2>Our Mission</h2>
  <p>Our mission is simple: to provide free, honest, and actionable information that helps Indians achieve financial freedom through online earning. We believe that every person — regardless of education, background, or location — deserves access to the knowledge needed to earn money online.</p>
  <p>India has one of the largest populations of internet users in the world. Yet many people do not know how to convert their time and skills into real income using the internet. PaiseKamao.in was created to bridge this gap.</p>
  <h2>What We Offer</h2>
  <p>On PaiseKamao.in, you will find detailed step-by-step guides on every major online earning method — from Freelancing and YouTube to Blogging, Affiliate Marketing, Instagram, and AI tools like ChatGPT. Every guide is written in simple, clear language so that anyone can understand and take action.</p>
  <h2>Who Is This Website For?</h2>
  <ul>
    <li>Students looking to earn money while studying</li>
    <li>Housewives and homemakers who want financial independence</li>
    <li>Working professionals seeking additional income streams</li>
    <li>Anyone who wants to build a full-time online career</li>
    <li>People in small towns and rural areas where traditional jobs are scarce</li>
  </ul>
  <h2>Our Promise to You</h2>
  <p>We will never promote get-rich-quick schemes or fake opportunities. Every method we cover is legitimate, tested, and genuinely used by thousands of Indians every day. We are honest about how long it takes to see results and what challenges you might face.</p>
  <div class="highlight">💰 Our Goal: Help 1,00,000 Indians earn money online by 2026. Join us on this journey!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

CONTACT_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>Contact Us - PaiseKamao.in</title>
<meta name="description" content="Contact PaiseKamao.in for any questions about earning money online in India. We are happy to help!">
''' + BASE_STYLE + '''
<style>
  .contact-box { background: var(--card); border-radius: 16px; padding: 2rem; border: 1px solid rgba(255,255,255,0.07); margin: 1.5rem 0; }
  .contact-box h3 { font-family: 'Baloo 2', cursive; color: var(--gold); margin-top: 0; font-size: 1.2rem; }
</style>
</head>
<body>''' + NAV + '''
<div class="container">
  <h1>Contact <span>Us</span></h1>
  <p>We would love to hear from you! Whether you have a question about earning money online, want to suggest a new article topic, or have feedback — please reach out. We respond within 24 to 48 hours.</p>
  <div class="contact-box"><h3>📧 Email Us</h3><p>For general inquiries, content suggestions, or partnership opportunities: <strong style="color:var(--gold);">contact@paisekamao.in</strong></p></div>
  <div class="contact-box"><h3>💼 Business and Partnerships</h3><p>Interested in advertising on PaiseKamao.in or collaborating on content? We welcome partnerships with brands that genuinely help Indians earn money online.</p></div>
  <div class="contact-box"><h3>❓ Have a Question?</h3><p>If you have a specific question about any earning method covered on our site, send us an email. We will either reply personally or write a detailed article answering your question.</p></div>
  <div class="contact-box"><h3>🐛 Found an Error?</h3><p>If you found any incorrect or outdated information, please let us know. We are committed to providing accurate, up-to-date information.</p></div>
  <div class="highlight">We aim to respond to all emails within 24 to 48 hours on working days. Thank you for being part of the PaiseKamao community!</div>
</div>
''' + FOOTER + '''
</body>
</html>'''

PRIVACY_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>''' + BASE_HEAD + '''
<title>Privacy Policy - PaiseKamao.in</title>
<meta name="description" content="Privacy Policy for PaiseKamao.in. Learn how we collect, use and protect your personal information.">
''' + BASE_STYLE + '''
</head>
<body>''' + NAV + '''
<div class="container">
  <h1>Privacy <span>Policy</span></h1>
  <p><strong style="color:var(--muted);">Last Updated: January 1, 2025</strong></p>
  <p>This Privacy Policy describes how PaiseKamao.in collects, uses, and shares information about you when you use our website.</p>
  <h2>Information We Collect</h2>
  <p>We collect information you provide directly, such as when you contact us via email. We also automatically collect certain information when you visit our website, including your IP address, browser type, operating system, referring URLs, and pages visited.</p>
  <h2>Google AdSense and Advertising</h2>
  <p>We use Google AdSense to display advertisements. Google AdSense uses cookies to serve relevant ads based on your prior visits to our and other websites. You may opt out of personalized advertising by visiting Google's Ads Settings at adssettings.google.com.</p>
  <h2>Third Party Ad Networks</h2>
  <p>We work with third-party advertising networks to display ads on our website. These networks may use cookies and similar tracking technologies to collect information about your visits to provide relevant advertisements.</p>
  <h2>Cookies</h2>
  <p>Our website uses cookies to improve your browsing experience and enable advertising functionality. You can control cookies through your browser settings. Disabling cookies may affect the functionality of our website.</p>
  <h2>How We Use Your Information</h2>
  <p>We use the information we collect to operate and improve our website, respond to your comments and questions, analyze website traffic, and display relevant advertisements through our advertising partners.</p>
  <h2>Information Sharing</h2>
  <p>We do not sell, trade, or rent your personal information to third parties. We may share information with service providers who assist us in operating our website, only to the extent necessary for them to perform those services.</p>
  <h2>Children's Privacy</h2>
  <p>Our website is not directed to children under the age of 13. We do not knowingly collect personal information from children under 13.</p>
  <h2>Contact Us</h2>
  <p>If you have any questions about this Privacy Policy, please contact us at: <strong style="color:var(--gold);">contact@paisekamao.in</strong></p>
</div>
''' + FOOTER + '''
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

@app.route('/how-to-earn-on-instagram')
def instagram():
    return render_template_string(INSTAGRAM_HTML)

@app.route('/how-to-earn-with-chatgpt')
def chatgpt():
    return render_template_string(CHATGPT_HTML)

@app.route('/how-to-start-freelancing')
def freelancing():
    return render_template_string(FREELANCING_HTML)

@app.route('/how-to-earn-from-affiliate-marketing')
def affiliate():
    return render_template_string(AFFILIATE_HTML)

@app.route('/about')
def about():
    return render_template_string(ABOUT_HTML)

@app.route('/contact')
def contact():
    return render_template_string(CONTACT_HTML)

@app.route('/privacy-policy')
def privacy():
    return render_template_string(PRIVACY_HTML)

@app.route('/sitemap.xml')
def sitemap():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://paisekamao.onrender.com/</loc><priority>1.0</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-on-fiverr</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-start-youtube-channel</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-from-blogging</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-on-instagram</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-with-chatgpt</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-start-freelancing</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/how-to-earn-from-affiliate-marketing</loc><priority>0.8</priority></url>
  <url><loc>https://paisekamao.onrender.com/about</loc><priority>0.5</priority></url>
  <url><loc>https://paisekamao.onrender.com/contact</loc><priority>0.5</priority></url>
  <url><loc>https://paisekamao.onrender.com/privacy-policy</loc><priority>0.3</priority></url>
</urlset>''', 200, {'Content-Type': 'application/xml'}

@app.route('/ads.txt')
def ads_txt():
    return "google.com, pub-1709475506645918, DIRECT, f08c47fec0942fa0", 200, {'Content-Type': 'text/plain'}

@app.route('/8fb04d7006a3a8b88912.txt')
def hilltopads_verify():
    return "8fb04d7006a3a8b88912", 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
