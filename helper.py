from nltk.corpus import treebank

TREEBANK_FILES = 199

def treebank_accessor():
  '''
  Function that reads the Penn treebank and returns all the trees 
  for each sentence in the corpus.
  '''
  trees = []

  for i in range(1, TREEBANK_FILES + 1):
    file_number = "%03d" % (i,)
    t = treebank.parsed_sents('wsj_0' + file_number + '.mrg')

    for sentence in range(len(t)):
      # For each sentence in the file, convert to a tree and add it to trees[]
      trees.append(t[sentence])

  return trees


def generate_grammar(trees):
  grammar = {}
  total_rules = 0

  for tree in trees:
    productions = tree.productions()

    for production in productions:
      lhs = production.lhs()
      rhs = production.rhs()

      # ignore rules with recursion
      if lhs in rhs:
        continue

      # only include rules derived from a NP
      if str(lhs) == 'NP':
        total_rules += 1
        if production in grammar:
          grammar[production] += 1
        else:
          grammar[production] = 1

  return grammar, total_rules


def get_probabilities(grammar, total_rules):
  probilistic_grammar = {}
  for rule in grammar:
    probilistic_grammar[rule] = grammar[rule] / float(total_rules)

  return probilistic_grammar


def calculate_accuracy(train, test, total_rules):
  count = 0
  for rule in test:
    if rule in train:
      count += test[rule]

  print 'NP rules found in grammar: {}'.format(count)
  print len(test)
  print 'total rules in found in test: {}'.format(total_rules)
  print len(train)
  error_ratio = total_rules - count
  error_ratio = total_rules / error_ratio
  print 'ratio 1:{}'.format(error_ratio)

  accuracy = (1.0 - (1.0 / error_ratio) ) * 100

  return accuracy


def write_grammar_in_file(grammar, sentences):
  file = open('results/'+str(sentences)+'.txt', 'w')

  file.write('# of rules: {}\n'.format(len(grammar)))
  for rule in grammar:
    file.write('{}\n'.format(rule))

  file.close()

