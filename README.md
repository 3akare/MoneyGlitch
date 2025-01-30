# MoneyGlitch
A Selenium-based automation script for watching videos on DollarTub.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/3akare/MoneyGlitch.git
   cd MoneyGlitch
   ```

2. Create a virtual environment (recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setup

1. Create a `.env` file in the project root and add the following variables:
   ```sh
   WEB_URL=your_target_url
   CHROME_PROFILE_PATH=/path/to/your/chrome/profile
   ```
   
2. **Find your Chrome profile path:**
   - Open Chrome and go to `chrome://version/`
   - Copy the **Profile Path** (e.g., `/Users/yourname/Library/Application Support/Google/Chrome/Profile 1`)
   - Ensure it **ends with 'Default' or 'Profile X'** and then remove it.

## Usage

1. Close all existing Chrome windows.
2. Run the script:
   ```sh
   python3 main.py
   ```
3. You must log in to your DollarTub account **within 20 seconds** after Chrome opens.
4. The script will:
   - Click the 'Watch Video' button
   - Wait 35 seconds for the video to play
   - Refresh the page
   - Wait 20 seconds before repeating

## Notes
- **Chrome is required** for this script.
- **Login manually** before automation starts.
- **Close all Chrome tabs** before running to avoid session conflicts.

## Troubleshooting
- If the script keeps opening the login page, check if the Chrome profile path is correct.
- If you get a "session not created" error, close all Chrome windows before running.
- If authentication issues persist, try manually logging in first, then running the script.
