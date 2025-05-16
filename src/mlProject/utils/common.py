# 📦 দরকারি প্যাকেজ ইমপোর্ট
import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# 🟡 YAML ফাইল পড়ার জন্য ফাংশন
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    🔍 YAML ফাইল পড়ে ConfigBox রিটার্ন করে (dictionary এর মতো কিন্তু .key দিয়ে অ্যাক্সেস করা যায়)
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully ✅")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("⚠️ YAML ফাইল ফাঁকা")
    except Exception as e:
        raise e

# 📁 একাধিক ডিরেক্টরি তৈরি করার জন্য
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    📂 লিস্টে দেওয়া সব path অনুযায়ী ডিরেক্টরি তৈরি করে
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"✅ ডিরেক্টরি তৈরি হয়েছে: {path}")

# 📄 Dictionary ডেটা JSON ফাইল হিসেবে সংরক্ষণ করে
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    💾 JSON ফাইল হিসেবে ডেটা সংরক্ষণ করে
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"✅ JSON ফাইল সেভ হয়েছে: {path}")

# 📄 JSON ফাইল থেকে ডেটা লোড করে ConfigBox আকারে রিটার্ন করে
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    🔄 JSON ফাইল লোড করে এবং ConfigBox আকারে রিটার্ন করে
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"✅ JSON ফাইল লোড হয়েছে: {path}")
    return ConfigBox(content)

# 💾 যেকোনো অবজেক্ট বাইনারি ফাইল হিসেবে সেভ করে (joblib)
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    📦 বাইনারি (Binary) ফাইল হিসেবে ডেটা সংরক্ষণ
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"✅ বাইনারি ফাইল সেভ হয়েছে: {path}")

# 🔄 বাইনারি ফাইল লোড করে অবজেক্ট রিটার্ন করে
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    📤 বাইনারি ফাইল থেকে অবজেক্ট লোড করে রিটার্ন করে
    """
    data = joblib.load(path)
    logger.info(f"✅ বাইনারি ফাইল লোড হয়েছে: {path}")
    return data

# 📏 ফাইলের সাইজ কিলোবাইটে রিটার্ন করে
@ensure_annotations
def get_size(path: Path) -> str:
    """
    🔍 ফাইলের সাইজ (KB) বের করে দেয়
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"








 

'''
@ensure_annotations হল একটি Python ডেকোরেটর (decorator) যেটা ensure লাইব্রেরি থেকে আসে এবং এটি ব্যবহার করা হয় function-এর type annotations enforce করার জন্য ✅

🔍 কাজ কী করে?
যখন তুমি @ensure_annotations ব্যবহার করো কোনো ফাংশনের উপর, তখন সেটা function call-এর সময় সব parameter আর return value-এর type annotations মিলিয়ে দেখে। যদি mismatch হয়, তাহলে RuntimeError বা TypeError দেয়।

📦 Installation:
bash
Copy
Edit
pip install ensure
✅ উদাহরণ:
python
Copy
Edit
from ensure import ensure_annotations

@ensure_annotations
def add(x: int, y: int) -> int:
    return x + y

print(add(5, 10))        # ✅ ঠিক আছে
print(add(5, "hello"))   # ❌ TypeError: Argument y must be <class 'int'>
🔐 কেন ব্যবহার করব?
🔸 Type hint শুধু documentation নয়, @ensure_annotations দিয়ে runtime-এ enforce করাও যায়
🔸 ভুল type দিলে bug detect করা সহজ হয়
🔸 Clean, safe, and predictable codebase তৈরি হয়

⚠️ সীমাবদ্ধতা:
Performance-sensitive জায়গায় ব্যবহার করলে একটু slowdown হতে পারে

Advanced type hints (Union, Optional, custom classes) সবসময় ঠিকঠাক detect নাও করতে পারে



'''