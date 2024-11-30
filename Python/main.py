from json import load
from auto_sphinx_generator import AutoSphinxGenerator


def main() -> None:
    with open('/home/dev/Dev/Docify/Python/config.json', 'r') as cf:
        configs = load(cf)

    docs_generator = AutoSphinxGenerator(configs=configs)
    docs_generator.run()

if __name__ == "__main__":
    main()