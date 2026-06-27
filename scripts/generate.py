import json
import shutil
from pathlib import Path
import time
import requests

# ----------------------------------
# Paths & Settings Setup
# ----------------------------------
PROJECT_ROOT = Path.home() / "YouTube-Automation"
WORKFLOW_PATH = PROJECT_ROOT / "workflows" / "flux_stickman.json"
PROMPTS_PATH = PROJECT_ROOT / "prompts" / "prompts.json"
OUTPUT_PATH = PROJECT_ROOT / "output"

COMFYUI_URL = "http://127.0.0.1:8188"

# ----------------------------------
# Helper Functions
# ----------------------------------
def wait_for_completion(prompt_id):
    print("\n⏳ Waiting for image generation...")

    while True:
        response = requests.get(
            f"{COMFYUI_URL}/history/{prompt_id}"
        )

        history = response.json()

        if prompt_id in history:

            outputs = history[prompt_id].get("outputs", {})

            for _, node in outputs.items():
                if "images" in node:
                    print("✅ Image generation complete!")
                    return node["images"]

            print("❌ Generation finished, but NO image was produced.")
            return None

        time.sleep(1)


def save_latest_image(filename):
    comfy_output = Path.home() / "ComfyUI-Installs" / "ComfyUI" / "ComfyUI" / "output"

    images = sorted(comfy_output.glob("ComfyUI*.png"))

    if not images:
        print("❌ No images found.")
        return

    latest = max(images, key=lambda x: x.stat().st_mtime)

    destination = OUTPUT_PATH / f"{filename}.png"

    shutil.move(latest, destination)

    print(f"✅ Saved as {destination.name}")


def generate_scene(scene):
    # Replace Prompt
    new_prompt = scene["prompt"]
    workflow[prompt_node]["inputs"]["text"] = new_prompt

    print(f"\n✨ Replacing prompt with: {new_prompt}")

    # Send workflow to ComfyUI
    response = requests.post(
        f"{COMFYUI_URL}/prompt",
        json={
            "prompt": workflow
        }
    )

    response.raise_for_status()
    data = response.json()
    prompt_id = data["prompt_id"]

    print(f"🚀 Prompt queued: {prompt_id}")

    # Wait for completion
    images = wait_for_completion(prompt_id)

    if images:
        print("History received successfully!")
        save_latest_image(scene["filename"])
    else:
        print(f"❌ Skipping {scene['filename']} because generation failed.")


# ----------------------------------
# Load Workflow and Prompts
# ----------------------------------
with open(WORKFLOW_PATH, "r") as f:
    workflow = json.load(f)

with open(PROMPTS_PATH, "r") as f:
    prompts = json.load(f)

print("✅ Workflow loaded successfully!")
print(f"✅ Loaded {len(prompts)} prompts.\n")


# ----------------------------------
# Find Prompt Node
# ----------------------------------
prompt_node = None

for node_id, node in workflow.items():
    if node.get("class_type") == "CLIPTextEncode":
        prompt_node = node_id
        break

if prompt_node:
    print(f"✅ Prompt node found: {prompt_node}")
    print("Current prompt:")
    print(workflow[prompt_node]["inputs"]["text"])


# ----------------------------------
# Generate Scenes
# ----------------------------------
if prompt_node:
    for scene in prompts:
        generate_scene(scene)
else:
    print("❌ Cannot generate scenes because prompt node was not found.")