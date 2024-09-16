import random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

def generate_bingo_card(verbs, form_key):
    # Randomly select 25 verbs without repetition
    selected_verbs = random.sample(verbs, 25)
    # Get the specified form of each verb
    selected_words = [verb[form_key] for verb in selected_verbs]
    # Arrange the words into a 5x5 grid
    grid = [selected_words[i:i+5] for i in range(0, 25, 5)]
    return grid

def create_pdf_bingo_cards(grids, form_name, page_number=1):
    # Use a unique filename for each PDF, including the form name
    c = canvas.Canvas(f"bingo_cards_{form_name}_{page_number}.pdf", pagesize=landscape(A4))
    width, height = landscape(A4)
    c.setFont("Helvetica", 12)

    columns = 2
    rows = 2

    card_width = width / columns
    card_height = height / rows

    # Set line width for borders
    c.setLineWidth(2)  # Bolder borders

    for index, grid in enumerate(grids):
        # Calculate position
        col = index % columns
        row = index // columns
        x_offset = col * card_width
        y_offset = height - ((row + 1) * card_height)

        # Draw card border
        c.rect(x_offset, y_offset, card_width, card_height)

        # Draw the grid and words within the card
        cell_width = card_width / 5
        cell_height = card_height / 5

        # Set thinner lines for grid
        c.setLineWidth(1)

        for i, row_words in enumerate(grid):
            for j, word in enumerate(row_words):
                x = x_offset + j * cell_width
                y = y_offset + card_height - (i + 1) * cell_height
                c.rect(x, y, cell_width, cell_height)
                # Handle multi-word entries (e.g., "was/were")
                c.setFont("Helvetica", 10 if '/' in word or len(word) > 10 else 12)
                c.drawCentredString(x + cell_width / 2, y + cell_height / 2 - 4, word.capitalize())
                c.setFont("Helvetica", 12)

        # Reset line width for the next card border
        c.setLineWidth(2)

    c.save()

