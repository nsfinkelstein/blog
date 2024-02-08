+++
title = "Parsing lab test results"
draft = true
+++

#### Overview

### Table parsing

Microsoft has a "table transformer" that they trained on each of the two table parsing datasets, and
then also on the combination of the two.

<https://github.com/microsoft/table-transformer#news>

Try these both on a lab test report. In particular, see how they account for "notes".


##### Tasks

Questio

Model Taxonomy & Specific Models

###### DocLLM: <https://arxiv.org/abs/2401.00908>

Takes OCR outputs as inputs. Operates on words, blocks and bounding boxes. Attention heads attend to
spatial and textual context.

###### Rationale Distillation: <https://arxiv.org/abs/2311.09612>


Datasets
