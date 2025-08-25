# The GridFather: Automated Crossword Solving from Images

## Overview
The GridFather is an end-to-end system designed to solve crossword puzzles directly from input images. Unlike conventional solvers that rely on structured text, this pipeline processes raw crossword images, extracts the grid and clues, generates potential answers using transformer-based models, and fills the puzzle grid through probabilistic inference.

This project was carried out as part of the INLP course under the guidance of **Dr. Manish Srivastava**.

**Team: The Tokenizers**
- Sanchit Kumar (2024201042)  
- Anubhav Mishra (2024201001)  
- Utkarsh Sachan (2024201012)  

---

## Features
- **Image Preprocessing**: Detect crossword grids using OpenCV (contours and perspective transformations).  
- **Clue Extraction**: Apply OCR and large language models (GPT-3.5/4) to parse and structure crossword clues.  
- **Candidate Generation**: Generate answer candidates using BERT, MiniBERT, QWEN, and T5 (fine-tuned on crossword datasets).  
- **Semantic Ranking**: Rank candidates via bi-encoder models trained for semantic similarity.  
- **Grid Solving**: Apply Loopy Belief Propagation (LBP) to enforce spatial constraints.  
- **Final Output**: Render the solved crossword grid as an image using Pillow.  

---

## Datasets
Two primary datasets were used in this project:

1. **CrosswordQA (Hugging Face)**  
   - Contains over 6.4M clue–answer pairs from multiple crossword publishers.  
   - Covers the period from 1950–2021, offering broad clue diversity.  

2. **New York Times Crossword Dataset (Kaggle)**  
   - Comprises 781K clues and answers (1993–2021).  
   - Utilized for fine-tuning and evaluation.  

---

## Methodology
The pipeline consists of the following stages:

1. **Image Processing** – Grid detection using contour extraction and perspective transformation.  
2. **OCR and LLM Parsing** – Extraction and structuring of clues.  
3. **Candidate Generation** – Fine-tuned models generate possible answers.  
4. **Semantic Ranking** – Candidates ranked using semantic similarity scores.  
5. **Grid Solving** – Loopy Belief Propagation applied to enforce crossword constraints.  
6. **Output Generation** – Solved crossword rendered as an image.  

**Pipeline Architecture:**  
```
Image → OCR & Grid Detection → LLM Clue Parsing → Candidate Generation
       → Semantic Ranking → Loopy Belief Propagation → Solved Grid
```

---

## Results
- **BERT (Closed-Book)**: 49% top-500 accuracy.  
- **MiniBERT (Fine-tuned)**: 39.5% top-500 accuracy.  
- **QWEN**: 14.55% top-10 accuracy.  
- **T5-small**: 15% top-10 accuracy.  

**End-to-End System Performance**:  
- Letter Accuracy: 11.28%  
- Word Accuracy: 1.43%  

**Benchmark Comparison (Gemini Solver):**  
- Gemini: 26.15% (letter), 11.43% (word)  
- The GridFather: 11.28% (letter), 1.43% (word)  

---

## Challenges
- OCR errors and noisy clue extraction.  
- Limited generalization of smaller transformer models.  
- Difficulty in handling figurative and wordplay clues.  
- Resource constraints limiting the use of larger-scale models.  

---

## Future Work
- Enhance OCR robustness for varied image quality.  
- Integrate larger models (e.g., GPT-4) for improved clue understanding.  
- Introduce clue-type tagging (puns, trivia, cryptic) to tailor candidate generation.  
- Refine the Loopy Belief Propagation framework for improved convergence.  

---

## Resources
All project files, source code, trained models, and experimental logs are available at the following link:  
[Project Resources](https://drive.google.com/drive/folders/1pHIToOkUD9Ayi__l03_0vHxV3D_8kf9I?usp=sharing)

This includes:
- Full Python implementation of the pipeline  
- Fine-tuned transformer checkpoints  
- Data samples and preprocessed files  
- Visualizations and final evaluation outputs  

---

## References
1. Littman, M. L., Keim, G. A., & Shazeer, N. M. (2002). *A probabilistic approach to solving crossword puzzles*. Artificial Intelligence, 134:23–55.  
2. Ginsberg, M. L. (2011). *Dr.Fill: Crosswords and an implemented solver for singly weighted CSPs*. arXiv, abs/1401.4597.  
3. Wallace, E., Tomlin, N., Xu, A., Yang, K., Pathak, E., Ginsberg, M., & Klein, D. (2022). *Automated crossword solving*.  
4. Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). *Tree of thoughts: Deliberate problem solving with large language models*.  

---
