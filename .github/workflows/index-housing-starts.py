name: Index.html - Update Housing Starts

on:
  schedule:
    - cron: "20 5 18 * *"  # Run on the 18th day of every month at 05:20 AM UTC
  workflow_dispatch:        # Allow manual triggering

permissions:
  contents: write

jobs:
  update-index:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the repository
      - name: Checkout repository
        uses: actions/checkout@v3

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'  # Use the latest Python 3 version

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          pip install pandas openpyxl

      # Step 4: Run the update script
      - name: Run the update script
        run: python scripts/index-housing-starts.py

      # Step 5: Commit and push changes
      - name: Commit and push changes
        run: |
          git config --global user.name "GitHub Actions Bot"
          git config --global user.email "actions@github.com"
          git add ./index.html
          git commit -m "Automated update of Food Sales data"
          git push
