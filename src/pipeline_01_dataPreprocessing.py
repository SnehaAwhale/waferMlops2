import argparse
import os
import yaml


def read_param(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def main(config_path,datasource):
    config=read_param(config_path)
    print(config)


if __name__=="__main__":
    args=argparse.ArgumentParser()
    default_config_path=os.path.join("config","param.yaml")
    args.add_argument('--config',default=default_config_path)
    args.add_argument('--datasource', default=None)

    prased_args=args.parse_args()

    print(default_config_path)
    # read_param('config/param.yaml')

    main(config_path=prased_args.config,datasource=prased_args.datasource)




