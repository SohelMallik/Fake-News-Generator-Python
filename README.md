# 📰 Fake News Generator

A fun, India-themed satirical headline generator built with Python. Combines quirky subjects, absurd actions, and real city names to produce hilarious breaking news headlines — because sometimes, the news writes itself.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Testing](#testing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

**Fake News Generator** is a lightweight Python script that generates absurd, satirical news headlines inspired by Indian cities and culture. Whether you need a laugh, a writing prompt, or just want to see what happens when Ranchi Zoo trains parrots to mimic traffic rules — this tool has you covered.

It supports two modes: fully random generation (great for surprises) and custom input (great for targeted humor). Headlines can be saved to a local text file for later use.

> **Disclaimer:** All headlines are entirely fictional and intended for humor and entertainment purposes only. No real news organizations, people, or institutions are represented.

---

## Features

- **Random Mode** — Picks a subject, action, and place at random from curated India-specific lists
- **Custom Mode** — Let you define your own subject, action, and place for personalized headlines
- **Save to File** — Optionally saves any generated headline to `headlines.txt`
- **Loop Support** — Keep generating headlines until you decide to stop
- **Zero Dependencies** — Uses only Python's built-in `random` module; no pip installs needed
- **India-Focused Content** — Subjects and places drawn from 20 Indian cities and cultural references

---

## Installation

### Prerequisites

- Python 3.6 or higher

Check your Python version with:

```bash
python --version
```

### Steps

1. Clone the repository:

```bash
git clone https://github.com/your-username/fake-news-generator.git
cd fake-news-generator
```

2. No additional packages are required. Run it directly:

```bash
python Fake_News_Generator.py
```

---

## Usage

Run the script from your terminal:

```bash
python Fake_News_Generator.py
```

You will be prompted to choose a mode:

```
Do you want a Random Headline or Custom Headline? (random/custom):
```

### Random Mode

Type `random` and press Enter. The program picks a subject, action, and place automatically:

```
BREAKING NEWS: Ranchi Zoo Trains parrots to mimic traffic rules Varanasi
```

### Custom Mode

Type `custom` and press Enter. You'll be asked to fill in three fields:

```
Enter the subject: Darjeeling Tea Board
Enter the action: Launches cloud-powered tea drones
Enter the place: Sikkim
```

Output:

```
BREAKING NEWS: Darjeeling Tea Board Launches cloud-powered tea drones Sikkim
```

### Saving a Headline

After any headline is generated, you'll be asked:

```
Do You Save this Headline? (yes/no):
```

Saved headlines are appended to `headlines.txt` in the same directory.

### Continuing or Exiting

```
Do you Want to Another Headline? (yes/no):
```

Type `no` to exit gracefully.

---

## Configuration

The generator draws from three hardcoded lists inside the script. You can customize these directly in `Fake_News_Generator.py`:

| List        | Variable    | Description                                      |
|-------------|-------------|--------------------------------------------------|
| Subjects    | `subjects`  | Organizations, bodies, or entities making news   |
| Actions     | `actions`   | What they are doing (the absurd part)            |
| Places      | `places`    | Indian cities or regions where it happens        |

**Adding a new subject:**

Open `Fake_News_Generator.py` and add an entry to the `subjects` list:

```python
subjects = [
    ...
    "Shimla Tourism Board",   # your new entry
]
```


The same pattern applies to `actions` and `places`. No other changes are needed.

**Changing the output file name:**

Find this line in the script:

```python
with open("headlines.txt", "a") as f:
```

Replace `"headlines.txt"` with any filename you prefer.

---

## Project Structure

```
fake-news-generator/
│
├── Fake_News_Generator.py   # Main script
├── headlines.txt            # Auto-created when you save a headline
└── README.md                # You are here
```

---

## Contributing

Contributions are welcome — especially new subjects, actions, and places that fit the satirical spirit of the project.

### How to Contribute

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/add-new-cities
   ```
3. Make your changes
4. Commit with a clear message:
   ```bash
   git commit -m "Add Mysuru and Coimbatore to places list"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/add-new-cities
   ```
6. Open a Pull Request

### Guidelines

- Keep new entries culturally relevant and in the spirit of gentle, harmless satire
- Avoid entries that target real individuals or make politically sensitive implications
- Keep actions imaginative but family-friendly
- Test that the script runs without errors before submitting

---

## Testing

Since the project has no external dependencies, testing is straightforward.

### Manual Testing

Run both modes and verify expected behavior:

```bash
python Fake_News_Generator.py
```

Check the following:

- [ ] `random` mode generates a valid headline each time
- [ ] `custom` mode accepts input and formats the headline correctly
- [ ] Empty input in `custom` mode shows the appropriate error and re-prompts
- [ ] Invalid mode input (e.g., `maybe`) shows an error and re-prompts
- [ ] Typing `yes` at the save prompt creates or appends to `headlines.txt`
- [ ] Typing `no` at the continue prompt exits cleanly with the goodbye message

### Automated Testing (Optional Setup)

If you extend the project and want to add unit tests, the recommended approach is:

```bash
pip install pytest
pytest tests/
```

A `tests/` directory with sample test cases can be added as the project grows.

---

## License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, and distribute this software for personal or commercial purposes. Attribution is appreciated but not required.

See the [LICENSE](LICENSE) file for full details.

---

## Contact

Made with chai and curiosity.

If you have suggestions, find a bug, or just want to share a headline that made you laugh:

- **GitHub Issues:** [Open an issue](https://github.com/SohelMallik/Fake-News-Generator-Python.git)
- **Email:** malliksohel582@gmail.com

---

**Why This Project Matters**

This project is a great starting point for beginners learning Python because it introduces important programming concepts in a fun and interactive way. Despite its simplicity, it demonstrates real programming fundamentals such as:

Data structures
User interaction
Input validation
File handling
Randomization logic

It also serves as a solid foundation for larger projects in automation, content generation, or web development.

*"In a world full of real news, sometimes you need to make your own."*