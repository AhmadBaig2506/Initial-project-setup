# On-Device AI Search

## Project Overview

A lightweight AI search assistant that retrieves web information, ranks relevant passages, and uses a locally running small language model to generate source-backed answers.

## Initial Architecture

1. User enters a search query.
2. DuckDuckGo retrieves relevant webpages.
3. Webpage text is extracted using trafilatura.
4. BM25 ranks relevant passages.
5. A local SLM generates a short answer.
6. The application displays the answer with source citations.

## Development Setup

Requirements: Python 3.11 or 3.12.

Install dependencies:

`
python -m pip install -r requirements.txt
`

Verify the environment:

`
python test_setup.py
`

## Current Progress

- [x] Development environment configured
- [x] Search pipeline implemented
- [x] Text extraction implemented
- [x] BM25 ranking implemented
- [x] Local SLM integrated
- [x] Streamlit interface implemented

## Target

Run model inference locally on a CPU with less than 4 GB RAM, following the group's project proposal.
