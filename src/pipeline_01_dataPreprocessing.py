import argparse
import os
import yaml


def read_param(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def get_data(config_path,datasource):
    config=read_param(config_path)
    data_path=config['data_source']['batch_files']
    print(data_path)


if __name__=="__main__":
    args=argparse.ArgumentParser()
    default_config_path=os.path.join("config","param.yaml")
    args.add_argument('--config',default=default_config_path)
    args.add_argument('--datasource', default=None)

    prased_args=args.parse_args()


    # read_param('config/param.yaml')

    get_data(config_path=prased_args.config,datasource=prased_args.datasource)




