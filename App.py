# SecureCheck - Data Breach Awareness Platform
# IT420 Project - Group 5
# Refactored version with separated components

from flask import Flask, request, render_template
from security_tools import check_password_hibp, check_email_xon

app = Flask(__name__)

@app.route("/")
def home():
    content = """
    <h1>Welcome to SecureCheck</h1>
    <div class="card warning">
      <h3>⚠️ Mandatory Ethics Check</h3>
      <p>Before using our tools, you must read and agree to the 
      <a href="/ethics">Ethical User Agreement</a>. 
      <strong>Do not</strong> check credentials that do not belong to you.</p>
    </div>
    
    <div class="card neutral">
      <h3>Our Mission</h3>
      <p>SecureCheck is dedicated to raising awareness about data breaches. 
      We provide transparency tools to help you secure your digital identity.</p>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px;">
      <div class="card">
        <h3>🔐 Password Check</h3>
        <p>Check if your password is compromised using privacy-safe k-anonymity.</p>
        <a href="/security"><button>Go to Tool</button></a>
      </div>
      <div class="card">
        <h3>📧 Email Check</h3>
        <p>Scan public breach databases for your email address.</p>
        <a href="/security"><button>Go to Tool</button></a>
      </div>
    </div>

    <h2>About SecureCheck</h2>
    <div class="card neutral">
      <h3>Project Description</h3>
      <p>Developed for the IT420 Computer Ethics course, this project aims to demonstrate 
      how security tools can be built ethically. We address the 'Dual-Use' dilemma by 
      implementing strict technical and policy controls.</p>
    </div>

    <h2>Technical Methodology</h2>
    <div class="card good">
      <h3>k-Anonymity (Privacy Preserving)</h3>
      <p>We utilize the k-anonymity model for password checking. This means we never 
      send your full password (or even its full hash) to any server. We only send the 
      first 5 characters of the hash, ensuring mathematical anonymity.</p>
    </div>
    """
    return render_template("base.html", content=content, page='home')


@app.route("/ethics")
def ethics():
    content = """
    <h1>Ethical User Agreement</h1>
    <p>This agreement governs your use of the SecureCheck platform.</p>

    <div class="card neutral">
      <h3>1. Privacy & Data Handling</h3>
      <p>We are committed to data minimization. We do not store logs of your queries. 
      Your IP address is processed transiently for the request but not retained.</p>
    </div>

    <div class="card bad">
      <h3>2. Prohibited Activities</h3>
      <p><strong>You strictly agree NOT to:</strong></p>
      <ul>
        <li>Use this service to verify credentials stolen from others.</li>
        <li>Automate queries for the purpose of credential stuffing.</li>
        <li>Use the data obtained here for harassment or social engineering.</li>
      </ul>
    </div>

    <div class="card warning">
      <h3>3. Limitation of Liability</h3>
      <p>This tool is for educational purposes. A 'Safe' result does not guarantee 
      that a credential is secure against all threats. We are not liable for any 
      damages arising from the use of this service.</p>
    </div>

    <div class="card good">
      <h3>Acceptance</h3>
      <p>By using the tools on this website, you implicitly accept these terms.</p>
    </div>
    """
    return render_template("base.html", content=content, page='ethics')


@app.route("/security", methods=["GET", "POST"])
def security():
    password_res_html = ""
    email_res_html = ""
    
    if request.method == "POST":
        # Handle password check
        if request.form.get("pw"):
            pw = request.form.get("pw", "")
            count = check_password_hibp(pw)
            if count is None:
                password_res_html = '<div class="card warning">⚠️ Error connecting to API.</div>'
            elif count == 0:
                password_res_html = '<div class="card good"><h3>✅ Safe</h3><p>No breaches found.</p></div>'
            else:
                password_res_html = f'<div class="card bad"><h3>⛔ BREACHED</h3><p>Found in {count:,} breaches!</p></div>'
        
        # Handle email check
        if request.form.get("email"):
            email = request.form.get("email", "")
            breaches = check_email_xon(email)
            if breaches is None:
                email_res_html = '<div class="card warning">⚠️ Error connecting to API.</div>'
            elif not breaches:
                email_res_html = '<div class="card good"><h3>✅ Safe</h3><p>No breaches found.</p></div>'
            else:
                list_items = "".join([f"<li>{b}</li>" for b in breaches])
                email_res_html = f'<div class="card bad"><h3>⛔ BREACHED</h3><p>Found in:</p><ul>{list_items}</ul></div>'
    
    content = f"""
    <h1>Security Check Center</h1>
    <div class="card neutral">
      <p>Check both your password security and email breach status using our privacy-safe tools.</p>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
      <div>
        <h2>🔐 Password Check</h2>
        <div class="card neutral">
          <p>Check if your password is compromised using k-anonymity.</p>
          <form method="post">
            <input type="password" name="pw" placeholder="Enter password...">
            <button type="submit">Check Password</button>
          </form>
          <small>Powered by Have I Been Pwned API (k-anonymity)</small>
        </div>
        {password_res_html}
      </div>

      <div>
        <h2>📧 Email Check</h2>
        <div class="card neutral">
          <p>Check if your email appears in public breach databases.</p>
          <form method="post">
            <input type="email" name="email" placeholder="name@example.com">
            <button type="submit">Check Email</button>
          </form>
          <small>Powered by XposedOrNot API</small>
        </div>
        {email_res_html}
      </div>
    </div>

    <div class="card warning" style="margin-top: 20px;">
      <h3>⚠️ Privacy Notice</h3>
      <p>We never store your queries or credentials. Passwords are processed using k-anonymity 
      (only first 5 characters of hash sent). Email checks are performed against public breach databases.</p>
    </div>
    """
    return render_template("base.html", content=content, page='security')


if __name__ == "__main__":
    app.run(debug=True, port=5000)