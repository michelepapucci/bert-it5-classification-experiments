import sys
sys.path.insert(0, '../')

from libraries.Experiment.metrics import Metrics


def main():
    m = Metrics("../output/gender/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("output/")


if __name__ == '__main__':
    main()