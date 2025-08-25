import os
import pandas as pd
from Solver import solve

print(os.getcwd())

N_CROSSWORDS = 50

df = pd.read_csv('final_code/new_crossword_info.csv')
data_folder_path = "flattened_files/"

sample = df.sample(n=N_CROSSWORDS)

solution_df = sample.copy()
acc_df = sample.copy()

letter_acc_col = []
word_acc_col = []
solutions_col = []
word_pred_col = []
if __name__ == "__main__":
    #count = 0
    letter_acc, word_acc, solution, word_pred = solve("inference_puzzles/merged_puzzle2.json", index=-99)
    # for row in sample.iterrows():
    #     count += 1
    #     if count % 10==0:
    #         print(f"{count} files complete!")
    #     filepath = row[-1][-1]
    #     full_path = os.path.join(data_folder_path, filepath)
    #     print("full_path")
    #     print(full_path)
    #     try:
    #         letter_acc, word_acc, solution, word_pred = solve(full_path, index=count)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         letter_acc, word_acc, solution, word_pred = -1, -1, "WRONG", "WRONG"
    #         print("Invalid attempt")

    #     letter_acc_col.append(letter_acc)
    #     word_acc_col.append(word_acc)
    #     solutions_col.append(solution)
    #     word_pred_col.append(word_pred)

# create and save solutions dataset

# solution_df['Solutions'] = solutions_col
# solution_df.to_csv('solutions_dataset.csv', index=False)

# create and save accuracies dataset

# acc_df['Letter'] = letter_acc_col
# acc_df['Word'] = word_acc_col
# acc_df['PredictionPairs'] = word_pred_col
# acc_df.to_csv('accuracies.csv', index=False)

