# Firefighter-Real-Time-Reporting
Mobile app and dashboard for real-time incident reporting and firefighter coordination.

A **real-time incident reporting system** designed to improve firefighter coordination during emergencies.  
The solution includes:  
- **Mobile App (Flutter)** for field reporting.  
- **Web Dashboard (React + TypeScript)** for monitoring.  
- **Backend (Django + PostgreSQL + Firebase)** for data management, authentication, and real-time updates.  

---

## 🚀 Tech Stack
- **Mobile App:** Flutter (Dart)  
- **Dashboard:** React.js + TypeScript  
- **Backend:** Django (Python)  
- **Database:** PostgreSQL (primary data storage)  
- **Realtime & Auth:** Firebase (Auth, Firestore, Cloud Messaging)  
- **Others:** REST API, WebSocket, Docker (optional for deployment)  

---

## 📱 Features
### Mobile App (Flutter)
- Real-time incident reporting with text, images, and GPS.  
- Live firefighter location tracking.  
- Push notifications for new assignments (via Firebase Cloud Messaging).  

### Dashboard (React + TypeScript)
- Monitor incident reports on an interactive map.  
- Assign and manage firefighter teams in real-time.  
- Generate performance and incident reports.  

### Backend (Django + PostgreSQL + Firebase)
- **Django REST Framework** to connect mobile & dashboard.  
- PostgreSQL for structured and relational data (incidents, firefighter profiles, reports).  
- Firebase Authentication for secure login.  
- Firebase Firestore for real-time event synchronization.  
- Firebase Cloud Storage for uploading incident evidence.  

---

## 🛠️ Installation & Setup

### Backend (Django + PostgreSQL + Firebase)
1. Clone repository:
   ```bash
   git clone https://github.com/your-username/firefighter-realtime-report.git
   cd firefighter-realtime-report/backend
