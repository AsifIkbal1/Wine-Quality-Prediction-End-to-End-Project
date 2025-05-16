# 📦 প্রয়োজনীয় মডিউল ইমপোর্ট করা হচ্ছে
import os
import sys
import logging

# 📝 লগ ফরম্যাট স্ট্রিং তৈরি করা হচ্ছে (সময়, লেভেল, মডিউল, মেসেজ)
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# 📁 লগ ফাইল সংরক্ষণের জন্য ফোল্ডার এবং ফাইলপাথ সেটআপ
log_dir = "logs"  # 📂 'logs' নামের ডিরেক্টরি
log_filepath = os.path.join(log_dir, "running_logs.log")  # 🗂️ লগ ফাইলের সম্পূর্ণ পথ

# 📁 যদি logs ফোল্ডার না থাকে তাহলে সেটা তৈরি করা হচ্ছে
os.makedirs(log_dir, exist_ok=True)

# 🔧 লগিং কনফিগারেশন সেট করা হচ্ছে
logging.basicConfig(
    level=logging.INFO,           # ℹ️ ইনফো লেভেলের উপরের সব লগ দেখাবে
    format=logging_str,           # 🧾 উপরের ফরম্যাট অনুযায়ী লগ প্রিন্ট হবে

    handlers=[
        logging.FileHandler(log_filepath),  # 📄 ফাইলের মধ্যে লগ সংরক্ষণ করবে
        logging.StreamHandler(sys.stdout)   # 🖥️ টার্মিনালেও লগ দেখাবে
    ]
)

# 🧠 কাস্টম লগার তৈরি করা হচ্ছে
logger = logging.getLogger("mlProjectLogger")  # ✅ 'mlProjectLogger' নামে লগার তৈরি
