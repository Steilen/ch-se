# ch##se

`ch##se` is a Python script designed to listen for specific offensive words through your microphone. If an offensive word is detected, the script will automatically shut down your computer.

## How It Works

The script uses the `speech_recognition` library to continuously listen to audio input from your microphone. If it recognizes any word from the predefined list of offensive words, it triggers a shutdown command.

### Offensive Words List

By default, the script is set to listen for the word **"cheese"**. You can easily modify the list of offensive words by editing the `offensive_words` variable in the script.

### Platform Support

The script is set up to work on both Windows and Linux:

- **Windows**: The script uses the `shutdown /s /t 1` command to shut down the computer.
- **Linux**: Uncomment the `shutdown now` line to enable shutdown on Linux.

## Usage

1. **Install Dependencies**: Ensure you have the `speech_recognition` library installed.

    ```bash
    pip install SpeechRecognition
    ```

2. **Run the Script**: Execute the script using Python.

    ```bash
    python main.py
    ```

3. **Listening Mode**: The script will start listening for the offensive word(s). If detected, it will shut down the computer.

## Error Handling

- **UnknownValueError**: If the audio cannot be understood, the script will notify you.
- **RequestError**: If there is an issue with the Google Speech Recognition service, the error will be printed.
- **KeyboardInterrupt**: You can safely terminate the script with `Ctrl+C`.

## Customization

- **Add/Remove Offensive Words**: Modify the `offensive_words` list to include the words you want to monitor.

- **Change Language**: The script is currently set to recognize Russian (`language='en-US'`). You can change this to another language supported by Google Speech Recognition.

## Disclaimer

Use this script responsibly. Automating a shutdown based on speech recognition could lead to unintended data loss or system interruptions.
