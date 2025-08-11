# Quarterly Earnings Presentation

This project contains an interactive presentation for the quarterly earnings report, utilizing RevealJS for modern presentation capabilities.

## Project Structure

```
quarterly-earnings-presentation
├── slides
│   ├── index.html          # Main HTML file for the presentation
│   ├── slides.md           # Markdown content for the slides
│   └── assets
│       └── custom.css      # Custom styles for the presentation
├── package.json            # npm configuration file
├── README.md               # Project documentation
└── .github
    └── workflows
        └── deploy.yml      # GitHub Actions workflow for deployment
```

## Features

- **Interactive Presentation**: Built using RevealJS for a modern look and feel.
- **Markdown Support**: Slides are written in Markdown for easy editing and formatting.
- **Animated Elements**: Use of fragments to create engaging animations within the slides.
- **Code Samples**: Syntax highlighting for code snippets to enhance readability.
- **Mathematical Equations**: Inclusion of financial formulas for clarity in reporting.
- **Speaker Notes**: Guidance for presenters included in the slides.

## Running the Presentation Locally

1. Clone the repository:
   ```
   git clone <repository-url>
   cd quarterly-earnings-presentation
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the local server:
   ```
   npm start
   ```

4. Open your browser and navigate to `http://localhost:8000` to view the presentation.

## Deploying to GitHub Pages

1. Ensure your changes are committed to the main branch.
2. Push your changes to the repository:
   ```
   git push origin main
   ```

3. The GitHub Actions workflow will automatically build and deploy the presentation to GitHub Pages.

## Contact

For any inquiries, please reach out via email: 24f2006003@ds.study.iitm.ac.in.