# PDFNotebook

PDFNotebook is a simple Python project that generates a notebook-style PDF from a CSV file of topics and page counts. It is designed for learners who want to print structured note pages while studying coding topics or any other subject.

## Features

- Reads topics and page counts from a CSV file.
- Generates a clean PDF notebook with one title page per topic.
- Adds lined note pages for writing by hand.
- Supports custom topic lists, page counts, and layouts.
- Useful for study notebooks, planners, workshop handouts, and printable journals.

## Example Output

The generated PDF creates a title page for each topic and additional lined pages for notes underneath that topic heading [file:30].

## How It Works

The script loads `topics.csv`, loops through each row, and creates a section in the PDF for each topic [file:30]. For every topic, it adds one main page with the topic title and then adds the number of extra lined pages defined in the `Pages` column [file:30].

## Requirements

- Python 3.x
- `pandas`
- `fpdf`

Install dependencies with:

```bash
pip install pandas fpdf
```

## CSV Format

Create a file named `topics.csv` with at least these columns:

```csv
Topic,Pages
Variables,3
Lists,4
Functions,5
```

- `Topic`: the title shown on the page.
- `Pages`: the total number of pages for that topic.

## Usage

1. Clone the repository.
2. Add or edit `topics.csv`.
3. Run the script:

```bash
python main.py
```

4. The generated file will be saved as `output.pdf`.

## Project Structure

```text
PDFNotebook/
├── main.py
├── topics.csv
├── output.pdf
└── README.md
```

## Customization

You can easily modify the script to change:

- Page size or orientation.
- Font family, font size, or text color.
- Line spacing and layout.
- Footer placement.
- Number of lined pages per topic.
- Output filename.

## Ideas for Extending the Project

- Add a table of contents page.
- Add page numbers.
- Use different page templates for different subjects.
- Add section dividers with colors or icons.
- Support subtopics inside each topic.
- Let users choose notebook themes like lined, dotted, or blank pages.
- Add a cover page with notebook title and date.
- Export multiple PDFs from one CSV file.
- Add a CLI prompt so users can generate PDFs interactively.
- Add Streamlit or Flask so users can upload a CSV and download the PDF in a browser.
- Generate notebooks for classrooms, training sessions, or conferences.

## Ways to Reuse This Project

This same codebase can be adapted to generate PDFs for:
- Study planners.
- Bullet journals.
- Meeting note packets.
- Workshop workbooks.
- Classroom handouts.
- Coding exercise books.
- Printable reflection journals.
- Daily practice notebooks.

## Example Modifications

### Create blank pages instead of lined pages
Replace the line-drawing loop with a blank page template.

### Add a cover page
Insert one page before the topic loop with the notebook title, author, and date.

### Support different page styles
Add a `Style` column in the CSV to choose between lined, dotted, or blank pages.

### Make it more flexible
Let the CSV include columns like `Topic`, `Pages`, `Color`, or `Subtitle` to personalize each section.

## License

Add your license information here.
