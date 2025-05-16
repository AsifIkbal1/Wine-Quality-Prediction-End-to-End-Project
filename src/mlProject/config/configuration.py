from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        # 📖 YAML ফাইলগুলো থেকে কনফিগারেশন, প্যারাম এবং স্কিমা পড়া হচ্ছে
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # 📁 প্রজেক্টের জন্য মূল artifacts ডিরেক্টরি তৈরি
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # 🧾 data_ingestion কনফিগারেশন অংশটা বের করা হচ্ছে
        config = self.config.data_ingestion

        # 📂 data_ingestion ডিরেক্টরি তৈরি
        create_directories([config.root_dir])

        # ⚙️ DataIngestionConfig ক্লাসের ইনস্ট্যান্স তৈরি
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        # ✅ অবজেক্ট রিটার্ন করা হচ্ছে
        return data_ingestion_config
