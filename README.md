# 🎭 AI Sentiment Analysis Web App 🚀

This is an AI-driven **Sentiment Analysis Web Page** with a **modern UI** built using **Tailwind CSS**, and **real-time sentiment visualization** using **Chart.js**. The backend is powered by **Flask and TextBlob** for sentiment detection.

## 🌟 Features
✅ **Real-time Sentiment Analysis** (Positive, Neutral, Negative)  
✅ **Modern UI with Tailwind CSS**  
✅ **Interactive Chart.js Visualization** for sentiment trends  
✅ **Fast and Lightweight** Flask backend  
✅ **Easy to Deploy & Extend**  

---

## 📌 Tech Stack
### **Frontend (UI)**
- **HTML, Tailwind CSS** for styling  
- **JavaScript (Fetch API)** to communicate with backend  
- **Chart.js** for real-time sentiment visualization  

### **Backend (API)**
- **Flask** for handling requests  
- **TextBlob (NLTK)** for AI-based sentiment analysis  
- **Flask-CORS** for cross-origin support  

---

## 🚀 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/sentiment-analysis-webapp.git
cd sentiment-analysis-webapp
```

### **2️⃣ Install Backend Dependencies**
```sh
pip install flask flask-cors textblob nltk
```
📌 **One-time setup for TextBlob**  
```sh
python -m textblob.download_corpora
```

### **3️⃣ Run the Backend (Flask Server)**
```sh
python sentiment_model.py
```
> **Server will run at:** `http://127.0.0.1:5000/`

### **4️⃣ Open the Frontend**
Simply open `index.html` in your browser and start analyzing text! 🎯  

---

## 🖥️ Project Structure
```
📁 sentiment-analysis-webapp
 ├── 📄 index.html         # Frontend UI with Tailwind & Chart.js
 ├── 📄 sentiment_model.py # Flask backend with TextBlob sentiment analysis
 ├── 📄 README.md          # Project Documentation
```

---

## 📊 How It Works?
1️⃣ **User enters text** in the input box.  
2️⃣ **Frontend sends a request** to the Flask backend (`/analyze`).  
3️⃣ **Flask processes the text** with **TextBlob AI** and returns a **sentiment score**.  
4️⃣ **Chart.js dynamically updates** the sentiment score on a bar chart.  

---

## 🌟 Example Sentences
Try analyzing these sample sentences!  

✔️ **Positive:** `"I absolutely love this product! It works perfectly."`  
❌ **Negative:** `"This service is terrible. I'm very disappointed."`  
➖ **Neutral:** `"The meeting lasted for an hour and covered updates."`  
🔄 **Mixed:** `"The design is great, but the performance needs improvement."`  

---

## 🎉 Future Improvements
🚀 **BERT-based deep learning model** for better accuracy  
🎨 **More UI enhancements** like dark mode & animations  
📊 **Live sentiment tracking** for tweets & news articles  

---
## 🌎 License
This project is **open-source** under the **MIT License**.  

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a **pull request (PR)**.  


---

## Contact

For any questions or feedback, feel free to contact:

Ankit kumar

Email: your-ankitrajj1068@gmail.com

GitHub: ankit1068

## Screenshots: 
![Screenshot 2025-03-22 232008](https://github.com/user-attachments/assets/a191fab5-ddac-4eae-821e-e2d18ec63cee)





