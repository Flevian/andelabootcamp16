def words(word_statement):

    """
    function that counts the number of word occurance in the input and return a dictionary
    the dictionary contains the word as the key and the total number of occurance as the value
    """

    wordcount={}

    for word in word_statement.split():

        """
        type cast the word to string if it is digit
        """
        if word.isdigit():
            word = int(word)

        """
        replace tabs an multilines with space since the are not counted
        """

        word_statement = word_statement.replace("\t", " ")
        word_statement = word_statement.replace("\n", " ")

        if word not in wordcount:
            wordcount[word] = 1

        else:
            wordcount[word] += 1

    return wordcount
