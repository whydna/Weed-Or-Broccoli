# Weed-Or-Broccoli

CNN that classifies images as containing either weed or broccoli. Uses Google Images for training data and achieves about 80% - 90% accuracy.

## Train It

- Add or modify training data from the `dataset` folder.
- Run `python train_model.py -d dataset -m output/my_model.hdf5`

## Detect

- Once you've generated the model, run `python test_model.py -m output/my_model.hdf5 -i ~/images/`
