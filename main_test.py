from label_services import LabelGenerator, LabelReader


class MainTest:

    def __init__(self, length=None):
        self.length = length
        self.generator = LabelGenerator()
        self.reader = LabelReader()

    def run(self):
        if self.length is None:
            label = self.generator.generate()
        else:
            label = self.generator.generate_randomly(self.length)
        print(label)

        print("-" * len(label))

        result = self.reader.read(label)
        print(result)


if __name__ == "__main__":
    main_test = MainTest()
    main_test.run()