def main():
    verbs = [
        {'base': 'be', 'past_simple': 'was/were', 'past_participle': 'been'},
        {'base': 'beat', 'past_simple': 'beat', 'past_participle': 'beaten'},
        {'base': 'become', 'past_simple': 'became', 'past_participle': 'become'},
        {'base': 'begin', 'past_simple': 'began', 'past_participle': 'begun'},
        {'base': 'break', 'past_simple': 'broke', 'past_participle': 'broken'},
        {'base': 'bring', 'past_simple': 'brought', 'past_participle': 'brought'},
        {'base': 'build', 'past_simple': 'built', 'past_participle': 'built'},
        {'base': 'buy', 'past_simple': 'bought', 'past_participle': 'bought'},
        {'base': 'catch', 'past_simple': 'caught', 'past_participle': 'caught'},
        {'base': 'choose', 'past_simple': 'chose', 'past_participle': 'chosen'},
        {'base': 'come', 'past_simple': 'came', 'past_participle': 'come'},
        {'base': 'cost', 'past_simple': 'cost', 'past_participle': 'cost'},
        {'base': 'cut', 'past_simple': 'cut', 'past_participle': 'cut'},
        {'base': 'do', 'past_simple': 'did', 'past_participle': 'done'},
        {'base': 'draw', 'past_simple': 'drew', 'past_participle': 'drawn'},
        {'base': 'drink', 'past_simple': 'drank', 'past_participle': 'drunk'},
        {'base': 'drive', 'past_simple': 'drove', 'past_participle': 'driven'},
        {'base': 'eat', 'past_simple': 'ate', 'past_participle': 'eaten'},
        {'base': 'fall', 'past_simple': 'fell', 'past_participle': 'fallen'},
        {'base': 'feel', 'past_simple': 'felt', 'past_participle': 'felt'},
        {'base': 'fight', 'past_simple': 'fought', 'past_participle': 'fought'},
        {'base': 'find', 'past_simple': 'found', 'past_participle': 'found'},
        {'base': 'fly', 'past_simple': 'flew', 'past_participle': 'flown'},
        {'base': 'forget', 'past_simple': 'forgot', 'past_participle': 'forgotten'},
        {'base': 'get', 'past_simple': 'got', 'past_participle': 'got/gotten'},
        {'base': 'give', 'past_simple': 'gave', 'past_participle': 'given'},
        {'base': 'go', 'past_simple': 'went', 'past_participle': 'gone'},
        {'base': 'have', 'past_simple': 'had', 'past_participle': 'had'},
        {'base': 'hear', 'past_simple': 'heard', 'past_participle': 'heard'},
        {'base': 'hit', 'past_simple': 'hit', 'past_participle': 'hit'},
        {'base': 'hold', 'past_simple': 'held', 'past_participle': 'held'},
        {'base': 'hurt', 'past_simple': 'hurt', 'past_participle': 'hurt'},
        {'base': 'keep', 'past_simple': 'kept', 'past_participle': 'kept'},
        {'base': 'know', 'past_simple': 'knew', 'past_participle': 'known'},
        {'base': 'learn', 'past_simple': 'learned/learnt', 'past_participle': 'learned/learnt'},
        {'base': 'leave', 'past_simple': 'left', 'past_participle': 'left'},
        {'base': 'lend', 'past_simple': 'lent', 'past_participle': 'lent'},
        {'base': 'let', 'past_simple': 'let', 'past_participle': 'let'},
        {'base': 'lose', 'past_simple': 'lost', 'past_participle': 'lost'},
        {'base': 'make', 'past_simple': 'made', 'past_participle': 'made'},
        {'base': 'mean', 'past_simple': 'meant', 'past_participle': 'meant'},
        {'base': 'meet', 'past_simple': 'met', 'past_participle': 'met'},
        {'base': 'pay', 'past_simple': 'paid', 'past_participle': 'paid'},
        {'base': 'put', 'past_simple': 'put', 'past_participle': 'put'},
        {'base': 'read', 'past_simple': 'read', 'past_participle': 'read'},
        {'base': 'ride', 'past_simple': 'rode', 'past_participle': 'ridden'},
        {'base': 'run', 'past_simple': 'ran', 'past_participle': 'run'},
        {'base': 'say', 'past_simple': 'said', 'past_participle': 'said'},
        {'base': 'see', 'past_simple': 'saw', 'past_participle': 'seen'},
        {'base': 'sell', 'past_simple': 'sold', 'past_participle': 'sold'},
        {'base': 'show', 'past_simple': 'showed', 'past_participle': 'shown'},
        {'base': 'sing', 'past_simple': 'sang', 'past_participle': 'sung'},
        {'base': 'sit', 'past_simple': 'sat', 'past_participle': 'sat'},
        {'base': 'sleep', 'past_simple': 'slept', 'past_participle': 'slept'},
        {'base': 'speak', 'past_simple': 'spoke', 'past_participle': 'spoken'},
        {'base': 'spend', 'past_simple': 'spent', 'past_participle': 'spent'},
        {'base': 'stand', 'past_simple': 'stood', 'past_participle': 'stood'},
        {'base': 'steal', 'past_simple': 'stole', 'past_participle': 'stolen'},
        {'base': 'swim', 'past_simple': 'swam', 'past_participle': 'swum'},
        {'base': 'take', 'past_simple': 'took', 'past_participle': 'taken'},
        {'base': 'teach', 'past_simple': 'taught', 'past_participle': 'taught'},
        {'base': 'tell', 'past_simple': 'told', 'past_participle': 'told'},
        {'base': 'think', 'past_simple': 'thought', 'past_participle': 'thought'},
        {'base': 'throw', 'past_simple': 'threw', 'past_participle': 'thrown'},
        {'base': 'understand', 'past_simple': 'understood', 'past_participle': 'understood'},
        {'base': 'wear', 'past_simple': 'wore', 'past_participle': 'worn'},
        {'base': 'win', 'past_simple': 'won', 'past_participle': 'won'},
        {'base': 'write', 'past_simple': 'wrote', 'past_participle': 'written'}
    ]
    random.shuffle(verbs)
    print(f'{len(verbs)} verbs in dataset')
    # Ask how many bingo cards to generate
    try:
        num_cards = int(input("Enter the number of bingo cards to generate (multiples of 4 recommended): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if num_cards <= 0:
        print("Please enter a positive number.")
        return

    # Display options for verb forms
    print("Choose the verb form to use on the bingo cards:")
    print("1. Base Form")
    print("2. Past Simple")
    print("3. Past Participle")
    form_choice = input("Enter the number corresponding to your choice (1-3): ").strip()

    form_key = ''
    form_name = ''
    if form_choice == '1':
        form_key = 'base'
        form_name = 'base'
    elif form_choice == '2':
        form_key = 'past_simple'
        form_name = 'past_simple'
    elif form_choice == '3':
        form_key = 'past_participle'
        form_name = 'past_participle'
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    grids = []
    page_number = 1

    for i in range(1, num_cards + 1):
        if len(verbs) < 25:
            print("Not enough verbs to generate more bingo cards without repeats.")
            break
        grid = generate_bingo_card(verbs, form_key)
        grids.append(grid)
        # Optionally remove used verbs to avoid repeats across cards
        # Remove selected verbs from the list if you don't want repeats across cards
        # verbs = [verb for verb in verbs if verb not in selected_verbs]

        # When we have 4 grids or it's the last card, create a PDF page
        if len(grids) == 4 or i == num_cards:
            create_pdf_bingo_cards(grids, form_name, page_number=page_number)
            print(f"Bingo cards saved as bingo_cards_{form_name}_{page_number}.pdf")
            grids = []
            page_number += 1

    print(f"Total of {i} bingo cards created.")

if __name__ == "__main__":
    main()
