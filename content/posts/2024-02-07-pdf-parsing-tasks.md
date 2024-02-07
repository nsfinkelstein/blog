+++
title = "Benchmarking Tasks for Document Analysis"
updated = "2024-02-08"
+++

This is the first post in a [series](@/posts/2024-02-06-pdf-parsing-series-intro.md) on document
parsing. I'm starting with a review of the benchmarking tasks because I want to understand problems
what the field is orienting itself around, and how they relate to the challenges of 
[extracting data from medical Documents](@/posts/2024-02-06-pdf-parsing-series-intro.md#challenges-in-extracting-medical-data-from-pdfs).

The [Accelerating Document AI](https://huggingface.co/blog/document-ai) post by Hugging Face covers
some of the same ground. It was helpful context in writing this post and is worth a read.

I'll update this post as I come across new relevant tasks.

#### Document Question Answering

The document question answer task takes a document (PDF, image, or text) and a natural language
question about the document as inputs, and produces a natural language answer to that question as an
output.

The [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/) dataset is a dataset in which the
documents are text (extracted from wikipedia articles), the questions are English, and each question
is paired with one or more related substrings of the corresponding document, or a special token
indicating that the question is not answered in the document. There are \~500 documents, with
\~100,000 question-answer pairs, and an additional \~50,000 adversarial questions that seem like they
might be answered in the document but are not. 

These documents are not PDFs, but might be used to train the language part of a PDF parsing model.
In the worst case, they can be automatically converted to either scanned or digital PDF format with
simulated visual artifacts.

The [DocVQA](https://www.docvqa.org/) collection has 4 distinct data sets. The 
[DocVQA](https://www.docvqa.org/datasets/docvqa) dataset has \~12,000 images with \~50,000 questions.
Answers are also text extracted from the given document image. There are also similar, smaller
datasets for Infographics (rather than documents) and handwritten documents. The final dataset
groups documents into a [collection](https://arxiv.org/abs/2104.14336), and any document in the
collection can be used to answer the question.

The datasets can be downloaded [here](https://rrc.cvc.uab.es/?ch=17&com=downloads), after creation
of an account.

The related [PFL-DocVQA](https://benchmarks.elsa-ai.eu/?ch=2&com=downloads) datasets, which has
\~1,000,000 question-answer pairs on \~110,000 documents in total. At the moment, it seems only
\~250,000 are public, but the remainder should be published soon.

Both <https://rrc.cvc.uab.es> and <https://benchmarks.elsa-ai.eu>, which host the DocVQA and
PFL-DocVQA datasets respectively also have other interesting image-to-text datasets that might be
useful for pre-training parts of a document model.

The [DUDE](https://rrc.cvc.uab.es/?ch=23&com=introduction) data set contains \~5,000 PDF documents,
with \~20,000 question-answer pairs. Questions can be _extractive_, in which case the answer must
appear in the document, as for the datasets above, or _abstractive_, in which case the answer does
not appear in the document.

#### Document Classification

Document classification is what it sounds like.

The [RVL-CDIP](https://paperswithcode.com/dataset/rvl-cdip) dataset contains 400,000 images of
documents, each of which is assigned to one of 16 classes. The leaderboard is 
[here](https://paperswithcode.com/sota/document-image-classification-on-rvl-cdip), and can be
downloaded [here](https://adamharley.com/rvl-cdip/).

#### Document Layout Analysis

The layout analysis task aims to segment the documents into blocks, and classify each block. Common
block labels are things like _text_, _title_, _figure_, _table_, etc.

[PubLayNet](https://github.com/ibm-aur-nlp/PubLayNet#getting-data) contains ~360,000 scientific
papers drawn from PubMed. The dataset was constructed by "automatically matching XML representations
and the contents" of the papers.

#### Document Parsing

The document parsing task aims to extract specific kinds of information from a document. In the case
of forms, the goal is to extract key-value pairs, where each key is the name of a form-field, and
the value is the user-entered text for that field. This is also sometimes called Key Information
Extraction (KIE). Form and table parsing may be especially relevant to pulling information from
medical records. 

##### Forms Parsing

The Form Understanding from Noisy Scanned Documents 
([FUNDS](https://guillaumejaume.github.io/FUNSD/download/)) dataset has \~200 forms, with
information about words and their locations, _semantic entities_ &mdash; collections of related
words &mdash;, and relations links between key-value pairs. 
[Here](https://guillaumejaume.github.io/FUNSD/description/) is a nice summary-by-example of the data
available on each form.

The related [XFUND](https://github.com/doc-analysis/XFUND) dataset extends this idea to documents in
other languages. The dataset repository doesn't have much information, but it's described in the
[LayoutXLM](https://arxiv.org/abs/2104.08836v3) paper. XFUND contains \~1,400 annotated forms, at
\~200 per language. The dataset contains standard OCR data (i.e. words with bounding boxes), as well
as semantically significant sets of words, each of which is called a _semantic entity_. It also
contains annotated key-value pairs; a major goal is identifying the value associated with a given
key.

##### Table parsing

The [PubTables-1M](https://huggingface.co/datasets/bsmock/pubtables-1m) dataset contains \~575,000
pages, with a total of \~950,000 fully annotated tables. 
[Table annotations](
https://user-images.githubusercontent.com/10793386/139559159-cd23c972-8731-48ed-91df-f3f27e9f4d79.jpg
)
include column headers and _projected row headers_, which are used to subdivide the table into
vertical sections (see the linked image for an example). The dataset can also be used to learn to
identify tables in documents. 

The [FinTabNet](https://developer.ibm.com/exchanges/data/all/fintabnet/) dataset "contains complex
tables from the annual reports of S\&P 500 companies with detailed table structure annotations". It
has \~90,000 pages with \~110,000 tables. The annotations here seem to just indicate a bounding box
for each _table_, and a bounding box for each _cell_ in the table. See the bottom of 
[this notebook](
https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/f57cf3f6-e972-48ff-ab7b-3771ba7b9683/view?access_token=317644327d84f5d75b4782f97499146c78d029651a7c7ace050f4a7656033c30
) for examples.

On first look, it doesn't seem that either dataset includes a class for the kinds of notes that 
often appear in lab test reports 
([example 1](https://www.researchgate.net/profile/John-Flach/publication/267494297/figure/fig1/AS:392037380706311@1470480403318/An-example-of-a-typical-format-used-to-report-results-of-blood-analysis-to-the-physician.png),
[example 2](https://i.pinimg.com/736x/8e/a6/ef/8ea6efe0d12a1a580e8d1b3390a3e066.jpg)).
These kinds of notes often disrupt table recognition, as the same column headers apply above and
below the note. I've had trouble in the past where table identifiers either considered the parts of
a table separated by a note to be distinct tables, or else only recognized the part of the table
that precedes the note, as the remaining parts do not have identifiable column headers. 

Because the FinTabNet does not contain as semantic information about table structure, models trained
on it might be better able to recognize the notes as distinct cells; this will be interesting to
explore.

##### Receipts Parsing

The [SROIE dataset](https://rrc.cvc.uab.es/?ch=13&com=introduction) has \~1,000 receipt images. Each
receipt is annotated with standard word / bbox information, as well as a number of key-value pairs
(the example keys given are _company_, _date_, _address_, and _total_).

The [CORD](https://github.com/clovaai/cord) dataset has \~1,0000 receipts. Each receipt is annotated
with word / bbox information, as well as line-level and receipt-level classifications.


##### Datasets in other languages

I'll focus on English datasets for now, both because I can read English and because the documents
I'm interested in working with are in English. There are interesting datasets in other languages,
especially in Chinese. In particular, the [HUSTL-CELL](https://rrc.cvc.uab.es/?ch=21) dataset looks
relevant to key information extraction, and is primarily in Chinese.

#### Conclusion

This post is meant to provide an overview of the kinds of tasks that are currently used to evaluate
methods for Document AI. The corresponding datasets can be used for training or fine-tuning as well.

My overall impression is that there is low availability of large, high-quality annotated datasets,
especially for the [parsing](#document-parsing)-based tasks. This seems to be a bottleneck for
training, though perhaps less so for evaluation.

In the next post in the series, we'll look at unlabeled datasets that can be used for
self-supervised pre-training. I will be especially interested in methods for generating synthetic
labeled data. For medical document information extraction, it may be relevant to see if plausible
documents of varied structures can be created using synthetic FHIR data from 
[Synthea](https://github.com/synthetichealth/synthea).
