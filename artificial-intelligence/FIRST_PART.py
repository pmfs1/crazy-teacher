import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import string
import time
from MODULES.SINGLE_NAIVE_BAYES_ALGORITHM import Bayes
from MODULES.SINGLE_PERCEPTRON_ALGORITHM import Perceptron
from MODULES.MODEL import Model

if __name__ == '__main__':
    # START A TIMER TO CALCULATE THE EXECUTION TIME:
    START_TIME = time.time()
    # ---------------------------- LOAD THE DATA ----------------------------
    VOCABULARY_START_TIME = time.time() # START A TIMER TO CALCULATE THE VOCABULARY EXECUTION TIME
    DATA = pd.read_csv("SPAM.csv", engine='python', encoding='ISO-8859-1') # LOAD THE DATA FROM THE CSV FILE
    DATA = DATA[['v1', 'v2']] # KEEP ONLY THE FIRST TWO COLUMNS
    DATA.rename(columns={'v1': 'SPAM', 'v2': 'TEXT'}, inplace=True) # RENAME THE COLUMNS TO 'SPAM' AND 'TEXT'
    DATA.SPAM = DATA.SPAM.apply(lambda s: 1 if s=='spam' else -1) # CONVERT THE 'SPAM' COLUMN TO 1 IF THE MESSAGE IS SPAM, -1 IF THE MESSAGE IS NOT SPAM
    DATA.TEXT = DATA.TEXT.apply(lambda t: t.lower().translate(str.maketrans('', '', string.punctuation))) # CONVERT THE 'TEXT' COLUMN TO LOWER CASE AND REMOVE PUNCTUATION FROM THE TEXT
    DATA.sample(frac=1).reset_index(drop=True) # SHUFFLE THE DATA
    TEXT = DATA.TEXT.values # GET THE TEXT COLUMN AS A LIST
    TAGS = DATA.SPAM.values # GET THE SPAM COLUMN AS A LIST
    # ---------------------------- PREPROCESS THE DATA ----------------------------
    VOCABULARY = np.unique(np.concatenate([SAMPLE.split() for SAMPLE in TEXT])) # CREATE A VOCABULARY OF UNIQUE WORDS FROM THE TEXT COLUMN
    # CREATES A DATASET WHERE EACH SAMPLE IS A DICIONARY WHERE THE KEY IS THE WORD AND THE VALUE IS THE ABSOLUTE FREQUENCY (COUNT) OF THE WORD IN THE SAMPLE FOR EACH WORD IN THE VOCABULARY:
    DATASET = [[SAMPLE.split().count(WORD) for WORD in VOCABULARY] for SAMPLE in TEXT]
    # SPLIT THE DATA INTO TRAINING, TEST AND VALIDATION SETS WITH A 70%/15%/15% PERCENTAGE RATIO:
    TRAIN_DATA = DATASET[:int(len(DATASET)*0.7)] # TRAINING SET
    TEST_DATA = DATASET[int(len(DATASET)*0.7):int(len(DATASET)*0.85)] # TEST SET
    VALIDATION_DATA = DATASET[int(len(DATASET)*0.85):] # VALIDATION SET
    TRAIN_TAGS = TAGS[:int(len(TAGS)*0.7)] # TRAINING SET
    TEST_TAGS = TAGS[int(len(TAGS)*0.7):int(len(TAGS)*0.85)] # TEST SET
    VALIDATION_TAGS = TAGS[int(len(TAGS)*0.85):] # VALIDATION SET
    # PRINT THE EXECUTION TIME OF THE VOCABULARY:
    print("[VOCABULARY EXECUTION TIME: {:.4} SECONDS]".format(time.time() - VOCABULARY_START_TIME))
    # ---------------------------- TRAIN AND EVALUATE THE MODELS ----------------------------
    # ---------------------------- BAYES ----------------------------
    BAYES_START_TIME = time.time() # START A TIMER TO CALCULATE THE BAYES EXECUTION TIME
    BAYES = Model(Bayes(), VALIDATION_DATA, VALIDATION_TAGS) # CREATE A MODEL FOR THE BAYES
    BAYES.FIND_BEST_HYPERPARAMETERS(TRAIN_DATA, TRAIN_TAGS) # FIND THE BEST HYPERPARAMETERS FOR THE BAYES
    # PRINT THE C HYPERPARAMETER FOR THE BAYES:
    print("[SELECTED THE BEST HYPERPARAMETER FOR THE BAYES: C = {}]".format(BAYES.BEST_C))
    BAYES.TRAIN(TRAIN_DATA, TRAIN_TAGS) # TRAIN THE MODEL ON THE TRAINING SET
    BAYES_ACCURACY, BAYES_ERROR_RATE, BAYES_SENSITIVITY, BAYES_SPECIFICITY, BAYES_PRECISION, BAYES_RECALL, BAYES_F_MEASURE, BAYES_GEOMETRIC_MEAN, BAYES_CONFUSION_MATRIX = BAYES.SCORE(TEST_DATA, TEST_TAGS) # USES THE TEST SET TO PROVIDE AN UNBIASED EVALUATION OF THE FINAL MODEL FIT ON THE TRAINING SET
    # PRINT THE METRICS IN GREEN:
    print("BAYES:")
    print("ACCURACY: {:.4%}".format(BAYES_ACCURACY))
    print("ERROR RATE: {:.4%}".format(BAYES_ERROR_RATE))
    print("SENSITIVITY: {:.4%}".format(BAYES_SENSITIVITY))
    print("SPECIFICITY: {:.4%}".format(BAYES_SPECIFICITY))
    print("PRECISION: {:.4%}".format(BAYES_PRECISION))
    print("RECALL: {:.4%}".format(BAYES_RECALL))
    print("F-MEASURE: {:.4%}".format(BAYES_F_MEASURE))
    print("GEOMETRIC MEAN: {:.4}".format(BAYES_GEOMETRIC_MEAN))
    # PRINTS THE CONFUSION MATRIX AS A TABLE (IN AN EASIER TO READ FORMAT):
    # CONFUSION_MATRIX = np.array([
    #         [TRUE_POSITIVES, FALSE_POSITIVES],
    #         [FALSE_NEGATIVES, TRUE_NEGATIVES]
    #     ]) # CREATE A CONFUSION MATRIX
    print("CONFUSION MATRIX:")
    print("TRUE POSITIVES: {}".format(BAYES_CONFUSION_MATRIX[0][0]))
    print("FALSE POSITIVES: {}".format(BAYES_CONFUSION_MATRIX[0][1]))
    print("FALSE NEGATIVES: {}".format(BAYES_CONFUSION_MATRIX[1][0]))
    print("TRUE NEGATIVES: {}".format(BAYES_CONFUSION_MATRIX[1][1]))
    # PRINT THE EXECUTION TIME OF THE BAYES IN MINUTES:
    print("[BAYES EXECUTION TIME: {:.4} MINUTES]".format((time.time() - BAYES_START_TIME)/60))
    # ---------------------------- PERCEPTRON ----------------------------
    PERCEPTRON_START_TIME = time.time() # START A TIMER TO CALCULATE THE PERCEPTRON EXECUTION TIME
    PERCEPTRON = Model(Perceptron(), VALIDATION_DATA, VALIDATION_TAGS) # CREATE A MODEL FOR THE PERCEPTRON
    PERCEPTRON.FIND_BEST_HYPERPARAMETERS(TRAIN_DATA, TRAIN_TAGS) # FIND THE BEST HYPERPARAMETERS FOR THE PERCEPTRON
    # PRINT THE T HYPERPARAMETER FOR THE PERCEPTRON:
    print("[SELECTED THE BEST HYPERPARAMETER FOR THE PERCEPTRON: T = {}]".format(PERCEPTRON.BEST_T))
    PERCEPTRON.TRAIN(TRAIN_DATA, TRAIN_TAGS) # TRAIN THE MODEL ON THE TRAINING SET
    PERCEPTRON_ACCURACY, PERCEPTRON_ERROR_RATE, PERCEPTRON_SENSITIVITY, PERCEPTRON_SPECIFICITY, PERCEPTRON_PRECISION, PERCEPTRON_RECALL, PERCEPTRON_F_MEASURE, PERCEPTRON_GEOMETRIC_MEAN, PERCEPTRON_CONFUSION_MATRIX = PERCEPTRON.SCORE(TEST_DATA, TEST_TAGS) # USES THE TEST SET TO PROVIDE AN UNBIASED EVALUATION OF THE FINAL MODEL FIT ON THE TRAINING SET
    # PRINT THE METRICS:
    print("[PERCEPTRON]")
    print("ACCURACY: {:.4%}".format(PERCEPTRON_ACCURACY))
    print("ERROR RATE: {:.4%}".format(PERCEPTRON_ERROR_RATE))
    print("SENSITIVITY: {:.4%}".format(PERCEPTRON_SENSITIVITY))
    print("SPECIFICITY: {:.4%}".format(PERCEPTRON_SPECIFICITY))
    print("PRECISION: {:.4%}".format(PERCEPTRON_PRECISION))
    print("RECALL: {:.4%}".format(PERCEPTRON_RECALL))
    print("F-MEASURE: {:.4%}".format(PERCEPTRON_F_MEASURE))
    print("GEOMETRIC MEAN: {:.4}".format(PERCEPTRON_GEOMETRIC_MEAN))
    # PRINTS THE CONFUSION MATRIX AS A TABLE (IN AN EASIER TO READ FORMAT):
    # CONFUSION_MATRIX = np.array([
    #         [TRUE_POSITIVES, FALSE_POSITIVES],
    #         [FALSE_NEGATIVES, TRUE_NEGATIVES]
    #     ]) # CREATE A CONFUSION MATRIX
    print("CONFUSION MATRIX:")
    print("TRUE POSITIVES: {}".format(PERCEPTRON_CONFUSION_MATRIX[0][0]))
    print("FALSE POSITIVES: {}".format(PERCEPTRON_CONFUSION_MATRIX[0][1]))
    print("FALSE NEGATIVES: {}".format(PERCEPTRON_CONFUSION_MATRIX[1][0]))
    print("TRUE NEGATIVES: {}".format(PERCEPTRON_CONFUSION_MATRIX[1][1]))
    # PRINT THE EXECUTION TIME OF THE PERCEPTRON IN MINUTES:
    print("[PERCEPTRON EXECUTION TIME: {:.4} MINUTES]".format((time.time() - PERCEPTRON_START_TIME) / 60))
    # ---------------------------- COMPARING THE TWO MODELS ----------------------------
    # COMPARING THE TWO MODELS:
    if BAYES_ACCURACY > PERCEPTRON_ACCURACY: # IF THE BAYES CLASSIFIER IS MORE ACCURATE THAN THE PERCEPTRON:
        print("[BAYES CLASSIFIER IS MORE ACCURATE THAN THE PERCEPTRON BY {:.4%}]".format(BAYES_ACCURACY - PERCEPTRON_ACCURACY)) # PRINT THE DIFFERENCE IN ACCURACY
    else: # IF THE PERCEPTRON IS MORE ACCURATE THAN THE BAYES CLASSIFIER:
        print("[PERCEPTRON IS MORE ACCURATE THAN THE BAYES CLASSIFIER BY {:.4%}]".format(PERCEPTRON_ACCURACY - BAYES_ACCURACY)) # PRINT THE DIFFERENCE IN ACCURACY
    # ---------------------------- END OF THE PROGRAM ----------------------------
    # PRINT THE TIME TAKEN TO RUN THE PROGRAM IN MINUTES:
    print("[PROGRAM EXECUTION TIME: {:.4} MINUTES]".format((time.time() - START_TIME) / 60))