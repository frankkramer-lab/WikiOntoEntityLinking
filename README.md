# WikiData-based Entity Linking for Medical Applications

This repository provides resources for entity linking task using Wikidata knowledge base. Building on a recently introduced [Named Entity Recognition pipeline](https://github.com/frankkramer-lab/WikiOntoNERCorpus/tree/main), this project offers a complementary module for normalizing medical recognized entities across various clinical terminology systems and languages.

## Repository Structure

- The `named_entity_linking` subfolder contains code for dataset acquision, model training and evaluation:
    - Scripts to generate custom entity linking dataset from Wikidata for given SPARQL-defined label classes
    - Model training via self-supervised contrastive learning strategy inspired by the [SapBERT paper](https://aclanthology.org/2021.naacl-main.334.pdf)
    - Evaluation pipeline using FAISS for large-scale similarity retrieval on external datasets

-  The `demo` subfolder includes a web application for querying custom ontologies via semantic similarity search:
    - Flask-based API with support for custom embedding models and knowledge bases
    - PostgreSQL database integration with the pgvector extension for fast vector-based retrieval