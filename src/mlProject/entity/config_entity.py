from dataclasses import dataclass  # 🧾 dataclass ব্যবহারে সহজে configuration বা data structure তৈরি করা যায়
from pathlib import Path  # 🗂️ ফাইল ও ডিরেক্টরি পাথ নিয়ে কাজ করার জন্য

# 📦 DataIngestionConfig একটি ইম্মিউটেবল (frozen=True) কনফিগারেশন ক্লাস
@dataclass(frozen=True)
class DataIngestionConfig:
    # 🗂️ মূল ডিরেক্টরি যেখানে ডেটা ইনজেশন সম্পর্কিত সব কিছু থাকবে
    root_dir: Path

    # 🌐 যেখান থেকে ডেটা ডাউনলোড করা হবে (source URL)
    source_URL: str

    # 💾 লোকাল সিস্টেমে কোথায় ZIP ফাইলটি সেভ হবে
    local_data_file: Path

    # 📂 ডেটা আনজিপ করার পর কোন ডিরেক্টরিতে রাখা হবে
    unzip_dir: Path

#config.yaml e ase data ingestion er configuration thakbe


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path