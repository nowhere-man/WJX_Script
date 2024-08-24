import Config
import Single_Test
import time

if __name__ == '__main__':
    config = Config.Config()
    for i in range(config.batch):
        with open("Single_Test.py", "r", encoding="utf-8") as f:
            code = f.read()
            exec(code)