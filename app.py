from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>💰 PaiseKamao.in – ऑनलाइन पैसे कमाने के 15 बेस्ट तरीके</title>
<meta name="description" content="घर बैठे ऑनलाइन पैसे कमाने के 15 प्रमाणित तरीके। Freelancing, YouTube, Blogging, Affiliate Marketing और बहुत कुछ।">
<meta name="keywords" content="online paise kaise kamaye, ghar baithe paise, freelancing hindi, youtube se paise, blogging se kamai">
<meta name="google-site-verification" content="TPjYlLn0L0W216UNfKt9sg2n9McE-NvepGERkWEtZVU" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Hind:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --gold: #f5c518;
    --gold2: #e8a900;
    --dark: #0a0a12;
    --card: #12121f;
    --accent: #00e5ff;
    --green: #00ff88;
    --text: #e8e8f0;
    --muted: #7a7a9a;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--dark); color: var(--text); font-family: 'Hind', sans-serif; overflow-x: hidden; }
  .hero { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; position: relative; padding: 2rem; background: radial-gradient(ellipse at 50% 0%, rgba(245,197,24,0.15) 0%, transparent 70%), radial-gradient(ellipse at 80% 100%, rgba(0,229,255,0.1) 0%, transparent 60%); }
  .badge { display: inline-block; background: rgba(245,197,24,0.15); border: 1px solid var(--gold); color: var(--gold); padding: 0.4rem 1.2rem; border-radius: 100px; font-size: 0.85rem; letter-spacing: 0.1em; margin-bottom: 1.5rem; animation: fadeDown 0.6s ease both; }
  h1 { font-family: 'Baloo 2', cursive; font-size: clamp(2.5rem, 7vw, 5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; animation: fadeDown 0.7s ease 0.1s both; }
  h1 span { color: var(--gold); }
  .hero p { font-size: 1.2rem; color: var(--muted); max-width: 600px; line-height: 1.7; margin-bottom: 2.5rem; animation: fadeDown 0.7s ease 0.2s both; }
  .stats-row { display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; margin-top: 1rem; animation: fadeUp 0.8s ease 0.3s both; }
  .stat { text-align: center; }
  .stat .num { font-family: 'Baloo 2', cursive; font-size: 2rem; font-weight: 800; color: var(--gold); }
  .stat .label { font-size: 0.8rem; color: var(--muted); }
  .section { max-width: 1100px; margin: 0 auto; padding: 5rem 1.5rem; }
  .section-title { font-family: 'Baloo 2', cursive; font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 0.5rem; }
  .section-title span { color: var(--gold); }
  .section-sub { text-align: center; color: var(--muted); margin-bottom: 3rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 1.5rem; }
  .card { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 1.8rem; transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease; position: relative; overflow: hidden; }
  .card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--gold), var(--accent)); opacity: 0; transition: opacity 0.3s; }
  .card:hover { transform: translateY(-5px); border-color: rgba(245,197,24,0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
  .card:hover::before { opacity: 1; }
  .card-icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
  .card-num { position: absolute; top: 1.2rem; right: 1.5rem; font-family: 'Baloo 2', cursive; font-size: 3rem; font-weight: 800; color: rgba(255,255,255,0.04); line-height: 1; }
  .card h3 { font-family: 'Baloo 2', cursive; font-size: 1.3rem; font-weight: 700; margin-bottom: 0.6rem; color: #fff; }
  .card p { font-size: 0.92rem; color: var(--muted); line-height: 1.7; margin-bottom: 1rem; }
  .earn-tag { display: inline-block; background: rgba(0,255,136,0.1); border: 1px solid rgba(0,255,136,0.3); color: var(--green); font-size: 0.75rem; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 100px; }
  .diff-tag { display: inline-block; margin-left: 0.5rem; background: rgba(245,197,24,0.1); border: 1px solid rgba(245,197,24,0.3); color: var(--gold); font-size: 0.75rem; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 100px; }
  .steps { background: var(--card); border: 1px solid rgba(255,255,255,0.07); border-radius: 20px; padding: 3rem; margin-top: 4rem; }
  .steps h2 { font-family: 'Baloo 2', cursive; font-size: 1.8rem; font-weight: 800; margin-bottom: 2rem; text-align: center; }
  .step-list { display: flex; flex-direction: column; gap: 1.2rem; max-width: 700px; margin: 0 auto; }
  .step { display: flex; gap: 1.2rem; align-items: flex-start; }
  .step-num { width: 40px; height: 40px; min-width: 40px; background: linear-gradient(135deg, var(--gold), var(--gold2)); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Baloo 2', cursive; font-weight: 800; color: #000; font-size: 1rem; }
  .step-content h4 { font-family: 'Baloo 2', cursive; font-weight: 700; margin-bottom: 0.2rem; }
  .step-content p { font-size: 0.9rem; color: var(--muted); }
  .ticker-wrap { background: var(--gold); overflow: hidden; padding: 0.7rem 0; white-space: nowrap; }
  .ticker { display: inline-block; animation: ticker 25s linear infinite; }
  .ticker span { color: #000; font-weight: 700; font-family: 'Baloo 2', cursive; margin: 0 2rem; font-size: 0.95rem; }
  footer { text-align: center; padding: 3rem 1.5rem; border-top: 1px solid rgba(255,255,255,0.07); color: var(--muted); font-size: 0.9rem; }
  footer strong { color: var(--gold); }
  @keyframes fadeDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
  .reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }
  .reveal.visible { opacity: 1; transform: translateY(0); }
  @media (max-width: 600px) { .steps { padding: 2rem 1.2rem; } .stats-row { gap: 1.2rem; } }
</style>
</head>
<body>
<div class="ticker-wrap">
  <div class="ticker">
    <span>💰 Freelancing से ₹50,000/माह</span>
    <span>📹 YouTube से लाखों कमाएं</span>
    <span>✍️ Blogging से Passive Income</span>
    <span>🛒 Affiliate Marketing</span>
    <span>📱 App बनाकर पैसे</span>
    <span>🎓 Online Teaching</span>
    <span>💰 Freelancing से ₹50,000/माह</span>
    <span>📹 YouTube से लाखों कमाएं</span>
    <span>✍️ Blogging से Passive Income</span>
    <span>🛒 Affiliate Marketing</span>
    <span>📱 App बनाकर पैसे</span>
    <span>🎓 Online Teaching</span>
  </div>
</div>
<section class="hero">
  <div class="badge">🇮🇳 100% भारतीयों के लिए</div>
  <h1>ऑनलाइन <span>पैसे कमाओ</span><br>घर बैठे!</h1>
  <p>2025 के सबसे बेस्ट और प्रमाणित 15 तरीके जिनसे आप महीने में ₹10,000 से ₹1,00,000+ कमा सकते हैं — बिना investment के भी।</p>
  <div class="stats-row">
    <div class="stat"><div class="num">50K+</div><div class="label">लोग कमा रहे हैं</div></div>
    <div class="stat"><div class="num">15</div><div class="label">तरीके</div></div>
    <div class="stat"><div class="num">₹0</div><div class="label">कई तरीकों में investment</div></div>
    <div class="stat"><div class="num">24/7</div><div class="label">Passive Income</div></div>
  </div>
</section>
<section class="section">
  <div class="section-title">15 तरीके <span>पैसे कमाने के</span></div>
  <p class="section-sub">हर तरीके में कमाई की जानकारी और शुरुआत कैसे करें</p>
  <div class="grid">
    <div class="card reveal"><span class="card-num">01</span><span class="card-icon">💻</span><h3>Freelancing</h3><p>Upwork, Fiverr, Freelancer पर अपनी skills बेचें। Web design, writing, video editing, coding — कोई भी skill काम आती है।</p><span class="earn-tag">₹20K–₹1L/माह</span><span class="diff-tag">आसान शुरुआत</span></div>
    <div class="card reveal"><span class="card-num">02</span><span class="card-icon">📹</span><h3>YouTube Channel</h3><p>किसी भी topic पर videos बनाओ — cooking, education, tech review, comedy। AdSense + Sponsorship से जबरदस्त income।</p><span class="earn-tag">₹10K–₹5L/माह</span><span class="diff-tag">धैर्य चाहिए</span></div>
    <div class="card reveal"><span class="card-num">03</span><span class="card-icon">✍️</span><h3>Blogging</h3><p>WordPress पर blog बनाओ। SEO से traffic लाओ और Google AdSense + Affiliate से Passive Income कमाओ।</p><span class="earn-tag">₹5K–₹2L/माह</span><span class="diff-tag">6-12 महीने</span></div>
    <div class="card reveal"><span class="card-num">04</span><span class="card-icon">🛒</span><h3>Affiliate Marketing</h3><p>Amazon, Flipkart, या किसी brand का product promote करो और हर sale पर commission कमाओ।</p><span class="earn-tag">₹5K–₹3L/माह</span><span class="diff-tag">Medium</span></div>
    <div class="card reveal"><span class="card-num">05</span><span class="card-icon">🎓</span><h3>Online Teaching</h3><p>Vedantu, Unacademy, Udemy पर पढ़ाओ या खुद course बनाओ। एक बार बनाओ, बार-बार बिको।</p><span class="earn-tag">₹15K–₹2L/माह</span><span class="diff-tag">आसान</span></div>
    <div class="card reveal"><span class="card-num">06</span><span class="card-icon">📱</span><h3>Social Media Management</h3><p>Local businesses के Instagram/Facebook page manage करो। हर client से ₹5,000–₹20,000/माह charge करो।</p><span class="earn-tag">₹20K–₹80K/माह</span><span class="diff-tag">आसान</span></div>
    <div class="card reveal"><span class="card-num">07</span><span class="card-icon">📸</span><h3>Stock Photography</h3><p>Shutterstock, Getty Images पर अपनी photos बेचो। एक photo बार-बार बिकती है — pure passive income।</p><span class="earn-tag">₹2K–₹30K/माह</span><span class="diff-tag">शुरुआती</span></div>
    <div class="card reveal"><span class="card-num">08</span><span class="card-icon">🎨</span><h3>Graphic Design</h3><p>Canva, Photoshop सीखो और logos, banners, social media posts बनाकर Fiverr पर बेचो।</p><span class="earn-tag">₹15K–₹1L/माह</span><span class="diff-tag">Medium</span></div>
    <div class="card reveal"><span class="card-num">09</span><span class="card-icon">🖥️</span><h3>Web Development</h3><p>HTML, CSS, Python/React सीखो और छोटे businesses की websites बनाओ। India में demand बहुत ज्यादा है।</p><span class="earn-tag">₹30K–₹2L/माह</span><span class="diff-tag">Hard लेकिन Worth It</span></div>
    <div class="card reveal"><span class="card-num">10</span><span class="card-icon">🤖</span><h3>AI Tools का उपयोग</h3><p>ChatGPT, Midjourney जैसे AI tools सीखो और content creation, image generation की service दो।</p><span class="earn-tag">₹20K–₹1.5L/माह</span><span class="diff-tag">नया Trend</span></div>
    <div class="card reveal"><span class="card-num">11</span><span class="card-icon">📦</span><h3>Dropshipping</h3><p>बिना stock रखे online store चलाओ। Customer order करे, supplier directly deliver करे — आप profit रखो।</p><span class="earn-tag">₹10K–₹3L/माह</span><span class="diff-tag">Medium Risk</span></div>
    <div class="card reveal"><span class="card-num">12</span><span class="card-icon">🎙️</span><h3>Podcast</h3><p>Spotify, Anchor पर podcast शुरू करो। Sponsorship, courses और affiliate से multiple income streams बनाओ।</p><span class="earn-tag">₹5K–₹1L/माह</span><span class="diff-tag">Long Term</span></div>
    <div class="card reveal"><span class="card-num">13</span><span class="card-icon">💹</span><h3>Share Market / Trading</h3><p>Zerodha, Groww पर invest करो। Dividend income और long-term wealth building के लिए best option।</p><span class="earn-tag">Variable Returns</span><span class="diff-tag">Risk है, सीखकर करो</span></div>
    <div class="card reveal"><span class="card-num">14</span><span class="card-icon">📝</span><h3>Content Writing</h3><p>Blogs, articles, copywriting करो। Internshala, LinkedIn पर Hindi/English content writers की खूब demand है।</p><span class="earn-tag">₹10K–₹60K/माह</span><span class="diff-tag">आसान शुरुआत</span></div>
    <div class="card reveal"><span class="card-num">15</span><span class="card-icon">🌐</span><h3>Domain Flipping</h3><p>सस्ते domains खरीदो (₹500-₹1000) और महंगे में बेचो। Godaddy Auctions पर लाखों में बिकते हैं अच्छे domains।</p><span class="earn-tag">₹5K–₹10L/sale</span><span class="diff-tag">Smart Investment</span></div>
  </div>
  <div class="steps reveal">
    <h2>🚀 शुरुआत कैसे करें?</h2>
    <div class="step-list">
      <div class="step"><div class="step-num">1</div><div class="step-content"><h4>अपनी Skill पहचानो</h4><p>आपको क्या आता है? Writing, Design, Teaching, Coding — कोई भी skill online पैसे बना सकती है।</p></div></div>
      <div class="step"><div class="step-num">2</div><div class="step-content"><h4>एक Platform चुनो</h4><p>शुरुआत में सिर्फ एक platform चुनो — YouTube, Fiverr, या अपना Blog। एक-एक करके बढ़ाओ।</p></div></div>
      <div class="step"><div class="step-num">3</div><div class="step-content"><h4>Free Courses लो</h4><p>YouTube पर free में सीखो। ChatGPT से help लो। Consistency रखो — 90 दिन जरूर दो।</p></div></div>
      <div class="step"><div class="step-num">4</div><div class="step-content"><h4>पहले ₹1 कमाओ</h4><p>Target ₹1 लाख नहीं, पहले ₹1 कमाओ। एक बार पहला पैसा आया — confidence आएगा।</p></div></div>
      <div class="step"><div class="step-num">5</div><div class="step-content"><h4>Scale करो</h4><p>जो काम करे, उसे और बड़ा करो। Team बनाओ, automate करो, multiple income streams बनाओ।</p></div></div>
    </div>
  </div>
</section>
<footer>
  <p style="font-family:'Baloo 2',cursive; font-size:1.5rem; font-weight:800; color:var(--gold); margin-bottom:0.5rem;">💰 PaiseKamao.in</p>
  <p>ऑनलाइन पैसे कमाने का सबसे भरोसेमंद हिंदी प्लेटफॉर्म</p>
  <p style="margin-top:1rem;">© 2025 PaiseKamao.in | <strong>Domain:</strong> paisekamao.in को GoDaddy पर register करें</p>
</footer>
<script>
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  reveals.forEach(el => observer.observe(el));
</script>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/sitemap.xml')
def sitemap():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://paisekamao.onrender.com/</loc><priority>1.0</priority></url>
</urlset>''', 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
