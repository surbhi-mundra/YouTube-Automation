# 🚀 YouTube Automation Pipeline

An AI-powered YouTube Shorts automation pipeline built with **Python**, **ComfyUI**, and **FLUX GGUF**.

This project automates the image generation workflow for educational and storytelling YouTube Shorts by controlling ComfyUI directly through its API.

---

## ✨ Features

- 📝 Reads prompts from a JSON file
- 🎨 Automatically replaces prompts inside a ComfyUI workflow
- ⚡ Queues image generation through the ComfyUI API
- ⏳ Waits for generation to finish
- 💾 Saves generated images with custom filenames
- 🔁 Batch generation of multiple scenes
- 🖥️ Runs entirely on a local machine (no paid APIs)

---

## 🛠 Tech Stack

- Python 3
- ComfyUI
- FLUX GGUF
- Requests
- JSON
- Git & GitHub

---

## 📂 Project Structure

```
YouTube-Automation/
│
├── assets/
├── output/
├── prompts/
│   └── prompts.json
├── scripts/
│   └── generate.py
├── subtitles/
├── videos/
├── voices/
├── workflows/
│   └── flux_stickman.json
└── README.md
```

---

## ⚙️ How It Works

```
prompts.json
      │
      ▼
generate.py
      │
      ▼
Load ComfyUI Workflow
      │
      ▼
Replace Prompt
      │
      ▼
Queue Prompt via API
      │
      ▼
Wait for Completion
      │
      ▼
Save Generated Image
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/surbhi-mundra/YouTube-Automation.git
cd YouTube-Automation
```

### Start ComfyUI

```bash
cd ~/ComfyUI-Installs/ComfyUI
./standalone-env/bin/python3 ./ComfyUI/main.py
```

### Run the automation

```bash
python3 scripts/generate.py
```

---

## 📋 Example Prompt

```json
{
  "scene": 1,
  "filename": "scene_01",
  "prompt": "Minimal black stickman holding a baby photograph with a confused expression, flat vector illustration, white background."
}
```

---

## 📌 Roadmap

### ✅ Version 1.0

- Prompt automation
- Workflow automation
- ComfyUI API integration
- Automatic image saving
- Batch image generation

### 🔜 Planned Improvements

- Faster generation pipeline
- Automatic voice generation
- Automatic subtitle generation
- Automatic video assembly
- One-click YouTube Shorts generation

---

## 📸 Example Output

```
output/

scene_01.png
scene_02.png
scene_03.png
...
scene_35.png
```

---

## 👩‍💻 Author

**Surbhi Mundra**

GitHub: https://github.com/surbhi-mundra

---

## ⭐ Future Vision

The long-term goal of this project is to build a complete AI-powered YouTube content pipeline capable of generating:

- Script
- Image prompts
- AI-generated images
- Voiceover
- Subtitles
- Final edited YouTube Shorts

with minimal manual intervention.
