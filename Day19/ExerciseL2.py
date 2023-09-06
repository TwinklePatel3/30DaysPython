#                           Exercises: Level 2
import csv
import math
import re

# 1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
with open('./Data/email_exchanges_big.txt') as f:
    data = f.read()
    regex_pattern = r'from:\s+\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(regex_pattern, data, re.I)
    emails_list = [re.sub("[fF]rom:\s", "", x, re.I) for x in set(emails)]
    print(emails_list)

# 2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]


def find_most_common_words(filepath, num):
    with open(filepath) as f:
        content = f.read()
        words = re.findall('\w+', content.lower(), re.I)
        words_count = [(words.count(x), x) for x in set(words)]
        return sorted(set(words_count), reverse=True)[:int(num)]


print(find_most_common_words("./Data/sample.txt", 5))

# 3. Use the function, find_most_frequent_words to find:
# a) The ten most frequent words used in Obama's speech
# b) The ten most frequent words used in Michelle's speech
# c) The ten most frequent words used in Trump's speech
# d) The ten most frequent words used in Melina's speech
print("The ten most frequent words used in Obama's speech : ",
      find_most_common_words("./Data/obama_speech.txt", 10))
print("The ten most frequent words used in Michelle's speech :",
      find_most_common_words("./Data/michelle_obama_speech.txt", 10))
print("The ten most frequent words used in Trump's speech :",
      find_most_common_words('./Data/donald_speech.txt', 10))
print("The ten most frequent words used in Melina's speech :",
      find_most_common_words('./Data/melina_trump_speech.txt', 10))

# 4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory


def clean_text(file_content):
    regex_pattern = r'[^\w|\s]'
    text = re.sub(regex_pattern, "", file_content)
    return text.split()


def remove_support_words(filepath):
    with open(filepath) as f:
        content = f.read()
        clean_words = clean_text(content)
        final_words = []
        with open('./Data/stop_words.py') as sw:
            stop_words = sw.read()
            final_words = [x for x in clean_words if x.lower()
                           not in stop_words]
        return set(final_words)


def check_text_similarity(filepath1, filepath2):
    txt1 = remove_support_words(filepath1)
    txt2 = remove_support_words(filepath2)
    return f'The similarity of {filepath1} and {filepath2} is :{math.floor(len(txt2.intersection(txt1))/len(txt1)*100)}%'


print(check_text_similarity('./Data/michelle_obama_speech.txt',
                            './Data/melina_trump_speech.txt'))

# 5. Find the 10 most repeated words in the romeo_and_juliet.txt
print("10 most repeated words in the romeo_and_juliet.txt",
      find_most_common_words("./Data/romeo_and_juliet.txt", 10))

# 6. Read the hacker news csv file and find out:
# a) Count the number of lines containing python or Python
# b) Count the number lines containing JavaScript, javascript or Javascript
# c) Count the number lines containing Java and not JavaScript


def count_number_of_lines(word):
    with open('./Data/hacker_news.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0

        for row in csv_reader:
            match = re.findall(word, str(row), re.I)
            if match:
                line_count += 1
        return line_count


print("The number of lines containing python or Python :",
      count_number_of_lines("[pP]ython"))

print("The number of lines containing JavaScript, javascript or Javascript :",
      count_number_of_lines("[Jj]ava[Ss]cript"))

print("The number of lines containing Java not Javascript :",
      count_number_of_lines("Java"))
