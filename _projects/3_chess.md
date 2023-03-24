---

name: Chess Pieces Image Classifier
tools: [Python, PyTorch, machine learning]
image: images/chess_pieces.png
description: Machine learning program to classify images of chess pieces

---

# Chess Pieces Classifier

[*View on GitHub*](https://github.com/nmarks99/chess-classifier.git)


The goal of this project is to create a program that takes an image of a single chess piece and output the name of that piece.
This Jupyter notebook creates and trains the model used for the classification and the `chess_classifier.py` script uses the
model to classify the chess piece in a provided image.

Originally, my project proposal suggested that I would make a program
that classifies an entire chess board, however this has proven to take longer than expected and I needed to scale the project
back slightly. However, this project could be adapted to classify an entire chess board without much trouble. The only additional
step that is needed is to create another program that breaks an image of a chess board into 64 images (1 image for each square on
the board) and classify each of the images.

A demonstration and walkthrough of the code is provided in the below video:
<figure>
  <center>
    <iframe width="760" height="515" src="https://www.youtube.com/embed/GcBdZo7Du3U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </center>
</figure>


## *Sources:*
- https://www.kaggle.com/code/nathanperkins4223970/chess-piece
- https://www.kaggle.com/datasets/anshulmehtakaggl/chess-pieces-detection-images-dataset
