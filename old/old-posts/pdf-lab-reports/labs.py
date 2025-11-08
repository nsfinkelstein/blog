import io
from functools import cache
from itertools import cycle
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
from transformers import AutoImageProcessor, TableTransformerForObjectDetection

# This module relies heavily on code in the following reference notebook:
# https://colab.research.google.com/github/NielsRogge/Transformers-Tutorials/blob/master/Table%20Transformer/Using_Table_Transformer_for_table_detection_and_table_structure_recognition.ipynb

OBJECT_MODEL_NAME = 'microsoft/table-transformer-detection'
STRUCTURE_MODEL_NAME = 'microsoft/table-transformer-structure-recognition'


@cache
def get_table_model(model_name):
    return TableTransformerForObjectDetection.from_pretrained(model_name)


@cache
def get_image_processor(model_name):
    return AutoImageProcessor.from_pretrained(model_name)


def get_image_paths(dir):
    return (path for path in (Path(__file__).parent / dir).iterdir() if str(path)[-3:] == 'png')


def load_images(dir='report-images'):
    return (Image.open(path).convert('RGB') for path in get_image_paths(dir))


def run_model(image, model_name, threshold=0.7):
    image_processor = get_image_processor(model_name)
    detection_model = get_table_model(model_name)

    with torch.no_grad():
        # NOTE: inference for all images at once would be faster; this is demo code
        outputs = detection_model(**image_processor(image, return_tensors='pt'))

    target_sizes = torch.tensor([image.size[::-1]])
    return image_processor.post_process_object_detection(
        outputs, threshold=threshold, target_sizes=target_sizes
    )[0]


def pull_best_table(image: Image.Image, tables):
    if len(tables['scores']) == 0:
        return None, None

    table_bbox = np.array(tables['boxes'][tables['scores'].argmax()])

    # get more padding
    table_bbox = [
        max(table_bbox[0] - 50, 0),
        max(table_bbox[1] - 50, 0),
        min(table_bbox[2] + 50, image.width),
        min(table_bbox[3] + 50, image.height),
    ]

    return table_bbox, image.crop(table_bbox)


def inserted_segmented_table(image: Image.Image, annotated_table: Image.Image, table_bbox):
    image.paste(annotated_table, box=tuple(np.array(table_bbox).astype(np.int32)[:2]))
    return image


def segment_tables(image, tables):
    table_bbox, table_image = pull_best_table(image, tables)

    if table_image is None:
        return image

    segmented_table = run_model(table_image, STRUCTURE_MODEL_NAME, threshold=0.7)
    annotated_table = plot_results(table_image, segmented_table, STRUCTURE_MODEL_NAME, font_size=7)
    return inserted_segmented_table(image, annotated_table, table_bbox)


def plot_results(img, output, model_name, font_size=20):
    scores, labels, boxes = (output[k] for k in ('scores', 'labels', 'boxes'))
    colors = cycle([tuple(int(x * 255) for x in c) for c in plt.get_cmap('tab10').colors])

    objects = zip(scores.tolist(), labels.tolist(), boxes.tolist(), colors)
    draw = ImageDraw.Draw(img, mode='RGBA')
    font = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSans.ttf', font_size)
    for score, label, box, c in objects:
        draw.rectangle([int(x) for x in box], outline=c, width=3)

        text = f'{get_table_model(model_name).config.id2label[label]}: {score:0.2f}'.upper()
        position = box[:2]

        b = draw.textbbox(position, text, font=font, font_size=font_size)
        draw.rectangle((b[0] - 3, b[1] - 3, b[2] + 3, b[3] + 3), fill=tuple(list(c) + [130]))
        draw.text(position, text, font=font, fill="black", font_size=font_size)

    return img


def create_tatr_pngs():
    # TODO: this is clearly broken. Fix tomorrow.
    results = ((i, run_model(i, OBJECT_MODEL_NAME, threshold=0.2)) for i in load_images())
    images = (plot_results(img, res, OBJECT_MODEL_NAME) for img, res in results)

    # todo: keep track of image names throughout processing in case of reordering
    img_dir = Path('tatr-report-images')
    img_dir.mkdir(exist_ok=True)
    for img, path in zip(images, get_image_paths('report-images')):
        img.save(img_dir / path.name)


def create_tatr_structure_pngs():
    results = ((i, run_model(i, OBJECT_MODEL_NAME, threshold=0.2)) for i in load_images())
    images = [segment_tables(img, res) for img, res in results]

    # todo: keep track of image names throughout processing in case of reordering
    img_dir = Path('tatr-structure-report-images')
    img_dir.mkdir(exist_ok=True)
    for img, path in zip(images, get_image_paths('report-images')):
        img.save(img_dir / path.name)
    return images
