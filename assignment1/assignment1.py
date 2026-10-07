#Task 1: hello function
def hello():
    return "Hello!"

print(hello())

#Task2: Greeting function
def greet(name):
    return f"Hello, {name}!"

print(greet("Roy"))

#calculator function
def calc(val1, val2, operation = "multiply"):
    try:
        low_case = operation.lower()
        match low_case:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "multiply":
                return val1 * val2 
            case "divide":
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                return val1 // val2
            case "power":
                return val1 ** val2
    except ZeroDivisionError:
        return f"You can't divide by 0!"
    except TypeError:
        return f"You can't {low_case} those values!"

#Task 4:
def data_type_conversion(value, type):
    try:
        match type:
            case "int":
                return int(value)
            case "str":
                return str(value)
            case "float":
                return float(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."

#Task 5: 
def grade(*args):
    try:
        avg = sum(args)/len(args)
        if avg < 60:
            return f"F"
        elif avg < 70:
            return f"D"
        elif avg <80:
            return f"C"
        elif avg <90:
            return f"B"
        else:
            return f"A"
    except TypeError:
        return f"Invalid data was provided."

#Task 6:
def repeat(word, count):
    words = ""
    for num in range(count):
        words = words + word
    return words

#Task 7: 
#input names and best, mean.
#output names, mean: mean of names
#output names, best: name w/highest grade
def student_scores(mean_or_best,**kwargs):
    if mean_or_best == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif mean_or_best == "best":
        target_score = 0
        target_name = ""
        for base_student, base_score in kwargs.items():
            if base_score > target_score:
                target_score = base_score
                target_name = base_student
        return target_name

#Task 8:
def titleize(string_param):
    words = string_param.split()
    not_these = ["a", "on", "an", "the", "of", "and", "is", "in"]
    #for loop to capitalize each word. 
    #need to capitalize all words except some.
    #not in ()
    for i, word in enumerate(words):
        if word not in not_these:  
            words[i] = word.capitalize()
    if words[-1] in not_these:
        words[-1] = words[-1].capitalize()
    if words[0] in not_these:
            words[0] = words[0].capitalize()
    return " ".join(words)

#Task 9:
#Result: __ __ a b __ __
#take in word find where letter exists in word
#if letter not in word, insert/replace with __
def hangman(secret, guess):
    empty_word = ""
    for element in secret:
        if element not in guess:
            empty_word = empty_word + "_"
        else:
            empty_word = empty_word + element
    return empty_word

#Task 10:
#determine where first vowel is
#slice to remove up to that point
#concatenate the other half of sliced word.
#concatenate ay
def pig_latin(word_or_sentence):
    split_entry = word_or_sentence.split()
    updated_pig_words = []
    for element in split_entry:
        for i, letter in enumerate(element):
            if i == 0 and letter in ['a', 'e', 'i', 'o', 'u']:
                pig_word = element + "ay"
                break
            elif letter == "u" and i > 0 and element[i - 1] == "q":
                continue
            elif letter not in ['a', 'e', 'i', 'o', 'u']:
                #then go to the next letter until first vowel
                #track how far you go to know where to slice word
                #then need to use what I know to attain the portion sliced and concat
                continue
            elif letter in ['a', 'e', 'i', 'o', 'u']:
                pig_word = element[i:] + element[:i] + "ay"
                break
        updated_pig_words.append(pig_word)    
    joined_pig = " ".join(updated_pig_words)
    return joined_pig
                

    