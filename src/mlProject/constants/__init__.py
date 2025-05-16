from pathlib import Path  # 📁 ফাইল ও ডিরেক্টরি পাথ হ্যান্ডল করার জন্য Path মডিউল

# 🛠️ মূল কনফিগারেশন ফাইল – যেখানে বিভিন্ন ধাপে ব্যবহার করার জন্য তথ্য রাখা থাকে (যেমন data_ingestion)
CONFIG_FILE_PATH = Path("config/config.yaml")

# ⚙️ মডেল ট্রেনিং বা অন্যান্য ধাপের জন্য হাইপারপ্যারামিটার সংরক্ষণের YAML ফাইল
PARAMS_FILE_PATH = Path("params.yaml")

# 📊 স্কিমা ফাইল – ডেটা কীভাবে স্ট্রাকচারড সেটা সংজ্ঞায়িত করে (যেমন column names, dtypes ইত্যাদি)
SCHEMA_FILE_PATH = Path("schema.yaml")
