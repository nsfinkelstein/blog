from pathlib import Path

import torch
from labs import (
    OBJECT_MODEL_NAME,
    get_image_paths,
    inserted_segmented_table,
    create_tatr_structure_pngs,
    load_images,
    plot_results,
    pull_best_table,
    run_model,
)
from PIL import Image


def test_image_paths():
    paths = list(get_image_paths('report-images'))
    assert all(isinstance(path, Path) for path in paths)

    path = paths[0]
    assert 'report-images' in str(path)
    assert str(path)[-3:]


def test_image_preprocessing():
    images = load_images('report-images')
    assert all(isinstance(image, Image.Image) for image in images)


def test_detect_tables():
    results = run_model(next(load_images('report-images')), OBJECT_MODEL_NAME)
    assert {'scores', 'labels', 'boxes'} == set(results.keys())


def test_pull_best_table():
    image: Image.Image = next(load_images('report-images'))
    table1 = (0, 0, image.width / 2, image.height / 2)
    table2 = (0, 0, image.width / 4, image.height / 4)
    boxes = torch.Tensor((table1, table2))
    bbox, result = pull_best_table(image, {'boxes': boxes, 'scores': torch.Tensor([0.7, 0.4])})
    assert result.height == image.height // 2
    assert result.width == image.width // 2
    assert (bbox == table1).all()


def test_plot_does_not_error():
    for image in load_images('report-images'):
        result = run_model(image, OBJECT_MODEL_NAME, 0.2)
        plot_results(image, result, OBJECT_MODEL_NAME)


def test_create_structure_pngs():
    create_tatr_structure_pngs()
