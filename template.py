# 📁 প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করা হচ্ছে
import os
from pathlib import Path
import logging

# 📝 লগিং কনফিগার করা হচ্ছে যাতে কোন ফাইল কখন তৈরি হচ্ছে সেটা দেখা যায়
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# 🎯 প্রজেক্টের নাম নির্ধারণ করা হচ্ছে
project_name = "mlProject"

# 📂 যেসব ফাইল ও ফোল্ডার তৈরি করতে হবে, সেগুলোর লিস্ট
list_of_files = [
    ".github/workflows/.gitkeep",                          # 🛠️ GitHub Actions-এর জন্য ফোল্ডার তৈরি
    f"src/{project_name}/__init__.py",                     # 📦 মেইন প্যাকেজ ফাইল
    f"src/{project_name}/components/__init__.py",          # 🧩 কম্পোনেন্ট ফোল্ডার
    f"src/{project_name}/utils/__init__.py",               # 🛠️ ইউটিলিটি ফাইল
    f"src/{project_name}/utils/common.py",                 # 🧰 সাধারণ ফাংশন এখানে থাকবে
    f"src/{project_name}/config/__init__.py",              # ⚙️ কনফিগারেশন ফোল্ডার
    f"src/{project_name}/config/configuration.py",         # ⚙️ কনফিগারেশন সেটিংস
    f"src/{project_name}/pipeline/__init__.py",            # 🧪 পাইপলাইন সম্পর্কিত ফাইল
    f"src/{project_name}/entity/__init__.py",              # 🧬 এনটিটি ডেটা ক্লাস
    f"src/{project_name}/entity/config_entity.py",         # 📄 কনফিগ এনটিটি
    f"src/{project_name}/constants/__init__.py",           # 📌 কনস্ট্যান্ট মান
    "config/config.yaml",                                  # ⚙️ YAML কনফিগ ফাইল
    "params.yaml",                                         # 📋 মডেল প্যারামিটার ফাইল
    "schema.yaml",                                         # 🗂️ স্কিমা সংক্রান্ত ফাইল
    "main.py",                                             # 🚀 প্রজেক্ট রান করার মেইন ফাইল
    "app.py",                                              # 🌐 ওয়েব অ্যাপ্লিকেশন ফাইল
    "Dockerfile",                                          # 🐳 ডকার কনফিগারেশন
    "requirements.txt",                                    # 📦 প্রয়োজনীয় লাইব্রেরিগুলো
    "setup.py",                                            # 📦 প্যাকেজ সেটআপ ফাইল
    "research/trials.ipynb",                               # 🔬 গবেষণা ও ট্রায়াল নোটবুক
    "templates/index.html",                                # 🖼️ ফ্রন্টএন্ড টেমপ্লেট
    "test.py"                                              # 🧪 টেস্টিং ফাইল
]

# 🔁 সব ফাইল ও ফোল্ডারের জন্য লুপ চালানো হচ্ছে
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # 📂 যদি ডিরেক্টরি না থাকে, তাহলে সেটা তৈরি করা হচ্ছে
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # 📄 যদি ফাইল না থাকে বা খালি থাকে, তাহলে সেটা তৈরি করা হচ্ছে
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        # 🔁 ফাইল আগে থেকেই আছে, তাই কিছু করা লাগবে না
        logging.info(f"{filename} is already exists")
