+++
title = "Benchmarking Tasks for Document Analysis"
+++

This is the first post in a [series](@/posts/2024-02-06-pdf-parsing-series-intro.md) on document
parsing. I'm starting with a review of the benchmarking tasks because I want to understand problems
what the field is orienting itself around, and how they relate to the challenges of 
[extracting data from medical PDFs](@/posts/2024-02-06-pdf-parsing-series-intro.md#challenges-in-extracting-medical-data-from-pdfs).

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
