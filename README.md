**Instagram Following Bot 🤖**

A Python automation project that logs into Instagram and follows a specified account using Selenium.

This project demonstrates:
1. Secure credential management using environment variables
2. Browser automation with Selenium
3. Handling dynamic web elements and popups
4. Clean project structure with proper dependency management

🚀 **Features**
1. Secure login using .env file
2. Automated search for a target account
3. Automatic navigation to profile
4. Follow button interaction
5. Basic popup handling

🛠 **Tech Stack**
1. Python 3
2. Selenium
3. python-dotenv
4. Chrome WebDriver

📦 **Installation & Setup**
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. pip install -r requirements.txt
5. Create a .env file in the root directory with:
      INSTA_USERNAME=your_instagram_username
      INSTA_PASSWORD=your_instagram_password
6. Run the script python main.py

🔐 **Security**
This project uses environment variables to protect credentials.
The .env file is excluded from version control using .gitignore.
Never upload your .env file to GitHub.

⚠️ **Disclaimer**
This project is for educational purposes only.
Automating Instagram actions may violate their terms of service and can result in account restrictions. Use responsibly.

📌 **Future Improvements**
1. Improved anti-detection techniques
2. Human-like delays and interaction patterns
3. Better exception handling
4. Logging system instead of print statements
5. Modular project structure

👨‍💻 **Author** 
Siddharth Goutham
Created on: 25-02-2026

Created as a learning project to understand web automation, environment management, and clean repository practices.
