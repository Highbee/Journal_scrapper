text = "<b> jdoth this is bec 複製品ause we are the best"

response_text = text
response_text = response_text.encode('ascii', errors='replace')
response_text = response_text.decode('utf-8')
print(response_text)
