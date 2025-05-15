# OpenAI Missing File Bug Reproduction

This repro replicates a bug in the OpenAI API where the model is unable to see
files when using old API keys.

Given two legacy API keys, one old and one new, the model is able to see files
when using the new key but not when using the old key.

The old key should be 51 characters long and the new key should be ~95 characters
long.

This reproduction hides a secret phrase (randomly generated) in a pdf
(./file.pdf). It then asks the model to respond with that phrase.

## Steps to Reproduce

1. Install UV
2. Modify .env by adding your two keys.
3. Run the script

```bash
$ ./main.py
```

## Expected Results

The final lines should match and show that the secret phrase was found,
something like

```
Good key result: The secret phrase is "consequence woman organization".
Bad key result: The secret phrase is "consequence woman organization".
```

## Actual Results

```
$ ./main.py
********************************************************************************
Full completion (good):
{'choices': [{'finish_reason': 'stop',
              'index': 0,
              'logprobs': None,
              'message': {'annotations': [],
                          'audio': None,
                          'content': 'The secret phrase is "consequence woman '
                                     'organization".',
                          'function_call': None,
                          'refusal': None,
                          'role': 'assistant',
                          'tool_calls': None}}],
 'created': 1747344042,
 'id': 'chatcmpl-BXaIM8ruH8qJ5ist52T0YCC2IxSF2',
 'model': 'gpt-4.1-2025-04-14',
 'object': 'chat.completion',
 'service_tier': 'default',
 'system_fingerprint': 'fp_b38e740b47',
 'usage': {'completion_tokens': 10,
           'completion_tokens_details': {'accepted_prediction_tokens': 0,
                                         'audio_tokens': 0,
                                         'reasoning_tokens': 0,
                                         'rejected_prediction_tokens': 0},
           'prompt_tokens': 244,
           'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0},
           'total_tokens': 254}}
********************************************************************************
Full completion (bad):
{'choices': [{'finish_reason': 'stop',
              'index': 0,
              'logprobs': None,
              'message': {'annotations': [],
                          'audio': None,
                          'content': 'Please upload the PDF file so I can '
                                     'review it and provide the secret phrase.',
                          'function_call': None,
                          'refusal': None,
                          'role': 'assistant',
                          'tool_calls': None}}],
 'created': 1747344043,
 'id': 'chatcmpl-BXaINEcUsKu96WQbnlIRTXwpPnVhd',
 'model': 'gpt-4.1-2025-04-14',
 'object': 'chat.completion',
 'service_tier': 'default',
 'system_fingerprint': 'fp_beec22d258',
 'usage': {'completion_tokens': 17,
           'completion_tokens_details': {'accepted_prediction_tokens': 0,
                                         'audio_tokens': 0,
                                         'reasoning_tokens': 0,
                                         'rejected_prediction_tokens': 0},
           'prompt_tokens': 17,
           'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0},
           'total_tokens': 34}}
********************************************************************************
Expected phrase: consequence woman organization
Good key result: The secret phrase is "consequence woman organization".
Bad key result: Please upload the PDF file so I can review it and provide the
secret phrase.
```
