#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "dotenv",
#   "pypdf",
#   "openai",
# ]
# ///

import sys
import os
import openai
import pypdf
import base64

import dotenv

HELP = """
Repro OpenAI API bug:

  In file .env:
  ```
  OPENAI_API_KEY_GOOD=... new working key (95 chars)
  OPENAI_API_KEY_BAD=... old non-working key (51 chars)
  ```

  Usage: python main.py
"""


def create_pdf(expected_phrase: str):
  pypdf.PdfWriter().add_page()


def run_with_pdf_contents(api_key: str, pdf_contents: bytes):
  # Encode the PDF as base64
  # https://platform.openai.com/docs/guides/pdf-files?api-mode=chat#base64-encoded-files
  b64_encoded = base64.b64encode(pdf_contents).decode()
  pdf_base64 = "data:application/pdf;base64," + b64_encoded

  messages = [
    {
      "role": "system",
      "content": "Respond with the secret phrase contained in the PDF.",
    },
    {
      "role": "user",
      "content": [
        {
          "type": "file",
          "file": {"file_data": pdf_base64, "filename": "questionnaire.pdf"},
        },
      ],
    },
  ]

  client = openai.Client(api_key=api_key)
  completion = await client.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=messages,
    temperature=0.0,
    n=1,
    seed=1338,
  )

  return completion.choices[0].message.content


def main():
  dotenv.load_dotenv()
  good_key = os.getenv("OPENAI_API_KEY_GOOD")
  bad_key = os.getenv("OPENAI_API_KEY_BAD")

  if not good_key or not bad_key:
    print(HELP)
    sys.exit(1)

  expected_phrase = "consequence woman organization"
  pdf_contents = create_pdf(expected_phrase)

  # Test with the good key
  good_result = run_with_pdf_contents(good_key, pdf_contents)
  bad_result = run_with_pdf_contents(bad_key, pdf_contents)

  print("Expected phrase:", expected_phrase)
  print("Good key result:", good_result)
  print("Bad key result:", bad_result)
