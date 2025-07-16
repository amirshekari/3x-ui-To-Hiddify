
# 🔄 3xuiToHiddify

A Python script to migrate users from an `x-ui` SQLite database to a Hiddify panel via API.

---

## 📌 Overview

This script extracts user data from the `x-ui.db` SQLite database, calculates data usage and remaining traffic, then sends each user to the Hiddify API to be created automatically.

---

## ⚙️ Requirements

### 1. Install Python (if not already installed)

Check your Python version:

```
python --version
```

If not installed, download it from:

🔗 [Python Downloads](https://www.python.org/downloads/)

> ⚠️ On Windows, make sure to check **"Add Python to PATH"** during installation.

---

### 2. Install required library (`requests`)

Install the `requests` package using:

```
pip install requests
```

---

## 🚀 How to Use

### 1. Clone or download the script

```
git clone https://github.com/username/3xuiToHiddify.git
cd 3xuiToHiddify
```

### 2. Run the script

```
python 3xuiToHiddify.py
```

### 3. Provide the following information when prompted:

| Input                     | Description                                                              |
|--------------------------|---------------------------------------------------------------------------|
| Path to `x-ui.db`        | Full path to your SQLite database (e.g., `/root/x-ui.db`)                |
| Hiddify API endpoint     | Full API URL (e.g., `https://domain.com/proxy/api/v2/admin/user/`)       |
| Hiddify API Key          | Your admin API key from the Hiddify panel                                |

---

## 📤 What the Script Does

1. Connects to your x-ui SQLite database
2. Reads user data and calculates usage/limits
3. Converts expiry timestamp to remaining days
4. Sends a POST request to create each user in Hiddify
5. Logs results in `migration_results.json`

---

## 📂 Output File

After execution, a `migration_results.json` file is generated like:

```json
[
  {
    "name": "testuser",
    "status_code": 201,
    "response": "{...}",
    "success": true
  },
  ...
]
```

---

## 🧪 Example Run

```
Enter path to x-ui.db: /root/x-ui.db
Enter full Hiddify API endpoint: https://panel.hiddify.com/proxy/api/v2/admin/user/
Enter your Hiddify API Key: 3f89e***-***-***-****-*******e87
[✓] testuser1 → 201
[✓] testuser2 → 201
[✗] user3 → Error: Connection timed out

Migration completed. Results saved to migration_results.json
```

---

## 🛡️ Security Notes

- Never store your API key in a public repository.
- For better security, consider using a `.env` file and the `python-dotenv` package.

---

## 📄 License

MIT License – Free to use, modify, and distribute with proper attribution.

---

## ✨ Author

[👤 github.com/username](https://github.com/username)

If this project was helpful, feel free to star it ⭐🙂
