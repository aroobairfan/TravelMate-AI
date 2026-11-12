🌍 TravelMate AI – Tourism Chatbot

TravelMate AI is an AI-powered tourism chatbot developed using Python, Streamlit, and Ollama (Llama 3.2). It helps users explore tourist destinations, discover local food, plan trips, and get travel recommendations.

✨ Features
🏔️ Explore famous tourist destinations.
🇵🇰 Discover popular places in Pakistan.
🏨 Get hotel and accommodation guidance.
🍕 Explore famous local food.
🗺️ Generate personalized travel itineraries.
💰 Get estimated travel budget suggestions.
🌦️ Learn about the best time to visit destinations.
💬 Interactive AI-powered chat interface.
🗑️ Clear chat history.
⚙️ Select between available Llama 3.2 models.
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
Streamlit	Web application interface
Ollama	Local AI model execution
Llama 3.2	Large Language Model
📁 Project Structure
text
TravelMate-AI/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore

⚙️ Installation and Setup
1. Clone the Repository
bash
git clone https://github.com/YOUR-USERNAME/TravelMate-AI.git

2. Open the Project Folder
bash
cd TravelMate-AI

3. Install Required Libraries
bash
pip install -r requirements.txt

4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

5. Download the AI Model

Open your terminal and run:

bash
ollama pull llama3.2

6. Start Ollama

If Ollama is not already running in the background:

bash
ollama serve

7. Run the Streamlit Application

Open another terminal in your project folder and execute:

bash
streamlit run app.py

8. Open in Browser

Visit:

http://localhost:8501

Your TravelMate AI chatbot is now ready!

💡 Example Questions

Try asking the chatbot:

What are the best tourist places in Pakistan?
Suggest a 3-day trip to Hunza Valley.
What is the estimated budget for visiting Skardu?
What is the famous food in Lahore?
Which is the best season to visit Murree?
Suggest beautiful tourist destinations in northern Pakistan.
🚀 Future Improvements
Destination recommendation system.
PDF-based travel guide using RAG.
Interactive maps and location information.
Weather API integration.
Hotel and restaurant recommendations.
Travel itinerary customization.
Multilingual chatbot support.
⚠️ Important Note

TravelMate AI uses a locally running Ollama model. Ollama must be installed and the selected model must be downloaded before running the application.

Travel recommendations, prices, hotel details, and travel conditions should be independently verified before making actual travel arrangements.

👨‍💻 Author

TravelMate AI – Tourism Chatbot

Developed using Python, Streamlit, and Ollama.

⭐ If you find this project useful, consider giving the repository a star!