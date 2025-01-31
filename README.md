
# Cliffhanger AI
Cliffhanger AI is a personal AI-powered assistant inspired by J.A.R.V.I.S., equipped with features like voice recognition, task automation, natural language processing, and image generation. This Python-based assistant leverages APIs such as OpenAI, Hugging Face, and pywhatkit to create a seamless interactive experience.

## Features


#### Voice Recognition:

Processes spoken commands using the speech_recognition library.
Translates commands dynamically for better language support.



#### **Task Management:**

Add, read, and notify about daily tasks using simple voice commands.



#### **Web Automation:**

Opens YouTube, Google, or performs searches on Bing based on commands.



#### **Wikipedia Search:**

Provides concise summaries for queried topics.



#### **WhatsApp Messaging:**

Sends scheduled WhatsApp messages using the pywhatkit library.



#### **Email Automation:**

Sends emails via Gmail with preconfigured credentials and app passwords.



#### **AI Chat Integration:**

Uses OpenAI's models (or compatible APIs) to respond intelligently to queries.
Maintains conversational context for ongoing interactions.


#### **Image Generation:**

Generates images using local models (like Stable Diffusion) or Hugging Face APIs.
Allows choosing between local or API-based generation dynamically.




#### **Screenshot Utility:**

Captures screenshots of the current screen and saves them locally.



#### **Text-to-Speech (TTS):**

Provides real-time audio responses with text translation capabilities.




## Installation
### Prerequisites

Python 3.8 or above
Install the required Python libraries:
```bash
pip install -r requirements.txt
```


### Required Libraries
The project uses the following Python libraries:

pyttsx3 – Text-to-speech functionality. <br>

**speech_recognition** – Voice recognition for taking commands. <br>
**pyautogui** – Screen automation and screenshot capabilities. <br>
**wikipedia** – Fetches summaries from Wikipedia. <br>
**pywhatkit** – For sending WhatsApp messages and emails. <br>
**tkinter** – GUI for displaying screenshots. <br>
**Pillow** – Image processing. <br>
**openai** – For AI chat integration and text generation. <br>
**mtranslate** – Language translation. <br>
**plyer** – Desktop notifications. <br>

### Setup

Clone the repository:
```bash
git clone https://github.com/Fasiuddin22/Cliffhanger-AI.git
```


Navigate to the project folder:
```bash
cd Cliffhanger-AI
```


Install dependencies:
```bash
pip install -r requirements.txt
```


Add your credentials:

Replace the placeholders in the script for:

OpenAI API key <br>

Gmail App Password <br>

Hugging Face token (if using image generation APIs). <br>

cohere token <br>






## Usage

Run the program:
```bash
python main.py
```


Interact with Cliffhanger AI through voice commands or text inputs.
**Example commands:**

"What is the time?" <br>
"Add a new task: Buy groceries." <br>
"Send a WhatsApp message." <br>
"Search Wikipedia about Python programming." <br>
"Generate an image of a futuristic city." <br>




## Customizing the Code

**Email Automation:**
Update your Gmail credentials and app password in the send_email() function.
**API Integration:**
Replace the placeholders for OpenAI and Hugging Face API keys in the main.py file.


## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch:
```bash
git checkout -b feature-name
```


Commit your changes
```bash
git commit -m "Add some feature"
```


Push the branch:
```bash
git push origin feature-name
```


Open a pull request.


## License
This project is licensed under the [MIT License](https://mit-license.org/).

## Contact
For questions or support, feel free to reach out:

Email: [mdfasiuddin2210@gmail.com](mailto:mdfasiuddin2210@gmail.com)
GitHub: [Fasiuddin22](https://github.com/Fasiuddin22)


Let me know if you'd like to add or modify any specific details!
