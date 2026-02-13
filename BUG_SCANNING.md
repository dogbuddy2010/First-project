# Turtle Project Bug Scanning System

## Overview
This repository has an automated daily bug scanning system that checks the Turtle project for code quality issues, bugs, and security vulnerabilities.

## How It Works

### Automated Daily Scans
The bug scanning workflow runs automatically:
- **Daily at 9:00 AM UTC** - Scheduled automatic scan
- **On every push** to main/master branch that affects Python files
- **Manual trigger** - You can run it anytime from the Actions tab

### What Gets Scanned

The workflow performs multiple checks on the `turtle_app.py` file:

1. **Flake8** - Checks for:
   - Python style violations (PEP 8)
   - Common programming errors
   - Code complexity issues

2. **Pylint** - Analyzes:
   - Code quality and maintainability
   - Potential bugs and errors
   - Code structure and best practices

3. **Bandit** - Scans for:
   - Security vulnerabilities
   - Unsafe coding patterns
   - Common security issues

4. **Syntax Check** - Verifies:
   - Python syntax is valid
   - No compilation errors

### Notification System

When bugs are found:
- ✅ A GitHub Issue is automatically created with:
  - Summary of what was found
  - Link to the detailed workflow run
  - Severity and type of issues
  
- ✅ If an issue already exists, a comment is added with the latest scan results

When no bugs are found:
- ✅ A success message is added to the workflow summary

## Viewing Scan Results

1. Go to the **Actions** tab in your GitHub repository
2. Click on **"Daily Bug Scan - Turtle Project"**
3. View the latest workflow run for detailed results

## Running Manual Scans

To run a scan manually:
1. Go to **Actions** tab
2. Click **"Daily Bug Scan - Turtle Project"**
3. Click **"Run workflow"** button
4. Select the branch and click **"Run workflow"**

## Recent Bug Fixes

### Fixed: Duplicate Input Prompts (2026-02-13)
- **Issue**: The program asked "Would you like to launch the Turtle mode?" twice
- **Location**: Lines 1-2 and 7 in original code
- **Fix**: Removed redundant first prompt and adjusted code structure
- **Impact**: Improved user experience, cleaner code flow

## Maintenance

The bug scanning system is self-maintaining and requires no manual intervention. However, you can:
- Adjust the scan schedule in `.github/workflows/daily-bug-scan.yml`
- Modify linting rules and thresholds
- Add or remove scanning tools as needed

---

*This automated system helps maintain code quality and catch bugs early in the Turtle project.*
