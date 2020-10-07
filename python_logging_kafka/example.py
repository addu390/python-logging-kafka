import logging
from python_logging_kafka import KafkaHandler


class Main:

    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.INFO,
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        self.logger = logging.getLogger('pylog')

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        f1 = logging.FileHandler("pylog.log")
        self.logger.addHandler(f1)

        kh = KafkaHandler('localhost:9092', "pylog")
        kh.setLevel(logging.INFO)
        self.logger.addHandler(kh)

    def run(self):
        while True:
            log = input("&gt; ")
            self.logger.info(log)


if __name__ == '__main__':
    main = Main()
    main.run()
