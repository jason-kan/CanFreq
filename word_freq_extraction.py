import pycantonese
token_list=[]
url = "https://childes.talkbank.org/data/Chinese/Cantonese/LeeWongLeung.zip"
if __name__ == "__main__":
    corpus = pycantonese.read_chat(url)
    line = filter(None, open("TOPOL_word_list.txt", "r", encoding='utf8').read().splitlines())
    for TOPOL_word in line:
        all_token_list = corpus.search(character=TOPOL_word)
        file = open("word_freq_LWL.txt", "a", encoding='utf8')
        file.write(TOPOL_word+"\t"+str(len(all_token_list)*0.849)+"\n")
    file.close()

url = "https://childes.talkbank.org/data/Chinese/Cantonese/HKU.zip"
if __name__ == "__main__":
    corpus = pycantonese.read_chat(url)
    line = filter(None, open("TOPOL_word_list.txt", "r", encoding='utf8').read().splitlines())
    for TOPOL_word in line:
        all_token_list = corpus.search(character=TOPOL_word)
        file = open("word_freq_HKU.txt", "a", encoding='utf8')
        file.write(TOPOL_word+"\t"+str(len(all_token_list)*5.609)+"\n")
    file.close()