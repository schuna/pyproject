import os
import random
from glob import glob

import tensorflow as tf
from tqdm import tqdm


def _byte_feature(value):
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy()
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _float_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def make_example(img_str, source_id, filename):

    feature = {
        "image/source_id": _int64_feature(source_id),
        "image/filename": _byte_feature(filename),
        "image/encoded": _byte_feature(img_str)
    }
    return tf.train.Example(features=tf.train.Features(feature=feature))


def main(dataset_path, output_path):
    labels = ["CNV", "DME", "DRUSEN", "NORMAL"]
    samples = []
    print("Reading data list...")
    for id_name in tqdm(os.listdir(dataset_path)):
        img_paths = glob(os.path.join(dataset_path, id_name, '*.jpeg'))
        for img_path in img_paths:
            filename = os.path.join(id_name, os.path.basename(img_path))
            samples.append((img_path, id_name, filename))
    random.shuffle(samples)

    print("Writing tfrecord file...")
    with tf.io.TFRecordWriter(output_path) as writer:
        for img_path, id_name, filename in tqdm(samples):

            tf_example = make_example(
                img_str=open(img_path, 'rb').read(),
                source_id=int(labels.index(id_name)),
                filename=str.encode(filename))

            writer.write(tf_example.SerializeToString())


if __name__ == '__main__':
    main("F:\\OCT2017\OCT2017\\test", "F:\\OCT2017\OCT2017\\oct2017.tfrecord")
