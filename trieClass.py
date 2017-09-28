from __future__ import print_function


# initialize MyTrie Node
class MyTrieNode:

    # Initialize attributes to call on self
    def __init__(self, isRootNode):
        self.isRoot = isRootNode
        self.isWordEnd = False
        self.isRoot = False
        self.count = 0
        self.next = {}

# initialize addWord function to add nodes to the Trie
    def addWord(self, w):
        # assert that w exists
        assert(len(w) > 0)
        # if the first index isnt in the dictionary
        if w[0] not in self.next:
            # set value
            self.next[w[0]] = MyTrieNode(False)
        # if w length is greater than one, make recursive call
        if (len(w) is not 1):
            # recursive call
            self.next[w[0]].addWord(w[1:])
        # if w length is one, set its word end value to true and increment the counter
        elif (len(w) is 1):
            self.next[w[0]].isWordEnd = True
            self.next[w[0]].count += 1
        return

    # initialize lookupWord function
    def lookupWord(self, w):
        # Determines the number of times the word appears
        # if there is no word then it does not occur
        if (len(w) is 0):
            return 0
        # if there are no corresponding elements then it does not occur
        if w[0] not in self.next:
            return 0

        # if we are not at the end yet, call function recursively to keep going
        if len(w) is not 1 or self.next[w[0]].isWordEnd is False:
            # recursive call
            return self.next[w[0]].lookupWord(w[1:])
        # otherwise, we are at the end, so return the incrementer so we know
        # the number of times the word appeared
        else:
            # returns incrementer
            return self.next[w[0]].count

    # initialize suffix finding function
    def determine_suffix(self, w):
        # this funtion will get all of the possible outcomes
        # initialize results list
        results = []
        # loop through self.next
        for inc in self.next:
            # call recursively to get every outcome on each loop
            results = results + self.next[inc].determine_suffix(w+inc)
        # if we hit the end of the word, append the word
        # and the number of times it occurs to the results list
        if self.isWordEnd is True:
            # appendage to results list
            results.append((w, self.count))
        # return the results list
        return results

    # intialize autocomplete function
    def autoComplete(self, w):
        # function to return tuples that give the word
        # completions and the number of times that they occur
        results = []
        # loop through to move through the input till the end of the input
        for inc in range(0, len(w)):
            if w[inc] in self.next:
                # reassign self node accordingly
                self = self.next[w[inc]]
            else:
                return []
        # if the end of the eord is the input, return results with corresponding incrementer
        if self.isWordEnd is True:
            results = [(w[0:], self.count)]
        # call determine_suffix to determine all the outcomes
        for inc in self.next:
            results = results + self.next[inc].determine_suffix(w + inc)
        # return final result
        return results


if (__name__ == '__main__'):
    t = MyTrieNode(True)
    lst1 = [
            'test',
            'testament',
            'testing',
            'ping',
            'pin',
            'pink',
            'pine',
            'pint',
            'testing',
            'pinetree'
    ]

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy')  # should return 0
    j2 = t.lookupWord('telltale')  # should return 0
    j3 = t.lookupWord('testing')  # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
