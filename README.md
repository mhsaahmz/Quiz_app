# Quiz App

A simple desktop quiz application built with Python and Tkinter. Users answer multiple-choice questions, and their scores are saved with a timestamp for tracking progress over time.

## Features

- Clean and simple GUI built with Tkinter
- Multiple-choice questions loaded from a JSON file
- Score tracking with history (saved in `scores.json`)
- Prevents duplicate answer submissions with disabled button state
- Automatic score display clearing after each session
- Cross-platform file path handling using `os.path`
- UTF-8 encoding support for non-English questions

## Screenshots

![Quiz App Screenshot](screenshots/screenshot.png)

## Requirements

- Python 3.x
- No external libraries required (Tkinter comes built-in with standard Python installations)

## How to Run
```bash
python quiz_app.py

## Project Structure


quiz-app/
│
├── quiz_app.py       # Main application code
├── questions.json    # Question bank (editable)
├── scores.json       # Score history (auto-generated, not tracked in git)
├── README.md
├── .gitignore
└── LICENSE

## Question Format

Questions are stored in `questions.json` using the following structure:

json
[
  {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter"],
        "answer": "Mars"
  }
]

To add new questions, simply append a new object with the same structure to the list.

## Future Improvements

- Support for dynamic question count instead of a fixed number
- Category-based question selection
- Timer for each question
- Export score history to CSV
- Dark mode UI option

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


اگه چند تا عکس داری (مثلاً صفحه شروع، صفحه سوال، صفحه نتیجه) بگو تا بخش Screenshots رو برات چندتایی بنویسم.
