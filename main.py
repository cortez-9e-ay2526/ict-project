# Declaring Variables and Identifying Data Types
from pyscript import display, document

# Step 1: string variable letter. ok?
shop = 'Readers cove'  # ts a string. heh.... ok?

# Step 2: integer variable (letter. only. name ok?)
price = 500  # This is an integer (int) #peak... ok?

# Step 3: float variable (letter and digit name ok?)
bookrating = 4.8  # This is a Floating-Point Number (float ok?)

# Step 4: list variable (letter. only name. ok?)
target_audience = ['Kids', 'Teens', 'Adults']  # this list. (list ok?)

# Step 5: boolean variable (strictly. student type. ok?)
student_type = True  # This is a Boolean (bool)

# Step 6: dictionary. variable. ok?
top_selling = {
    'title': 'Beauty and the Beast',
    'author': 'Ursula Jones',
    'illustrator': 'Sara Gibb',
    'genre': 'Fairy Tale',
    'format': 'Paperback',
    'price': 150
}  # this dictionary. ok?

# Step 7: set variable (letters only. name. ok?)
bookgenres = set(['Fairy Tale', 'Satire Manga', 'Psychological Fiction'])  # This is a Set (set)

# Step 8: tuple variable (letters only. name. ok?)
booktitles = ('Beauty and the Beast', 'HETALIA', 'No Longer Human')  # This is a Tuple (tuple)


# step 10: display function. heh. ok?
display(shop, target="out_name")
display(str(price), target="out_age")
display(str(bookrating), target="out_height")
display(", ".join(target_audience), target="out_countries")
display(str(student_type), target="out_student")
display(str(bookgenres), target="out_fruits")
display(", ".join(booktitles), target="out_days")


# SKU and Receipt Generator... ok?

def create_order(e=None):
    # get all elements... ok?
    prod1 = document.getElementById("Beauty")
    prod2 = document.getElementById("Hetalia")
    prod3 = document.getElementById("NoLongerHuman")

    # Add all product values... ok?
    subtotal = 0

    if prod1.checked:
        subtotal += float(prod1.value)

    if prod2.checked:
        subtotal += float(prod2.value)

    if prod3.checked:
        subtotal += float(prod3.value)

    Tax = 1.12  # this is the tax. ok?
    Total = subtotal * Tax  # calculate total. ok?


    # Display output... ok?
    document.getElementById('output1').innerHTML = (
        f'Subtotal: ₱{subtotal:.2f}<br>'
        f'Tax: 12%<br>'
        f'Total: ₱{Total:.2f}'
    )


def generate_sku(e=None):
    # Get all element values... ok?
    Category = document.getElementById("category").value
    Product = document.getElementById("product").value
    Quantity = document.getElementById("quantity").value

    # abbreviate product name... ok?
    Product_skuval = Product[:3]

    # set quantity number to a 3 digit number if lower than 100... ok?
    if Quantity == "":
        document.getElementById('output2').innerHTML = "Please enter a quantity."
        return

    Quantity = int(Quantity)
    quantity_skuval = f'{Quantity:03d}'


    # Display output... ok?
    document.getElementById('output2').innerHTML = (
        f'{Category}-{Product_skuval.upper()}-{quantity_skuval}'
    )