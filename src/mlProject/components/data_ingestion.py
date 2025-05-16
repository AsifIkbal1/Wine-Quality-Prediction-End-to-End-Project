import os  # 📁 ফাইল ও ডিরেক্টরি সংক্রান্ত অপারেশনের জন্য

# 🌐 URL থেকে ফাইল ডাউনলোড করার জন্য urllib এর request মডিউল
import urllib.request as request

# 📦 .zip ফাইল এক্সট্রাক্ট করার জন্য
import zipfile

# 📝 প্রজেক্টের কাস্টম লগার – লগ মেসেজ জেনারেট করার জন্য
from mlProject import logger

# 📏 ফাইল সাইজ বের করার ইউটিলিটি ফাংশন
from mlProject.utils.common import get_size

from pathlib import Path  # 🗂️ ফাইল ও ডিরেক্টরি পাথ নিয়ে কাজ করার জন্য

from mlProject.entity.config_entity import (DataIngestionConfig)





class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        # ⚙️ কনফিগারেশন অবজেক্ট সেট করা হচ্ছে (যেখানে path ও URL আছে)
        self.config = config

    def download_file(self):
        # 🌐 যদি লোকাল ফাইল আগে থেকে না থাকে, তাহলে ডাউনলোড করা হবে
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            # ✅ সফলভাবে ডাউনলোড হলে লগে দেখানো হবে
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            # 📁 ফাইল আগে থেকেই আছে, তাহলে শুধু সাইজ দেখাবে
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        📦 `.zip` ফাইল আনজিপ করে নির্ধারিত ফোল্ডারে এক্সট্রাক্ট করা হয়
        """
        unzip_path = self.config.unzip_dir

        # 📂 আনজিপ করার ডিরেক্টরি যদি না থাকে, তাহলে তৈরি করো
        os.makedirs(unzip_path, exist_ok=True)

        # 🔓 zip ফাইল খুলে এক্সট্রাক্ট করে নির্দিষ্ট ফোল্ডারে
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to: {unzip_path}")
