from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

# 🏁 স্টেজের নাম নির্ধারণ করা হয়েছে - লগিং ও ট্র্যাকিং-এর সুবিধার্থে
STAGE_NAME = "Data Ingestion stage"

# 🛠️ Data Ingestion স্টেজের ট্রেনিং পাইপলাইন ক্লাস
class DataIngestionTrainingPipeline:
    def __init__(self):
        # 🚧 ভবিষ্যতের জন্য প্রস্তুত: এখানে ইনিশিয়ালাইজেশন কোড আসবে
        pass
    def main(self):
        # 🛠️ কনফিগারেশন ম্যানেজার কল করে কনফিগ অবজেক্ট তৈরি করা হচ্ছে
        config = ConfigurationManager()

        # 📦 ডেটা ইনজেশন সংক্রান্ত কনফিগ সংগ্রহ
        data_ingestion_config = config.get_data_ingestion_config()

        # 🍽️ DataIngestion অবজেক্ট তৈরি
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # 🌐 ডেটা ডাউনলোড করা হচ্ছে
        data_ingestion.download_file()

        # 📂 ডেটা আনজিপ করে এক্সট্রাক্ট করা হচ্ছে
        data_ingestion.extract_zip_file()


# 🧠 মেইন ফাংশন: যখন স্ক্রিপ্ট সরাসরি রান হবে তখনই নিচের অংশটি চলবে
if __name__ == '__main__':
    try:
        # 🚀 স্টেজ শুরু হওয়ার লগ
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # 🧱 DataIngestionTrainingPipeline অবজেক্ট তৈরি করা
        obj = DataIngestionTrainingPipeline()

        # 🔁 পাইপলাইনের মূল কাজ চালানো (main() ফাংশন এখানে ডিফাইন থাকতে হবে)
        obj.main()

        # ✅ স্টেজ সফলভাবে শেষ হলে লগ
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        # ❌ কোন এরর হলে সেটার বিস্তারিত লগ করা হবে
        logger.exception(e)
        raise e
