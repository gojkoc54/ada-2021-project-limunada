## Title

Detection and analysis of major topics addressed by US politicians

## Abstract

The goal of our project is to investigate what are the topics and the problems that US politicians have addressed the most in the period of 2015 until the April of 2020. For this purpose, we used the Quotebank dataset that consists of more than 178M quotations extracted from English articles. We are not only interested in categorizing topics, but we also want to dive deeper into specific events that happened during the mentioned period. 

## Research question

1. What are the major topics addressed among US politicians?
2. How does the popularity of these topics change over time? 
3. Is it possible to detect certain events which justify such trends?
4. How much do US parties, Republicans and Democrats, address these problems?
5. Is it possible to compare the results with the results from previous research done on this matter?

## Data story website

To check out our data story website, with much more details, results, and a clear step-by-step walkthrough of our little ADA project journey, please visit the following website:

https://vukvukovic.github.io/limunADA-datastory/

## Milestones and methods

### Data cleaning, filtering and augmentation

(demonstrated in notebook **_basic_cleaning_and_filtering_**)

In this beginning phase, we got acquainted with the Quotebank dataset and performed initial cleaning of our data, before diving into the analysis:

- Filter out the quotations from the years of interest
- Drop quotations with the most probable speaker being unidentified

Since we decided to analyze the quotes as two separate categories - Democrats and Republicans, we split the quotes into those respective groups accordingly, depending on the political party of each of the speakers. We used the Wikidata API to associate speakers to their political parties. Thus, the final two steps of this phase were the following:

- Enrich Quotebank dataset with features from Wikidata: add speaker&#39;s age, nationality, political party (at the time of the quote), academic degree, ethnicity, etc.
- Filter out the quotations from political figures from the Democratic and Republican parties

### Methodology

**_LDA for topic modeling_**

(demonstrated in notebook **_topic_modelling_**)

In order to detect major topics addressed among US politicians, we used the LDA (Latent Dirichlet Allocation) method.

**_SBERT for quote-topic categorization_**

(demonstrated in notebook **_BERT_embeddings_**)

In order to categorize the quotations into certain topics, we applied the SBERT (Sentence-BERT) model. In a sense, this could be interpreted as a method for searching quotes, given topics.

### Analysis of topics and their presence in the media over time

Finally, we assemble the results of the two previous points and analyze the topics that have been covered by Republicans and Democrats over time. We don't only detect these topics, but also assess to which extent they were addressed by the members of the two parties. Additionally, we cover our 5th research question by comparing these results to a study by the Pew Research Center, but please read more on that on our data story website.

## Contributions of our team members

| Week | Milestone | Responsibility \* |
| --- | --- | --- |
| 1 | Data cleaning, filtering and augmentation | M, V |
| 2 | LDA topic modelling | G, V |
| 3 | LDA cluster analysis | J, M |
| 4 | SBERT quote-topic categorization | G, J |
| 5 | Analysis and visualization of obtained results | J, M |
| 6 | Code organization and cleaning | G |
| 7 | Data storytelling | J, V |
| 8 | Website | V |

\* G = Gojko, J = Jana, M = Miloš, V = Vuk

## References

- [Quotebank Dataset](https://zenodo.org/record/4277311#.Yb0QV73MIUF)

- [SBERT (Sentence-BERT)](https://www.sbert.net/)

- [Huggingface SBERT](https://huggingface.co/sentence-transformers)

- [Gensim LDA model](https://radimrehurek.com/gensim/models/ldamodel.html)

- [LDA Visualizer](https://github.com/bmabey/pyLDAvis)

- [Pew Research Center - Views of the major problems facing the country](https://www.pewresearch.org/politics/2019/12/17/views-of-the-major-problems-facing-the-country/)



