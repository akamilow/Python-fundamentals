import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back,",
          "Kanye West",
          "Samuel L. Jackson",
          "Camilo Castellar",
          "Andres Mercado",
          "Andres Castellar"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_personTwo = random.choice(people)
random_personThree = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}, {random_personTwo} and {random_personThree}")

