from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from utils.diamond_helper import getDiamonds

app = Flask(__name__)



# Sample data
diamonds = getDiamonds(4)


@app.route('/diamond/<int:diamond_id>')
def show_diamond(diamond_id):
    # Find the selected diamond
    selected_diamond = next((diamond for diamond in diamonds if diamond.id == diamond_id), None)

    if selected_diamond:
        # Get the index of the selected diamond
        index = diamonds.index(selected_diamond)

        # Calculate indices for next and previous diamonds
        prev_index = index - 1 if index > 0 else None
        next_index = index + 1 if index < len(diamonds) - 1 else None

        # Get diamonds for next and previous indices
        prev_diamond = diamonds[prev_index] if prev_index is not None else None
        next_diamond = diamonds[next_index] if next_index is not None else None

        # Create a scatter plot for the selected diamond
        plt.figure(figsize=(8, 5))
        plt.scatter(selected_diamond.carat, selected_diamond.price, marker='o', color='red')
        plt.title(f'Diamond Information - ID: {selected_diamond.id}')
        plt.xlabel('Carat')
        plt.ylabel('Price ($)')

        # Annotate the point with attribute values
        plt.annotate(
            f'Carat: {selected_diamond.carat}\nCut: {selected_diamond.cut}\nColor: {selected_diamond.color}\n'
            f'Clarity: {selected_diamond.clarity}\nDepth: {selected_diamond.depth}\n'
            f'Table: {selected_diamond.table}\nPrice: {selected_diamond.price}\n'
            f'X: {selected_diamond.x}\nY: {selected_diamond.y}\nZ: {selected_diamond.z}',
            (selected_diamond.carat, selected_diamond.price),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=8,
            color='black'
        )

        # Save the plot to a BytesIO object
        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)

        # Encode the image to base64 for embedding in HTML
        encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')

        plt.close()  # Close the plot to free resources

        return render_template('diamond.html', image=encoded_image,
                               diamond=selected_diamond,
                               prev_diamond_id=prev_diamond.id if prev_diamond else None,
                               next_diamond_id=next_diamond.id if next_diamond else None)
    else:
        return 'Diamond not found', 404

if __name__ == '__main__':
    app.run(debug=True)