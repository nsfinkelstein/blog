+++
title = "Benchmarking Tasks for Document Analysis"
+++

This is the first post in a [series](@/posts/2024-02-06-pdf-parsing-series-intro.md) on document
parsing. I'm starting with a review of the benchmarking tasks because I want to understand problems
what the field is orienting itself around, and how they relate to the challenges of 
[extracting data from medical PDFs](@/posts/2024-02-06-pdf-parsing-series-intro.md#challenges-in-extracting-medical-data-from-pdfs).

I found [this post by hugging face](https://huggingface.co/blog/document-ai) on the same
topic to be a very useful overview.  
This post reviews that major categories of tasks, and key benchmarking datasets used in each
category. 
post offers less high-level descriptions of the task
categories and more details about specific benchmarking datasets.

#### Document Question Answering

The document question answer task takes a document (PDF, image, or text) and a natural language
question about the document as inputs, and produces a natural language answer to that question as an
output.

The [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/) dataset is a dataset in which the
documents are text (extracted from wikipedia articles), the questions are English, and each question
is paired with one or more related substrings of the corresponding document, or a special token
indicating that the question is not answered in the document. There are ~500 documents, with
~100,000 question-answer pairs, and an additional ~50,000 adversarial questions that seem like they
might be answered in the document but are not. 

These documents are not PDFs, but might be used to train the language part of a PDF parsing model.
In the worst case, they can be automatically converted to either scanned or digital PDF format with
simulated visual artifacts.


The [DocVQA](https://www.docvqa.org/) collection has 4 distinct data sets. The 
[DocVQA](https://www.docvqa.org/datasets/docvqa) dataset has ~12,000 images with ~50,000 questions.
Answers are also text extracted from the given document image. There are also similar, smaller
datasets for Infographics (rather than documents) and handwritten documents. The final dataset
groups documents into a [collection](https://arxiv.org/abs/2104.14336), and any document in the
collection can be used to answer the question.

The datasets can be downloaded [here](https://rrc.cvc.uab.es/?ch=17&com=downloads), after creation
of an account.

The related [PFL-DocVQA](https://benchmarks.elsa-ai.eu/?ch=2&com=downloads) datasets, which has
~1,000,000 question-answer pairs on ~110,000 documents in total. At the moment, it seems only
~250,000 are public, but the remainder should be published soon.

Both <https://rrc.cvc.uab.es> and <https://benchmarks.elsa-ai.eu>, which host the DocVQA and
PFL-DocVQA datasets respectively also have other interesting image-to-text datasets that might be
useful for pre-training parts of a document model.

#### Document Classification

Document classification is what it sounds like.

The [RVL-CDIP](https://paperswithcode.com/dataset/rvl-cdip) dataset contains 400,000 images of
documents, each of which is assigned to one of 16 classes. The leaderboard is 
[here](https://paperswithcode.com/sota/document-image-classification-on-rvl-cdip), and can be
downloaded [here](https://adamharley.com/rvl-cdip/).

#### Layout Analysis

The layout analysis problem

#### Parsing

The 
[Form Understanding from Noisy Scanned Documents dataset](https://guillaumejaume.github.io/FUNSD/download/)
