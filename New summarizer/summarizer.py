from transformers import PegasusForConditionalGeneration, PegasusTokenizer
#from web_page import new_summ

def generate_summary(text):

    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-multi_news")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-multi_news")
    tokens = tokenizer(text, truncation=True,padding="longest",return_tensors="pt")
    summary = model.generate(**tokens)
    decoded_summary = tokenizer.decode(summary[0])
    return decoded_summary

