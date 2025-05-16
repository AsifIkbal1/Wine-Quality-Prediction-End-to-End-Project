from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


# 🏁 স্টেজ নাম (লগের জন্য)
STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        # 🔧 এখানে future enhancements এর জন্য constructor আছে
        pass

    def main(self):
        try:
            # 📄 স্ট্যাটাস ফাইল থেকে ডেটা ভ্যালিডেশন স্ট্যাটাস পড়া হচ্ছে
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            # ✅ যদি ভ্যালিডেশন সফল হয়, তাহলে ট্রান্সফরমেশন শুরু হবে
            if status == "True":
                # ⚙️ কনফিগারেশন সেটআপ
                config = ConfigurationManager()

                # 📁 ডেটা ট্রান্সফরমেশন কনফিগারেশন পাওয়া যাচ্ছে
                data_transformation_config = config.get_data_transformation_config()

                # 🧠 ডেটা ট্রান্সফরমেশন অবজেক্ট তৈরি
                data_transformation = DataTransformation(config=data_transformation_config)

                # ✂️ ট্রেইন-টেস্ট স্প্লিট করা হচ্ছে
                data_transformation.train_test_spliting()

            else:
                # 🚫 যদি স্কিমা ভুল হয়, তাহলে error তুলে ধরা হবে
                raise Exception("❌ আপনার ডেটা স্কিমা সঠিক নয়!")

        except Exception as e:
            # ⚠️ যেকোনো এরর হলে প্রিন্ট করা হবে
            print(e)


if __name__ == '__main__':
    try:
        # 🚀 স্টেজ শুরু
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # 🎯 অবজেক্ট তৈরি এবং মেইন ফাংশন চালানো হচ্ছে
        obj = DataTransformationTrainingPipeline()
        obj.main()

        # 🏁 স্টেজ শেষ
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        # 🧯 এক্সসেপশন হ্যান্ডেল এবং লগ
        logger.exception(e)
        raise e
