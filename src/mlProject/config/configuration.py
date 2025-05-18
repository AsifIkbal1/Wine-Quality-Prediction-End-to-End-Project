from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig)


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


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        # 🔧 কনফিগারেশন, প্যারামিটার এবং টার্গেট কলাম লোড করা হচ্ছে
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        # 📂 মডেল ইভ্যালুয়েশনের জন্য রুট ডিরেক্টরি তৈরি
        create_directories([config.root_dir])

        # ✅ ModelEvaluationConfig অবজেক্ট তৈরি
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,  # 📁 মূল ডিরেক্টরি
            test_data_path=config.test_data_path,  # 🧪 টেস্ট ডেটার পাথ
            model_path=config.model_path,  # 🤖 ট্রেইনকৃত মডেল ফাইল পাথ
            all_params=params,  # ⚙️ মডেল হাইপারপ্যারামিটারস
            metric_file_name=config.metric_file_name,  # 📊 মেট্রিক সংরক্ষণের জন্য ফাইল পাথ
            target_column=schema.name,  # 🎯 টার্গেট কলামের নাম
            mlflow_uri="https://dagshub.com/AsifIkbal1/Wine-Quality-Prediction-End-to-End-Project.mlflow",  # 🌐 MLflow tracking URI
        )

        return model_evaluation_config  # 🔄 কনফিগারেশন রিটার্ন করা হচ্ছে