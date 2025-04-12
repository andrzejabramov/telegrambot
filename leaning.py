import requests
import json

#r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')# делаем запрос на сервер по переданному адресу
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
# texts = json.loads(r.content)
# #print(r.content, r.status_code)
# print(type(texts))
#
# for text in texts:
#     print(text[:50], '\n')

# r = requests.post('https://httpbin.org/post', data = {'key':'value'})  # отправляем POST-запрос
# print(r.content)

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)
print(r[0])



