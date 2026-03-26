# SecureCheck - Data Breach Awareness Platform

**IT420 Computer Ethics Project - Group 5**

## 🎯 Overview

SecureCheck is a web-based platform designed to help users check if their passwords and email addresses have been compromised in data breaches. The application demonstrates how security tools can be built ethically while addressing the "Dual-Use" dilemma through strict technical and policy controls.

This project was developed for the **IT420 Computer Ethics course** at **Al Imam Mohammad Ibn Saud Islamic University**.

---

## 👥 Team Members

| Name | Role |
|------|------|
| **Fahad AlGhamdi** | Project Lead & Backend Developer |
| **Turki AlShaalan** | Frontend Developer & UI/UX Designer |
| **Ahmed AlAsmari** | Security Implementation & API Integration |
| **Mushari Hussainan** | Documentation & Testing Lead |

---

## 🔧 Features

### Password Breach Checker
- Uses **k-Anonymity** model to check passwords against the Have I Been Pwned database
- **Privacy-safe**: Only sends first 5 characters of SHA-1 hash to the API
- Full password hash never leaves the user's device

### Email Breach Checker
- Checks email addresses against the XposedOrNot public breach database
- Displays list of breaches if found
- Shows "Safe" status if no breaches detected

### Ethical User Agreement
- Mandatory ethics page before using the tools
- Clear terms of service and prohibited activities
- Data minimization policy

---

## 🛠 Technical Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python (Flask) |
| **Security Tools** | Python requests, hashlib |
| **Frontend** | HTML, CSS (Wireframe style) |
| **APIs** | Have I Been Pwned API, XposedOrNot API |
| **Server** | Flask Development Server |

---

## 💡 How It Works

### Password Checking (k-Anonymity)
```
1. User enters password
2. Password is hashed using SHA-1
3. Only the first 5 characters of the hash are sent to the API
4. API returns all hashes starting with those 5 characters
5. Local search finds exact match (if any)
6. Result is displayed to user
```

### Email Checking
```
1. User enters email address
2. Email is sent to XposedOrNot API
3. API returns breach data (if found)
4. Results are displayed to user
```

---

## 🔒 Privacy & Security

### Data Handling
- **No data storage**: Queries are not logged or stored
- **Transient processing**: IP addresses are processed but not retained
- **k-Anonymity**: Passwords are never transmitted in full

### Security Measures
- HTTPS API connections only
- No sensitive data in URLs
- Local hash comparison (password never leaves device)
- User-Agent header for API identification

---

## 📦 Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. Clone or download the project
2. Install dependencies:

```bash
pip install flask requests
```

---

## 🚀 Running the Application

### Start the Server

```bash
python App.py
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

### Available Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with tool overview |
| `/ethics` | Ethical User Agreement |
| `/security` | Security check tools (Password & Email) |

---

## ⚖️ Ethical Considerations

This project addresses the **Dual-Use Dilemma** in cybersecurity:

### Technical Controls
- k-Anonymity prevents mass password harvesting
- No database storage of user queries
- Rate limiting through API design

### Policy Controls
- Mandatory ethics agreement
- Clear prohibited activities list
- Educational purpose disclaimer
- No liability for misuse

### Educational Value
- Demonstrates ethical security tool development
- Shows how privacy-preserving techniques work
- Teaches about data breach awareness

---

## 📄 License

This project is developed for educational purposes as part of the IT420 Computer Ethics course.

---

## 🙏 Acknowledgments

- **Have I Been Pwned** for the password breach API
- **XposedOrNot** for the email breach API
- **Al Imam Mohammad Ibn Saud Islamic University** for the course support
- **IT420 Course Instructors** for guidance

---

*Last Updated: 2025*
*Group 5 - IT420 Computer Ethics*