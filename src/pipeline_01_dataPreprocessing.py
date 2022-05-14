import argparse
import os



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument('--config')
    args.add_argument('--datasource')


    parsed_arg=args.parse_args()
    print(parsed_arg)


