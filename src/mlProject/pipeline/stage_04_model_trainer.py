from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger


# 🏁 এই স্টেজটি হচ্ছে "Model Trainer stage"
STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # ⚙️ কনফিগারেশন লোড করা হচ্ছে
        config = ConfigurationManager()

        # 📦 মডেল ট্রেইনারের জন্য কনফিগারেশন নেওয়া হচ্ছে
        model_trainer_config = config.get_model_trainer_config()

        # 🤖 ModelTrainer অবজেক্ট তৈরি করা হচ্ছে (❗ এখানে ছিল ভুল নাম!)
        model_trainer = ModelTrainer(config=model_trainer_config)

        # 🏋️‍♂️ মডেল ট্রেইন করা হচ্ছে
        model_trainer.train()


if __name__ == '__main__':
    try:
        # 🚀 স্টেজ শুরু হচ্ছে লগে
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # 🎯 অবজেক্ট তৈরি করে মেইন ফাংশন কল
        obj = ModelTrainerTrainingPipeline()
        obj.main()

        # ✅ স্টেজ সফলভাবে শেষ
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        # ❌ এক্সসেপশন হলে লগে দেখানো হচ্ছে
        logger.exception(e)
        raise e
