# Addition Quiz with Voice Interaction

This is a Python program that helps users practice addition through a voice-based quiz. It listens for spoken answers, checks the responses, and provides feedback. Users can exit the quiz anytime by pressing the 'q' key.

## Features:
- Voice-based interaction using **speech recognition** and **text-to-speech**.
- Randomized addition questions with single-digit numbers.
- User input is captured through voice, and the answer is evaluated.
- Users can exit the program by pressing the 'q' key.

## Technologies Used:
- **Speech Recognition** (`speech_recognition`): Captures and transcribes spoken language to text.
- **Text-to-Speech** (`pyttsx3`): Converts text responses to speech.
- **Keyboard Input** (`keyboard`): Detects keypresses to quit the program.

## Installation:
To get started, you need to have Python installed along with the following libraries:

1.  **speech_recognition**
2.  **pyttsx3**
3.  **keyboard**

You can install these libraries via pip:

```bash
pip install SpeechRecognition pyttsx3 keyboard
```
## Usage:

- Run the program by executing ``` python Audioquiz.py ```
- The program will start the addition quiz, and it will ask you random addition questions.
- Respond to each question by speaking the answer.
- If you're ready to stop, press the 'q' key to exit the quiz.

## Example interaction

```bash
Question: What is 3 + 2?
Listening...
You said: 5
Correct! Well done.
```
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
