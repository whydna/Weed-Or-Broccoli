# Weed-Or-Broccoli

CNN that classifies images as containing either weed or broccoli. Uses Google Images for training data and achieves about 80% - 90% accuracy.

## Train It

- Add or modify training data from the `dataset` folder.
- Run `python train_model.py -d dataset -m output/my_model.hdf5`

## Detect

- Once you've generated the model, run `python test_model.py -m output/my_model.hdf5 -i ~/images/`

## Results

<img src="https://i.imgur.com/Zq3SIV1.png" width="250">
<img src="https://i.imgur.com/NWMxaxe.png" width="250">
<img src="https://i.imgur.com/Y6FpYuf.png" width="250">
<img src="https://i.imgur.com/qWTzd6W.jpg" width="250">
<img src="https://i.imgur.com/YOoozny.png" width="250">
