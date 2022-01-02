from transitions.extensions import GraphMachine

from utils import send_text_message
import random
import json



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        with open("flex.json") as f:
            self.json_flex = json.load(f)
        cards = []
        for value in range(1,14):
            for color in range(1,5):
                cards.append([value,color,0])
        random.shuffle(cards)
        length = 0
        self.dealed_card = []
        while(1):
            if len(cards) > 0:
                temp = cards.pop(0)
                self.dealed_card.append(temp)
                length += 1
            for i,s in enumerate(cards):
                if s[0] == temp[0]:
                    self.dealed_card.append(cards.pop(i))
                    length += 1
                    break
            if length == 20:
                break
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def game_show(self):
        print(self.dealed_card)