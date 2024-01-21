from flask import Flask, render_template, request, send_file, jsonify
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend
import matplotlib.pyplot as plt
import base64
from utils.diamond_helper import getDiamonds

app = Flask(__name__)

# Sample data (you can replace it with your data)
diamonds = getDiamonds(None)

# Create a dictionary for quick access to Diamond objects by ID
diamonds_dict = {diamond.id: diamond for diamond in diamonds}

# Initialize diamonds_to_compare as an empty list
diamonds_to_compare = []

@app.route('/')
def show_main_page():
    diamonds_id_list = list(diamonds_dict.keys())
    return render_template('index.html', diamonds_id_list=diamonds_id_list, diamonds_to_compare=diamonds_to_compare)

@app.route('/compare', methods=['GET', 'POST'])
def compare_diamonds():
    global diamonds_to_compare

    # Get the selected diamond IDs from the form submission
    diamond_id1 = int(request.form.get('diamondId1'))
    diamond_id2 = int(request.form.get('diamondId2'))

    # Retrieve diamond information for comparison
    diamonds_to_compare = [diamonds_dict.get(diamond_id1), diamonds_dict.get(diamond_id2)]

    # Pass the retrieved data and diamonds_id_list to the front end
    diamonds_id_list = list(diamonds_dict.keys())
    return render_template('index.html', diamonds_id_list=diamonds_id_list, diamonds_to_compare=diamonds_to_compare)

@app.route('/get_chart/<int:diamond_id>')
def get_chart(diamond_id):
    diamond = diamonds_dict.get(diamond_id)

    if not diamond:
        return 'Diamond not found', 404

    try:
        # Create a bar chart with all attributes
        attributes = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
        values = [getattr(diamond, attr) for attr in attributes]

        # Use Agg backend to avoid GUI-related warnings
        plt.switch_backend('Agg')

        plt.bar(attributes, values)
        plt.title(f'Diamond Attributes - ID {diamond_id}')
        plt.xlabel('Attributes')
        plt.ylabel('Values')

        # Save the chart to a BytesIO object
        img_io = BytesIO()
        plt.savefig(img_io, format='png')
        img_io.seek(0)

        # Encode the image as base64 and return it
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return f'data:image/png;base64,{img_base64}'
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
