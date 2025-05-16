# 🔧 কনফিগারেশন ম্যানেজার এবং ডেটা ভ্যালিডেশন কম্পোনেন্ট ইমপোর্ট করা হচ্ছে
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValiadtion
from mlProject import logger

# 🏁 স্টেজের নাম নির্ধারণ
STAGE_NAME = "Data Validation stage"

# 🧪 ডেটা ভ্যালিডেশন ট্রেনিং পাইপলাইন ক্লাস
class DataValidationTrainingPipeline:
    def __init__(self):
        pass  # 🙈 আপাতত constructor এ কিছু নেই

    def main(self):
        # 🔧 কনফিগারেশন সেটআপ
        config = ConfigurationManager()
        
        # 📦 ডেটা ভ্যালিডেশন কনফিগারেশন সংগ্রহ
        data_validation_config = config.get_data_validation_config()
        
        # 🔍 ডেটা ভ্যালিডেশন অবজেক্ট তৈরি
        data_validation = DataValiadtion(config=data_validation_config)
        
        # ✅ কলাম গুলো যাচাই করা হচ্ছে স্কিমা অনুযায়ী
        data_validation.validate_all_columns()

# 🚀 যখন স্ক্রিপ্ট রান করা হবে
if __name__ == '__main__':
    try:
        # 🟢 স্টেজ শুরু হচ্ছে
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # 📦 pipeline অবজেক্ট তৈরি এবং main() মেথড কল
        obj = DataValidationTrainingPipeline()
        obj.main()

        # ✅ স্টেজ সফলভাবে শেষ
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        # ❌ কোনো এক্সসেপশন ঘটলে লগ করে দিচ্ছে
        logger.exception(e)
        raise e
