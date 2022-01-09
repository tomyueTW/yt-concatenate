from yt_concatenate.pipeline.steps.get_video_list import GetVideoList
from yt_concatenate.pipeline.pipeline import Pipeline


def main():
    inputs = {
        'channel_id': 'UCKSVUHI9rbbkXhvAXK-2uxA'
    }
    steps = [
        GetVideoList(),
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
