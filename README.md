# LT2212 V20 Assignment 1


Part 1

For part 1 I decided to get rid of punctuation and numbers and make a data frame only containing words with alphabetic characters because numbers and punctuation marks do not offer information as important as the information provided by actual words with meaning. I also decided to lowercase the terms to make my data structure case insensitive and consequently more generalized. In this assignment we were not asked to carry out a task related to e.g. syntactic disambiguation, in which case capitalization could matter in the analysis. Unfortunately, there was a drawback to lowercasing and removing punctuation and numbers since words like U.S. would be split up and turn into lowercase letters. That is why the data frame contains some random letters that can’t appear on their own in a text(for example u and s).

Part 4

In the plot made for the data frame from part 1 we could find mostly function words in both classes which makes sense because they are needed to express the grammatical relations between all the other words in the text and that is why their raw count is so high(for n=5, the top 5 words were the, to, of, in, said. When visualizing the tf-idf frame, on the other hand, we can see that most of the function words are filtered out and more “meaningful” content words appear in the plot and they highlight the content of the class as well. For example, words like oil are very common in the crude class while words like wheat are more often in the grain class

Part Bonus

I opted for a simple probabilistic classifier, that is why I chose the Gaussian Naïve Bayes Classifier. The accuracy score that I got for n=300 is higher for the  data drame with tf-idf scores than the data frame with the raw counts but only by very little(0.9568965517241379 for tf-idf, 0.9525862068965517 for the raw counts). The higher score of the tf-idf data frame makes sense since tf-idf’s role is to reflect the importance of a word in a corpus. It helps us distinct the two classes by pointing out which content words are more common in which class. As a result, the occurrence of a particular word that appears very often in a specific class will increase the chances of the document that it appears in belonging to that specific class once we classify it.
