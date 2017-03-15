from release.preprocessing.process_properties import PreProcessor
from release.preprocessing.utils import * 
import sys


if __name__=="__main__":
    processor = PreProcessor(sys.argv[1])
    vocab = create_vocab(processor.input)
    w2v = loadVectors(vocab,processor.w2v_file,processor.w2v_type)

    folds = ['one', 'two', 'three', 'four', 'five']
    for fold in folds:
        if(processor.separate):
            train_test_separate(fold, vocab, w2v, processor.input, processor.output)
        else:
            train_test(fold, vocab, w2v, processor.input, processor.output, processor.both, processor.topSim)

            


