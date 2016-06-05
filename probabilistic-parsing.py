import helper

TRAINING_SENTENCES = 3524 # ~90%
TESTING_SENTENCES = 390 # ~10%

trees = helper.treebank_accessor()

sentences = len(trees) #3914
print 'total sentences: {}'.format(sentences)

# train grammar and probabilistic grammar
grammar_train, train_rules = helper.generate_grammar(trees[:TRAINING_SENTENCES]) # train grammar and probabilistic grammar
train_prob_grammar = helper.get_probabilities(grammar_train, train_rules)

helper.write_grammar_in_file(grammar_train, sentences)

# test grammar and probabilistic grammar
grammar_test, test_rules = helper.generate_grammar(trees[TRAINING_SENTENCES:])
# test_prob_grammar = helper.get_probabilities(grammar_test, test_rules)

# check how many rules were found in the train from the test
accuracy = helper.calculate_accuracy(grammar_train, grammar_test, test_rules)
print 'accuracy: {}'.format(accuracy)