from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


def get_sentiment(messages):
    results = model.predict(messages, k=2)
    for message, sentiment in zip(messages, results):
        return message + "\n Эмоциональный контекст: " + list(sentiment.items())[0][0] + "\n С точностью: " + str(list(sentiment.items())[0][1] * 100) + "\n"


